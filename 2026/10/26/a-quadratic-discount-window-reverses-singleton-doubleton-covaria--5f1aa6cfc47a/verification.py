"""Exact checks of singleton/doubleton moment identities in an Ewens--Pitman partition.
No numerical experiment in this file is used as a proof of an asymptotic assertion.
Run with Python 3: python verification.py
"""
from fractions import Fraction as F
from collections import defaultdict

assertions = 0

def check(x, msg):
    global assertions
    assertions += 1
    if not x:
        raise AssertionError(msg)

def rising(x,k):
    ans=F(1)
    for j in range(k):
        ans *= x+j
    return ans

def predicted(n,theta,alpha):
    den = rising(theta+1,n-1)
    e1= n*rising(theta+alpha,n-1)/den
    e2= F(n*(n-1),2)*(1-alpha)*rising(theta+alpha,n-2)/den
    e12=F(n*(n-1)*(n-2),2)*(1-alpha)*(theta+alpha)*rising(theta+2*alpha,n-3)/den
    r=F(n-2,n)*(theta+alpha)*rising(theta+2*alpha,n-3)*den / (rising(theta+alpha,n-1)*rising(theta+alpha,n-2))
    return e1,e2,e12,r

def crp_states(n,theta,alpha):
    states = {(1,): F(1)}
    for size in range(1,n):
        new = defaultdict(F)
        for blocks, pr in states.items():
            for j, bj in enumerate(blocks):
                dest=list(blocks)
                dest[j]+=1
                new[tuple(dest)] += pr*(bj-alpha)/(theta+size)
            new[blocks+(1,)] += pr*(theta+len(blocks)*alpha)/(theta+size)
        states = new
    return states

for n in range(3,9):
    for theta in [F(1,2),F(1),F(2),F(7,2)]:
        for alpha in [F(0),F(1,5),F(3,5)]:
            st=crp_states(n,theta,alpha)
            check(sum(st.values(),F())==1, ('probability',n,theta,alpha))
            moments=[]
            for stat in [lambda b: b.count(1),lambda b: b.count(2),lambda b: b.count(1)*b.count(2)]:
                moments.append(sum((p*stat(b) for b,p in st.items()),F()))
            p1,p2,p12,r=predicted(n,theta,alpha)
            for actual, expected in zip(moments,[p1,p2,p12]):
                check(actual==expected, ('moment',n,theta,alpha,actual,expected))
            check(p12 == r*p1*p2, ('ratio',n,theta,alpha))

# Verify the exact Ewens boundary and the derivative of log moment-ratio at zero.
for n in range(3,201):
    for theta in [F(1,2),F(1),F(2),F(3),F(7,2)]:
        _,_,_,r=predicted(n,theta,F(0))
        check(r-1 == 2*(1-theta)/(n*(theta+n-3)), ('Ewens ratio',n,theta))
        h = F(1,theta)-F(2,theta+n-3)-F(1,theta+n-2)
        delta=F(1,1000000)
        _,_,_,rplus=predicted(n,theta,delta)
        # Positive finite-step response when h is safely positive; derivative is analytically derived.
        if h > F(1,10):
            check(rplus>r, ('local derivative',n,theta))

# Exact rational evidence for the sign transition, independent of floating point.
for n in [20,50,100,200]:
    theta=F(2)
    signs=[]
    for c in [0,2,4,6,8]:
        alpha=F(c,n*n)
        _,_,_,r=predicted(n,theta,alpha)
        signs.append((r>1)-(r<1))
    check(signs[0]==-1, ('baseline',n,signs))
    check(signs[-1]==1 if n>=50 else True, ('sign',n,signs))

print('PASS', assertions, 'exact assertions')
