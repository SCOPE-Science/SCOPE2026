"""Exact rational checks for a two-patch source--sink map.
Run with Python 3; no third-party dependencies.
"""
from fractions import Fraction as F

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):z[i+j]+=u*v
    return z
def val(a,t):
    v=F(0)
    for c in a[::-1]:v=v*t+c
    return v
U=[1,3,3,1]
Rpoly=[13,-165,-45,25]
S=[0]+Rpoly
P=[33,-178,-9165,17364,11995,-4854,-1695,500]
# The elimination identity is 25 S U - (U-S)(108 x+4 S) = 5 x P.
L=add(mul([25],mul(S,U)),mul([-1],mul(add(U,mul([-1],S)),add([0,108],mul([4],S)))))
assert L==[0]+[5*a for a in P]
# Four sign changes in descending coefficient order: exactly four positive
# roots (each simple), one in each of these disjoint rational brackets.
assert sum(P[i]*P[i+1]<0 for i in range(len(P)-1))==4
pairs=[(F(53,1000),F(54,1000)),(F(43,100),F(44,100)),
       (F(16,5),F(13,4)),(F(18,5),F(361,100))]
for lo,hi in pairs:
    assert val(P,lo)*val(P,hi)<0
# R'=75x^2-90x-165 = 15(x+1)(5x-11): R decreases to 11/5,
# increases thereafter. These bounds determine physical feasibility.
a,b=pairs[0]
assert val(Rpoly,b)>0 and b*13<F(1) # 0<V(x)<1 on first bracket.
a,b=pairs[1]
assert val(Rpoly,a)<0 # V(x)<0 throughout bracket 2.
a,b=pairs[2]
assert val(Rpoly,b)<0 # V(x)<0 throughout bracket 3.
a,b=pairs[3]
assert val(Rpoly,a)>0 and val(Rpoly,b)<8
assert b*8<(1+a)**3 # 0<V(x)<1 on last bracket.
# The sufficient positive-retention inequality is strict at this tuple.
assert F(9,10)>F(1,3)
assert 4*(F(4,5)*6)**2>27*F(9,10)
# At extinction the eigenvalues are (8 +/- 2sqrt(31))/25; both modulus <1.
assert (8+2*6)<25 and 2*6<8+25 # sqrt(31)<6, enough for bounds.
# Derivatives at x: H'= (.48+18.24x+4.8x^2)/(1+x)^4,
# K'= (108/25)(1-2x)/(1+x)^4.
Hprime=lambda x:(F(12,25)+F(456,25)*x+F(24,5)*x*x)/(1+x)**4
Kprime=lambda x:F(108,25)*(1-2*x)/(1+x)**4
lo,hi=pairs[0]
assert (F(12,25)+F(456,25)*lo)/(1+hi)**4>1
assert lo>0 and hi<F(1,2)
# At the small positive root, J is nonnegative, lambda_+>1,
# lambda_-<J22<4/25 and lambda_->-sqrt(J12*J21)>-1.
assert F(1,25)*F(108,25)<1
lo,hi=pairs[-1]
# Upper bounds on absolute Jacobian row sums throughout last bracket.
H_bound=(F(12,25)+F(456,25)*hi+F(24,5)*hi**2)/(1+lo)**4
K_bound=F(108,25)*(2*hi-1)/(1+lo)**4
assert H_bound+F(1,25)<1
assert K_bound+F(4,25)<1
# Re-verify the low-density Jacobian numerators independently.
assert F(4,5)*6*(1-F(9,10))==F(12,25)
assert F(4,5)*F(1,5)*F(1,4)==F(1,25)
assert F(4,5)*6*F(9,10)==F(108,25)
assert F(4,5)*F(4,5)*F(1,4)==F(4,25)
print('PASS: polynomial elimination, four exact root brackets, physical roots, extinction and hyperbolicity bounds')
