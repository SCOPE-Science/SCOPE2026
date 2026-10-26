"""Reproduce symbolic and finite exact checks for a uniform Berrut range bound.
Requires Python 3.10+ and sympy. Finite checks complement the general proof.
"""
from fractions import Fraction as Q
import sympy as sp

z,t = sp.symbols('z t')
f = t*(t-1)*(t-2)/(2*(t*t-t+1))
p = t**4-2*t**3+4*t**2-6*t+2
qpoly = 12*z**4+24*z**3+32*z**2-6*z-1
assert sp.factor(sp.diff(f,t)-p/(2*(t*t-t+1)**2)) == 0
assert sp.simplify(sp.resultant(p,sp.together(z-f).as_numer_denom()[0],t) - 12*qpoly) == 0
assert p.subs(t,0)>0 and p.subs(t,sp.Rational(1,2))<0
root_t = float(sp.nroots(p, maxsteps=200)[0]); root_z=float(f.subs(t,root_t))
assert 0<root_t<.5 and abs(root_z-.255032152490845)<1e-12
assert abs(float(qpoly.subs(z,root_z)))<1e-9
print('critical point',root_t,'sharp defect',root_z)

def cs(n,m,v):
    x=m+v
    w=[(1 if (j-m)%2==0 else -1)/(x-j) for j in range(n+1)]
    den=sum(w,Q(0))
    a=sum(((1 if j%2 else -1)/(j+v) for j in range(1,m+1)),Q(0))
    b=sum(((1 if j%2 else -1)/(j+1-v) for j in range(1,n-m)),Q(0))
    u=1/v+1/(1-v)
    assert den==u-a-b
    assert den>0
    heights=[sum(w[k:],Q(0))/den for k in range(1,n+1)]
    assert all(-b/den<=h<=1+a/den for h in heights)
    if m>=1: assert heights[m-1]==1+a/den
    if m+2<=n:assert heights[m+1]==-b/den
    if n>1: assert max(max(h-1,-h) for h in heights)==max(a,b)/den
    assert max(a,b)/den<=max(1/(1+v),1/(2-v))/(u-1/(1+v)-1/(2-v))

for n in range(1,31):
    for m in range(n):
        for k in range(1,35):cs(n,m,Q(k,35))
print('exact-rational checks for n=1..30, all cells and 34 positions each: passed')

# For y=(0,1,1,1), the n=3 step at X=1+root_t is 1+root_z.
rt=root_t; X=1+rt
weights=[(-1)**(j-1)/(X-j) for j in range(4)]
value=sum(weights[1:])/sum(weights)
assert abs(value-(1+root_z))<1e-12
# reflected complementary data (0,0,0,1) at X=2-root_t.
X=2-rt
weights=[(-1)**(j-1)/(X-j) for j in range(4)]
value=weights[-1]/sum(weights)
assert abs(value+root_z)<1e-12
print('sharp four-node witnesses: passed')
