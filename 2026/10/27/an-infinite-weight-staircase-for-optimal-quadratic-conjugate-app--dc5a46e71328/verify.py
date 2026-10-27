"""Exact checks for the weighted Bergman quadratic conjugate approximation theorem.

Requires Python 3 and SymPy.  All algebraic identities are exact.
"""
from fractions import Fraction
import math
import sympy as sp

b,n=sp.symbols('b n', real=True)

def v_symbol(k):
    return ((k+1)*(k+2)/((b+k+2)*(b+k+3))
            - k*(k-1)/((b+k)*(b+k+1)))

v0=2/((b+2)*(b+3))
v1=6/((b+3)*(b+4))
v=v_symbol(n)
closed=2*(b+1)*(2*b*n+b+2*n*n+4*n)/((b+n)*(b+n+1)*(b+n+2)*(b+n+3))
delta=4*(b+1)*(b*b+(1-n)*b-2*n*n-5*n)/sp.prod(b+n+i for i in range(5))
assert sp.cancel(v-closed)==0
assert sp.cancel(v_symbol(n+1)-v_symbol(n)-delta)==0
assert sp.cancel(v1-v0-4*(b+1)/((b+2)*(b+3)*(b+4)))==0
assert sp.cancel(v_symbol(2)-v1-4*(b*b-7)/sp.prod(b+i for i in (2,3,4,5)))==0
count=4

def moment_int(k,beta):
    acc=Fraction(1)
    for t in range(1,int(beta)+2):
        acc*=Fraction(t,k+t)
    return acc

def variance(k,beta):
    mm=moment_int
    a=mm(k+2,beta)/mm(k,beta)
    if k>=2:a-=mm(k,beta)/mm(k-2,beta)
    return a

def index_at(beta):
    # Exact sign test of adjacent differences; no floating thresholds.
    index=1
    while True:
        q=beta*beta+(1-index)*beta-2*index*index-5*index
        if q>0:index+=1
        else:return index

for beta in [Fraction(-9,10),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1),Fraction(2),Fraction(3),Fraction(5),Fraction(8),Fraction(11),Fraction(20),Fraction(100)]:
    for j in range(120):
        exact=variance(j,beta) if beta.denominator==1 and beta>=0 else Fraction(1)
        expr=sp.factor((v0 if j==0 else v_symbol(j)).subs(b,sp.Rational(beta.numerator,beta.denominator)))
        assert expr.is_Rational and expr>=0
        if beta.denominator==1 and beta>=0:assert sp.Rational(exact.numerator,exact.denominator)==expr
        count+=1
    vals=[sp.Rational((v0 if j==0 else v_symbol(j)).subs(b,sp.Rational(beta.numerator,beta.denominator))) for j in range(120)]
    i=index_at(beta)
    assert vals[i]==max(vals)
    count+=1

for j in range(1,18):
    root=(j-1+sp.sqrt(9*j*j+18*j+1))/2
    assert sp.simplify((v_symbol(j+1)-v_symbol(j)).subs(b,root))==0
    assert 2*j<root<2*j+1
    count+=3

# Direct orthogonal-projection identity on finite holomorphic polynomials.
for beta in (0,1,2,5):
    for t in range(31):
        coeff=[complex((i+3*t)%11-5,(i*7+t)%13-6) for i in range(1,11)]
        m=[float(moment_int(k,beta)) for k in range(15)]
        unproj=sum(abs(a)**2*m[k+2] for k,a in enumerate(coeff))
        projected=sum(abs(coeff[k])**2*m[k]**2/m[k-2] for k in range(2,len(coeff)))
        diagonal=sum(abs(coeff[k])**2*m[k]*(float(variance(k,beta))) for k in range(len(coeff)))
        assert math.isclose(unproj-projected,diagonal,rel_tol=1e-10,abs_tol=1e-10)
        count+=1

# Parameter-dependent norming modes; compare with long prefixes.
for beta in [0.01,0.2,1.,2.,2.7,4.7,4.8,6.,10.,20.,50.,100.,1000.]:
    i=index_at(Fraction(str(beta)))
    vals=[float((v0 if j==0 else v_symbol(j)).subs(b,beta)) for j in range(min(3000,2*int(beta)+100))]
    assert i==max(range(len(vals)),key=lambda k:vals[k])
    count+=1

for beta in (1000,5000,20000):
    i=index_at(Fraction(beta))
    val=float(v_symbol(i).subs(b,beta))
    assert abs(beta*val-16/27)<15/beta
    assert abs(i/beta-0.5)<2/beta
    count+=2

print('PASS: exact rational identities, root boundaries, direct projection checks, finite mode tests.')
print('Assertion groups completed:',count)
print('First transition beta = sqrt(7) =',sp.N(sp.sqrt(7),16))
print('Limiting beta * sharp squared constant = 16/27.')
