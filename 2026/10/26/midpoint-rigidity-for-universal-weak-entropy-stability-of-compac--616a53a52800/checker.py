"""Exact-rational checks of the stated two-stage cRKDG identities."""
from fractions import Fraction as F
from itertools import product


def mean_flux(a,b,r):
    return a+(1-r)*b


def stage_fluxes(a,b,r,gamma):
    w2=1/(2*gamma)
    w1=1-w2
    return (a+b,a+(1-2*gamma*r)*b,w1,w2)


def new_mean(a,b,a_left,b_left,r,gamma):
    p1,p2,w1,w2=stage_fluxes(a,b,r,gamma)
    q1,q2,_,_=stage_fluxes(a_left,b_left,r,gamma)
    return a-r*(w1*(p1-q1)+w2*(p2-q2))


def mean_square(a,b):
    return (a*a+b*b/F(3))/2


def square(x):
    return x*x/2


def entropy_budget_square(a,b,a_left,b_left,r,gamma):
    p1,p2,w1,w2=stage_fluxes(a,b,r,gamma)
    q1,q2,_,_=stage_fluxes(a_left,b_left,r,gamma)
    return mean_square(a,b)-r*(w1*(square(p1)-square(q1))+w2*(square(p2)-square(q2)))

n=0
for r,gamma,a,b,al,bl in product(
    [F(0),F(1,8),F(1,3),F(2,3),F(1)],
    [F(1,2),F(2,3),F(1),F(3,2)],
    [F(-2),F(1,2)],
    [F(-3,2),F(1)],
    [F(-1),F(5,2)],
    [F(-2,3),F(3,4)]):
    assert new_mean(a,b,al,bl,r,gamma)==a-r*(mean_flux(a,b,r)-mean_flux(al,bl,r))
    if gamma==F(1,2):
        ell=a-r*b
        q=mean_flux(al,bl,r)
        exact=(b*b*((1-r)**3+r**3)/F(6)+r*(1-r)*(ell-q)**2/F(2))
        assert entropy_budget_square(a,b,al,bl,r,gamma)-square(new_mean(a,b,al,bl,r,gamma))==exact
        assert exact>=0
    n+=1

# A concrete C^3, globally strongly convex entropy that fails at arbitrarily
# specified tableau parameters in the non-midpoint family (example gamma=1).
r=F(1,4);gamma=F(1);delta=F(1,4);t=1-delta;mu=F(1,1000)
# current polynomial u(xi)=xi; upstream constant -r
avg_core=delta**5/F(10)
p1,p2,w1,w2=stage_fluxes(F(0),F(1),r,gamma)
assert p1==1 and p2==F(1,2) and t==F(3,4)
core_budget=avg_core-r*(w1*(max(p1-t,F(0))**4)+w2*(max(p2-t,F(0))**4))
quad_defect=entropy_budget_square(F(0),F(1),-r,F(0),r,gamma)-square(-r)
assert core_budget==-F(1,2560)
assert quad_defect==F(25,384)
assert core_budget+mu*quad_defect==-F(1,3072)

# Every positive step admits a quartic-hinge counterexample when gamma>1/2.
for gamma,r in product([F(2,3),F(1),F(3,2),F(7,2)], [F(1,100),F(1,4),F(1),F(3)]):
    w1=1-F(1)/(2*gamma)
    delta=min(F(1,4),gamma*r,F(5)*r*w1)
    assert 0<delta<2*gamma*r and delta<10*r*w1 and 1-delta>-r
    defect=delta**5/F(10)-r*w1*delta**4
    assert defect<0
    quad=entropy_budget_square(F(0),F(1),-r,F(0),r,gamma)-square(-r)
    mu=(-defect)/(2*(abs(quad)+1))
    assert defect+mu*quad<0

# At gamma=1/2 the Courant boundary is sharp even for constants.
for r in [F(9,8),F(3,2),F(2)]:
    assert entropy_budget_square(F(0),F(0),F(1),F(0),r,F(1,2))-square(r)==r*(1-r)/2<0

# At alternating Fourier mode, the determinant of the full affine update is
# 1-2r+6r^2; for r>1/3 it exceeds one.
for r in [F(2,5),F(1,2),F(1)]:
    m11=1-2*r; m12=-2*r*(1-r)
    m21=6*r; m22=1-6*r*r
    assert m11*m22-m12*m21==1-2*r+6*r*r>1

print(f'PASS: {n} exact coefficient/entropy identities, explicit strongly convex witness, 16 universal family witnesses, and Fourier determinant checks.')
