"""Exact checks for root windows of prisms over empty lattice tetrahedra.

Run: python check.py
Requires SymPy for exact polynomial identities.  Point-count tests use integers.
"""
from math import comb
import sympy as sp

z, a, k, n = sp.symbols('z a k n', integer=True)
H = 1 + a*z*z
NUM = sp.expand((1+(4*k-1)*z)*H + k*z*(1-z)*sp.diff(H,z))
EXPECTED = 1+(4*k-1)*z+a*(2*k+1)*z*z+a*(2*k-1)*z**3
assert sp.expand(NUM-EXPECTED) == 0

# Compute numerator a second way, from the Ehrhart inversion formula.
M = a+1
LR = M*n**3/sp.Integer(6)+n**2+(12-M)*n/sp.Integer(6)+1
LQ = (k*n+1)*LR
inv = []
for j in range(5):
    coeff = sum((-1)**i*comb(5,i)*LQ.subs(n,j-i) for i in range(j+1))
    inv.append(sp.factor(coeff))
assert sp.expand(sum(inv[j]*z**j for j in range(5))-EXPECTED) == 0
assert inv[4] == 0

DISC = sp.discriminant(EXPECTED,z)
FACTOR = 4*a*(2*k-1-a)*(a*(2*k+1)**3-(4*k-1)**3)
assert sp.expand(DISC-FACTOR) == 0
assert sp.expand((2*k-1)*(2*k+1)**3-(4*k-1)**3-16*k*(k-1)**3) == 0
assert sp.expand(EXPECTED.subs(a,2*k-1)-(1+z)*(1+(2*k-1)*z)**2) == 0
assert sp.expand(EXPECTED.subs({a:1,k:1})-(1+z)**3) == 0

# Direct lattice-point enumeration by horizontal sections, without Ehrhart formulas.
def direct_reeve_count(m,N):
    total=0
    for height in range(N*m+1):
        lower=(height + m - 1)//m
        upper=N + height//m
        for x in range(lower,upper+1):
            for y in range(lower,upper-x+1):
                total+=1
    return total

count_cases=0
for m in range(1,16):
    for N in range(0,7):
        actual=direct_reeve_count(m,N)
        predicted=comb(N+3,3)+(m-1)*(comb(N+1,3) if N+1>=3 else 0)
        assert actual == predicted,(m,N,actual,predicted)
        count_cases+=1

# Exact arithmetic on a two-parameter grid; classification is proved algebraically above.
parameter_checks=0
for mm in range(1,151):
    for kk in range(1,151):
        aa=mm-1
        if aa==0:
            predicted=True
        elif mm==2:
            predicted=(kk==1)
        elif mm==3:
            predicted=False
        elif mm==4:
            predicted=(kk==2)
        elif mm==5:
            predicted=(kk==3)
        elif mm==6:
            predicted=kk in (3,4)
        elif mm==7:
            predicted=4<=kk<=7
        elif mm==8:
            predicted=4<=kk<=16
        else:
            predicted=kk >= (mm+1)//2
        if aa:
            by_interval=((4*kk-1)**3 <= aa*(2*kk+1)**3 and aa<=2*kk-1)
        else:
            by_interval=True
        assert predicted==by_interval, (mm,kk,predicted,by_interval)
        parameter_checks+=1

print('EMPTY_TETRA_PRISM_OK', 'symbolic_identities=5',
      'independent_lattice_counts=',count_cases,
      'parameter_pairs=',parameter_checks)
