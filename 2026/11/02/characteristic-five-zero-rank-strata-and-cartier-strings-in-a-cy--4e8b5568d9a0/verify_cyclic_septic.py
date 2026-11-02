#!/usr/bin/env python3
"""Exact check of characteristic-five Cartier formulas for a cyclic septic cover.

Uses only Python's standard library.  Coefficients are polynomials in L over F_5.
"""
from math import comb
P = 5

def add(a, b):
    r = dict(a)
    for mon, c in b.items():
        z = (r.get(mon, 0) + c) % P
        if z: r[mon] = z
        else: r.pop(mon, None)
    return r

def mul(a, b):
    r = {}
    for (x, l), c in a.items():
        for (xx, ll), d in b.items():
            mon = (x + xx, l + ll)
            z = (r.get(mon, 0) + c*d) % P
            if z: r[mon] = z
            else: r.pop(mon, None)
    return r

def power(a, n):
    r = {(0, 0): 1}
    for _ in range(n): r = mul(r, a)
    return r

X = {(1, 0): 1}
Xm1 = {(1, 0): 1, (0, 0): 4}
XmL = {(1, 0): 1, (0, 1): 4}
F = mul(mul(X, Xm1), power(XmL, 6))

def expected_scalar(j):
    Q = {(0, 0): 1, (0, 1): 4, (0, 2): 1}
    R = {(0, 0): 4, (0, 1): 2} # 2(L+2)
    if j in (1, 6): return Q
    if j in (3, 4): return R
    return {(0, 0): 1}

def coefficient_by_binomial(j, exponent):
    jj = (3*j) % 7
    k = (5*jj-j)//7
    e = 6*k+j-1
    wanted = exponent-k
    ans = {}
    for a in range(k+1):
        b = wanted-a
        if not 0 <= b <= e: continue
        c = comb(k,a)*comb(e,b)*(-1)**(k-a+e-b)
        mon = (0, e-b)
        ans = add(ans, {mon: c%P})
    return ans

def coefficient_by_expansion(poly, exp):
    return {(0, ell):c for (x,ell),c in poly.items() if x==exp}

def target_coefficient(H, jtarget, t):
    # H(L)*binomial(jtarget-1,t)*(-L^5)^(jtarget-1-t)
    c = comb(jtarget-1, t)*(-1)**(jtarget-1-t)
    term = {(0, 5*(jtarget-1-t)): c%P}
    return mul(H, term)

for j in range(1,7):
    target = (3*j)%7
    k = (5*target-j)//7
    G = mul(power(XmL,j-1),power(F,k))
    H = expected_scalar(j)
    max_t = max((i-4)//5 for i, l in G if i % 5 == 4) if any(i%5==4 for i,l in G) else -1
    assert max_t == target-1,(j,max_t,target)
    for t in range(target):
        a = coefficient_by_expansion(G,5*t+4)
        b = coefficient_by_binomial(j,5*t+4)
        c = target_coefficient(H,target,t)
        assert a == b == c,(j,t,a,b,c)
    print('CARTIER_COEFFICIENT_OK',j,'->',target,'k',k,'dimension',1)

# The directed permutation is one six-cycle.  Each zero scalar kills one arrow.
sigma={j:(3*j)%7 for j in range(1,7)}
assert len({sigma[j] for j in sigma})==6

def ranks(zero_set):
    out=[]
    for r in range(7):
        rank=0
        for start in range(1,7):
            j=start
            good=True
            for i in range(r):
                if j in zero_set:
                    good=False
                    break
                j=sigma[j]
            rank+=int(good)
        out.append(rank)
    return out
assert ranks(set())==[6]*7
assert ranks({3,4}) == [6,4,2,0,0,0,0]
assert ranks({1,6}) == [6,4,2,0,0,0,0]
# The two factors are separable, coprime and avoid the boundary lambda=0,1.
# The quadratic L^2-L+1 has discriminant -3=2, a nonsquare in F_5.
assert {z*z % 5 for z in range(5)} == {0,1,4}
assert all((z*z-z+1)%5 for z in range(5))
assert (-2)%5 not in (0,1)
assert ((-2)**2 - (-2) + 1)%5 != 0
# Invariant t=L(1-L): Q=1-t and (L+2)^2=4-t modulo 5.
# Compare polynomials in L rather than numerical surrogates.
t={(0,1):1,(0,2):4}  # L(1-L)
one_minus_t=add({(0,0):1},{mon:(-c)%5 for mon,c in t.items()})
four_minus_t=add({(0,0):4},{mon:(-c)%5 for mon,c in t.items()})
assert one_minus_t==expected_scalar(1)
assert four_minus_t==power({(0,1):1,(0,0):2},2)
print('STRATA_OK: generic ordinary, exceptional Cartier ranks 6/4/2/0, p-rank zero, a-number two')
print('MODULI_OK: one F5 exceptional parameter and a conjugate F25 pair, invariant t=4 or t=1')
