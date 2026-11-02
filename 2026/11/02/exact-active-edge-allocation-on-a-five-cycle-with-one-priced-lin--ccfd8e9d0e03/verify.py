"""Symbolic and numerical checks of the priced five-cycle spectral-gap theorem.
Requires sympy and numpy; execute: python verify.py.
This code is supplementary: the interval-wide inequalities are proved in RESULT.md.
"""
import math
import sympy as sp
import numpy as np

x,y=sp.symbols('x y',real=True)
d=5*x**2-6*x+2
b=(2*x-1)/(5*x-3)
t=(2*x-1)**2/d
q=sp.factor(-2*(1+sp.diff(b,x))/sp.diff(t,x))
D=50*x**4-90*x**3+65*x**2-24*x+4
E=10*x**2-10*x+3
alpha=-(5*x**2-2)*d*E/(2*(x-1)*(2*x-1)*(5*x-3)**2)
beta=(5*x-4)*(5*x-2)*D/(2*(x-1)*(2*x-1)*(5*x-3)**2)

def z(expr):
    assert sp.factor(sp.cancel(expr))==0,expr

# Two spectral branches have the eigenvalue 1.
z(1-(2*x+3*b)+5*x*b)
z((x+2*t-1)*(x+b-1)-x*x)
z(D-d*d-x*x*(5*x-3)**2)
z(sp.diff(b,x)+1+(q/2)*sp.diff(t,x))

# Derivatives and KKT identity, independently obtained from eigenvector Rayleigh quotients.
se=sp.Matrix([1,(x-1)/x,2*b*(x-1)/(x*(2*b-1)),(x-1)/x,1])
so=sp.Matrix([1,x/(x+b-1),0,-x/(x+b-1),-1])
seq=[(0,1),(1,2),(2,3),(3,4),(4,0)]
for vector in (se,so):
    z(sum(vector))
    w=[x,b,b,x,t]
    L=sp.zeros(5)
    for (i,j),ww in zip(seq,w):
        L[i,i]+=ww;L[j,j]+=ww;L[i,j]-=ww;L[j,i]-=ww
    for elem in (L*vector-vector):z(elem)

norme=sp.factor((se.T*se)[0]);normo=sp.factor((so.T*so)[0])
dee=lambda i:sp.factor((se[seq[i][0]]-se[seq[i][1]])**2/norme)
doo=lambda i:sp.factor((so[seq[i][0]]-so[seq[i][1]])**2/normo)
for i in range(5):
    price= q if i==4 else 1
    z(alpha*dee(i)+beta*doo(i)-price)
z(alpha+beta-2*x-2*b-q*t)
# Explicit rational coefficient positivity on x=(3+y)/5, y in [0,1].
P=2500*x**6-10125*x**5+16575*x**4-14100*x**3+6600*x**2-1620*x+164
bcoeff=[-sp.Rational(4,25),-sp.Rational(11,50),-sp.Rational(31,125),-sp.Rational(29,125),-sp.Rational(24,125),-sp.Rational(6,25),-sp.Rational(12,25)]
z(P.subs(x,(3+y)/5)-sum(sp.binomial(6,j)*bcoeff[j]*y**j*(1-y)**(6-j) for j in range(7)))
z(sp.diff(q,x)-(d*P)/((x-1)**2*(2*x-1)**2*(5*x-3)**3))

# Exact rational nontrivial witness q=25/16, normalized cost=4.
u=sp.Rational(7,10)
assert (sp.simplify(b.subs(x,u)),sp.simplify(t.subs(x,u)),sp.simplify(q.subs(x,u)))==(sp.Rational(4,5),sp.Rational(16,25),sp.Rational(25,16))
assert sp.simplify((2*x+2*b+q*t).subs(x,u))==4

# Independent five-by-five spectra, random perturbations and target prices.
rng=np.random.default_rng(27182818)
checks=0
for Q in [0.001,0.02,0.1,0.5,1.0,25/16,3,7,12,15.9]:
    lo=math.sqrt(2/5);hi=0.8
    for _ in range(70):
        mid=(lo+hi)/2
        if float(q.subs(x,mid))>Q: lo=mid
        else: hi=mid
    u=(lo+hi)/2
    aa=float(u);bb=float(b.subs(x,u));tt=float(t.subs(x,u))
    cost=2*aa+2*bb+Q*tt
    L=np.zeros((5,5))
    for (i,j),ww in zip(seq,[aa,bb,bb,aa,tt]):
        L[i,i]+=ww;L[j,j]+=ww;L[i,j]-=ww;L[j,i]-=ww
    eig=np.linalg.eigvalsh(L)
    assert abs(eig[1]-1)<2e-11 and abs(eig[2]-1)<2e-11,(Q,eig)
    checks+=2
    for j in range(150):
        v=np.exp(rng.normal(size=5)*1.3)
        v/=np.dot(v,[1,1,1,1,Q])
        LL=np.zeros((5,5))
        for (ii,jj),ww in zip(seq,v):
            LL[ii,ii]+=ww;LL[jj,jj]+=ww;LL[ii,jj]-=ww;LL[jj,ii]-=ww
        assert np.linalg.eigvalsh(LL)[1] <= 1/cost+3e-10
        checks+=1
print('PASS: symbolic eigenpairs, dual identity, degree-six Bernstein sign certificate, exact rational witness, and',checks,'numeric checks.')
