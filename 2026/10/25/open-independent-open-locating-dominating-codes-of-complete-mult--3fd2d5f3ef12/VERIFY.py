#!/usr/bin/env python3
"""Direct computational checks of the multipartite line-graph formula.

The code concerns only simple finite graphs. Run: python verify_old_oind_multipartite.py.
"""
from itertools import combinations
from functools import lru_cache
from math import factorial
from fractions import Fraction


def partitions(n, floor=1):
    if n==0:
        yield ()
    for x in range(floor,n+1):
        for rest in partitions(n-x,x):
            yield (x,)+rest


def multipartite(parts):
    colors = tuple(i for i, size in enumerate(parts) for _ in range(size))
    edges = tuple((i,j) for i in range(len(colors)) for j in range(i+1,len(colors)) if colors[i]!=colors[j])
    return colors,edges


def old_oind(S, edges):
    # Open neighborhood in line graph of G. S is the list of chosen edge indices.
    sets = []
    active = set(S)
    for p,(a,b) in enumerate(edges):
        neighbors = frozenset(j for j in active if j!=p and (a in edges[j] or b in edges[j]))
        if not neighbors: return False
        if p in active and len(neighbors)!=1: return False
        sets.append(neighbors)
    return len(set(sets)) == len(sets)


def enumeration(parts):
    colors,edges=multipartite(parts)
    N=len(colors)
    k=N//3
    if k == 0: return 0, set()
    known=set()
    # Independent graph code criterion: 1-neighbor each selected => 2j selected edges.
    # j can be 1..floor(N/3), checked without assuming any further theorem.
    for j in range(1,k+1):
        for S in combinations(range(len(edges)),2*j):
            if old_oind(S,edges):known.add(S)
    return len(known),known


def exact_factor_count(colors):
    N=len(colors)
    @lru_cache(None)
    def rec(vertices):
        if not vertices:return 1
        a=vertices[0]
        ans=0
        for b,c in combinations(vertices[1:],2):
            triple=(a,b,c)
            w=sum(all(colors[center]!=colors[v] for v in triple if v!=center) for center in triple)
            if w:
                rem=tuple(t for t in vertices if t not in triple)
                ans+=w*rec(rem)
        return ans
    return rec(tuple(range(N)))


def egf_coefficient(parts):
    """Coefficient of exp(Q) multiplied by product of part factorials.

    Q=sum_{i!=j} x_i^2*x_j/2 + 3*sum_{i<j<k}x_i*x_j*x_k.
    Uses exact rational arithmetic; Q is homogeneous of degree three.
    """
    r=len(parts)
    N=sum(parts)
    if N%3:return 0
    k=N//3
    if k==0:return 1
    monomials=[]
    for i in range(r):
        for j in range(r):
            if i!=j:
                v=[0]*r;v[i]=2;v[j]=1
                monomials.append((tuple(v),Fraction(1,2)))
    for i,j,h in combinations(range(r),3):
        v=[0]*r;v[i]=v[j]=v[h]=1
        monomials.append((tuple(v),Fraction(3)))
    polynomial={(0,)*r:Fraction(1)}
    for _ in range(k):
        new={}
        for exponent,coefficient in polynomial.items():
            for vector,weight in monomials:
                e=tuple(a+b for a,b in zip(exponent,vector))
                if all(e[i]<=parts[i] for i in range(r)):
                    new[e]=new.get(e,Fraction(0))+coefficient*weight
        polynomial=new
    coefficient=polynomial.get(tuple(parts),Fraction(0))/factorial(k)
    answer=coefficient
    for x in parts:answer*=factorial(x)
    assert answer.denominator==1
    return int(answer)


def predicted(parts):
    N=sum(parts)
    if N%3==2:return 0
    if N%3==0:
        if max(parts)>2*(N//3):return 0
        return egf_coefficient(parts)
    k=(N-1)//3
    if k<1:return 0
    return sum(factorial(2*k+1)//2**k for a in parts if a==2*k+1)


def run():
    profiles=0
    total_candidates=0
    for N in range(3,9):
        for parts in partitions(N):
            if len(parts)<2:continue
            actual,S=enumeration(parts)
            expected=predicted(parts)
            if actual!=expected:raise AssertionError((parts, actual,expected,S))
            if N%3==0:
                assert expected==exact_factor_count(tuple(i for i,a in enumerate(parts) for _ in range(a)))
            profiles+=1
            total_candidates+=actual
            if N==6:
                print('N=6',parts,'count=',actual)
    print('PASS',profiles,'integer-partition profiles with 3<=N<=8; sum of actual valid codes',total_candidates)
    for n in (3,6,9):
        if n!=9:
            actual,_=enumeration((1,)*n)
            assert actual==factorial(n)//(2**(n//3)*factorial(n//3))
    print('PASS triangular graphs n=3 and n=6')
    # Deliberately cross-check exceptional family nontrivially for n=7.
    for parts in ((5,2),(5,1,1)):
        actual,_=enumeration(parts)
        assert actual==30
    print('PASS one-uncovered examples K(5,2), K(5,1,1): 30 codes each')

if __name__=='__main__':run()
