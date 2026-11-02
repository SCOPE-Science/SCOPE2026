"""Exact two-epoch fitness-order classification for the finite Moran birth-death chain.
Requires sympy >= 1.10; run: python moran_epoch_checker.py
All identities use exact symbolic/rational arithmetic, not floating-point samples.
"""
from fractions import Fraction as F
from itertools import product
from sympy import Rational, Symbol, factor, simplify, expand

a,b=Symbol('a',positive=True),Symbol('b',positive=True)

def up(n,k,w):
    return Rational(k*(n-k),n)*w/(k*w+n-k) if 0<k<n else 0

def down(n,k,w):
    return Rational(k*(n-k),n)/(k*w+n-k) if 0<k<n else 0

def drift(n,k,w):
    return up(n,k,w)-down(n,k,w)

def two_order_gap(n,k,a,b):
    fa=[drift(n,j,a) for j in range(n+1)]
    fb=[drift(n,j,b) for j in range(n+1)]
    def residual(first,second,second_f):
        return up(n,k,first)*(second_f[k+1]-second_f[k])+down(n,k,first)*(second_f[k-1]-second_f[k])
    return residual(a,b,fb)-residual(b,a,fa)

P=3*a*a*b*b+6*a*a*b-9*a*a+6*a*b*b+116*a*b+6*a-9*b*b+6*b+3
formulas = {
 (2,1):(a-b)/(2*(a+1)*(b+1)),
 (3,1):4*a*b*(a-b)/((a+2)*(2*a+1)*(b+2)*(2*b+1)),
 (3,2):4*(a-b)/((a+2)*(2*a+1)*(b+2)*(2*b+1)),
 (4,1):3*a*b*(a-b)/(2*(a+1)*(a+3)*(b+1)*(b+3)),
 (4,2):(a-b)*P/(4*(a+1)*(a+3)*(3*a+1)*(b+1)*(b+3)*(3*b+1)),
 (4,3):3*(a-b)/(2*(a+1)*(3*a+1)*(b+1)*(3*b+1)),
}
count=0
for (n,k),formula in formulas.items():
    assert simplify(two_order_gap(n,k,a,b)-formula)==0,(n,k)
    count+=1
x,y=Symbol('x',nonnegative=True),Symbol('y',nonnegative=True)
positive_poly=3*x*x*y*y+12*x*x*y+12*x*y*y+152*x*y+128*x+128*y+128
assert expand(P.subs({a:1+x,b:1+y})-positive_poly)==0
assert simplify(P.subs({a:1/(1+x),b:1/(1+y)})-positive_poly/((1+x)**2*(1+y)**2))==0
assert simplify(P.subs(b,1)-128*a)==0
assert simplify(P-(3*(a-1)*(a+3)*b*b+(6*a*a+116*a+6)*b-3*(a-1)*(3*a+1)))==0
count+=4

# Independently form the one-step stochastic matrix by exact fractions,
# then evaluate both complete two-step distributions and compare their means.
def kernel(n,w):
    out=[]
    for k in range(n+1):
        row=[F(0) for _ in range(n+1)]
        if 0<k<n:
            den=k*w+n-k
            row[k+1]=F(k*(n-k),n)*w/den
            row[k-1]=F(k*(n-k),n)/den
            row[k]=1-row[k+1]-row[k-1]
        else:
            row[k]=F(1)
        assert sum(row)==1
        out.append(row)
    return out

def direct(n,k,aa,bb):
    ka=kernel(n,aa);kb=kernel(n,bb)
    return sum(F(j)*(sum(ka[k][h]*kb[h][j] for h in range(n+1))-sum(kb[k][h]*ka[h][j] for h in range(n+1))) for j in range(n+1))

for n in (2,3,4):
    for k in range(1,n):
        for aa,bb in product((F(1,7),F(1,3),F(1,2),F(4,5),F(1),F(6,5),F(2),F(5),F(11)),repeat=2):
            aa_s=Rational(aa.numerator,aa.denominator)
            bb_s=Rational(bb.numerator,bb.denominator)
            symbolic=F(formulas[n,k].subs({a:aa_s,b:bb_s}))
            assert direct(n,k,aa,bb)==symbolic,(n,k,aa,bb)
            count+=1
assert direct(4,2,F(5),F(1,5)) == F(-1,96)
assert direct(4,2,F(5),F(1,2)) == F(5,224)
count+=2
print(f'PASS: {count} exact symbolic identities and independent rational two-step checks')
