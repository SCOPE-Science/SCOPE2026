"""Finite exact tests for the square-boundary collapse of line-graph neighborhood complexes.

Python 3, standard library only. Enumerates faces and runs elementary collapses, rather
than inferring a result from homology; the mathematical proof covers arbitrary graphs.
"""
from itertools import combinations
import random


def bit_subsets(s):
    t=s
    while t:
        yield t
        t=(t-1)&s
    yield 0


def verified_case(n, edges):
    edges=[tuple(sorted(e)) for e in edges]
    edges=sorted(set(edges))
    assert all(0<=a<b<n for a,b in edges)
    adj=[0]*n
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    for a,b,c in combinations(range(n),3):
        assert not ((adj[a]>>b)&(adj[b]>>c)&(adj[c]>>a)&1),"not triangle-free"
    m=len(edges)
    stars=[0]*n
    for i,(a,b) in enumerate(edges):stars[a]|=1<<i;stars[b]|=1<<i
    centers=[(stars[a]|stars[b]) for a,b in edges]
    K={0}
    for s in centers:K.update(bit_subsets(s))
    Y={0}
    for s in stars:Y.update(bit_subsets(s))
    C4=[]
    for vs in combinations(range(n),4):
        if sum(bool((adj[a]>>b)&1) for a,b in combinations(vs,2))==4:
            if all(sum(bool((adj[a]>>b)&1) for b in vs if b!=a)==2 for a in vs):
                qm=0
                for i,(a,b) in enumerate(edges):
                    if a in vs and b in vs:qm|=1<<i
                assert qm.bit_count()==4
                C4.append(qm)
    target=Y.copy()
    for q in C4:
        target.update(t for t in bit_subsets(q) if t!=q)
    assert target<=K
    # An explicit unique-center pairing for all faces outside the target.
    lower=[]
    outside=K-target
    for face in outside:
        witnesses=[i for i,s in enumerate(centers) if face&~s==0]
        assert len(witnesses)==1,("ambiguous outside target",n,edges,face,witnesses)
        e=witnesses[0]
        if not(face>>e)&1:
            upper=face|(1<<e)
            assert upper in outside
            lower.append((face,upper))
        else:
            down=face&~(1<<e)
            assert down in outside,("unpaired upper",n,edges,face)
            assert sum(down&~s==0 for s in centers)==1
    touched=[f for lo,up in lower for f in (lo,up)]
    assert len(touched)==len(set(touched))==len(outside)
    working=K.copy()
    for lo,up in sorted(lower,key=lambda p:(-p[0].bit_count(),p[0])):
        assert lo in working and up in working
        cofacets=[lo|(1<<j) for j in range(m) if (not(lo>>j)&1) and lo|(1<<j) in working]
        assert cofacets==[up],("not free",n,edges,lo,up,cofacets)
        working.remove(lo);working.remove(up)
    assert working==target
    return m,len(K)-1,len(lower),len(C4),len(target)-1


def theta(L1,L2,L3):
    edges=[];n=2
    for L in (L1,L2,L3):
        path=[0]
        for _ in range(L-1):path.append(n);n+=1
        path.append(1)
        edges.extend(zip(path,path[1:]))
    return n,edges


def grid(a,b):
    edges=[]
    for i in range(a):
        for j in range(b):
            if i+1<a:edges.append((i*b+j,(i+1)*b+j))
            if j+1<b:edges.append((i*b+j,i*b+j+1))
    return a*b,edges


def cube(d):
    return 1<<d,[(i,i^(1<<j)) for i in range(1<<d) for j in range(d) if not(i>>j)&1]


def petersen():
    return 10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+((i+2)%5)) for i in range(5)]


def main():
    cases=[]
    for n in range(2,6):
        E=list(combinations(range(n),2))
        for flag in range(1<<len(E)):
            edges=[e for k,e in enumerate(E) if (flag>>k)&1]
            edset={e for e in edges}
            if any((a,b) in edset and (a,c) in edset and (b,c) in edset for a,b,c in combinations(range(n),3)):
                continue
            if not edges:continue
            cases.append((f"all labeled n={n}",n,edges))
    rng=random.Random(314159)
    for j in range(120):
        n=6;E=list(combinations(range(n),2))
        edges=[e for e in E if rng.randrange(2)]
        edset=set(edges)
        if not edges or any((a,b) in edset and (a,c) in edset and (b,c) in edset for a,b,c in combinations(range(n),3)):continue
        cases.append(("random6",n,edges))
    for L in (3,4,5,7,11):
        for x in ((2,2,L),(2,3,L),(3,3,L)):
            cases.append((f"theta{x}",*theta(*x)))
    cases.extend([("K23",5,[(i,j) for i in range(2) for j in range(2,5)]),
                  ("K33",6,[(i,j) for i in range(3) for j in range(3,6)]),
                  ("Petersen",*petersen()),("grid3x3",*grid(3,3)),
                  ("cube3",*cube(3))])
    totalfaces=totalpairs=totalq=0
    for tag,n,edges in cases:
        m,f,p,q,final=verified_case(n,edges)
        totalfaces+=f;totalpairs+=p;totalq+=q
        if tag in ("K23","K33","cube3","grid3x3") or tag.startswith("theta(2, 2"):
            print(tag, "edges",m,"faces",f,"pairs",p,"squares",q,"residual",final)
    print("VERIFY_OK",len(cases),"triangle-free graph instances;",totalfaces,"nonempty simplices;",totalpairs,"verified elementary collapses;",totalq,"four-cycle occurrences")


if __name__=="__main__":main()
