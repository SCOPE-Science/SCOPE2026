"""Standalone finite exact-arithmetic consistency checks for a planar reshuffled Kaczmarz model."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

u_perp = (Q(0), Q(1))
v_perp = (Q(-4, 5), Q(3, 5))
x = Q(9, 25)
P_u = ((Q(0), Q(0)), (Q(0), Q(1)))
P_v = ((Q(16, 25), Q(-12, 25)), (Q(-12, 25), Q(9, 25)))
checks = 0

def apply(P, z):
    return (P[0][0]*z[0]+P[0][1]*z[1], P[1][0]*z[0]+P[1][1]*z[1])

def norm2(z):
    return z[0]*z[0]+z[1]*z[1]

def transition(z, a, j):
    for P in [P_u]*j+[P_v]+[P_u]*(a-j):
        z = apply(P, z)
    return z

for a in range(1,9):
    m = Q(a+1)
    T = ((Q(a)*x*x/m, (x+Q(a-1)*x*x*x)/m),
         (x/m, x*x/m))
    for state,z in enumerate((u_perp, v_perp)):
        totals = [Q(0),Q(0)]
        for j in range(a+1):
            out = transition(z,a,j)
            endpoint = 1 if j==a else 0
            # The projection is onto the indicated line.
            expected_direction = v_perp if endpoint else u_perp
            assert out[0]*expected_direction[1] == out[1]*expected_direction[0]
            totals[endpoint] += norm2(out)/m
            checks += 2
        for endpoint in (0,1):
            assert totals[endpoint] == T[endpoint][state]
            checks+=1
    trace=T[0][0]+T[1][1]
    determinant=T[0][0]*T[1][1]-T[0][1]*T[1][0]
    assert trace==x*x
    assert determinant==-x*x*(1-x*x)/(m*m)
    checks+=2

for a in range(1,5):
    for k in range(1,6):
        for js in product(range(a+1), repeat=k):
            z=u_perp
            for j in js:
                z=transition(z,a,j)
            A_last = (js[-1]==a)
            C=sum(1 for prev,cur in zip(js,js[1:]) if prev==a and cur==0)
            exponent=2*k-int(A_last)-2*C
            assert exponent>=0
            assert norm2(z)==x**exponent, (a,k,js,norm2(z),exponent)
            checks+=2

for a in range(1,21):
    t=1.0/((a+1)**2)
    for X in [0.01,0.09,0.25,0.36,0.64,0.81,0.99]:
        lam=(X*X+sqrt(X**4+4*X*X*(1-X*X)*t))/2
        qs=X**(2*(1-t))
        assert qs<lam<X, (a,X,qs,lam)
        checks+=1

print(f'PASS: {checks} deterministic exact-arithmetic and floating-point consistency assertions')
