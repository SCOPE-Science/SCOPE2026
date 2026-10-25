#!/usr/bin/env python3
"""Independent exact finite checks for the private-square-edge 3-cut theorem.

The theorem's infinite range is proved mathematically, not by these tests.
"""
from itertools import combinations


def edges(*pairs):
    return {frozenset(p) for p in pairs}


def mobius(n):
    N = 2*n
    return N, edges(*[(i, (i+1)%N) for i in range(N)],
                    *[(i, i+n) for i in range(n)])


def ladder(n):
    return 2*n, edges(*[(i, i+1) for i in range(n-1)],
                      *[(i+n, i+n+1) for i in range(n-1)],
                      *[(i, i+n) for i in range(n)])


def analyze(N, E):
    def linked(u,v):return frozenset((u,v)) in E
    assert N>=8 and all(len(e)==2 for e in E)
    assert all(sum(linked(a,b) for a,b in combinations(t,2))<3
               for t in combinations(range(N),3)), 'triangle'
    assert all(sum(linked(u,w) and linked(v,w) for w in range(N)
                   if w not in (u,v))<=2 for u,v in combinations(range(N),2)), 'K2,3'
    triples={t for t in combinations(range(N),3)
             if sum(linked(a,b) for a,b in combinations(t,2))>=2}
    squares={s for s in combinations(range(N),4)
             if sum(linked(a,b) for a,b in combinations(s,2))==4
             and all(sum(linked(a,b) for a,b in combinations(t,2))>=2
                     for t in combinations(s,3))}
    five={s for s in combinations(range(N),5)
          if all(t in triples for t in combinations(s,3))}
    assert not five
    usage={e:sum(e.issubset(s) for s in squares) for e in E}
    assert all(any(usage[e]==1 for e in E if e.issubset(s)) for s in squares), 'square without a private edge'
    assert len(triples)==sum(sum(u in e for e in E)*(sum(u in e for e in E)-1)//2
                             for u in range(N))
    faces={1:set(combinations(range(N),2)),2:set(triples),3:set(squares)}
    operations=[]
    def collapse(top, bottom):
        t=tuple(sorted(top));b=tuple(sorted(bottom));d=len(t)-1
        assert t in faces[d] and b in faces[d-1],(t,b)
        assert len(t)==len(b)+1 and set(b).issubset(t)
        # A free face must belong to exactly one current coface, across all dimensions.
        assert sum(set(b).issubset(c) for c in faces[d])==1, ('nonfree codim1',t,b)
        assert all(not set(b).issubset(c) for higher in range(d+1,4)
                   for c in faces[higher]), ('higher coface',t,b)
        faces[d].remove(t); faces[d-1].remove(b)
        operations.append((t,b))
    for t in sorted(triples):
        if not any(set(t).issubset(s) for s in squares):
            ends=next((a,b) for a,b in combinations(t,2) if not linked(a,b))
            collapse(t,ends)
    for s in sorted(squares):
        a,d=sorted(next(e for e in E if e.issubset(s) and usage[e]==1))
        b=next(v for v in s if v not in (a,d) and linked(a,v))
        c=next(v for v in s if v not in (a,b,d))
        assert linked(b,c) and linked(c,d) and not linked(a,c) and not linked(b,d)
        collapse((a,b,c,d),(a,c,d))
        collapse((a,b,c),(a,c))
        collapse((a,b,d),(a,d))
        collapse((b,c,d),(b,d))
    assert not faces[2] and not faces[3]
    # The original G remains connected within each of its components through retained edges.
    graph={u:set() for u in range(N)}
    for a,b in faces[1]:graph[a].add(b);graph[b].add(a)
    seen={0};work=[0]
    while work:
        for v in graph[work.pop()]:
            if v not in seen:seen.add(v);work.append(v)
    assert len(seen)==N,'remaining graph disconnected'
    r=len(faces[1])-N+1
    formula=(N-1)*(N-2)//2 -len(triples)+len(squares)
    assert r==formula>=0
    return (N,len(E),len(triples),len(squares),len(operations),r)


def cut_mod2_betti(N,E):
    # Direct computation of the ACTUAL ordinary cut complex, for N<=10 only.
    good=[s for s in combinations(range(N),3)
          if sum(frozenset(p) in E for p in combinations(s,2))<2]
    fs=[{s for s in combinations(range(N),k)
         if any(set(t).isdisjoint(s) for t in good)} for k in range(1,N-1)]
    def rank(rows,cols):
        index={t:i for i,t in enumerate(rows)};basis={}
        for s in cols:
            x=0
            for t in combinations(s,len(s)-1):x^=1<<index[t]
            while x:
                pivot=x.bit_length()-1
                if pivot in basis:x^=basis[pivot]
                else:basis[pivot]=x;break
        return len(basis)
    boundaries=[0]+[rank(fs[k-1],fs[k]) for k in range(1,len(fs))]+[0]
    betti=[len(s)-boundaries[k]-boundaries[k+1]-(1 if k==0 else 0)
           for k,s in enumerate(fs)]
    return {i:b for i,b in enumerate(betti) if b}


def main():
    for n in range(4,13):
        N,E=mobius(n);result=analyze(N,E)
        expected=2*n*n-8*n+1
        assert result[-1]==expected
        if n<=5:assert cut_mod2_betti(N,E)=={N-4:expected}
        print('MOBIUS',n,result)
    for n in range(4,9):
        N,E=ladder(n);print('LADDER',n,analyze(N,E))
    E=edges((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4))
    print('DISCONNECTED',analyze(8,E))
    print('VERIFY_OK')

if __name__=='__main__':main()
