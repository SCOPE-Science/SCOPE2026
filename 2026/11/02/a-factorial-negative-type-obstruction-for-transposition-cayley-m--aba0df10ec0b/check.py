"""Exact rational interval certificate for powered transposition distance on S_6.
Pure Python 3 standard library. All logarithm, exponential bounds are rational.
"""
from fractions import Fraction as Q
from math import factorial

def parts(n,hi=None):
    if hi is None: hi=n
    if n == 0:
        yield ()
    else:
        for k in range(min(n,hi),0,-1):
            for tail in parts(n-k,k):
                yield (k,)+tail

def coeffs(shape):
    out=[1]
    for i,length in enumerate(shape,1):
        for j in range(1,length+1):
            c=j-i
            nex=[0]*(len(out)+1)
            for k,z in enumerate(out):
                nex[k]+=z
                nex[k+1]+=c*z
            out=nex
    return out

def ln_interval(j,nterms=110):
    # log j = 2 atanh((j-1)/(j+1)); geometric tail certificate.
    z=Q(j-1,j+1)
    lo=2*sum((z**(2*k+1))/Q(2*k+1) for k in range(nterms))
    rem=2*z**(2*nterms+1)/Q((2*nterms+1)) / (1-z*z)
    return lo,lo+rem

def exp_interval(x,nterms=24):
    # x in [0, 1/3], Taylor series positive, remainder bounded
    assert 0<=x<=Q(1,3)
    lo=sum(x**k/Q(factorial(k)) for k in range(nterms+1))
    term=x**(nterms+1)/Q(factorial(nterms+1))
    tail=term/(1-x/Q(nterms+2))
    return lo,lo+tail

def pow_interval(j,p):
    l,u=ln_interval(j)
    lower,_=exp_interval(p*l)
    _,upper=exp_interval(p*u)
    return lower,upper

def f_interval(c,p):
    lo=Q(0);hi=Q(0)
    for j,a in enumerate(c):
        if j==0 or a==0:continue
        u,v=pow_interval(j,p)
        if a>0:lo+=a*u;hi+=a*v
        else:lo+=a*v;hi+=a*u
    return lo,hi

def hook_dim(shape):
    n=sum(shape)
    prod=1
    for i,row in enumerate(shape):
        for j in range(row):
            below=sum(1 for r in shape[i+1:] if r>j)
            prod*=row-j+below
    return factorial(n)//prod

L=Q(1541377737,10**10);U=Q(1541377739,10**10)
hook=(4,1,1)
hc=coeffs(hook)
assert hc==[1,3,-5,-15,4,12,0]
fl=f_interval(hc,L);fu=f_interval(hc,U)
assert fl[1]<0<fu[0],(float(fl[1]),float(fu[0]))
print('ROOT_BOUNDS',L,U, 'signed endpoints:',float(fl[1]),float(fu[0]))
print('S6 IRREP UPPER EIGENVALUE BOUNDS')
for lam in parts(6):
    if lam==(6,): continue
    c=coeffs(lam)
    assert sum(c[1:])==-1
    if lam==hook: continue
    # all p in [L,U] bounded by endpoint monotonicity of each j^p
    lo=Q(0);hi=Q(0)
    for j,a in enumerate(c):
        if j==0 or a==0:continue
        vl,_=pow_interval(j,L);_,vu=pow_interval(j,U)
        if a>0:lo+=a*vl;hi+=a*vu
        else:lo+=a*vu;hi+=a*vl
    assert hi < -Q(3,10), (lam,float(hi))
    print(lam, 'upper <',Q(hi.numerator//hi.denominator*0) if False else float(hi), 'dimension',hook_dim(lam))
assert hook_dim(hook)==10
assert sum(hook_dim(lam)**2 for lam in parts(6))==factorial(6)
print('TRANSPOSE_CYCLE_CONTENT_CERTIFICATE_OK; endpoint nullity 100')
# Rational inequalities used for the all-n factorial obstruction:
m=50
Q50=Q(m*(m+1)**2*(m+2),2**(m+1))
assert Q50*Q(9,16) < Q(1,100)
assert Q(3,200)+Q(1,100) < Q(1,12)
# For m>=5 the ratio Q(m+1)/Q(m)=(m+2)(m+3)/(2m(m+1))<1.
assert (m+2)*(m+3) < 2*m*(m+1)
print('FACTORIAL_BOUND_RATIONAL_INEQUALITIES_OK')
