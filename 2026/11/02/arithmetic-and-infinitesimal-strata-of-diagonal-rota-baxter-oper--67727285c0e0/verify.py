"""Independent exact finite-field checks for diagonal Rota--Baxter operators on cycle evolution algebras.
Pure Python, standard library only. Run: python verify.py
"""
from itertools import product
from math import gcd


def ff(p, x):
    return x % p


def rank_mod(mat, p):
    a = [[x % p for x in row] for row in mat]
    m = len(a); n = len(a[0]); rank = 0
    for j in range(n):
        k = next((k for k in range(rank, m) if a[k][j]), None)
        if k is None: continue
        a[rank], a[k] = a[k], a[rank]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [(x*inv)%p for x in a[rank]]
        for k in range(m):
            if k != rank and a[k][j]:
                v = a[k][j]
                a[k] = [(x-v*y)%p for x,y in zip(a[k], a[rank])]
        rank += 1
    return rank


def is_rb(r, lam, p):
    n=len(r)
    # Verify the defining Rota-Baxter identity on all pairs of natural basis vectors.
    for i in range(n):
        for j in range(n):
            left=[0]*n; right=[0]*n
            if i == j:
                left[(i+1)%n] = r[i]*r[i] % p
                right[(i+1)%n] = (2*r[i]+lam)*r[(i+1)%n] % p
            if left != right: return False
    return True


def jacobian(r, lam, p):
    n=len(r); a=[[0]*n for _ in range(n)]
    for i in range(n):
        a[i][i] += 2*(r[i]-r[(i+1)%n])
        a[i][(i+1)%n] -= (2*r[i]+lam)
    return a


def predicted(p,n,lam):
    M=2**n-1
    if lam:
        g=gcd(M,p-1)
        count=g+1
        orbits=1 + sum(gcd(g,2**s-1) for s in range(n))//n
        return count,orbits
    if (2**n-1)%p:
        return 1,1
    d=1
    while pow(2,d,p)!=1:
        d+=1
    return p,1+(p-1)//d


def trial(p,n,lam):
    points=[r for r in product(range(p), repeat=n) if is_rb(r,lam,p)]
    actual={r for r in points}
    expected_n, expected_o=predicted(p,n,lam)
    assert len(actual)==expected_n,(p,n,lam,len(actual),expected_n)
    seen=set(); orbit_sizes=[]
    for r in actual:
        if r in seen: continue
        orbit={r[i:]+r[:i] for i in range(n)}
        seen |= orbit; orbit_sizes.append(len(orbit))
    assert seen==actual and len(orbit_sizes)==expected_o,(p,n,lam,orbit_sizes,expected_o)
    for r in actual:
        tdim=n-rank_mod(jacobian(r,lam,p),p)
        if lam:
            # There is a unique reduced zero point and the reduced all-minus-lambda point.
            special=all(v==0 for v in r) or all(v==-lam%p for v in r)
            expected_tdim = 0 if special else (1 if (2**n-1)%p==0 else 0)
            assert tdim==expected_tdim,(p,n,lam,r,tdim,expected_tdim)
    return len(actual),len(orbit_sizes)

if __name__=='__main__':
    runs=0
    for p in (2,3,5,7,11,13,17):
        for n in range(3,7):
            if p**n>150000: continue
            for lam in (0,1):
                trial(p,n,lam)
                runs+=1
    assert trial(7,3,0)==(7,3)
    assert trial(7,3,1)==(2,2)
    assert trial(7,6,1)==(4,3)
    print('VERIFY_OK prime_field_parameter_cases=',runs)

def mul_f2e(a,b,m,poly):
    z=0
    while b:
        if b & 1: z ^= a
        b >>= 1; a <<= 1
        if a & (1<<m): a ^= poly
    return z

def trial_binary_extension(m, poly, n):
    q=2**m; sq=lambda t:mul_f2e(t,t,m,poly)
    vals=[]
    for r in product(range(q), repeat=n):
        if all(sq(r[i])==r[(i+1)%n] for i in range(n)):
            vals.append(r)
    g=gcd(2**n-1,q-1)
    assert len(vals)==g+1,('extension',q,n,len(vals),g+1)
    seen=set();count=0
    for r in vals:
        if r not in seen:
            count+=1
            seen.update(r[i:]+r[:i] for i in range(n))
    expected=1+sum(gcd(g,2**i-1) for i in range(n))//n
    assert count==expected,('extension-orbits',q,n,count,expected)
    return len(vals),count

if __name__=='__main__':
    assert trial_binary_extension(2,0b111,3)==(2,2)
    assert trial_binary_extension(3,0b1011,3)==(8,4)
    assert trial_binary_extension(4,0b10011,4)==(16,6)
    print('VERIFY_OK extension_field_cases=3')
