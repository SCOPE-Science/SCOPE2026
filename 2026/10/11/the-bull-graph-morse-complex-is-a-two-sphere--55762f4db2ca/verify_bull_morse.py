#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter, deque

# Bull graph: triangle 0-1-2-0 with leaves 3 at 0 and 4 at 1.
VERTICES=tuple(range(5))
EDGES=((0,1),(1,2),(0,2),(0,3),(1,4))
PRIM=tuple((a,i,b) for i,(a,b) in enumerate(EDGES) for a,b in ((a,b),(b,a)))
ORDER=tuple(range(len(PRIM)))

def valid(face):
    tails=set(); used_edges=set(); parent={}
    for j in face:
        a,e,b=PRIM[j]
        if a in tails or e in used_edges: return False
        tails.add(a); used_edges.add(e); parent[a]=b
    # In a graph, a nontrivial closed V-path is exactly a directed cycle.
    for a in parent:
        seen=set(); x=a
        while x in parent:
            if x in seen: return False
            seen.add(x); x=parent[x]
    return True

def faces_all():
    out=[]
    for k in range(1,5):
        for f in combinations(range(len(PRIM)),k):
            if valid(f): out.append(f)
    return out

def independent_tail_count():
    # Independent reconstruction: each graph vertex chooses no outgoing edge or
    # one incident oriented edge; reject duplicated underlying edges and cycles.
    choices=[]
    for v in VERTICES:
        choices.append([-1]+[j for j,(a,e,b) in enumerate(PRIM) if a==v])
    c=Counter()
    for picks in product(*choices):
        f=tuple(sorted(j for j in picks if j>=0))
        if f and valid(f): c[len(f)-1]+=1
    return c

def matching(faces):
    fset=set(faces); unmatched=set(faces); pairs=[]; stages=[]
    for v in ORDER:
        c=0
        for s in sorted(tuple(unmatched), key=lambda x:(len(x),x)):
            if s not in unmatched or v in s: continue
            t=tuple(sorted(s+(v,)))
            if t in unmatched and t in fset:
                unmatched.remove(s); unmatched.remove(t); pairs.append((s,t)); c+=1
        stages.append(c)
    return pairs,unmatched,stages

def hasse_check(faces,pairs):
    pairset=set(pairs); indeg={s:0 for s in faces}; adj={s:[] for s in faces}; covers=0
    for t in faces:
        if len(t)<=1: continue
        for j in range(len(t)):
            s=t[:j]+t[j+1:]
            if not s: continue
            covers+=1
            if (s,t) in pairset: u,v=s,t
            else: u,v=t,s
            adj[u].append(v); indeg[v]+=1
    q=deque([s for s,d in indeg.items() if d==0]); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return covers,seen==len(faces)

def boundary_rows(high,low):
    idx={s:i for i,s in enumerate(low)}; rows=[{} for _ in low]
    for j,t in enumerate(high):
        for pos in range(len(t)):
            s=t[:pos]+t[pos+1:]
            rows[idx[s]][j]=1 if pos%2==0 else -1
    return rows

def rank_mod_p(rows,ncols,p):
    a=[{j:(v%p) for j,v in r.items() if v%p} for r in rows]
    r=0
    for col in range(ncols):
        piv=next((i for i in range(r,len(a)) if a[i].get(col,0)),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][col],-1,p)
        a[r]={j:(v*inv)%p for j,v in a[r].items() if (v*inv)%p}
        for i in range(len(a)):
            if i==r: continue
            c=a[i].get(col,0)
            if not c: continue
            nr=dict(a[i])
            for j,v in a[r].items():
                w=(nr.get(j,0)-c*v)%p
                if w:nr[j]=w
                elif j in nr:del nr[j]
            a[i]=nr
        r+=1
        if r==len(a): break
    return r

def main():
    assert len(PRIM)==10
    faces=faces_all(); fv=Counter(len(s)-1 for s in faces)
    assert [fv[i] for i in range(4)]==[10,33,40,15]
    assert independent_tail_count()==fv
    pairs,critical,stages=matching(faces)
    crit=Counter(len(s)-1 for s in critical)
    assert len(pairs)==48 and crit==Counter({0:1,2:1})
    covers,acyclic=hasse_check(faces,pairs)
    assert covers==246 and acyclic
    by=[[s for s in faces if len(s)==d+1] for d in range(4)]
    for p in (2,3,5,7):
        ranks=[]
        for d in range(1,4):
            ranks.append(rank_mod_p(boundary_rows(by[d],by[d-1]),len(by[d]),p))
        assert ranks==[9,24,15]
        betti=[1,len(by[1])-9-24,len(by[2])-24-15,len(by[3])-15]
        assert betti==[1,0,1,0]
        print(f'p={p}: boundary_ranks={ranks}, betti={betti}')
    print('GRAPH bull edges='+repr(EDGES))
    print('PRIMITIVE_FIELDS',len(PRIM))
    print('FACE_VECTOR',[fv[i] for i in range(4)])
    print('NONEMPTY_FACES',len(faces))
    print('HASSE_COVERS',covers)
    print('MATCHING_STAGE_COUNTS',stages)
    print('MATCHED_PAIRS',len(pairs))
    print('CRITICAL_VECTOR',[crit.get(i,0) for i in range(4)])
    print('EULER',sum((-1)**i*fv[i] for i in range(4)))
    print('VERIFY_OK')
if __name__=='__main__':main()
