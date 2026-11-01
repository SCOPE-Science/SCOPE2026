#!/usr/bin/env python3
"""Finite checks for fixed orbit graphs of Mycielskian complete bipartite graphs.
No finite check is used as a proof of the all-parameter structural theorem.
"""
from itertools import combinations
from math import comb


def graph(a,b,L):
    assert a >= 1 and b >= 1 and L >= 1
    V=[('w',0,0)]+[('A',j,i) for j in range(L+1) for i in range(a)]+[('B',j,i) for j in range(L+1) for i in range(b)]
    E=set()
    def edge(u,v):
        assert u!=v
        E.add(frozenset((u,v)))
    for j in range(L):
        for i in range(a):
            for k in range(b):
                edge(('A',j,i),('B',j+1,k));edge(('B',j,k),('A',j+1,i))
    for i in range(a):
        for k in range(b):edge(('A',L,i),('B',L,k))
    for v in V[1:]:
        if v[1]==0: edge(V[0],v)
    return V,E


def orbits(a,b,L,balanced=False):
    out=[[('w',0,0)]]
    for j in range(L+1):
        A=[('A',j,i) for i in range(a)];B=[('B',j,i) for i in range(b)]
        if balanced:
            assert a==b
            out.append(A+B)
        else:out.extend((A,B))
    return out


def orbit_graph(a,b,L,balanced=False):
    V,E=graph(a,b,L); O=orbits(a,b,L,balanced)
    O=[o for o in O if not any(frozenset(x) in E for x in combinations(o,2))]
    OE={frozenset((i,j)) for i,j in combinations(range(len(O)),2) if any(frozenset((x,y)) in E for x in O[i] for y in O[j])}
    return len(O),OE


def independence_faces(n,E):
    e={tuple(sorted(x)) for x in E}
    return [tuple(v for v in range(n) if mask>>v&1) for mask in range(1<<n) if not any(mask>>i&1 and mask>>j&1 for i,j in e)]


def rank_mod2(rows):
    pivots={}
    for row in rows:
        r=row
        while r:
            i=r.bit_length()-1
            if i in pivots:r^=pivots[i]
            else:pivots[i]=r;break
    return len(pivots)


def reduced_betti(n,E):
    faces=independence_faces(n,E)
    levels={j: [x for x in faces if len(x)==j+1] for j in range(-1,n)}
    top=max(i for i,v in levels.items() if v)
    dims={i:len(faces) for i,faces in levels.items() if i<=top}
    ranks={}
    for d in range(0,top+1):
        col={x:i for i,x in enumerate(levels[d-1])}
        rows=[]
        for x in levels[d]:
            mask=0
            for j in range(len(x)):
                y=x[:j]+x[j+1:]
                mask ^= 1<<col[y]
            rows.append(mask)
        ranks[d]=rank_mod2(rows)
    return {i:dims[i]-ranks.get(i,0)-ranks.get(i+1,0) for i in range(-1,top+1) if dims[i]-ranks.get(i,0)-ranks.get(i+1,0)}


def top_trace_under_swap(l):
    # The quotient cycle order is w,A0,B1,A2,... , opposite-end B_l,A_l, ... B0.
    L=2*l+3
    E={frozenset((i,(i+1)%L)) for i in range(L)}
    F=independence_faces(L,E)
    # w is 0; reflection swaps i with L-i.
    pi={i:(-i)%L for i in range(L)}
    val=-1
    for f in F:
        if not f:continue
        sf={pi[x] for x in f}
        if sf!=set(f):continue
        y=[pi[x] for x in f]
        inv=sum(y[i]>y[j] for i in range(len(y)) for j in range(i+1,len(y)))
        val+=(-1)**(len(f)-1+inv)
    # reduced Lefschetz = (-1)^(top dimension) * trace since homology is concentrated in top dim
    top=(2*(l//3)) if l%3==0 else (2*(l//3)+1)
    return (-1)**top*val


def expected_betti(l):
    k=l//3
    return ({2*k:2} if l%3==0 else {2*k+1:1})


def main():
    graph_cases=0; homology_cases=0; trace_cases=0
    for a in (1,2,3):
        for b in (1,2,3):
            for l in range(1,10):
                n,E=orbit_graph(a,b,l)
                assert n==2*l+3
                assert len(E)==n
                assert sorted(sum(i in e for e in E) for i in range(n)) == [2]*n
                graph_cases+=1
                if a==b:
                    n2,E2=orbit_graph(a,b,l,True)
                    assert n2==l+1 and len(E2)==l
                    assert sorted(sum(i in e for e in E2) for i in range(n2))==[1]*2+[2]*(n2-2)
                    graph_cases+=1
                if (a,b)==(2,3) and l<=8:
                    assert reduced_betti(n,E)==expected_betti(l)
                    homology_cases+=1
    for l in range(1,11):
        n,E=orbit_graph(2,2,l,True)
        expected=({} if l%3==0 else {l//3:1})
        assert reduced_betti(n,E)==expected
        homology_cases+=1
    for l in range(1,9):
        tr=top_trace_under_swap(l)
        expected=0 if l%3==0 else (-1)**(l//3+1)
        assert tr==expected,(l,tr,expected)
        trace_cases+=1
    print('PASS',graph_cases,'orbit graphs,',homology_cases,'homology cases,',trace_cases,'signed swap character checks')

if __name__=='__main__':main()
