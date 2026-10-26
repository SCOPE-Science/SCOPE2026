"""Exact characteristic-two polynomial certificate for the Weddle fixed locus.

Run with Python 3: python weddle_fixed_verifier.py
Only the standard library is required.
"""
from itertools import permutations
N = 7
Z = (0,) * N

def const():
    return {Z: 1}

def var(i):
    e = list(Z)
    e[i] = 1
    return {tuple(e): 1}

def add(*polys):
    out = {}
    for p in polys:
        for mon in p:
            if mon in out:
                del out[mon]
            else:
                out[mon] = 1
    return out

def mul(*polys):
    out = const()
    for p in polys:
        nxt = {}
        for a in out:
            for b in p:
                mon = tuple(x+y for x,y in zip(a,b))
                if mon in nxt:
                    del nxt[mon]
                else:
                    nxt[mon] = 1
        out = nxt
    return out

def power(p,n):
    out = const()
    for _ in range(n):
        out = mul(out,p)
    return out

def det(mat):
    out = {}
    for perm in permutations(range(len(mat))):
        out = add(out, mul(*(mat[i][perm[i]] for i in range(len(mat)))))
    return out

def coeff(p, exponents):
    e = tuple(exponents)
    return {m[:4] + (0,0,0):1 for m in p if m[4:] == e}

A,B,C,D,u,v,t = (var(i) for i in range(7))
one=const()
x,y,z,w = mul(A,add(one,u)),mul(B,add(one,v)),mul(C,add(one,t)),D
a,b,c,d = power(A,2),power(B,2),power(C,2),power(D,2)
M = [
 [mul(a,y,z,w), x, one, a],
 [mul(b,x,z,w), y, one, b],
 [mul(c,x,y,w), z, one, c],
 [mul(d,x,y,z), w, one, d]
]
f = det(M)
# No squarefree monomial in local coordinates survives mod 2.
for e in ((i,j,k) for i in (0,1) for j in (0,1) for k in (0,1)):
    assert not coeff(f,e), ("squarefree coefficient nonzero",e)

# Leading quadratic rows of f, d(f)/dv, d(f)/dt respectively.
q = [coeff(f,(2,0,0)), coeff(f,(0,2,0)), coeff(f,(0,0,2))]
dv = [coeff(f,(2,1,0)), coeff(f,(0,3,0)), coeff(f,(0,1,2))]
dt = [coeff(f,(2,0,1)), coeff(f,(0,2,1)), coeff(f,(0,0,3))]
minor = det([q,dv,dt])
expected = mul(power(A,4),power(B,4),power(C,4),power(D,4),
               add(A,B),add(A,C),power(add(A,D),2),
               power(add(B,C),2),add(B,D),add(C,D))
assert minor == expected, ("symbolic determinant mismatch",len(minor),len(expected))
assert minor
# On the six-point general-position locus, the four nonzero square roots
# A,B,C,D are pairwise distinct, so the displayed minor is nonzero.
# The tangent-cone and derivative jets span the three squares, and
# Nakayama's lemma identifies the Tjurina and fixed-locus ideals locally.
print('VERIFY_OK: Weddle determinant; Frobenius-fixed thickening; Jacobian jet minor')
