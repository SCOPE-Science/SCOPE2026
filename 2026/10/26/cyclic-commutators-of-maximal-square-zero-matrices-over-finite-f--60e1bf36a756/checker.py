#!/usr/bin/env python3
"""Independent small-field checks for the conditional cyclic-commutator law.
Uses only Python's standard library. Fields in this checker are prime fields.
"""
from itertools import product
from fractions import Fraction
from math import comb, prod


def matmul(a,b,q):
    n=len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)) for i in range(n))

def eye(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))

def rank_vectors(vectors,q):
    pivots={}
    for vec in vectors:
        v=list(vec)
        for j in sorted(pivots):
            if v[j]:
                s=v[j]
                pv=pivots[j]
                v=[(x-s*y)%q for x,y in zip(v,pv)]
        j=next((j for j,x in enumerate(v) if x),None)
        if j is None:
            continue
        inv=pow(v[j],-1,q)
        pivots[j]=[(inv*x)%q for x in v]
    return len(pivots)

def is_unit(t,q):
    return rank_vectors(t,q)==len(t)

def cyclic_commutator_type(t,q):
    """Compute minimal-polynomial degree via independent powers of diag(T,-T)."""
    m=len(t); cur=eye(m);vectors=[]
    for k in range(2*m):
        flat=[x for row in cur for x in row]
        vectors.append(tuple(flat+[(x if k%2==0 else -x)%q for x in flat]))
        cur=matmul(cur,t,q)
    return rank_vectors(vectors,q)==2*m

def pair_count(q,d):
    # Small-degree irreducible-orbit counts; no polynomial factorization assumption.
    if d==1: return (q-1)//2
    if d==2: return (q-1)**2//4
    if d==3: return (q**3-q)//6
    raise ValueError('Only small degrees required here')

def exact_cyclic_probability(q,m):
    if q % 2 == 0:
        return Fraction(0)
    # Truncated rational Euler factors, independently from matrix enumeration.
    coefficients=[Fraction(1)]+[Fraction(0)]*m
    for d in range(1,m+1):
        for _ in range(pair_count(q,d)):
            local=[Fraction(0)]*(m+1)
            local[0]=Fraction(1)
            for k in range(1,m//d+1):
                local[d*k]=Fraction(2,(q**d-1)*q**(d*(k-1)))
            coefficients=[sum(coefficients[j]*local[i-j] for j in range(i+1)) for i in range(m+1)]
    return coefficients[m]

def exhaustive_general_linear(q,m):
    hits=tot=0
    for flat in product(range(q),repeat=m*m):
        t=tuple(tuple(flat[m*i:m*(i+1)]) for i in range(m))
        if not is_unit(t,q): continue
        tot+=1
        hits+=cyclic_commutator_type(t,q)
    prediction=exact_cyclic_probability(q,m)
    assert Fraction(hits,tot)==prediction,(q,m,hits,tot,prediction)
    print(f'GL_CHECK q={q} m={m} cyclic={hits} total={tot} probability={prediction}')
    return tot

def is_sqzero(a,q):
    return matmul(a,a,q)==tuple(tuple(0 for _ in row) for row in a)

def rank(a,q):
    return rank_vectors(a,q)

def matdiff(a,b,q):
    n=len(a)
    return tuple(tuple((a[i][j]-b[i][j])%q for j in range(n)) for i in range(n))

def gaussian_middle(q,m):
    # [2m choose m]_q
    return prod(q**(2*m-i)-1 for i in range(m))//prod(q**(m-i)-1 for i in range(m))

def brute_squarezero_pairs(q,m):
    n=2*m; zero=tuple(tuple(0 for _ in range(n)) for _ in range(n))
    a_list=[]
    for flat in product(range(q),repeat=n*n):
        a=tuple(tuple(flat[n*i:n*(i+1)]) for i in range(n))
        if matmul(a,a,q)==zero and rank(a,q)==m:
            a_list.append(a)
    gl=prod(q**m-q**j for j in range(m))
    assert len(a_list)==gaussian_middle(q,m)*gl
    good=0
    for a in a_list:
        for b in a_list:
            c=matdiff(matmul(a,b,q),matmul(b,a,q),q)
            good+=rank(c,q)==n
    expected=gaussian_middle(q,m)*q**(m*m)*gl**2
    assert good==expected,(q,m,good,expected)
    print(f'SQZERO_PAIR_CHECK q={q} m={m} sqzero_matrices={len(a_list)} invertible_commutators={good} pairs={len(a_list)**2}')
    return len(a_list)**2

if __name__=='__main__':
    units=0
    for q,m in [(2,1),(3,1),(5,1),(2,2),(3,2),(5,2),(7,2),(2,3),(3,3)]:
        units+=exhaustive_general_linear(q,m)
    pairs=brute_squarezero_pairs(2,1)+brute_squarezero_pairs(3,1)+brute_squarezero_pairs(2,2)
    print(f'ALL_CYCLIC_SQUAREZERO_COMMUTATOR_CHECKS_PASSED units={units} pairs={pairs}')
