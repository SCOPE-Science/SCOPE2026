"""Exact intersection checks for anticanonical classes of Schubert pencil surfaces.

The proof for all curves is geometric; the finite tests below are only regression checks.
"""
from fractions import Fraction as Q
from itertools import combinations, product

def intersection(a, b):
    assert len(a) == len(b)
    return a[0] * b[0] - sum(x*y for x,y in zip(a[1:],b[1:]))

def calc(sizes_by_eigenvalue, regular):
    # Each tuple lists distinct Jordan sizes for one eigenvalue.
    assert all(t and tuple(sorted(set(t))) == tuple(t) for t in sizes_by_eigenvalue)
    maxima = [t[-1] for t in sizes_by_eigenvalue]
    kappa = sum(maxima)
    if regular: assert kappa >= 2
    n = kappa + 1
    H = [Q(1)] + [Q(0)] * kappa
    L = [Q(1)] + [Q(-1)] * kappa
    K = [Q(-3)] + [Q(1)] * kappa
    zero = [Q(0)] * n
    if regular:
        r = kappa - 1
        discrepancy = Q(2-r, r)
        D = [(-x + discrepancy*y) for x,y in zip(K,L)]
        assert D == [2*H[j] + Q(2,r)*L[j] for j in range(n)]
        assert intersection(D,L) == 0
        assert intersection(D,D) == Q(4*kappa,r)
    else:
        D = [-x for x in K]
        assert D == [2*H[j] + L[j] for j in range(n)]
        assert intersection(D,L) == 3-kappa
        assert intersection(D,D) == 9-kappa
    assert intersection(L,L) == 1-kappa
    assert intersection(K,L) == kappa-3
    idx = 0
    zeros_on_Y = []
    for i,t in enumerate(sizes_by_eigenvalue):
        for j in range(1, t[-1]+1):
            A = zero.copy()
            A[idx+j] = Q(1)
            if j < t[-1]: A[idx+j+1] = Q(-1)
            assert intersection(A,A) == (-1 if j==t[-1] else -2)
            assert intersection(H,A) == 0
            assert intersection(L,A) == (1 if j==t[-1] else 0)
            value = intersection(D,A)
            assert value == (Q(2,kappa-1) if regular and j==t[-1]
                             else Q(1) if not regular and j==t[-1] else 0)
            # The j-th exceptional curve survives iff j is a distinct Jordan size.
            if j in t and value==0: zeros_on_Y.append((i,j))
        idx += t[-1]
    assert idx == kappa
    if not regular and kappa==3: zeros_on_Y.append(('infinity',0))
    weak = regular or kappa <= 3
    fano = ((regular or kappa <= 2) and
            all(len(t)==1 for t in sizes_by_eigenvalue))
    assert fano == (weak and not zeros_on_Y)
    return kappa, intersection(D,D), weak, fano, zeros_on_Y

assert calc([],False)[:4] == (0,Q(9),True,True)
assert calc([(1,),(1,)],True)[:4] == (2,Q(8),True,True)
assert calc([(2,)],True)[:4] == (2,Q(8),True,True)
assert calc([(1,2)],True)[:4] == (2,Q(8),True,False)
assert calc([(3,),(2,)],True)[:4] == (5,Q(5),True,True)
assert calc([(1,),(1,),(1,)],False)[:4] == (3,Q(6),True,False)
assert calc([(1,2)],False)[:4] == (2,Q(7),True,False)
assert calc([(4,)],False)[:4] == (4,Q(5),False,False)

# Exercise all distinct-size profiles through total blow-up count 6.
profiles=[()]
for _ in range(3):
    options=[tuple(t) for z in range(1,7) for ell in range(1,z+1)
             for t in combinations(range(1,z+1),ell) if t[-1]==z]
    profiles += [v for v in product(options,repeat=_+1)
                 if sum(w[-1] for w in v)<=6]
for profile in profiles:
    calc(profile,False)
    if sum(t[-1] for t in profile)>=2: calc(profile,True)
print('VERIFY_OK',len(profiles),'profiles')
