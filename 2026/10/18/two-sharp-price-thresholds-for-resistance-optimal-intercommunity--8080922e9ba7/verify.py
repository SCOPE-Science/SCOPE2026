"""Exact-rational finite checks for priced two-community effective-resistance design.
Requires sympy. This supplements, rather than replaces, the general analytical proof.
"""
from fractions import Fraction
from itertools import combinations
import sympy as S

checks=0

def check(condition, label):
    global checks
    assert bool(condition), label
    checks+=1

def data(p,q,t,capacity=1):
    p,q=S.Integer(p),S.Integer(q)
    n=p+q; t=S.Rational(t); capacity=S.Rational(capacity)
    H=(p-1)/q+(q-1)/p+1/n
    Hb=(q-1)/p+1/n
    thi=2*p/(q*H)
    tlo=2*p*n/(2*p*n-2*p-q)
    if t >= thi:
        x=y=S.Integer(0); z=capacity/(p*q)
        regime='cross'
    elif t >= tlo:
        dx=p*q-(p-1)*q*t/2
        r=S.sqrt(2*dx/(t*Hb))
        z=S.simplify(capacity/(dx+(p-1)*t*r/2))
        x=S.simplify((r-q)*z/p); y=S.Integer(0)
        regime='large'
    else:
        d=p*q-t*((p-1)*q+(q-1)*p)/2
        f=S.sqrt(2*n*d/t)
        z=S.simplify(capacity/(d+(n-2)*t*f/2))
        x=S.simplify((f-q)*z/p); y=S.simplify((f-p)*z/q)
        regime='both'
    return x,y,z,regime,S.simplify(thi),S.simplify(tlo)

def setup(p,q,x,y,z):
    n=p+q; L=S.zeros(n)
    edges=[]
    for i,j in combinations(range(n),2):
        if i<p and j<p: w=x; cost=S.Integer(1) # will override
        elif i>=p and j>=p: w=y; cost=S.Integer(1)
        else: w=z; cost=S.Integer(1)
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
        edges.append((i,j,w))
    return L,edges

def resistance_by_matrix(L):
    n=L.rows
    return S.factor(n*(S.trace((L+S.ones(n)/n).inv())-1))

def resistance_by_spectrum(p,q,x,y,z):
    n=p+q
    return S.factor(n*((p-1)/(p*x+q*z)+(q-1)/(q*y+p*z)+1/(n*z)))

def check_point(p,q,t,tag):
    n=p+q
    x,y,z,reg,thi,tlo=data(p,q,t)
    check(S.simplify(p*(p-1)*t*x/2 +q*(q-1)*t*y/2 +p*q*z-1)==0,(p,q,tag,'budget'))
    check(all(S.N(v)>-1e-12 for v in [x,y,z]),(p,q,tag,'nonnegative'))
    check(S.N(z)>0,(p,q,tag,'connected'))
    L,edges=setup(p,q,x,y,z)
    spec=resistance_by_spectrum(p,q,x,y,z)
    calc=resistance_by_matrix(L)
    check(S.simplify(spec-calc)==0,(p,q,tag,'full matrix'))
    hh=S.Rational(p-1,q)+S.Rational(q-1,p)+S.Rational(1,n)
    hb=S.Rational(q-1,p)+S.Rational(1,n)
    dx=S.Rational(p*q)-S.Rational((p-1)*q,2)*t
    dd=S.Rational(p*q)-S.Rational((p-1)*q+(q-1)*p,2)*t
    if reg=='cross': target=S.Rational(n*p*q)*hh
    elif reg=='large': target=((p-1)*S.sqrt(S.Rational(n)*t/2)+S.sqrt(n*hb*dx))**2
    else: target=((n-2)*S.sqrt(S.Rational(n)*t/2)+S.sqrt(dd))**2
    check(S.simplify(spec-target)==0,(p,q,tag,'minimum value formula'))
    check(all(S.simplify(sum(L.row(i)))==0 for i in range(n)),(p,q,tag,'row sum'))
    # Check single-edge marginal first-order KKT conditions from full matrix, independent of quotient calculus.
    A=(L+S.ones(n)/n).inv()
    a2=A*A
    ci,cj,_=next((i,j,w) for i,j,w in edges if i<p and j>=p)
    cross_deriv=S.factor(n*(a2[ci,ci]+a2[cj,cj]-2*a2[ci,cj]))
    for i,j,w in edges:
        price=t if ((i<p)==(j<p)) else S.Integer(1)
        d=S.factor(n*(a2[i,i]+a2[j,j]-2*a2[i,j])/price)
        if i<p and j>=p:
            cross_deriv=d if cross_deriv is None else cross_deriv
            check(S.simplify(d-cross_deriv)==0,(p,q,tag,'cross symmetry'))
        elif w>0:
            check(S.simplify(d-cross_deriv)==0,(p,q,tag,'active KKT'))
        else:
            check(S.N(d-cross_deriv)<1e-12,(p,q,tag,'inactive KKT'))
    check(S.simplify(thi-tlo)>=0,(p,q,tag,'threshold order'))
    return reg, spec

for p,q in [(2,2),(3,2),(4,2),(5,3),(6,5)]:
    x,y,z,_,hi,lo=data(p,q,3)
    tests=[('cross',max(S.Rational(3),hi+1)),('high boundary',hi),('low boundary',lo)]
    if p>q:
        rr=S.Rational(p+q,2)
        hb=S.Rational(q-1,p)+S.Rational(1,p+q)
        # Choose a rational U/z ratio between q and p.
        tmid=S.factor(2*p*q/(q*(p-1)+hb*rr**2))
        tests.append(('large',tmid))
    # Choose a rational U/z ratio strictly above p (full interior).
    ff=S.Rational(p+2)
    tboth=S.factor(2*(p+q)*p*q/(ff**2+(p+q)*((p-1)*q+(q-1)*p)))
    tests.append(('both',tboth))
    for tag,tt in tests:
        regime,value=check_point(p,q,tt,tag)
        if tag=='large': check(regime=='large',(p,q,tag,regime))
        if tag=='both': check(regime=='both',(p,q,tag,regime))
        if tag=='cross': check(regime=='cross',(p,q,tag,regime))
    print('PASS',p,q,'thresholds',hi,lo,'tests',len(tests))

# Equal edge prices make every edge identical, so strict convexity must return uniform conductance.
for p,q in [(2,2),(3,2),(5,4),(10,2)]:
    a,b,c,_,_,_=data(p,q,1)
    expected=S.Rational(2,(p+q)*(p+q-1))
    check(a==expected and b==expected and c==expected,(p,q,'uniform prices'))
# Derive the asymptotic price boundaries exactly with fixed smaller part q.
P,Q=S.symbols('P Q',integer=True,positive=True)
NN=P+Q
HH=(P-1)/Q+(Q-1)/P+1/NN
TMAX=2*P/(Q*HH)
TMIN=2*P*NN/(2*P*NN-2*P-Q)
check(S.limit(TMAX,P,S.oo)==2,'high threshold limit')
check(S.limit(TMIN,P,S.oo)==1,'low threshold limit')
print('Total exact assertions:',checks)
