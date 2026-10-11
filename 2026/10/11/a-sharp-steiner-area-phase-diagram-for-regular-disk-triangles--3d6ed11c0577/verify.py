#!/usr/bin/env python3
"""Exact analytic identities for parallel-area phase transitions of regular disk triangles.
This code checks algebraic Fourier/Taylor certificates; the proof explains their use.
Requires Python 3 and SymPy. No random experiments are used as proof.
"""
from sympy import symbols, sqrt, sin, cos, diff, expand, simplify, series, Poly, I, factorial, Rational, pi, limit, sign

b,x,y,z=symbols('b x y z',real=True)
rt=sqrt(3)
f=1-x+rt*y
f1=y+rt*x
f2=x-rt*y
g=rt*y*y+3*b-3*x*y
g1=2*y*(rt*x+3*y)
g2=2*(rt*(x*x-y*y)+6*x*y)
A=g1*f-2*g*f1
B=f*(f-b*f1)
H=expand(A*(f1*(f-b*f1)-b*f*f2)-(g2*f-g1*f1-2*g*f2)*B)

# Laurent-Fourier representation H(b)=sum_{j,k} c[j,k]*b**j*exp(i*k*b).
Z=(z+1/z)/2;Y=(z-1/z)/(2*I)
poly=expand(H.subs({x:Z,y:Y}))
coeff={}
for term in poly.as_ordered_terms():
    j=k=0; c=1
    for fact in term.as_ordered_factors():
        if fact==b:j+=1
        elif fact==z:k+=1
        elif fact.is_Pow and fact.base==b:j+=int(fact.exp)
        elif fact.is_Pow and fact.base==z:k+=int(fact.exp)
        else:c*=fact
    coeff[(j,k)]=coeff.get((j,k),0)+c
coeff={p:simplify(c) for p,c in coeff.items() if simplify(c)!=0}
assert len(coeff)==20 and max(abs(k) for j,k in coeff)==4
assert max(j for j,k in coeff)==2
# Exact L1 coefficient sums, calculated from c[j,k] by complex absolute values.
sums=[simplify(sum(sqrt(simplify(c* c.conjugate())) for (jj,k),c in coeff.items() if jj==j)) for j in range(3)]
assert simplify(sums[0]-(14*sqrt(3)+6*sqrt(7)+2*sqrt(291)+4*sqrt(111)))==0
assert sums[1]==114 and sums[2]==48
assert sums[0]<117

# Degree-20 Taylor polynomial; verify ALL coefficients, not just selected ones.
Taylor=expand(sum(c*b**j*sum((I*k*b)**m/factorial(m) for m in range(21-j)) for (j,k),c in coeff.items()))
Taylor=expand(simplify(Taylor))
assert all(simplify(Taylor.coeff(b,n))==0 for n in range(6))
expected=[rt/4, Rational(12,5),-51*rt/80,-Rational(137,168),
          6337*rt/33600,Rational(11,112),-1067*rt/37800,
          -Rational(2267,554400),18943*rt/6899200,
          -Rational(53071,216216000),-3735917*rt/19372953600,
          Rational(105817,2306304000),108473503*rt/10461394944000,
          -Rational(50336081,14820309504000),
          -131402039*rt/296406190080000]
assert len(expected)==15
for j,c in enumerate(expected):
    assert simplify(Taylor.coeff(b,j+6)-c)==0,(j,Taylor.coeff(b,j+6),c)

# Rigorous error: for b in [0,3/5], |H-Taylor| <= C*b**21,
# with C <= sum L_j*4**(21-j)/(21-j)! < 1/5000.
C=117*4**21/factorial(21)+114*4**20/factorial(20)+48*4**19/factorial(19)
assert C<Rational(1,5000)
assert expected[0]>Rational(2,5)
assert abs(expected[2])<Rational(111,100)
assert abs(expected[3])<Rational(82,100)
negative_hi=sum(abs(c) for j,c in enumerate(expected) if j>=4 and c<0)
assert negative_hi<Rational(6,100)
# For 0<b<=3/5, Taylor/b**6 >= .4 + b*(2.4-1.11*b-.82*b*b-.06*b**5).
a=Rational(3,5)
assert Rational(12,5)-Rational(111,100)*a-Rational(82,100)*a*a-Rational(6,100)*a**5>0
assert Rational(2,5)-Rational(1,5000)>0

# Endpoint normalization independently checked with direct expressions.
v=symbols('v',positive=True)
ff=1-cos(v)+rt*sin(v)
GG=rt*sin(v)**2+3*(v-sin(v)*cos(v))
PP=6*v/ff
AA=GG/ff**2
assert simplify(ff.subs(v,pi/6)-1)==0
assert simplify(diff(PP,v).subs(v,pi/6)-(6-2*pi))==0
assert simplify(diff(AA,v).subs(v,pi/6)-(3+2*rt-2*pi))==0
assert limit(diff(PP,v),v,0,dir='+')==-1
assert limit(diff(AA,v),v,0,dir='+')==Rational(1,3)
print('PARALLEL_DISK_TRIANGLE_PHASE_CERTIFICATE_OK')
