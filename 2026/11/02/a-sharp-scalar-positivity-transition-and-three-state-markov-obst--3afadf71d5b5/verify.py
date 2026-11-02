#!/usr/bin/env python3
"""Exact-rational verification of the positivity phase law for a two-derivative integrator.

Uses only the Python standard library. Run with: python3 verify.py
The analytical proof of the all-step and all-generator quantifiers is in RESULT.md.
"""
from fractions import Fraction as F

CHECKS = 0

def check(condition, description):
    global CHECKS
    if not condition:
        raise AssertionError(description)
    CHECKS += 1

# Bivariate exact polynomials with monomials C**i * z**j.
def term(v, i=0, j=0):
    return {} if not v else {(i, j): F(v)}

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}

def scale(p, a):
    return {k: v*F(a) for k, v in p.items() if v*a}

def mul(*ps):
    out = term(1)
    for p in ps:
        q = {}
        for (a, b), x in out.items():
            for (c, d), y in p.items():
                k = (a+c, b+d)
                q[k] = q.get(k, F(0)) + x*y
        out = {k: v for k, v in q.items() if v}
    return out

def dz(p):
    return {(i,j-1): v*j for (i,j),v in p.items() if j}

def subz(p, x):
    return {i: sum((v*F(x)**j for (a,j),v in p.items() if a == i), F(0))
            for i in sorted({a for (a,b) in p})}

def subc(p, c):
    return {j: sum((v*F(c)**i for (i,b),v in p.items() if b == j), F(0))
            for j in sorted({b for (a,b) in p})}

def simplify1(p):
    return {k:v for k,v in p.items() if v}

def as_poly_c(p, x):
    return simplify1({(i, 0): v for i,v in subz(p, x).items()})

one=term(1)
z=term(1, 0, 1)
z2=term(1, 0, 2)
z3=term(1, 0, 3)
C=term(1, 1, 0)
cz=mul(C,z)
cz2=mul(C,z2)
cz3=mul(C,z3)

hn=add(one,scale(z,F(1,4)),scale(z2,F(1,48)))
hd=add(one,scale(z,-F(1,4)),scale(z2,F(1,48)))
a0=add(term(F(1,6)),scale(C,F(7,2)))
a1=add(term(F(2,3)),scale(C,-10))
a2=add(term(F(1,6)),scale(C,F(13,2)))
num_stage=add(mul(add(one,mul(a0,z),cz2),hd),mul(add(mul(a1,z),scale(cz2,-1)),hn))
den_stage=mul(add(one,scale(mul(a2,z),-1),scale(cz2,F(3,2))),hd)
num=scale(add(add(scale(cz3,183),scale(z3,-5)),
                  add(scale(cz2,972),scale(z2,-42)),
                  add(scale(cz,1872),scale(z,-168)),term(-288)),-1)
den=mul(add(z2,scale(z,-12),term(48)),
        add(scale(cz2,9),scale(cz,-39),scale(z,-1),term(6)))
check(mul(num_stage,den)==mul(num,den_stage),
      'stage rational factorization equals published stability function')

# Rational function numerator and denominator at z=-x.
x=term(1, 0, 1)
num_neg=add(scale(cz3,183),scale(z3,-5),scale(cz2,-972),scale(z2,42),
            scale(cz,1872),scale(z,-168),term(288))
den_neg=mul(add(z2,scale(z,12),term(48)),
            add(scale(cz2,9),scale(cz,39),z,term(6)))
def flipz(p):
    return {(i,j): v*(-1)**j for (i,j),v in p.items()}
check(flipz(num)==num_neg,'exact numerator at negative real axis')
check(flipz(den)==den_neg,'exact denominator at negative real axis')

Cq=F(5,183)
# N_{Cq}(x)>0 by a negative quadratic discriminant; dN/dC>0.
check(1188**2-4*157*2928 == -427440,'positive quadratic discriminant sign')
check(324**2-4*61*624 == -47280,'positive parametric slope discriminant sign')
# Explicit published source specialisation: 2*(157x²-1188x+2928) /
# ((x²+12x+48)(5x²+42x+122)).
num_q= {j:v for j,v in subc(num_neg,Cq).items() if v}
den_q= {j:v for j,v in subc(den_neg,Cq).items() if v}
check(num_q == {0:F(288),1:F(-7128,61),2:F(942,61)},'numerator at Cq')
check(den_q == {0:F(48*366,61),1:F(12*366+48*126,61),
                      2:F(366+12*126+48*15,61),3:F(126+12*15,61),4:F(15,61)},
      'denominator at Cq')
