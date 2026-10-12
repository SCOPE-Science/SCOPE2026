"""Finite exact-rational corroboration of a Gödel frame witness-depth separation.

This checks finite truncations only. The infinite nonattainment statement
is established by the proof, not by these calculations.
"""
from fractions import Fraction


def imply(a, b):
    return Fraction(1) if a <= b else b


def model(n):
    # root=0; first-layer worlds 1,...,n; terminal worlds n+1,...,2n
    worlds = range(2*n + 1)
    edges = {}
    for k in range(1, n+1):
        edges[0, k] = Fraction(1)
        edges[k, n+k] = Fraction(1, k+1)
    p = {n+k: Fraction(1) for k in range(1, n+1)}
    def box(values, w):
        return min(imply(edges.get((w, z), Fraction(0)), values.get(z, Fraction(0))) for z in worlds)
    def diamond(values, w):
        return max(min(edges.get((w, z), Fraction(0)), values.get(z, Fraction(0))) for z in worlds)
    D = {z:diamond(p,z) for z in worlds}
    DD = {z:Fraction(int(value>0)) for z,value in D.items()}
    out = box(D, 0)
    double_out = box(DD, 0)
    # The schema Box(not-not Diamond p) -> not-not Box(Diamond p)
    scheme = imply(double_out, Fraction(int(out>0)))
    assert all(len({v for (a,b),v in edges.items() if a==z})<=1 for z in worlds)
    assert all(D[k] == Fraction(1,k+1) for k in range(1,n+1))
    assert out == Fraction(1,n+1)
    assert double_out == 1
    assert scheme == 1 # Finite truncations are witnessed.
    # Every positive local weight set is singleton, and all positive grades
    # in the frame form an initial segment of {1,1/2,1/3,...}.
    return out


def bad_diamond_prefix(n):
    # A one-step row with increasing fuzzy weights; Boolean p is everywhere 1.
    grades = [Fraction(k,k+1) for k in range(1,n+1)]
    value = max(grades)
    assert value == Fraction(n,n+1)
    return value

if __name__ == '__main__':
    ns = (1,2,3,4,8,16,32,64,128)
    for n in ns:
        a = model(n)
        b = bad_diamond_prefix(n)
        print(f'N={n}: finite root Box Diamond p={a}; increasing-row Diamond p={b}')
    print('VERIFY_OK: finite-prefix identities and uniform row-grade restriction checked.')
    print('The limiting infimum/supremum nonattainment is a symbolic proof obligation.')
