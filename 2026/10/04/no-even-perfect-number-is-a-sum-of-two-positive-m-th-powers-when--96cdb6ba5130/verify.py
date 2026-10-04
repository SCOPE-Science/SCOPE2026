#!/usr/bin/env python3

def Bmod8(u, v, m):
    s = 0
    for j in range(m):
        term = pow(u, m - 1 - j, 8) * pow(v, j, 8)
        s += term if j % 2 == 0 else -term
    return s % 8

for u in (1, 3, 5, 7):
    for v in (1, 3, 5, 7):
        inv_v = pow(v, -1, 8)
        r = (u * inv_v) % 8
        for k in range(1, 501):
            m = 4 * k + 1
            direct = Bmod8(u, v, m)
            closed = (1 + 2 * k * (1 - r)) % 8
            assert direct == closed, (u, v, m, direct, closed)
            assert direct in (1, 5), (u, v, m, direct)

# Small endpoint check for the Euclid--Euler exception p=2.
for m in range(5, 50, 4):
    assert 1**m + 1**m == 2
    assert 2**m + 1 >= 33

print("VERIFY_OK")
