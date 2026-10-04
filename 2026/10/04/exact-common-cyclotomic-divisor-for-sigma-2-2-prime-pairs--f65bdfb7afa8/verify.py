#!/usr/bin/env python3
from math import gcd

def chain(N):
    t = [None, 1, 1]
    while len(t) <= N:
        k = len(t) - 2
        t.append(5*t[k+1] - t[k] - 1)
    return t

def expected_gcd(n):
    return (3 if n % 3 == 1 else 1) * (7 if n % 14 == 8 else 1)

def main():
    t = chain(505)

    for k in range(1, 503):
        assert t[k] * t[k+2] == t[k+1]*t[k+1] + t[k+1] + 1
        assert t[k+2] == 5*t[k+1] - t[k] - 1
        assert gcd(t[k], t[k+1]) == 1

    assert [t[k] % 3 for k in range(1, 7)] == [1,1,0,1,1,0]

    mod7 = [t[k] % 7 for k in range(1, 15)]
    assert mod7 == [1,1,3,6,5,4,0,2,2,0,4,5,6,3]
    assert t[15] % 7 == 1 and t[16] % 7 == 1

    for n in range(3, 500):
        p, q = t[n], t[n+1]
        lhs = gcd(p*p+p+1, q*q+q+1)
        assert lhs == expected_gcd(n)
        assert 21 % lhs == 0

    known = [
        (3, 13, 1),
        (13, 61, 3),
        (22419767768701, 107419560853453, 21),
    ]
    for p, q, g in known:
        assert (p*p+p+1) % q == 0
        assert (q*q+q+1) % p == 0
        assert gcd(p*p+p+1, q*q+q+1) == g

    for x in (1,4,7):
        assert (x*x+x+1) % 9 == 3

    x = pow(4, -1, 49)
    assert (4*x - 1) % 49 == 0
    assert (x*x+x+1) % 49 != 0

    print("VERIFY_OK")
    print("checked_chain_indices=3..499")
    print("mod3_period=3")
    print("mod7_period=14")
    print("known_gcds=[1,3,21]")

if __name__ == "__main__":
    main()
