"""Independent, finite exact arithmetic checks for a two-spectral Heinz claim.

Run with Python 3 (standard library only). The infinite-dimensional/dimension-
n theorem is proved analytically, not by this script.
"""
from fractions import Fraction as F
from math import sqrt


def identity(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def add(A, B):
    return tuple(tuple(a + b for a, b in zip(row_a, row_b)) for row_a, row_b in zip(A, B))


def sub(A, B):
    return tuple(tuple(a - b for a, b in zip(row_a, row_b)) for row_a, row_b in zip(A, B))


def times(t, A):
    return tuple(tuple(t * a for a in row) for row in A)


def mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def normsq(A):
    return sum(x*x for row in A for x in row)


def spectral_power(low_root, high_root, exponent_num, P):
    # Eigenvalues are fourth powers of integers; exponent_num/4 is exact.
    n = len(P)
    lo = F(low_root ** exponent_num)
    hi = F(high_root ** exponent_num)
    return add(times(lo, identity(n)), times(hi-lo, P))


def rank1(c, s):
    return ((c*c, c*s), (c*s, s*s))


def blocks(matrices):
    N = sum(len(m) for m in matrices)
    out = [[F(0) for _ in range(N)] for _ in range(N)]
    pos = 0
    for block in matrices:
        n = len(block)
        for i in range(n):
            for j in range(n):
                out[pos+i][pos+j] = block[i][j]
        pos += n
    return tuple(tuple(row) for row in out)


def eval_pair(P, Q, ah, bh, tnum):
    # tnum=1 -> 1/4; tnum=2 -> 1/2; tnum=3 -> 3/4.
    at = spectral_power(1, ah, tnum, P)
    ar = spectral_power(1, ah, 4-tnum, P)
    bt = spectral_power(1, bh, tnum, Q)
    br = spectral_power(1, bh, 4-tnum, Q)
    C = add(mul(at, br), mul(bt, ar))
    H = add(mul(at, br), mul(ar, bt))
    comm = sub(mul(P, Q), mul(Q, P))
    coefficient = (ah**tnum-1)*(ah**(4-tnum)-1)*(bh**tnum-1)*(bh**(4-tnum)-1)
    return C, H, F(coefficient)*normsq(comm)


def singular_values_2(A):
    a,b=A[0]; c,d=A[1]
    f2=float(a*a+b*b+c*c+d*d)
    determinant=float(a*d-b*c)
    discriminant=max(0.0,f2*f2-4*determinant*determinant)
    return [sqrt(max(0.,(f2+sqrt(discriminant))/2)),sqrt(max(0.,(f2-sqrt(discriminant))/2))]


ratios = [(F(0),F(1)), (F(1),F(0)), (F(3,5),F(4,5)),
          (F(5,13),F(12,13)), (F(8,17),F(15,17)), (F(7,25),F(24,25))]
exact = 0
kyfan = 0
for c,s in ratios:
    Q2=rank1(c,s)
    P2=((F(1),F(0)), (F(0),F(0)))
    for ah in (2,3,4):
        for bh in (2,3,4):
            for tnum in (1,2,3):
                C,H,expected=eval_pair(P2,Q2,ah,bh,tnum)
                assert normsq(H)-normsq(C)==expected
                exact+=1
                sc=singular_values_2(C); sh=singular_values_2(H)
                assert sc[0] <= sh[0] + 1e-9*(1+sh[0])
                assert sum(sc)<=sum(sh)+1e-9*(1+sum(sh))
                kyfan+=2
                # Nontrivial higher-dimensional two-projection pairs,
                # including a 1-dimensional shared component and 2 blocks.
                one=((F(1),),)
                P3=blocks((one,P2))
                Q3=blocks((one,Q2))
                C3,H3,exp3=eval_pair(P3,Q3,ah,bh,tnum)
                assert normsq(H3)-normsq(C3)==exp3
                exact+=1
                c2,s2=F(5,13),F(12,13)
                P4=blocks((P2,P2))
                Q4=blocks((Q2,rank1(c2,s2)))
                C4,H4,exp4=eval_pair(P4,Q4,ah,bh,tnum)
                assert normsq(H4)-normsq(C4)==exp4
                exact+=1
                # Ky Fan concatenation on the actual two independent blocks.
                c0,h0,_=eval_pair(P2,Q2,ah,bh,tnum)
                c1,h1,_=eval_pair(P2,rank1(c2,s2),ah,bh,tnum)
                svC=sorted(singular_values_2(c0)+singular_values_2(c1),reverse=True)
                svH=sorted(singular_values_2(h0)+singular_values_2(h1),reverse=True)
                for k in range(1,5):
                    assert sum(svC[:k])<=sum(svH[:k])+1e-9*(1+sum(svH[:k]))
                    kyfan+=1
assert exact==486 and kyfan==972
print(f"PASS {exact} exact rational squared-defect identities; {kyfan} two-block Ky Fan checks")
