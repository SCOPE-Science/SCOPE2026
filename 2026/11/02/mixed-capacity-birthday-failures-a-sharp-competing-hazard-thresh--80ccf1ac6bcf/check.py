"""Exact checks for mixed-capacity first-overflow laws.

Standard-library-only; exact state calculations do not certify the asymptotic
argument, which is provided separately in the mathematical proof.
"""
from collections import defaultdict
from fractions import Fraction
from math import exp, log1p, factorial

CHECKS = 0

def check(condition, reason):
    global CHECKS
    assert condition, reason
    CHECKS += 1

def convolve(x, y):
    out = [Fraction(0)] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i+j] += a*b
    return out

def product_poly(a, b):
    out = [Fraction(1)]
    for _ in range(a):
        out = convolve(out, [Fraction(1), Fraction(1)])
    for _ in range(b):
        out = convolve(out, [Fraction(1), Fraction(1), Fraction(1, 2)])
    return out

def coeff(p, k):
    return p[k] if 0 <= k < len(p) else Fraction(0)

def exact_laws(a, b, max_k):
    n = a + b
    assert n >= 1
    allp = product_poly(a, b)
    p1 = product_poly(a-1,b) if a else []
    p2 = product_poly(a,b-1) if b else []
    survives = []
    mark1 = []
    mark2 = []
    for k in range(max_k + 1):
        survives.append(Fraction(factorial(k),n**k) * coeff(allp,k))
        mark1.append(Fraction(a*factorial(k),n**(k+1)) * coeff(p1,k-1))
        mark2.append(Fraction(b*factorial(k),2*n**(k+1)) * coeff(p2,k-2))
    return survives,mark1,mark2

def chain_laws(a, b, max_k):
    n = a+b
    dist = {(a,0,b,0,0):Fraction(1)}
    survives = [Fraction(1)]
    mark1=[]
    mark2=[]
    for k in range(max_k+1):
        nxt=defaultdict(Fraction)
        f1=f2=Fraction(0)
        for (a0,a1,b0,b1,b2),pr in dist.items():
            if a0: nxt[(a0-1,a1+1,b0,b1,b2)]+=pr*a0/n
            if a1: f1+=pr*a1/n
            if b0: nxt[(a0,a1,b0-1,b1+1,b2)]+=pr*b0/n
            if b1: nxt[(a0,a1,b0,b1-1,b2+1)]+=pr*b1/n
            if b2: f2+=pr*b2/n
        mark1.append(f1); mark2.append(f2)
        dist=dict(nxt)
        survives.append(sum(dist.values(),Fraction(0)))
    return survives,mark1,mark2

def direct_laws(a,b,max_k):
    # Independent ordered-word enumeration.  Check survival after k and first type at k+1.
    n=a+b
    alive={():1}
    sf=[Fraction(1)]
    m1=[];m2=[]
    for k in range(max_k+1):
        nxt={}
        e1=e2=0
        for hist,c in alive.items():
            ct=[0]*n
            for j in hist: ct[j]+=1
            for j in range(n):
                if ct[j] >= (1 if j<a else 2):
                    if j<a: e1+=c
                    else:e2+=c
                else:
                    s=hist+(j,)
                    nxt[s]=nxt.get(s,0)+c
        m1.append(Fraction(e1,n**(k+1)))
        m2.append(Fraction(e2,n**(k+1)))
        alive=nxt
        sf.append(Fraction(sum(alive.values()),n**(k+1)))
    return sf,m1,m2

def poisson_log_survival(n,a,x):
    t=x*n**(2.0/3.0)
    lam=t/n
    b=n-a
    return -t + a*log1p(lam) + b*log1p(lam+lam*lam/2)

def p_low(alpha, step=0.001, bound=16.0):
    m=int(bound/step)
    s=0.0
    for j in range(1,m):
        x=j*step
        s+=alpha*x*exp(-alpha*x*x/2-x*x*x/6)
    return step*s

def main():
    for n in range(1,9):
        for a in range(n+1):
            b=n-a
            r=exact_laws(a,b,9)
            q=chain_laws(a,b,9)
            for k in range(10):
                check(r[0][k]==q[0][k],f'survival n={n},a={a},k={k}')
                check(r[1][k]==q[1][k],f'low mark n={n},a={a},k={k}')
                check(r[2][k]==q[2][k],f'high mark n={n},a={a},k={k}')
                check(r[0][k]-r[0][k+1] == r[1][k]+r[2][k] if k<9 else True,'conservation')
            if n<=4:
                d=direct_laws(a,b,6)
                for k in range(7):
                    check(r[0][k]==d[0][k],f'words survival n={n},a={a},k={k}')
                    check(r[1][k]==d[1][k],f'words first1 n={n},a={a},k={k}')
                    check(r[2][k]==d[2][k],f'words first2 n={n},a={a},k={k}')
    for alpha in [0,0.25,0.5521857197,1.,3.]:
        for x in [0.25,0.75,1.0,2.,3.]:
            errors=[]
            for n in [1000,10000,100000,1000000]:
                a=round(alpha*n**(2/3))
                check(0<=a<=n,'admissible')
                logp=poisson_log_survival(n,a,x)
                target=-alpha*x*x/2-x**3/6
                errors.append(abs(logp-target))
            # Allow small roundoff; convergence check is numerical corroboration only.
            check(errors[-1]<errors[-2],'asymptotic numeric '+str((alpha,x,errors)))
    check(p_low(0)==0,'zero fragile')
    check(0.49<p_low(0.5521857197)<0.51,'equal mark threshold')
    check(p_low(0.1)<0.2,'low alpha')
    check(p_low(10)>0.95,'high alpha')
    print('PASS:',CHECKS,'deterministic assertions; exact rational and independent word checks')

if __name__=='__main__':main()
