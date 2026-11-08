"""Independent finite checks for the edge-subdivision controllability theorem.

Run: python3 verify.py. Requires only the Python standard library.
Finite-field Krylov computations test sampled/exhaustive instances, not an infinite proof.
"""
from itertools import combinations
from math import comb
from random import Random

PRIME = 1000000007

def laplacian(p, q):
    n = p + q + p*q
    L = [[0]*n for _ in range(n)]
    for i in range(p):
        for j in range(q):
            e = p+q+i*q+j
            for v in (i,p+j):
                L[e][e] += 1
                L[v][v] += 1
                L[v][e] -= 1
                L[e][v] -= 1
    return L

def matrix_times(L, v):
    return [sum(a*b for a,b in zip(row,v)) % PRIME for row in L]

def controllable_mod_prime(L, selected):
    """Exact rank over a fixed prime field, via the Krylov basis."""
    n = len(L)
    pivot = {}
    def insert(vec):
        v = vec[:]
        while True:
            lead = next((i for i,z in enumerate(v) if z%PRIME), None)
            if lead is None: return False
            if lead in pivot:
                row=pivot[lead]
                coefficient=v[lead]
                v=[(a-coefficient*b)%PRIME for a,b in zip(v,row)]
            else:
                inv=pow(v[lead], -1, PRIME)
                pivot[lead]=[(a*inv)%PRIME for a in v]
                return True
    for start in selected:
        v=[int(i==start) for i in range(n)]
        for _ in range(n):
            if len(pivot)==n: return True
            insert(v)
            v=matrix_times(L,v)
    return len(pivot)==n

def is_forest(p, q, edges):
    par = list(range(p+q))
    def find(x):
        while x!=par[x]:
            x=par[x]
        return x
    for i,j in edges:
        a,b=find(i),find(p+j)
        if a==b:return False
        par[a]=b
    return True

def expected(p,q,selected):
    e0=p+q
    S=set(selected)
    remaining=[(i,j) for i in range(p) for j in range(q) if e0+i*q+j not in S]
    return is_forest(p,q,remaining) and (p!=q or any(i in S for i in range(e0)))

def verify_exhaustive(p,q):
    L=laplacian(p,q);n=len(L);k=0
    for mask in range(1<<n):
        selected=[i for i in range(n) if mask>>i&1]
        pred=expected(p,q,selected)
        actual=controllable_mod_prime(L,selected)
        assert pred==actual,(p,q,mask,pred,actual)
        k+=1
    return k

def verify_trees(p,q, cap=100):
    es=[(i,j) for i in range(p) for j in range(q)]
    L=laplacian(p,q);count=0;checks=0
    for inds in combinations(range(p*q),p+q-1):
        if not is_forest(p,q,[es[i] for i in inds]):continue
        count+=1
        controls=[p+q+i for i in range(p*q) if i not in inds]
        assert len(controls)==(p-1)*(q-1)
        if count <= cap:
            if p==q:
                assert not controllable_mod_prime(L,controls)
                for v in range(p+q):
                    assert controllable_mod_prime(L,controls+[v])
                    checks+=1
            else:
                assert controllable_mod_prime(L,controls)
                checks+=1
    assert count==p**(q-1)*q**(p-1), (p,q,count)
    return count,checks

def verify_random(p,q,trials):
    rng=Random(93000 + 37*p + q)
    L=laplacian(p,q);n=len(L)
    for _ in range(trials):
        mask=rng.getrandbits(n)
        selected=[i for i in range(n) if mask>>i&1]
        assert expected(p,q,selected)==controllable_mod_prime(L,selected)
    return trials

if __name__=='__main__':
    checks=0
    for p,q in [(2,2)]:
        k=verify_exhaustive(p,q)
        print('EXHAUSTIVE',p,q,k)
        checks+=k
    for p,q in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        n,k=verify_trees(p,q,cap=15 if max(p,q)>=4 else 40)
        print('TREE_COMPLEMENTS',p,q,n,'CONTROL_CHECKS',k)
        checks+=k
    for p,q in [(2,3),(3,3),(3,4),(4,4)]:
        k=verify_random(p,q,15)
        print('SAMPLED_ALL_SUBSETS',p,q,k)
        checks+=k
    print('VERIFIED',checks)
