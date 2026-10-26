"""Finite checks of monomial stabilizers of perfect evolution algebras.
Only prime fields are needed for these independent small-dimensional checks.
Run: python3 check_generic_evolution.py
"""
from itertools import product, permutations
from collections import Counter
from math import factorial


def is_invertible(entries, q, n):
    rows = [list(entries[i*n:(i+1)*n]) for i in range(n)]
    rank = 0
    for c in range(n):
        pivot = next((i for i in range(rank,n) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][c], -1, q)
        rows[rank] = [(x*scale) % q for x in rows[rank]]
        for i in range(rank+1,n):
            factor = rows[i][c]
            if factor:
                rows[i] = [(x-factor*y) % q for x,y in zip(rows[i],rows[rank])]
        rank += 1
    return rank == n


def check(q,n):
    assert q in (2,3)
    automorphisms = []
    for perm in permutations(range(n)):
        for t in product(range(1,q), repeat=n):
            automorphisms.append((perm, t))
    assert len(automorphisms)==factorial(n)*(q-1)**n
    size, exceptional, stabilizer_sum = 0,0,0
    profile = Counter()
    for entries in product(range(q), repeat=n*n):
        if not is_invertible(entries,q,n):
            continue
        size+=1
        s=0
        for perm,t in automorphisms:
            if all((entries[perm[i]*n+perm[j]]*t[j]*t[j]-entries[i*n+j]*t[i])%q==0 for i in range(n) for j in range(n)):
                s+=1
        assert s>=1
        stabilizer_sum+=s
        exceptional+=(s>1)
        profile[s]+=1
    G=len(automorphisms)
    assert stabilizer_sum%G==0
    classes=stabilizer_sum//G
    print('q=',q,'n=',n,'GL=',size,'G=',G,'orbits=',classes,'exceptional_matrices=',exceptional,'stabilizer_profile=',sorted(profile.items()))
    return q,n,size,G,classes,exceptional,profile

if __name__ == '__main__':
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
        check(q,n)
    print('VERIFY_OK')
