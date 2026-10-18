"""Independent characteristic-two coefficient checks for a plane-curve stabilizer.

Run: python3 check_stabilizer.py
No external libraries are required. This finite-field check is supplementary,
not a proof of the uniform group-scheme statements.
"""
from itertools import product
from math import gcd


def mul(a, b):
    """GF(4) as F2[u]/(u*u+u+1), bit pairs."""
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return out


def padd(f, g):
    out = dict(f)
    for m, c in g.items():
        out[m] = out.get(m, 0) ^ c
        if out[m] == 0:
            del out[m]
    return out


def pmul(f, g):
    out = {}
    for m, c in f.items():
        for n, d in g.items():
            k = tuple(a + b for a, b in zip(m, n))
            out[k] = out.get(k, 0) ^ mul(c, d)
            if not out[k]:
                del out[k]
    return out


def ppow(f, e):
    out = {(0, 0, 0): 1}
    while e:
        if e & 1:
            out = pmul(out, f)
        f = pmul(f, f)
        e >>= 1
    return out


def lin(a, b, c):
    return {m: v for m, v in zip(((1,0,0),(0,1,0),(0,0,1)),(a,b,c)) if v}


def transformed(q, a, b, c, f, g, d):
    X = lin(a, 0, b)
    Y = lin(c, f, g)
    Z = lin(0, 0, d)
    return padd(padd(pmul(ppow(Z,2), ppow(Y,q)),ppow(X,q+2)),pmul(X,ppow(Z,q+1)))


def expected(q, scale):
    return {(q+2,0,0):scale,(1,0,q+1):scale,(0,q,2):scale}


def rank_binary(rows):
    basis = {}
    for x in rows:
        while x:
            j = x.bit_length()-1
            if j in basis:
                x ^= basis[j]
            else:
                basis[j] = x
                break
    return len(basis)


def check_lie(q):
    # Partial derivatives: FX=Z^(q+1), FY=0, FZ=X Z^q.
    # For each elementary matrix E_ij, evaluate deltaF=sum F_i*E_ij*x_j.
    X, Y, Z = lin(1,0,0),lin(0,1,0),lin(0,0,1)
    coords = (X,Y,Z)
    FX, FY, FZ = ppow(Z,q+1), {}, pmul(X,ppow(Z,q))
    derivs = (FX,FY,FZ)
    polys = [pmul(derivs[i],coords[j]) for i in range(3) for j in range(3)]
    monomials = sorted(set().union(*(set(p) for p in polys)))
    # all polynomials here have coefficients in F2
    columns = [sum(((1 << k) if p.get(m,0) else 0) for k,m in enumerate(monomials)) for p in polys]
    image_rank = rank_binary(columns)
    # The scalar matrices are always in the kernel; quotient by scalar dimension 1.
    lie_dimension = 9 - image_rank - 1
    assert lie_dimension == 3
    return image_rank, lie_dimension


def run():
    for n in (2, 3, 4):
        q=2**n
        stabilizers = []
        for f,d,b,c,g in product((1,2,3),(1,2,3),range(4),range(4),range(4)):
            if transformed(q,1,b,c,f,g,d) == expected(q,1):
                stabilizers.append((1,b,c,f,g,d))
        expected_count=gcd(q+1,3)
        assert len(stabilizers)==expected_count,(q,stabilizers)
        assert all(b==0 and c==0 and g==0 and f==mul(d,d) for a,b,c,f,g,d in stabilizers)
        image_rank,lie_dimension=check_lie(q)
        print(f'q={q}; GF4 projective stabilizers={len(stabilizers)}; '
              f'predicted={expected_count}; infinitesimal constraint rank={image_rank}; '
              f'Lie dimension={lie_dimension}; matrices={stabilizers}')
    print('All independent small-field and first-order checks passed.')

if __name__=='__main__':
    run()
