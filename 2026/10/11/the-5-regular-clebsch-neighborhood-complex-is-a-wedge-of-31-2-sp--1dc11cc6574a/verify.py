#!/usr/bin/env python3
import json, sys
from collections import defaultdict, deque
from itertools import combinations, product

GENS=(1,2,4,8,15)
N=16

def graph():
    adj={v:set() for v in range(N)}
    for v in range(N):
        for s in GENS:
            w=v^s
            assert w!=v
            adj[v].add(w)
    assert all(len(adj[v])==5 for v in range(N))
    for v in range(N):
        for w in adj[v]: assert v in adj[w]
    return adj

def faces(adj):
    F=set()
    for v in range(N):
        nb=sorted(adj[v])
        for r in range(1,len(nb)+1):
            for c in combinations(nb,r):
                F.add(sum(1<<x for x in c))
    return F

def face_vertices(m):
    return [i for i in range(N) if (m>>i)&1]

def gf_rank(columns, nrows, p):
    # columns as sparse dictionaries row -> coefficient mod p
    A=[{} for _ in columns]
    for j,col in enumerate(columns):
        A[j]={r:(a%p) for r,a in col.items() if a%p}
    pivot_to_col={}
    rank=0
    for j in range(len(A)):
        col=A[j]
        while col:
            r=max(col)
            if r not in pivot_to_col:
                inv=pow(col[r],-1,p)
                if inv!=1:
                    col={rr:(aa*inv)%p for rr,aa in col.items() if (aa*inv)%p}
                pivot_to_col[r]=col.copy(); rank+=1; break
            pc=pivot_to_col[r]
            fac=col[r]
            for rr,aa in pc.items():
                nv=(col.get(rr,0)-fac*aa)%p
                if nv: col[rr]=nv
                elif rr in col: del col[rr]
        A[j]=col
    return rank

def boundary_ranks(F,p):
    bydim=defaultdict(list)
    for m in F: bydim[m.bit_count()-1].append(m)
    for d in bydim: bydim[d].sort()
    ranks={}
    for d in range(1,max(bydim)+1):
        rows={m:i for i,m in enumerate(bydim[d-1])}
        cols=[]
        for m in bydim[d]:
            vs=face_vertices(m); col={}
            for k,v in enumerate(vs):
                sub=m^(1<<v)
                if sub in rows:
                    col[rows[sub]]=1 if k%2==0 else -1
            cols.append(col)
        ranks[d]=gf_rank(cols,len(rows),p)
    betti={}
    maxd=max(bydim)
    for d in range(maxd+1):
        dim=len(bydim[d])
        rd=ranks.get(d,0)
        rnext=ranks.get(d+1,0)
        betti[d]=dim-rd-rnext
    return ranks,betti

def toggle_matching(F, order):
    unmatched=set(F); pairs=[]
    for v in order:
        for lo in sorted(list(unmatched), key=lambda x:(x.bit_count(),x)):
            if lo not in unmatched or ((lo>>v)&1): continue
            hi=lo|(1<<v)
            if hi in unmatched:
                unmatched.remove(lo); unmatched.remove(hi); pairs.append((lo,hi,v))
    return pairs,sorted(unmatched,key=lambda x:(x.bit_count(),x))

def hasse_acyclic(F,pairs):
    pairset={(lo,hi) for lo,hi,_ in pairs}
    out={m:[] for m in F}; indeg={m:0 for m in F}; covers=0
    for hi in F:
        for v in face_vertices(hi):
            lo=hi^(1<<v)
            if lo==0 or lo not in F: continue
            covers+=1
            # Standard gradient orientation: unmatched covers high -> low, matched low -> high.
            a,b=(lo,hi) if (lo,hi) in pairset else (hi,lo)
            out[a].append(b); indeg[b]+=1
    q=deque([m for m in F if indeg[m]==0]); seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    return seen==len(F),covers

def chromatic(adj,k):
    order=sorted(range(N), key=lambda v:-len(adj[v]))
    color=[-1]*N
    def dfs(t):
        if t==N:return color.copy()
        v=order[t]
        forbidden={color[w] for w in adj[v] if color[w]>=0}
        for c in range(k):
            if c not in forbidden:
                color[v]=c
                if dfs(t+1):return color.copy()
        color[v]=-1
        return None
    return dfs(0)

def main():
    cert_path=sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
    with open(cert_path,encoding='utf-8') as f: cert=json.load(f)
    adj=graph()
    # Strongly regular parameters (16,5,0,2).
    ac=[]; nac=[]
    for u in range(N):
        for v in range(u+1,N):
            c=len(adj[u]&adj[v])
            (ac if v in adj[u] else nac).append(c)
    assert set(ac)=={0} and set(nac)=={2}
    F=faces(adj)
    fv=defaultdict(int)
    for m in F: fv[m.bit_count()-1]+=1
    fv=[fv[d] for d in range(max(fv)+1)]
    assert len(F)==cert['nonempty_faces']==352
    assert fv==cert['face_vector']==[16,80,160,80,16]
    assert 16-sum(adj[0] for _ in [])==16  # inert sanity: deterministic execution path
    order=cert['toggle_order']
    assert sorted(order)==list(range(16))
    pairs,critical=toggle_matching(F,order)
    assert len(pairs)==cert['matching_pairs']==160
    crit_by_dim=defaultdict(int)
    for m in critical: crit_by_dim[m.bit_count()-1]+=1
    assert {str(k):v for k,v in sorted(crit_by_dim.items())}==cert['critical_by_dimension']
    assert len(critical)==32 and crit_by_dim[0]==1 and crit_by_dim[2]==31
    ok,covers=hasse_acyclic(F,pairs)
    assert ok and covers==cert['hasse_covers']
    rank_report={}; betti_report={}
    for p in (2,3,5):
        ranks,betti=boundary_ranks(F,p)
        rank_report[str(p)]={str(k):v for k,v in ranks.items()}
        betti_report[str(p)]={str(k):v for k,v in betti.items()}
        assert [betti[d] for d in range(5)]==[1,0,31,0,0]
    assert rank_report==cert['boundary_ranks']
    chi=sum(((-1)**d)*fv[d] for d in range(len(fv)))
    assert chi==32
    assert chromatic(adj,3) is None
    c4=chromatic(adj,4); assert c4 is not None
    print('graph=5-regular Clebsch Cayley model on F2^4')
    print('strongly_regular=(16,5,0,2)')
    print('nonempty_faces=352')
    print('face_vector=' + repr(fv))
    print('hasse_covers=' + str(covers))
    print('matching_pairs=160')
    print('critical_cells=1x0-cell+31x2-cells')
    print('boundary_ranks=' + json.dumps(rank_report,sort_keys=True))
    print('betti_mod_2_3_5=[1,0,31,0,0]')
    print('chromatic_number=4')
    print('euler_characteristic=32')
    print('ACYCLIC_MATCHING_OK')
    print('VERIFY_OK')

if __name__=='__main__': main()
