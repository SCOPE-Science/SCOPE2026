"""Exact certificate for degree-wise harmonic sampling on 12 truncated-tetrahedral nodes.

Requires Python 3.9+ standard library only. All finite rank assertions are over
GF(1000000007) or Q, never floating-point. The analytic large-degree bound is
proved in RESULT.md, not inferred from these computations.
"""
from fractions import Fraction
from itertools import product
from hashlib import sha256
import json

P = 1000000007

def prime(n):
    if n < 2: return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0: return False
    return True

def vertices(a):
    return [tuple(e[i] * (a if i == j else 1) for i in range(3))
            for j in range(3) for e in product((-1, 1), repeat=3)
            if e[0] * e[1] * e[2] == 1]

def dot_table(a):
    v = vertices(a)
    assert len(v) == len(set(v)) == 12
    return [[sum(u[i] * w[i] for i in range(3)) for w in v] for u in v]

def legendre_fraction(n, x):
    u, v = Fraction(1), x
    if n == 0: return u
    for k in range(1, n):
        u, v = v, ((2*k+1)*x*v-k*u)/Fraction(k+1)
    return v

def modular_ranks(a, maxdeg):
    dot = dot_table(a)
    z = a*a+2
    X = [[(v * pow(z, -1, P)) % P for v in row] for row in dot]
    lo = [[1]*12 for _ in range(12)]
    hi = [row[:] for row in X]
    out = []
    for n in range(maxdeg+1):
        if n == 0: cur = lo
        elif n == 1: cur = hi
        else:
            inv = pow(n, -1, P)
            cur = [[(((2*n-1)*X[i][j]*hi[i][j] - (n-1)*lo[i][j]) * inv) % P
                    for j in range(12)] for i in range(12)]
            lo,hi = hi,cur
        out.append(rank_mod(cur))
    return out

def rank_mod(A):
    B=[row[:] for row in A]
    n=len(B); m=len(B[0]); row=0
    for col in range(m):
        piv=next((r for r in range(row,n) if B[r][col]),None)
        if piv is None: continue
        B[row], B[piv] = B[piv], B[row]
        inv=pow(B[row][col], -1, P)
        for j in range(col,m): B[row][j] = B[row][j]*inv % P
        for r in range(row+1,n):
            mul=B[r][col]
            if mul:
                for j in range(col,m):
                    B[r][j]=(B[r][j]-mul*B[row][j]) % P
        row+=1
        if row==n:break
    return row

W = [
    (-1,1,1,-1,1,-1,-1,1,0,0,0,0),
    (-1,1,0,0,1,0,-1,0,0,-1,1,0),
    (0,0,1,-1,1,0,-1,0,-1,0,0,1),
]

def main():
    assert prime(P)
    dots=dot_table(3)
    off=[dots[0][j] for j in range(1,12)]
    assert {v:off.count(v) for v in set(off)} == {-9:2,-5:2,-1:4,7:3}
    # The exact rational Legendre Gram matrix at degree six annihilates
    # three independent integer weight vectors.
    G6=[[legendre_fraction(6,Fraction(v,11)) for v in row] for row in dots]
    for w in W:
        for row in G6: assert sum(row[j]*w[j] for j in range(12)) == 0
    assert rank_mod([[x % P for x in w] for w in W])==3
    rankseq=modular_ranks(3,324)
    assert rankseq[:7] == [1,3,5,7,9,11,9],rankseq[:7]
    assert all(r==12 for r in rankseq[7:]),[
        (i,r) for i,r in enumerate(rankseq[7:],7) if r!=12]
    # At a=2 the degree-six Gram matrix is nonsingular: the rational
    # determinant function of a is not identically zero, so a=3 is an
    # isolated exceptional parameter.
    assert modular_ranks(2,6)[6] == 12
    # Explicit *rational* bounds used in the analytic Gershgorin step.
    # Sin(theta)=sqrt(1-(dot/11)^2), proven above each lower bound by squaring.
    for d,r in [(-9,Fraction(57,100)),(-5,Fraction(89,100)),
                (-1,Fraction(99,100)),(7,Fraction(77,100))]:
        assert Fraction(121-d*d,121) > r*r
    S=2*Fraction(100,57)+2*Fraction(100,89)+4*Fraction(100,99)+3*Fraction(100,77)
    assert S < 14
    assert Fraction(11,7) < Fraction(9,7)**2
    return {
      "verification":"passed",
      "prime":P,
      "low_degree_ranks":rankseq[:7],
      "full_rank_interval":[7,324],
      "all_full_rank":True,
      "degree6_nullity":len(W),
      "degree6_deformation_a2_rank":12,
      "bernstein_free_gershgorin_start":325,
      "reciprocal_sine_rational_upper_bound":str(S),
      "finite_rank_sequence_sha256":sha256(bytes(rankseq)).hexdigest(),
    }

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
