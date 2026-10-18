"""Independent exact-arithmetic finite checks for the tent-memory entrance theorem.

The asymptotic statements rely on the analytic proof; this script is not an
infinite proof or a certificate of novelty.
"""
from fractions import Fraction as F
from math import sqrt

B=((F(0), F(1)), (F(1,2), F(3,2)))
def rowmul(a):
    return (a[0]*B[0][0]+a[1]*B[1][0],
            a[0]*B[0][1]+a[1]*B[1][1])

def clipped(poly, a, b, t, keep_ge):
    def val(z): return a*z[0]+b*z[1]-t
    result=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        vp,vq=val(p),val(q)
        onp=vp>=0 if keep_ge else vp<=0
        onq=vq>=0 if keep_ge else vq<=0
        if onp: result.append(p)
        if onp!=onq:
            result.append(((vq*p[0]-vp*q[0])/(vq-vp),
                           (vq*p[1]-vp*q[1])/(vq-vp)))
    return result

def area(poly):
    if len(poly)<3:return F(0)
    return abs(sum(p[0]*q[1]-p[1]*q[0]
                   for p,q in zip(poly,poly[1:]+poly[:1])))/2

square=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
row=(F(1),F(3))
trow=(F(1),F(2))
remaining_areas={}
conditional={}
for n in range(1,19):
    row_next=rowmul(row)
    trow=rowmul(trow)
    if n>=3:
        surviving=clipped(square,*row,F(2),False)
        assert area(surviving)==F(2)/(row[0]*row[1]), 'survivor area'
        # Geometric first-entrance region, with two linear inequalities.
        entrance=clipped(surviving,*row_next,F(2),True)
        assert area(entrance)==(F(2)/(row[0]*row[1])-
                                F(2)/(row_next[0]*row_next[1]))
        # The exact infinitely invariant upper strip is 5/3<=x+2y<=7/3.
        captured=clipped(entrance,*trow,F(5,3),True)
        captured=clipped(captured,*trow,F(7,3),False)
        assert F(0)<area(captured)<area(entrance)
        conditional[n]=float(area(captured)/area(entrance))
    row=row_next
rho=(3+sqrt(17))/4
pstar=2*(1+3*rho)**2/(3*(rho*rho-1)*(1+2*rho)**2)
assert abs(pstar-0.5935921354681382)<1e-14
assert abs(conditional[11]-pstar)<2e-9
assert abs(conditional[16]-pstar)<1e-12
# The limiting signed phase density 3(2+t)/4 normalizes and symmetrizes
# to the constant 3 on 0<t<1/3.
for t in (0,.09,.25,1/3):
    f=lambda x: F(3,4)*(2+x)
    assert abs(float(f(t)+f(-t))-3)<1e-12
# Exact companion upper-branch dynamics for a nontrivial rational state.
x,y=F(2,5),F(4,5)
assert x+3*y>=2
H=x+y-F(4,3);s=x+2*y-2
nx,ny=y,2-(x+3*y)/2
assert nx+ny-F(4,3)==-H/2
assert nx+2*ny-2==-s
print('VERIFY_OK', 'polygon_levels=3..18',
      'conditional_at_16='+str(conditional[16]),
      'limit='+str(pstar))
