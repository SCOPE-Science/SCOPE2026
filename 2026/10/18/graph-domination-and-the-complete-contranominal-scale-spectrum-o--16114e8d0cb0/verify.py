#!/usr/bin/env python3
"""Independent finite checks of complement-incidence Boolean-scale formulas.

Uses only the Python standard library.  No assumptions about graph isomorphism.
"""
from itertools import combinations
from collections import defaultdict


def edge_list(n):
    return list(combinations(range(n), 2))


def degree_into(v, chosen, edges):
    return sum(1 for a,b in edges if (a == v and b in chosen) or (b == v and a in chosen))


def profile_from_domination(n, edges):
    answer = [0] * (n+1)
    for a_mask in range(1 << n):
        A = {i for i in range(n) if (a_mask >> i) & 1}
        D = set(range(n)) - A
        weight = 1
        for a in A:
            weight *= degree_into(a,D,edges)
        answer[len(A)] += weight
    return tuple(answer)


def profile_from_submatrices(n, edges):
    answer = [0] * (n+1)
    answer[0] = 1  # conventional empty scale
    vertices = tuple(range(n))
    for k in range(1,n+1):
        for A_tuple in combinations(vertices,k):
            A = set(A_tuple)
            for Es in combinations(edges,k):
                touches = []
                for u,v in Es:
                    w = A.intersection((u,v))
                    if len(w)!=1:
                        break
                    touches.append(next(iter(w)))
                else:
                    if len(set(touches)) == k:
                        answer[k] += 1
    return tuple(answer)


def domination_number(n, edges):
    vertices = tuple(range(n))
    for k in range(n+1):
        for Ds in combinations(vertices,k):
            D = set(Ds)
            if all(v in D or degree_into(v,D,edges)>0 for v in vertices):
                return k
    raise AssertionError('Every finite graph admits its entire vertex set')


def closed_intents(n, edges):
    full = (1<<n)-1
    columns = [full ^ (1<<u) ^ (1<<v) for u,v in edges]
    intents={full}
    for col in columns:
        intents |= {s & col for s in list(intents)}
    return intents


def is_star(n, edges):
    if n < 2 or len(edges)!=n-1:
        return False
    return any(all(v in edge for edge in edges) for v in range(n))


def is_universal(n, edges):
    return any(sum(v in e for e in edges)==n-1 for v in range(n))


def mulpoly(a,b):
    d=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items():
            d[i+j]+=x*y
    return {i:x for i,x in d.items() if x}


def matmul(a,b):
    size=len(a)
    c=[[{} for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            v=defaultdict(int)
            for k in range(size):
                for exp,coeff in mulpoly(a[i][k],b[k][j]).items():
                    v[exp]+=coeff
            c[i][j]={exp:coeff for exp,coeff in v.items() if coeff}
    return c


def plus(a,b):
    o=defaultdict(int,a)
    for k,v in b.items():o[k]+=v
    return {k:v for k,v in o.items() if v}


def scale(a,powr,coeff):
    return {k+powr:v*coeff for k,v in a.items()}


states=[(0,0),(0,1),(1,0),(1,1)]
t=[ [{} for j in range(4)] for i in range(4) ]
for i,(a,b) in enumerate(states):
    for j,(bb,c) in enumerate(states):
        if b != bb:continue
        if b==1:t[i][j]={0:1}
        elif a+c:t[i][j]={1:a+c}


def polynomial_from_transfer(n,cycle):
    identity=[[{0:1} if i==j else {} for j in range(4)] for i in range(4)]
    w=identity
    for _ in range(n):w=matmul(w,t)
    if cycle:
        out={}
        for i in range(4):out=plus(out,w[i][i])
    else:
        out={}
        for i in (0,1):
            for j in (0,2):out=plus(out,w[i][j])
    return tuple(out.get(k,0) for k in range(n+1)),w


def edges_path(n):return [(i,i+1) for i in range(n-1)]
def edges_cycle(n):return edges_path(n)+[(n-1,0)]


def run():
    graph_cases=0
    scale_submatrix_tests=0
    concept_tests=0
    for n in range(1,6):
        universe=edge_list(n)
        for mask in range(1<<len(universe)):
            edges=[e for j,e in enumerate(universe) if mask>>j&1]
            p=profile_from_domination(n,edges)
            q=profile_from_submatrices(n,edges)
            assert p==q,(n,edges,p,q)
            k=max(j for j,x in enumerate(q) if x)
            assert k==n-domination_number(n,edges),(n,edges,k)
            L=len(closed_intents(n,edges))
            assert L>=2**k,(n,edges,L,k)
            if n>=2 and is_universal(n,edges):
                assert (L == 2**(n-1)) == is_star(n,edges),(n,edges,L)
            graph_cases+=1
            scale_submatrix_tests+=sum(q[1:])
            concept_tests+=L

    path_cycles=0
    for n in range(1,12):
        brute=profile_from_domination(n,edges_path(n))
        transfer,_=polynomial_from_transfer(n,False)
        assert brute==transfer,(n,'P',brute,transfer)
        assert max(j for j,x in enumerate(brute) if x) == n-(n+2)//3
        path_cycles+=1
        if n>=3:
            brute=profile_from_domination(n,edges_cycle(n))
            transfer,_=polynomial_from_transfer(n,True)
            assert brute==transfer,(n,'C',brute,transfer)
            assert max(j for j,x in enumerate(brute) if x) == n-(n+2)//3
            path_cycles+=1

    for n in range(2,9):
        edges=edge_list(n)
        direct=profile_from_domination(n,edges)
        from math import comb
        expected=tuple(comb(n,k)*(n-k)**k if k<n else 0 for k in range(n+1))
        assert direct==expected,(n,'K',direct,expected)
        stars=edges_path(2) if n==2 else [(0,j) for j in range(1,n)]
        direct=profile_from_domination(n,stars)
        expected=[0]*(n+1)
        expected[0]=1
        for k in range(1,n):
            expected[k]=comb(n-1,k)+(n-1 if k==1 else 0)
        assert direct==tuple(expected),(n,'star',direct,expected)

    ident=[[{0:1} if i==j else {} for j in range(4)] for i in range(4)]
    powers=[ident]
    for i in range(4):powers.append(matmul(powers[-1],t))
    for i in range(4):
        for j in range(4):
            rhs=plus(plus(powers[3][i][j],scale(powers[2][i][j],1,2)),scale(powers[1][i][j],2,1))
            assert powers[4][i][j]==rhs,(i,j,powers[4][i][j],rhs)

    print('VERIFY_OK labeled_graphs=',graph_cases,'submatrix_witnesses=',scale_submatrix_tests,
          'concept_totals=',concept_tests,'path_cycle_profiles=',path_cycles,
          'max_n=11','complete_star_max_n=8','transfer_matrix_identity=PASS')

if __name__=='__main__':run()
