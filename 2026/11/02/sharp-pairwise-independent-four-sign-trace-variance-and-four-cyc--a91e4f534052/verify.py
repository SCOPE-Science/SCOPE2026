"""Exact finite checks for four-coordinate isotropic binary trace probing.

Uses Python standard library only.  The infinite/universal theorem follows
from the algebraic argument in RESULT.md, not from this finite verification.
"""
from fractions import Fraction
from itertools import product

SIGNS = tuple(product((-1, 1), repeat=4))
PARITY = {c: tuple(z for z in SIGNS if z[0]*z[1]*z[2]*z[3] == c) for c in (-1, 1)}
PAIRS = ((0,1,2,3), (0,2,1,3), (0,3,1,2))
EDGES = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))


def mat(offdiag, diagonal=(0,0,0,0)):
    out = [[0]*4 for _ in range(4)]
    for i,d in enumerate(diagonal):out[i][i] = d
    for (i,j),v in zip(EDGES,offdiag):out[i][j] = out[j][i] = v
    return out


def q(B,z):
    return sum(B[i][j]*z[i]*z[j] for i in range(4) for j in range(4))


def var(B,law):
    vals = tuple(q(B,z) for z in law)
    mean = Fraction(sum(vals),len(vals))
    trace = sum(B[i][i] for i in range(4))
    assert mean == trace
    return sum((Fraction(v)-mean)**2 for v in vals)/len(vals)


def formula(B):
    a = [(B[i][j],B[k][l]) for i,j,k,l in PAIRS]
    S = sum(u*v for u,v in a)
    F = 4*sum(u*u+v*v for u,v in a)
    Vp = 4*sum((u+v)**2 for u,v in a)  # parity +1
    Vm = 4*sum((u-v)**2 for u,v in a)  # parity -1
    assert Vp == F + 8*S and Vm == F - 8*S
    assert min(Vp,Vm)==F-8*abs(S)
    return F,Vp,Vm,S


def isotropic(law):
    for i in range(4):
        assert sum(z[i] for z in law)==0
    for i in range(4):
        for j in range(4):
            target = len(law)*(i==j)
            assert sum(z[i]*z[j] for z in law)==target


def verify():
    count=0
    for law in (SIGNS,PARITY[1],PARITY[-1]):
        isotropic(law)
    assert len(SIGNS)==16 and len(PARITY[1])==len(PARITY[-1])==8
    count+=3
    # Exhaustively range over integer offdiagonal coefficients in [-2,2].
    for offdiag in product(range(-2,3),repeat=6):
        B=mat(offdiag)
        F,Vp,Vm,S=formula(B)
        assert var(B,SIGNS)==F
        assert var(B,PARITY[1])==Vp
        assert var(B,PARITY[-1])==Vm
        if S>0:assert Vm<Vp
        if S<0:assert Vp<Vm
        if S==0:assert Vp==Vm
        count+=1
    # Arbitrary diagonal shifts do not change the variance.
    for k in range(1000):
        a = tuple(((k+7*j)*(j+3))%17-8 for j in range(6))
        d = tuple(((k+5*j)*(j+7))%19-9 for j in range(4))
        B=mat(a,d)
        F,Vp,Vm,_=formula(B)
        assert var(B,SIGNS)==F
        assert var(B,PARITY[1])==Vp
        assert var(B,PARITY[-1])==Vm
        count+=1
    # Sharp one-probe C4 example, strictly positive definite I+adjacency/4.
    c4=mat((Fraction(1,4),0,Fraction(1,4),Fraction(1,4),0,Fraction(1,4)),(1,1,1,1))
    assert formula(c4)==(1,2,0,Fraction(1,8))
    assert set(q(c4,z) for z in PARITY[-1])=={4}
    assert var(c4,SIGNS)==1
    count+=1
    # Multiple independent four-cycles: each block is exact with a single
    # full-length isotropic probe, selected blockwise from the parity - coset.
    blk1=mat((2,0,3,3,0,2),(7,8,9,10))
    blk2=mat((Fraction(1,5),0,Fraction(2,5),Fraction(2,5),0,Fraction(1,5)),(3,4,5,6))
    for z1,z2 in product(PARITY[-1],repeat=2):
        assert q(blk1,z1)+q(blk2,z2)==sum(blk1[i][i]+blk2[i][i] for i in range(4))
        count+=1
    # Robust weighted 4-cycle: paired-edge defects alone determine variance.
    for a,b,da,db in product((-2,0,3),repeat=4):
        B=mat((a,0,b,b+db,0,a+da))
        assert var(B,PARITY[-1])==4*(da*da+db*db)
        count+=1
    print(f"VERIFY_OK exact_cases={count} exhaustive_integer_coefficient_matrices=15625")


if __name__ == '__main__':verify()
