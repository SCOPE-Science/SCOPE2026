#!/usr/bin/env python3
from fractions import Fraction

NMAX = 5000
KS = range(2, 7)
TS = [Fraction(-199,100), Fraction(-3,2), Fraction(-1,2), Fraction(0), Fraction(1), Fraction(7)]

def factor(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def is_prime(n):
    if n < 2:
        return False
    f = factor(n)
    return len(f) == 1 and next(iter(f.values())) == 1

def mu(n):
    f = factor(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1

def jordan(n, k):
    ans = n**k
    for p in factor(n):
        ans = (ans // (p**k)) * (p**k - 1)
    return ans

def sigma_inv(n, k):
    ans = 1
    for p, e in factor(n).items():
        q = p**k
        if e == 1:
            ans *= -(q + 1)
        elif e == 2:
            ans *= q
        else:
            return 0
    return ans

def P(n, k, t):
    return Fraction(sigma_inv(n,k) + jordan(n,k) + 2) + t*(mu(n)+1)

def cube_free_nonsquarefree(n):
    exps = list(factor(n).values())
    return bool(exps) and max(exps) <= 2 and any(e == 2 for e in exps)

prime_list = [n for n in range(1, NMAX+1) if is_prime(n)]
case3 = 0
for k in KS:
    for t in TS:
        zeros = [n for n in range(1, NMAX+1) if P(n,k,t) == 0]
        assert zeros == prime_list, (k,t,zeros[:20])
    boundary = [n for n in range(1, NMAX+1) if P(n,k,Fraction(-2)) == 0]
    assert boundary == [1] + prime_list, (k,boundary[:20])
    for n in range(2, NMAX+1):
        if cube_free_nonsquarefree(n):
            h = sigma_inv(n,k) + jordan(n,k) + 2
            assert h >= 6, (k,n,h)
            case3 += 1
print(f"VERIFY_OK k=2..6 n=1..{NMAX} t_cases={len(TS)} boundary_t=-2 case3_checks={case3}")
