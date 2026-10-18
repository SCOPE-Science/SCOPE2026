"""Independent finite checks of adjacency types and dihedral orbits of simple cycles.
Run: python check_cycle_types.py
Only the Python standard library is required.
"""
from itertools import permutations, product
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def stirling(k,j):
    if k == j == 0: return 1
    if k == 0 or j == 0 or j > k: return 0
    return stirling(k-1,j-1)+j*stirling(k-1,j)

@lru_cache(None)
def forest_count(j,r):
    if j == r == 0: return 1
    if j == 0 or r == 0 or r > j: return 0
    return sum(comb(j-1,s-1)*(1 if s==1 else factorial(s)//2)*forest_count(j-s,r-1) for s in range(1,j+1))

def inj_formula(n,j):
    assert 1 <= j <= n
    if j==n: return factorial(n-1)//2
    return sum(forest_count(j,r) for r in range(1,min(j,n-j)+1))

def full_types(n,k):
    return sum(stirling(k,j)*inj_formula(n,j) for j in range(1,min(n,k)+1))

def orbit_formula(n,k):
    result=1+stirling(k,2)*(n//2)
    for j in range(3,min(k,n)+1):
        falling=1
        for t in range(j): falling*=n-t
        assert falling%(2*n)==0
        result+=stirling(k,j)*(falling//(2*n))
    return result

def inj_direct(n,j):
    types=set()
    for a in permutations(range(n),j):
        bits=0; pos=0
        for u in range(j):
            for v in range(u+1,j):
                if (a[u]-a[v])%n in (1,n-1):bits|=1<<pos
                pos+=1
        types.add(bits)
    return len(types)

def orbits_direct(n,k):
    canons=set()
    for a in product(range(n),repeat=k):
        images=[]
        for s in range(n):
            images.append(tuple((v+s)%n for v in a))
            images.append(tuple((s-v)%n for v in a))
        canons.add(min(images))
    return len(canons)

def run():
    inj_cases=0;inj_assignments=0
    for n in range(3,11):
        for j in range(1,min(n,5)+1):
            d=inj_direct(n,j)
            f=inj_formula(n,j)
            assert d==f,(n,j,d,f)
            inj_cases+=1
            v=1
            for x in range(j):v*=n-x
            inj_assignments+=v
    orbit_cases=0;orbit_tuples=0
    for n in range(3,9):
        for k in range(1,5):
            d=orbits_direct(n,k)
            f=orbit_formula(n,k)
            assert d==f,(n,k,d,f)
            orbit_cases+=1; orbit_tuples+=n**k
    for k in range(2,7):
        stable=sum(stirling(k,j)*sum(forest_count(j,r) for r in range(1,j+1)) for j in range(1,k+1))
        for n in range(3,2*k+5):
            f=full_types(n,k)
            assert (f==stable)==(n>=2*k),(n,k,f,stable)
    print('VERIFY_OK',f'injective_cases={inj_cases}',f'injective_assignments={inj_assignments}',f'dihedral_cases={orbit_cases}',f'orbit_tuples={orbit_tuples}', 'sharp_cutoff_k2..6=YES', 'cycle3_k3=',full_types(3,3),'cycle5_k3=',full_types(5,3),'cycle6_k3=',full_types(6,3))

if __name__=='__main__':run()
