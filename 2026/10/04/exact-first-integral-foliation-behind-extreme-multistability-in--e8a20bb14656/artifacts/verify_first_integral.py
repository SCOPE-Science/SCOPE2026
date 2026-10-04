#!/usr/bin/env python3
from fractions import Fraction as F

# Minimal exact polynomial arithmetic in (lambda, s).
def add(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,F(0))+c
        if r[m]==0: del r[m]
    return r
def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            m=(i+k,j+l); r[m]=r.get(m,F(0))+a*b
    return {m:c for m,c in r.items() if c}
def const(c): return {} if c==0 else {(0,0):F(c)}
L={(1,0):F(1)}; S={(0,1):F(1)}
def scale(p,c): return {m:c*v for m,v in p.items() if c*v}
def det(M):
    n=len(M)
    if n==1: return M[0][0]
    out={}
    for j in range(n):
        minor=[row[:j]+row[j+1:] for row in M[1:]]
        term=mul(M[0][j],det(minor))
        out=add(out, term if j%2==0 else neg(term))
    return out

# First integral identity.
a=F(121,50); b=F(34,25)
coef = -F(3,10) - a + 2*b
assert coef == 0

# Jacobian at E_s; form lambda I - J.
Z={}; one=const(1)
J=[
 [Z,one,Z,Z,Z],
 [Z,Z,one,Z,Z],
 [Z,Z,Z,one,Z],
 [scale(S,F(82,25)),scale(S,F(7,25)),Z,const(-F(51,50)),one],
 [Z,Z,Z,scale(S,F(121,50)),Z]
]
M=[]
for i in range(5):
    row=[]
    for j in range(5):
        row.append(sub(L if i==j else Z,J[i][j]))
    M.append(row)
char=det(M)
target={
 (5,0):F(1), (4,0):F(51,50), (3,1):-F(121,50),
 (2,1):-F(7,25), (1,1):-F(82,25)
}
assert char==target, (char,target)

# Routh-Hurwitz data for negative branch s=-u.
ucrit=F(213282,38297)
D2coef=F(51,50)*F(121,50)-F(7,25)
assert D2coef==F(5471,2500)
# Delta_3 = u * (38297 u - 213282)/62500.
quad=F(51,50)*F(121,50)*F(7,25)-F(7,25)**2
lin=F(51,50)**2*F(82,25)
assert quad==F(38297,62500)
assert lin==F(213282,62500)
assert lin/quad==ucrit
Ccrit=-F(41,25)*ucrit*ucrit
assert Ccrit==F(-1865057672484,36666505225)
omega2=F(14,51)*ucrit
assert omega2==F(8364,5471)

# Source initial family exact offset.
x0=F(-277,100); y0=F(-53,100); z0=F(27,10)
offset=-a*x0*z0+b*y0*y0
assert offset==F(4620301,250000)
assert float(offset)==18.481204

print('first_integral_yz_coefficient =', coef)
print('characteristic_polynomial = lambda^5 + 51/50 lambda^4 - 121/50 s lambda^3 - 7/25 s lambda^2 - 82/25 s lambda')
print('negative_branch_Delta2 = (5471/2500) u')
print('negative_branch_Delta3 = u(38297 u - 213282)/62500')
print('u_critical =', ucrit, float(ucrit))
print('C_critical =', Ccrit, float(Ccrit))
print('omega_squared_at_boundary =', omega2, float(omega2))
print('source_scan_offset =', offset, float(offset))
print('VERIFY_OK')
