#!/usr/bin/env python3
"""Standalone finite checks for formulas of weighted slant Toeplitz commutators.
Does not certify the limiting operator theorem.
"""
import math

checks=0

def check(condition, detail=''):
    global checks
    if not condition:
        raise AssertionError(detail)
    checks+=1

def logmoment(j, alpha):
    return math.lgamma(j+1)+math.lgamma(alpha+2)-math.lgamma(j+alpha+2)

def amp(k,l,alpha):
    return math.exp((logmoment(l,alpha)-logmoment(k,alpha))/2)

def step(s,m,t,alpha):
    if (t+m)%s:
        return None
    l=(t+m)//s
    return l,amp(t,l,alpha)

def compose(s,m,n,t,alpha):
    v=step(s,n,t,alpha)
    if v is None:return None
    w=step(s,m,v[0],alpha)
    if w is None:return None
    return w[0],v[1]*w[1]

def explicit(s,m,n,t,alpha):
    residue=(-n-s*m)%(s*s)
    if t%(s*s)!=residue:
        return None
    l=(t+n+s*m)//(s*s)
    return l,amp(t,l,alpha)

for alpha in [-0.75,-0.2,0,0.6,2.5]:
    for s in [2,3,4,5]:
        for m in range(10):
            for n in range(10):
                ra=(-n-s*m)%(s*s)
                rb=(-m-s*n)%(s*s)
                check((ra==rb)==((m-n)%(s*s)==0),(alpha,s,m,n))
                for t in range(70):
                    a=compose(s,m,n,t,alpha)
                    b=explicit(s,m,n,t,alpha)
                    check((a is None)==(b is None),('support',alpha,s,m,n,t,a,b))
                    if a is not None:
                        check(a[0]==b[0] and abs(a[1]-b[1])<1e-11,('coeff',alpha,s,m,n,t,a,b))
                j=120000
                t=s*s*j+ra
                l=j+(ra+n+s*m)//(s*s)
                limit=s**(alpha+1)
                check(abs(amp(t,l,alpha)/limit-1)<0.0002,('asymptotic',alpha,s,m,n))

# Check finite-tail row signatures of C C* in both arithmetic regimes.
def row_terms(s,m,n,alpha,out):
    """Coefficients of commutator output row (indexed by input), directly from products."""
    ans={}
    for first,second,sign in ((m,n,1),(n,m,-1)):
        # Output = (t + second + s*first)/s**2.
        t=s*s*out-second-s*first
        if t<0:continue
        v=compose(s,first,second,t,alpha)
        check(v is not None and v[0]==out,('row formula',s,m,n,out,t,v))
        ans[t]=ans.get(t,0.0)+sign*v[1]
    return {i:v for i,v in ans.items() if abs(v)>1e-14}

for alpha in [-0.5,0,1.25]:
    for s in [2,3,4]:
        c=s**(alpha+1)
        for m,n in ((0,1),(0,s*s),(2,3),(1,1+s*s)):
            equal=(m-n)%(s*s)==0
            for out in (50000,80000):
                row=row_terms(s,m,n,alpha,out)
                diagonal=sum(x*x for x in row.values())
                check(abs(diagonal/(2*c*c)-1)<0.0003,('diagonal',alpha,s,m,n,out,diagonal))
                if equal:
                    delta=abs((s-1)*(m-n)//(s*s))
                    other=row_terms(s,m,n,alpha,out+delta)
                    cross=sum(v*other.get(i,0.) for i,v in row.items())
                    check(abs(cross/(c*c)+1)<0.0003,('offdiag',alpha,s,m,n,out,cross))
                else:
                    other=row_terms(s,m,n,alpha,out+1)
                    cross=sum(v*other.get(i,0.) for i,v in row.items())
                    check(abs(cross)<1e-11,('offdiag-distinct',alpha,s,m,n,out,cross))

print(f'PASS: {checks} finite assertions, including full monomial composition identities and tail signatures.')

# Orthonormal-basis slant normalization from weighted Bergman literature:
# W e_{sj} = e_j, not W z^{sj}=z^j.
def step_on(s,m,t,alpha):
    if (t+m)%s:return None
    j=(t+m)//s
    return j,amp(t,t+m,alpha)

def compose_on(s,m,n,t,alpha):
    a=step_on(s,n,t,alpha)
    if a is None:return None
    b=step_on(s,m,a[0],alpha)
    if b is None:return None
    return b[0],a[1]*b[1]

for alpha in [-0.75,0,1.4,3.0]:
    for s in [2,3,5]:
        for m,n in [(0,1),(2,7),(0,s*s),(3,3+s*s),(7,10)]:
            ra=(-n-s*m)%(s*s)
            rb=(-m-s*n)%(s*s)
            for t in range(200):
                a=compose_on(s,m,n,t,alpha)
                b=compose_on(s,n,m,t,alpha)
                check((a is not None)==(t%(s*s)==ra),('on support A',alpha,s,m,n,t))
                check((b is not None)==(t%(s*s)==rb),('on support B',alpha,s,m,n,t))
            t=100000*s*s+ra
            l=(t+n+s*m)//(s*s)
            a=compose_on(s,m,n,t,alpha)
            check(a is not None and a[0]==l and abs(a[1]-1)<.0003,('on asymptote',alpha,s,m,n,t,a))
print(f'PASS: {checks} total assertions including both slant normalizations.')
