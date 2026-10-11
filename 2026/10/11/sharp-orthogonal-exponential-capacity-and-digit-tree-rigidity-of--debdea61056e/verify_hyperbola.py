"""Exact cyclotomic checks for orthogonal exponentials on a modular hyperbola.

Run with Python 3.9+. No third-party packages are needed.
"""
from itertools import combinations


def is_zero_exact(p, k, a, b):
    """Decide sum_{x unit} zeta_(p^k)^(a*x+b/x)==0 over Q."""
    n = p ** k
    c = [0] * n
    for x in range(1, n):
        if x % p:
            c[(a*x + b*pow(x, -1, n)) % n] += 1
    q = n // p
    # Minimal polynomial: Phi_(p^k)(X)=sum_{j=0}^{p-1}X^(j*q).
    return all(c[r + j*q] == c[r] for r in range(q) for j in range(1, p))


def is_zero_predicted(p, k, a, b):
    n = p**k
    a %= n
    b %= n
    if not a and not b:
        return False
    v = 0
    while a % p == 0 and b % p == 0:
        a //= p
        b //= p
        v += 1
    if v == k - 1:
        return False
    aa, bb = a % p, b % p
    return aa == 0 or bb == 0 or pow(aa*bb % p, (p-1)//2, p) == p-1


def zero_table_test(p, k):
    n = p**k
    z = 0
    for a in range(n):
        for b in range(n):
            actual = is_zero_exact(p, k, a, b)
            expected = is_zero_predicted(p, k, a, b)
            if actual != expected:
                raise AssertionError((p,k,a,b,actual,expected))
            z += actual
    return z


def extremal_family_test(p,k):
    n=p**k
    L=[(j,0) for j in range(p**(k-1))]
    for (a,b),(c,d) in combinations(L,2):
        if not is_zero_exact(p,k,a-c,b-d):
            raise AssertionError(('family',p,k,a,b,c,d))
    return len(L)


def compatible_digits(p):
    q=lambda u,v: (u[0]-v[0])*(u[1]-v[1])%p
    return {(a,b): (q(a,b) == 0 or pow(q(a,b),(p-1)//2,p)==p-1)
            for a in [(x,y) for x in range(p) for y in range(p)]
            for b in [(x,y) for x in range(p) for y in range(p)] if a != b}


def count_digit_cliques(p):
    # Exact combinatorial census for small p, no scientific argument relies on it.
    vertices = [(x,y) for x in range(p) for y in range(p)]
    good=compatible_digits(p)
    ans=0
    for S in combinations(vertices,p):
        if all(good[(a,b)] for a,b in combinations(S,2)):
            ans+=1
    return ans


if __name__=='__main__':
    cases=[(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,2)]
    for p,k in cases:
        z=zero_table_test(p,k)
        n=extremal_family_test(p,k)
        print(f'EXACT_CYCLOTOMIC p={p} k={k} frequency_pairs={p**(2*k)} zeros={z} sharp_family={n}')
    for p in (3,5):
        print('EXHAUSTIVE_DIGIT_CLIQUES',p,count_digit_cliques(p))
    print('VERIFY_OK')
