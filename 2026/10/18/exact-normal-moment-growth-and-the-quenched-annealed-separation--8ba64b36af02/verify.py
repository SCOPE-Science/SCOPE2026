"""Reproduce exact finite-n identities for a logistic-boundary normal cocycle.
Requires Python 3 standard library; optional mpmath used only for numerical quadrature.
Mathematical proof of all-n identities is in RESULT.md, not inferred from these finite checks.
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import comb, sqrt, log, cos, sin, pi

def multiply(p, q):
    r=defaultdict(Q)
    for i,a in p.items():
        for j,b in q.items():
            r[i+j]+=a*b
    return dict(r)

def power_cocycle_fourier(n, a, b):
    """Fourier coefficients of P_n(theta), with x_k=sin^2(2^k theta/2)."""
    a,b=Q(a),Q(b)
    A=b/2-a
    B=-b/2
    out={0:Q(1)}
    for k in range(n):
        out=multiply(out,{0:A, 2**k:B/2, -(2**k):B/2})
    return out

def moments(coeffs):
    two=sum(q*q for q in coeffs.values())
    sq=multiply(coeffs, coeffs)
    four=sum(q*q for q in sq.values())
    return two,four

def matrix_square_moment(n,a,b):
    a,b=Q(a),Q(b)
    A=b/2-a; B=-b/2
    M=((A*A+B*B/2,A*B),(B*B/2,A*B))
    u,v=Q(1),Q(0)
    for _ in range(n): u,v=M[0][0]*u+M[0][1]*v,M[1][0]*u+M[1][1]*v
    return u

def expected_resonance(n,b):
    b=Q(b); N=2**n
    return (b*b/8)**n, (b/4)**(4*n)*Q(2*N**3+N,3)

assertions=0
for (a,b) in [(Q(3,2),Q(3)),(Q(7,4),Q(3)),(Q(3,4),Q(3)),(Q(5,2),Q(3)),(Q(1),Q(4))]:
    for n in range(0,8):
        c=power_cocycle_fourier(n,a,b)
        m2,m4=moments(c)
        assert m2 == matrix_square_moment(n,a,b),(a,b,n,m2)
        assertions+=1
        if a==b/2:
            expected2,expected4=expected_resonance(n,b)
            assert (m2,m4)==(expected2,expected4),(a,b,n,m4,expected4)
            assertions+=1
            if n>0: assert c.get(0,0)==0; assertions+=1
assert Q(9,8)>1 and Q(3,4)<1
assertions+=1
for b in [Q(3),Q(4),Q(5)]:
    a=b/2; A=b/2-a; B=-b/2
    assert A==0 and matrix_square_moment(4,a,b)==(b*b/8)**4
    assertions+=1
print(f"PASS {assertions} exact checks: Fourier products, normal second/fourth moments, transfer matrices.")
print("b=3, a=3/2: quenched exp = log(3/4) =", log(.75),"; annealed second-moment exp = log(9/8) =",log(1.125))

# Independent deterministic angle samples corroborate the non-resonant Jensen formula.
for a,b in [(1.5,3.),(3.5,3.),(0.5,3.),(3.,3.),(2.,4.),(4.5,4.)]:
    C=b/2-a; D=b/2
    if a<=b: exact=log(b/4)
    else: exact=log((a-b/2+sqrt(a*(a-b)))/2)
    grid=131071
    est=sum(log(abs(C-D*cos(2*pi*(j+.370321)/grid))) for j in range(grid))/grid
    assert abs(est-exact)<.0002,(a,b,est,exact)
    assertions+=1
    print('integral test',a,b,'error',round(est-exact,9))
print(f"TOTAL PASS {assertions}")
