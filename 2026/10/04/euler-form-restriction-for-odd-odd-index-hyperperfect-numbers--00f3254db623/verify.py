#!/usr/bin/env python3
from math import isqrt

def factor(n):
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def sigma_from_factor(f):
    s = 1
    for p,a in f.items():
        s *= (p**(a+1)-1)//(p-1)
    return s

def v2(x):
    c = 0
    while x % 2 == 0:
        c += 1
        x //= 2
    return c

def check_structure(n, k):
    f = factor(n)
    s = sigma_from_factor(f)
    assert n == 1 + k*(s-n-1)
    assert v2(s) == 1
    odd = [(p,a) for p,a in f.items() if a % 2]
    assert len(odd) == 1
    q,a = odd[0]
    assert q % 4 == 1 and a % 4 == 1

def main():
    found = []
    limit = 400000
    for n in range(9, limit+1, 2):
        f = factor(n)
        if len(f) == 1:
            continue
        s = sigma_from_factor(f)
        den = s-n-1
        if den > 0 and (n-1) % den == 0:
            k = (n-1)//den
            if k > 1 and k % 2 == 1:
                check_structure(n,k)
                found.append((n,k))
    known = [(325,3),(10693,11),(51301,19),(214273,31),(306181,35)]
    for n,k in known:
        check_structure(n,k)
    print("VERIFY_OK", f"limit={limit}", f"odd_index_hits={len(found)}",
          f"first_hits={found[:8]}", f"known_checked={len(known)}")

if __name__ == "__main__":
    main()
