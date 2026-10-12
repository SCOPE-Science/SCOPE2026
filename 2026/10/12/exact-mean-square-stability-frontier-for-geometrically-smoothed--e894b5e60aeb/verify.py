"""Exact-arithmetic spot tests for a diagonal KGSM moment law.
Run: python3 verify.py (Python 3 standard library only).
Finite checks corroborate formulas; the all-parameter proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def mat(beta, mass, prob):
    d=1-beta
    c=beta+d*mass
    return [[1-prob,2*(1-prob)*mass,mass*mass],
            [F(0), (1-prob)*c-prob*mass*d, mass*c],
            [prob*d*d,-2*prob*d*c,c*c]]

def mv(T,x):
    return [sum((T[i][j]*x[j] for j in range(3)),F(0)) for i in range(3)]

def step(x,y,selected,beta,mass):
    d=1-beta
    xn=(F(0) if selected else x)+mass*y
    yn=beta*y+d*(xn-x)
    return xn,yn

count=0
for prob,beta,mass in product((F(1,7),F(1,3),F(1,2),F(4,5)),
                             (F(0),F(1,4),F(1,2),F(4,5)),
                             (F(0),F(1,3),F(7,10),F(1))):
    T=mat(beta,mass,prob)
    d=1-beta
    a=2*d*d
    ell=2*beta*beta*prob-3*beta*beta+2*beta-2*prob+1
    gamma=beta*beta*(1-prob)-beta*prob-1
    pred=prob*(beta-1)*(a*mass*mass+ell*mass+gamma)
    Iminus=[[int(i==j)-T[i][j] for j in range(3)] for i in range(3)]
    assert determinant3(Iminus)==pred
    state=[F(1),F(0),F(0)]
    for k in range(1,6):
        state=mv(T,state)
        actual=[F(0),F(0),F(0)]
        for bits in product((0,1),repeat=k):
            x,y=F(1),F(0)
            weight=F(1)
            for select in bits:
                x,y=step(x,y,select,beta,mass)
                weight*=prob if select else (1-prob)
            for z,v in enumerate((x*x,x*y,y*y)):
                actual[z]+=weight*v
        assert state==actual
    count+=1
assert F(1,2)*(1-2*F(9,10)**2)==F(-31,100)
assert (F(5,2)-sqrt(17)/2) > F(0)
# Smoothness boundary for two equiprobable rows: critical mass
# (-beta+sqrt(beta+2))/(2(1-beta)).
for b in (0,0.1,0.4,0.5,0.8):
    c=(-b+sqrt(b+2))/(2*(1-b))
    g=lambda m:4*(1-b)**2*m*m+4*b*(1-b)*m +b*b-b-2
    assert abs(g(c))<1e-12
assert abs(sqrt(2)/2-0.7071067811865476)<1e-14
print(f'PASS: {count} exact rational determinant identities and {5*count} exact dynamic moment matches; threshold identities validated')
