"""Independent stdlib-only check of exhaustive Cayley-colour-refinement certificates.

Run: python check_certificates.py cayley_certificates.json
"""
import json,sys,itertools
from collections import defaultdict

GROUPS=[(1,), (2,), (3,), (4,), (2,2), (5,), (6,), (7,),
        (8,), (4,2), (2,2,2), (9,), (3,3), (10,), (11,),
        (12,), (6,2), (13,), (14,), (15,)]

def calc(fac, mask):
    verts=list(itertools.product(*(range(k) for k in fac)))
    N=len(verts);pos={a:i for i,a in enumerate(verts)}
    # Inverse-orbit order independent of the witness producer's internal code.
    pairs=[];used={(0,)*len(fac)}
    for v in verts[1:]:
        if v in used:continue
        neg=tuple((-v[i])%fac[i] for i in range(len(fac)))
        pairs.append(sorted({v,neg}));used.add(v);used.add(neg)
    S=[d for j,orb in enumerate(pairs) if (mask>>j)&1 for d in orb]
    a=[[False]*N for _ in range(N)]
    for i,u in enumerate(verts):
        for d in S:
            z=tuple((u[k]+d[k])%fac[k] for k in range(len(fac)))
            a[i][pos[z]]=True
    assert all(not a[i][i] for i in range(N))
    assert all(a[i][j]==a[j][i] for i in range(N) for j in range(N))
    col=[1]+[0]*(N-1)
    rounds=0
    for r in range(N+1):
        sig=[]
        for i in range(N):
            counts=[0]*(max(col)+1)
            for j in range(N):
                if a[i][j]:counts[col[j]]+=1
            sig.append((col[i],tuple(counts)))
        codes={v:k for k,v in enumerate(sorted(set(sig)))}
        nxt=[codes[x] for x in sig]
        if len(set(nxt))==len(set(col)):
            rounds=r;break
        col=nxt
    else:raise AssertionError('nonterminating refinement')
    classes=defaultdict(list)
    for i,c in enumerate(col):classes[c].append(i)
    return a,classes,rounds

def replay(path):
    with open(path,encoding='utf8') as f:data=json.load(f)
    assert data['version']==1
    expected=[];counts=defaultdict(int);nw=0
    for fac in GROUPS:
        n=1
        for k in fac:n*=k
        invol=1
        for k in fac:invol*=2 if k%2==0 else 1
        # Number of inversion orbits among nonzero points.
        ntypes=(n-1+invol-1)//2
        for mask in range(1<<ntypes):expected.append((fac,mask));counts[n]+=1
    assert len(expected)==len(data['cases'])
    for (fac,mask),row in zip(expected,data['cases']):
        assert row['factors']==list(fac) and row['mask']==mask
        adj,classes,rounds=calc(fac,mask);N=len(adj)
        assert len(classes)==row['colour_classes'] and row['rounds']==rounds
        expected_pairs={(v[0],w) for v in classes.values() for w in v[1:]}
        got_pairs=set()
        for x,y,p in row['witnesses']:
            assert (x,y) in expected_pairs and (x,y) not in got_pairs
            assert len(p)==N and sorted(p)==list(range(N)) and p[0]==0 and p[x]==y
            assert all(adj[i][j]==adj[p[i]][p[j]] for i in range(N) for j in range(N))
            got_pairs.add((x,y));nw+=1
        assert got_pairs==expected_pairs
    assert data['total_cases']==len(expected) and data['total_witnesses']==nw
    assert data['case_counts']=={str(n):counts[n] for n in sorted(counts)}
    print('PASS',data['total_cases'],'exhaustive cases',nw,'checked root-fixing automorphisms')
    print('COUNTS',json.dumps(data['case_counts'],sort_keys=True))

if __name__=='__main__':replay(sys.argv[1])
