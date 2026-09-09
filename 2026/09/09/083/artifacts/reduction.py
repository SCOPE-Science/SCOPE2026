#!/usr/bin/env python3
"""Reduction leg: behavior of the integral point P0 mod bad primes.
Stdlib only (ints). Prints VERIFY_OK_REDUCTION on success.
P0=(2,4,1), F=0 over Z, grad=(0,8,-34).
Per p: F mod p = 0 (Z-equality implies it), grad mod p recorded.
Note: mod 2 the gradient vanishes ((0,0,0)), so P0 reduces to a singular point
of the Z-model's special fiber at 2 — this does NOT affect the Q_2-point status
(exact Z-equality gives a Z_2-point directly; Hensel lifting is not needed when
an exact solution is in hand). At 3,5,17 the reduction is smooth.
This nuance is recorded to pre-empt a 'singular reduction invalidates locals'
objection: it doesn't, since locals.py uses exact equality, not lifting.
"""
def main():
    x, y, z = 2, 4, 1
    F = y*y - 17*z*z - (x*x - 3)*(x*x - 5)
    assert F == 0
    g = (-4*x**3 + 16*x, 2*y, -34*z)
    assert g == (0, 8, -34)
    print(f"F(P0)={F} over Z; grad={g} over Q (nonzero => smooth/Q) OK")
    for p in (2, 3, 5, 17):
        assert F % p == 0
        gm = (g[0] % p, g[1] % p, g[2] % p)
        smooth = gm != (0, 0, 0)
        print(f"mod {p}: F=0 OK; grad mod p = {gm} => {'smooth' if smooth else 'SINGULAR special-fiber point (still exact Z_p solution)'}")
    assert (0 % 2, 8 % 2, -34 % 2) == (0, 0, 0)
    assert (0 % 17, 8 % 17, -34 % 17) == (0, 8, 0) != (0, 0, 0)
    assert (0 % 3, 8 % 3, -34 % 3) != (0, 0, 0)
    assert (0 % 5, 8 % 5, -34 % 5) != (0, 0, 0)
    print("Q_p-point status at every p: exact integral solution => Z_p-point regardless of special-fiber smoothness OK")
    print("VERIFY_OK_REDUCTION")

if __name__ == '__main__':
    main()
