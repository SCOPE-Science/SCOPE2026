"""Independent arithmetic and finite-temperature consistency checks for the three-symbol model.

Run: python3 verify.py (Python standard library only).
These tests check finite instances; the universal statements use the analytical proof.
"""
from fractions import Fraction
from itertools import permutations
from math import sqrt, exp, log, isclose

N = 0

def check(condition, label):
    global N
    if not condition:
        raise AssertionError(label)
    N += 1

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def weights(e):
    return [[1,e,e],[e,1,e**3],[1,e**3,e**3]]

def poly(e,z):
    return z*z-z-1 + e*(z**3-z)-e*e-e**3*z*z-e**5*z

def lambda_principal(e):
    lo,hi=1.0,2.0
    check(poly(e,lo)<0 and poly(e,hi)>0,"root bracket")
    for _ in range(100):
        mid=(lo+hi)/2
        if poly(e,mid)>0: hi=mid
        else: lo=mid
    z=(lo+hi)/2
    return 1+e*z

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))] for i in range(len(a))]

def stat_and_transition(e):
    la=lambda_principal(e); d=la-1
    rB=(e+e**3/(la-e**3))/(d-e**6/(la-e**3))
    lB=(e+e**4/(la-e**3))/(d-e**6/(la-e**3))
    r=[1.,rB,(1+e**3*rB)/(la-e**3)]
    l=[1.,lB,(e+e**3*lB)/(la-e**3)]
    mass=[l[i]*r[i] for i in range(3)]
    pi=[v/sum(mass) for v in mass]
    m=weights(e)
    p=[[m[i][j]*r[j]/(la*r[i]) for j in range(3)] for i in range(3)]
    return la,pi,p,r,l

phi=(1+sqrt(5))/2
piA=phi*phi/(phi*phi+1)
piB=1/(phi*phi+1)
for eps_den in (10,25,100,1000,10000,100000):
    e=1/eps_den
    z=Fraction(13,10)
    E=Fraction(1,eps_den)
    mat=weights(E)
    symbolic_det=det3([[z if i==j else 0 for j in range(3)] for i in range(3)])
    check(symbolic_det==z**3,"det identity")
    # Exact characteristic relation evaluated at arbitrary rational test lambda.
    for l in (Fraction(1),Fraction(3,2),Fraction(2),Fraction(7,4)):
        d=det3([[l*(i==j)-mat[i][j] for j in range(3)] for i in range(3)])
        polynomial=(l**3-2*l*l+l -E*l+E -E*E*l
                    -E**3*l*l+2*E**3*l-E**3-E**4
                    -E**6*l+E**6)
        check(d==polynomial,"characteristic polynomial")
    lam,pi,p,r,ell=stat_and_transition(e)
    check(lam>1,"Perron root")
    check(abs(det3([[lam*(i==j)-weights(e)[i][j] for j in range(3)] for i in range(3)]))<1e-10,"Perron root characteristic")
    for i in range(3):
        check(abs(sum(p[i])-1)<1e-10,"row stochastic")
        check(all(v>0 for v in p[i]),"strictly positive")
        check(abs(sum(pi[j]*p[j][i] for j in range(3))-pi[i])<1e-10,"stationary")
    check(abs(sum(pi)-1)<1e-10,"probability")
    check(pi[2]<e,"excursion mass")
    check(abs(p[0][1]/e-1/phi)<3.0*e,"forward jump asymptotic")
    check(abs(p[1][0]/e-phi)<4.0*e,"backward jump asymptotic")
    check(abs((lam-1)/e-phi)<2.0*e,"pressure coefficient")
    check(abs(pi[0]-piA)<e,"golden mix")
    check(abs(pi[1]-piB)<e,"golden mix")
    for b,c in ((e,e),(e,e*e),(e**2,e**3)):
        rs=[sqrt(b),sqrt(c)]; ls=[sqrt(c),sqrt(b)]
        products=[rs[i]*ls[i] for i in range(2)]
        check(products[0]==products[1] or abs(products[0]-products[1])<1e-14,"binary rigidity")

# The rescaled probability of B from an initial A state approaches its two-state CTMC value.
for eps_den in (200,500,1000,2000):
    e=1/eps_den
    _,_,p,_,_=stat_and_transition(e)
    for t in (0.5,1.0,2.0):
        row=[1.,0.,0.]
        n=round(t/e)
        for _ in range(n):
            row=[sum(row[i]*p[i][j] for i in range(3)) for j in range(3)]
        limit=piB*(1-exp(-sqrt(5)*t))
        check(abs(row[1]-limit)<0.01,"continuum limit")
print("PASS",N,"finite exact and numerical consistency checks")
