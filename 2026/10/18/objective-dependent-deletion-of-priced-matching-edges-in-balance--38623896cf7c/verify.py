"""Direct finite checks for matching-priced bipartite resistance design.
These checks supplement, but do not replace, the analytical proof.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

checks = 0

def determinant_threshold(n):
    return n*(2*n-3)/((2*n-1)*(n-2))


def ensure(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def threshold(n):
    return n*n*(4*n*n-11*n+8)/((n-2)*(4*n**3-11*n*n+10*n-4))

def T(n,r):
    x=n-2+2*r;y=n-1+r
    return (2*(n-1)/x**2+0.5/y**2)/(1/n+(n-2)/x**2+0.5/y**2)

def allocation(n,t,B=1.):
    tc=threshold(n)
    if t>=tc:
        r=0.
    else:
        hi=1.
        while T(n,hi)>t:
            hi*=2
        r=brentq(lambda v:T(n,v)-t,0,hi,xtol=1.e-13)
    a=B/(n*(n-1+t*r)); b=a*r
    return a,b,r

def spectral_value(n,a,b):
    if a<=0:return math.inf
    return 2*n*((n-1)/(n*a)+(n-1)/((n-2)*a+2*b)+1/(2*((n-1)*a+b)))

def laplacian(n,weights):
    L=np.zeros((2*n,2*n))
    for i in range(n):
        for j in range(n):
            w=weights[i,j]
            L[i,i]+=w; L[n+j,n+j]+=w
            L[i,n+j]-=w; L[n+j,i]-=w
    return L

def matrix_value(L):
    eig=np.linalg.eigvalsh(L)
    ensure(abs(eig[0])<1e-8,'zero eigen')
    ensure(eig[1]>0,'connected')
    return len(L)*np.sum(1/eig[1:])

nvar=sp.symbols('n',integer=True,positive=True)
r,t=sp.symbols('r t',positive=True)
x=nvar-2+2*r; y=nvar-1+r
H=(nvar-1)/nvar+(nvar-1)/x+1/(2*y)
N=2*(nvar-1)/x**2+1/(2*y**2)
D=1/nvar+(nvar-2)/x**2+1/(2*y**2)
assert sp.simplify(sp.diff((nvar-1+t*r)*H,r)-(nvar-1)*D*(t-N/D))==0
checks+=1
assert sp.simplify((N/D).subs(r,0)-nvar**2*(4*nvar**2-11*nvar+8)/((nvar-2)*(4*nvar**3-11*nvar**2+10*nvar-4)))==0
checks+=1
assert sp.simplify((N/D).subs(r,1)-1)==0
checks+=1
detc=nvar*(2*nvar-3)/((2*nvar-1)*(nvar-2))
assert sp.factor((N/D).subs(r,0)-detc)==2*nvar*(nvar-1)*(4*nvar**2-9*nvar+6)/((nvar-2)*(2*nvar-1)*(4*nvar**3-11*nvar**2+10*nvar-4))
checks+=1
logtau=(nvar-1)*sp.log(x)+sp.log(y)-(2*nvar-1)*sp.log(nvar-1+t*r)
assert sp.simplify(sp.diff(logtau,r).subs(r,0).subs(t,detc))==0
checks+=1
assert sp.simplify((N/D).subs(r,0)-1-8*(nvar-1)**3/((nvar-2)*(4*nvar**3-11*nvar**2+10*nvar-4)))==0
checks+=1
# Derivative identity and its negative sign for all n >= 3, r>=0:
p=x**-2; q=y**-2
ensure(sp.simplify(sp.diff(N,r)*D-N*sp.diff(D,r)-(sp.diff(N,r)/nvar-nvar**2*p*q/(x*y)))==0,'T derivative cancellation')
for n in range(3,13):
    ensure(threshold(n)>1,'threshold >1')
    ensure(threshold(n)>determinant_threshold(n),'resistance design retains matching longer')
    for rv in [0.,.01,.1,1,3.,10.,100.]:
        ensure(T(n,rv)>=0,'T positive')
        ensure(T(n,rv+.001)<T(n,rv),'T decreasing')
    if n<12:ensure(threshold(n)>threshold(n+1),'threshold decreases in n')
    for av,bv in [(Fraction(1,4),Fraction(1,2)),(Fraction(3,7),Fraction(0,1)),(Fraction(2,5),Fraction(3,5))]:
        if n>5:break
        av=sp.Rational(av.numerator,av.denominator);bv=sp.Rational(bv.numerator,bv.denominator)
        L=sp.zeros(2*n)
        for i in range(n):
            for j in range(n):
                w=bv if i==j else av
                L[i,i]+=w;L[n+j,n+j]+=w
                L[i,n+j]-=w;L[n+j,i]-=w
        vals=L.eigenvals()
        want=[(sp.Integer(0),1), (sp.Rational(n)*av,n-1), ((n-2)*av+2*bv,n-1), (2*((n-1)*av+bv),1)]
        # Distinct eigenvalues can coalesce; collect multiplicity before comparison.
        coll={}
        for eigen,mul in want:coll[eigen]=coll.get(eigen,0)+mul
        ensure(vals==coll, f'exact spectrum n={n}, av={av}, bv={bv}, vals={vals}, want={coll}')
        # Direct exact Kirchhoff index from grounded inverse.
        H_=L+sp.ones(2*n)/(2*n)
        direct=2*n*(sp.trace(H_.inv())-1)
        calc=2*n*((n-1)/(n*av)+(n-1)/((n-2)*av+2*bv)+1/(2*((n-1)*av+bv)))
        ensure(sp.simplify(direct-calc)==0,'exact resistance')

rng=np.random.default_rng(13751)
for n in range(3,8):
    for tval in [.15,.4,.85,1.,1.1,1.4,2.2,3.5,10.]:
        B=1.7
        a,b,rstar=allocation(n,tval,B)
        ensure(abs(n*((n-1)*a+tval*b)-B)<1e-10,'budget')
        ensure((b>0)==(tval<threshold(n)),'support threshold')
        w=np.full((n,n),a)
        np.fill_diagonal(w,b)
        matrix=matrix_value(laplacian(n,w))
        theory=spectral_value(n,a,b)
        ensure(abs(matrix-theory)<1e-7*theory,'full matrix spectral')
        # The scalar rational formula is minimized at the analytical root.
        fun=lambda rr:spectral_value(n,B/(n*(n-1+tval*rr)), B*rr/(n*(n-1+tval*rr)))
        mini=minimize_scalar(fun,method='bounded',bounds=(0.,max(20.,rstar*3+2)),options={'xatol':1e-13})
        ensure(theory<=mini.fun+1e-6*theory,'numeric global scalar')
        for _ in range(12):
            # Asymmetric feasible conductances with the same total cost.
            rand=rng.lognormal(mean=0.,sigma=1.3,size=(n,n))
            costs=np.ones((n,n)); np.fill_diagonal(costs,tval)
            rand*=B/np.sum(costs*rand)
            ensure(matrix_value(laplacian(n,rand))>=theory-1e-8*theory,'unrestricted perturbation')
for n in [40,80,160,320,640,1280]:
    ensure(abs(n*(threshold(n)-determinant_threshold(n))-1)<.2,'phase-gap scaling')
for tval in [.15,.3,.55,.8]:
    c=(math.sqrt(2/tval-1)-1)/2
    a,b,rstar=allocation(12000,tval,1.)
    ensure(abs(rstar/12000-c)<3e-4,'large n matched ratio')

print('PASSED',checks,'finite checks')