check(-9360*Cq*Cq+600*Cq-8 == F(5232,3721)>0,'Cq strictly inside A-stable interval')
check(1204*Cq*Cq+4*Cq-1 == F(271,33489)>0,'uniform three-state derivative sign')

# Rational-function derivative at -12: verify the identity as a polynomial in C.
n12=as_poly_c(num,-12)
d12=as_poly_c(den,-12)
np12=as_poly_c(dz(num),-12)
dp12=as_poly_c(dz(den),-12)
num_der=add(mul(np12,d12),scale(mul(n12,dp12),-1))
# (num_der / d12**2) == -5*(1204C²+4C-1)/(49(98C+1)²)
claim_p=add(scale(mul(C,C),1204),scale(C,4),term(-1))
claim_base=add(scale(C,98),one)
check(mul(scale(num_der,49),mul(claim_base,claim_base)) ==
      scale(mul(claim_p,mul(d12,d12)),-5),
      'exact derivative rational identity for all C')

def evaluate(p, c, zz):
    return sum((v*F(c)**i*F(zz)**j for (i,j),v in p.items()),F(0))
def r(c, zz):
    return evaluate(num,c,zz)/evaluate(den,c,zz)
def dr(c,zz):
    return (evaluate(dz(num),c,zz)*evaluate(den,c,zz)-
            evaluate(num,c,zz)*evaluate(dz(den),c,zz))/evaluate(den,c,zz)**2
check(r(Cq,-12)==F(235,4711),'R(-12) at Cq')
check(dr(Cq,-12)==-F(1355,22193521),'Rprime(-12) at Cq')
check(12*dr(Cq,-12)==-F(16260,22193521),'negative three-state transition coefficient')
check(r(F(1,50),-12)<0,'two-state witness below Cq')
for c in [Cq,F(1,30),F(1,25),F(9,200)]:
    check(dr(c,-12)<0,f'three-state witness at rational C={c}')

# Independent exact computation of R(hQ3) by rational matrix-polynomial evaluation.
def mm(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0))
             for j in range(n)] for i in range(n)]
def ma(A,B):
    return [[a+b for a,b in zip(rowa,rowb)] for rowa,rowb in zip(A,B)]
def ms(A,f):
    return [[f*x for x in row] for row in A]
def ident(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse(A):
    n=len(A)
    aug=[A[i][:]+ident(n)[i] for i in range(n)]
    for i in range(n):
        pivot=next(k for k in range(i,n) if aug[k][i])
        aug[i],aug[pivot]=aug[pivot],aug[i]
        den=aug[i][i];aug[i]=[v/den for v in aug[i]]
        for j in range(n):
            if j!=i:
                f=aug[j][i]
                aug[j]=[a-f*b for a,b in zip(aug[j],aug[i])]
    return [row[n:] for row in aug]
def matrixpoly(bivar,cc,AA):
    n=len(AA);pows=[ident(n)]
    for k in range(1,max(j for (i,j) in bivar)+1):
        pows.append(mm(pows[-1],AA))
    out=ms(ident(n),F(0))
    for (i,j),v in bivar.items():
        out=ma(out,ms(pows[j],v*cc**i))
    return out
Q=[[-F(1),F(1),F(0)],[F(0),-F(1),F(1)],[F(0),F(0),F(0)]]
A=ms(Q,F(12))
Rmat=mm(matrixpoly(num,Cq,A),inverse(matrixpoly(den,Cq,A)))
check(Rmat[0][1] == -F(16260,22193521), 'direct 3x3 matrix rational evaluation')
for row in Rmat:
    check(sum(row)==1,'mass conservation of rational matrix update')
check(Rmat[0][1]<0,'entrywise positivity failure on pure-birth generator')
# A first-row negative initial density occurs for column-state evolution Q^T.
initial=[row[0] for row in zip(*Rmat)]
check(min(initial)<0,'transposed generator maps a nonnegative column state negative')
print('VERIFY_OK',CHECKS,'exact-rational assertions')
