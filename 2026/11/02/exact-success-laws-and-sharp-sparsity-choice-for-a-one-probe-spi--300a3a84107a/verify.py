"""Reproduce finite checks of the one-probe spike benchmark.
Mathematical proof and scope are in RESULT.md; these are independent numerical and
exact-rational consistency checks, not infinite certificates.
"""
import itertools
import math
from fractions import Fraction
from math import comb
import numpy as np

checks=0

def check(c, label):
    global checks
    if not c:
        raise AssertionError(label)
    checks+=1

for m in range(2,7):
    for aa,bb in [(3,1),(5,2),(7,3)]:
        a=Fraction(aa); b=Fraction(bb)
        gap=a*a-b*b
        steps=[b*b*j*gap/(a*a+b*b*j) for j in range(m+1)]
        check(steps[0]==0 and all(steps[j]<steps[j+1] for j in range(m)), 'increasing levels')
        check(steps[-1] < gap,'gap separation')
        for pn,pd in [(1,4),(1,2),(3,4),(1,1)]:
            p=Fraction(pn,pd)
            spectrum={}
            for state in itertools.product((-1,0,1),repeat=m+1):
                weight=Fraction(1)
                for x in state:
                    weight*=p/2 if x else 1-p
                if not weight: continue
                w=np.array(state,dtype=float)
                A=np.diag([aa]+[bb]*m)
                v=A@w
                if np.linalg.norm(v)>0:
                    q=v/np.linalg.norm(v)
                    R=A-np.outer(q,q@A)
                else:
                    R=A.copy()
                eig=float(np.linalg.norm(R,2)**2)
                fro=float(np.linalg.norm(R,'fro')**2)
                if state[0]!=0:
                    j=sum(x!=0 for x in state[1:])
                    formula_s=b*b+steps[j]
                    formula_f=m*b*b+steps[j]
                elif any(x!=0 for x in state[1:]):
                    formula_s=a*a
                    formula_f=a*a+(m-1)*b*b
                else:
                    formula_s=a*a
                    formula_f=a*a+m*b*b
                check(abs(eig-float(formula_s))<1e-9 * (1+float(formula_s)), 'spectral formula')
                check(abs(fro-float(formula_f))<1e-9 * (1+float(formula_f)), 'frobenius formula')
                key=(formula_s,formula_f)
                spectrum[key]=spectrum.get(key,Fraction(0))+weight
            for j in range(m+1):
                key=(b*b+steps[j],m*b*b+steps[j])
                expected=p * Fraction(comb(m,j))*p**j*(1-p)**(m-j)
                check(spectrum.get(key,Fraction(0))==expected, 'exact level masses')
            key=(a*a,a*a+(m-1)*b*b)
            check(spectrum.get(key,Fraction(0))==(1-p)*(1-(1-p)**m),'missed spike')
            key=(a*a,a*a+m*b*b)
            check(spectrum.get(key,Fraction(0))==(1-p)**(m+1),'all-zero')
            check(sum(spectrum.values())==1,'normalization')

# Independent differentiation check in polynomial integer arithmetic.
for m in range(2,30):
    for k in range(m):
        # q=p B_{m,k}; compare derivative via exact arithmetic.
        for p in (Fraction(1,11),Fraction(2,7),Fraction(3,5),Fraction(9,10)):
            F=sum(Fraction(comb(m,j))*p**j*(1-p)**(m-j) for j in range(k+1))
            fp=F - Fraction(m*comb(m-1,k))*p**(k+1)*(1-p)**(m-1-k)
            # numerical finite diff in exact finite arithmetic of polynomial expression
            eps=Fraction(1,100000)
            def f(t):
                return t*sum(Fraction(comb(m,j))*t**j*(1-t)**(m-j) for j in range(k+1))
            diff=(f(p+eps)-f(p-eps))/(2*eps)
            check(abs(float(fp-diff))<0.0003,'derivative check')
        if k==0:
            pstar=Fraction(1,m+1)
            check(abs(float(pstar*(1-pstar)**m) - (m/(m+1))**m/(m+1))<1e-14,'k0 optimum')
        if k==m-1:
            pstar=(m+1)**(-1/m)
            check(abs(1-(m+1)*pstar**m)<1e-12,'k=m-1 optimum')

# Sharp large-m Poisson benchmark for k=0.
for m in (50,100,500,2000):
    p=1/(m+1)
    v=m*p*(1-p)**m
    check(abs(v-1/math.e)<0.016,'Poisson k0 asymptotic')

# Unique positive root and global sparsity optimum for all tested m,k.
def CDF(m,k,p):
    return sum(comb(m,j)*p**j*(1-p)**(m-j) for j in range(k+1))

def objective(m,k,p):
    return p*CDF(m,k,p)

for m in range(2,80):
    for k in range(m):
        lo=0.0; hi=1.0
        for _ in range(85):
            x=(lo+hi)/2
            der=CDF(m,k,x)-m*comb(m-1,k)*x**(k+1)*(1-x)**(m-1-k)
            if der>=0: lo=x
            else: hi=x
        ps=(lo+hi)/2
        for j in range(101):
            p=j/100
            check(objective(m,k,ps)+1e-12>=objective(m,k,p),'unique optimum grid')
        check(0<ps<1,'interior maximizer')
        if k==0:
            check(abs(ps-1/(m+1))<1e-12,'lowest-band pstar')
        if k==m-1:
            check(abs(ps-(m+1)**(-1/m))<1e-12,'highest-band pstar')

# Large-dimensional low-band Poisson limit at fixed k.
for k in range(5):
    def poisson_poly(x):
        return sum(x**j/math.factorial(j) for j in range(k+1))-x**(k+1)/math.factorial(k)
    lo,hi=0.,20.
    for _ in range(100):
        mid=(lo+hi)/2
        if poisson_poly(mid)>0: lo=mid
        else: hi=mid
    lam=(lo+hi)/2
    target=lam*math.exp(-lam)*sum(lam**j/math.factorial(j) for j in range(k+1))
    for m in (300,1000):
        lo,hi=0.,1.
        for _ in range(95):
            p=(lo+hi)/2
            d=CDF(m,k,p)-m*comb(m-1,k)*p**(k+1)*(1-p)**(m-1-k)
            if d>0: lo=p
            else: hi=p
        ps=(lo+hi)/2
        check(abs(m*ps-lam)<0.09,'Poisson optimizer asymptotic')
        check(abs(m*objective(m,k,ps)-target)<0.09,'Poisson success asymptotic')

print('PASS: %d independent finite checks' % checks)
