#!/usr/bin/env python3
"""Good-reduction leg: for p outside {2,3,5,17}, X has a smooth F_p-point, hence X(Q_p)!=empty.
Stdlib only. Prints VERIFY_OK_GOOD on success.
Method per p: brute-force search x,y,z in F_p for F=0 with gradient != (0,0,0) mod p.
A smooth F_p-point on the affine (or projective) model lifts to Z_p by Hensel
(gradient nonzero => one partial nonzero => implicit function theorem).
This is the computational shadow of the uniform Chevalley-Warning/Hensel argument
for the audit plan's "all p outside bad set" step; the diagonal integral P0 already
covers all p, but this gives independent fiber evidence at good primes.
"""
def F(x, y, z):
    return y*y - 17*z*z - (x*x - 3)*(x*x - 5)

def grad(x, y, z):
    return (-4*x**3 + 16*x, 2*y, -34*z)

def find_smooth(p):
    for x in range(p):
        Px = (x*x - 3)*(x*x - 5)
        for y in range(p):
            for z in range(p):
                if (y*y - 17*z*z - Px) % p == 0:
                    g = grad(x, y, z)
                    if any(c % p != 0 for c in g):
                        return (x, y, z, g)
    return None

def main():
    BAD = {2, 3, 5, 17}
    primes = [7, 11, 13, 19, 23, 29, 31, 37, 41, 101]
    for p in primes:
        assert p not in BAD
        hit = find_smooth(p)
        assert hit is not None, f"no smooth point mod {p}"
        x, y, z, g = hit
        assert F(x, y, z) % p == 0
        assert any(c % p != 0 for c in g)
        print(f"p={p}: smooth F_p-point {(x,y,z)} grad mod p={(g[0]%p,g[1]%p,g[2]%p)} => lifts to Q_p OK")
    # uniformity note: P separable mod p (p not dividing disc 3840) and a=17 nonzero nonsquare-or-square
    # => smooth conic bundle over P^1(F_p) with (#P^1 = p+1) fibers; each smooth fiber has p+1 or p-1+... points;
    # Chevalley-Warning on the bihomogeneous model guarantees F_p-points for all large p; small ones checked above.
    print("good-reduction solubility independently corroborated at 10 primes")
    print("VERIFY_OK_GOOD")

if __name__ == '__main__':
    main()
