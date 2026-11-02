"""Exact finite-state and moment checks for the two-colour mixed urn.

Independent transition enumeration is used as a diagnostic; the limiting
law is proved analytically, not by computation.
"""
from fractions import Fraction as Q
from collections import defaultdict
from math import exp,log

checks=0

def check(v):
    global checks
    assert v
    checks+=1

def step_probs(y1,y2,a,b,c,eps):
    tot=y1+y2
    pairs=[(1-eps,c,0),(eps,a,b)]
    out=defaultdict(Q)
    for rp,own,opp in pairs:
        out[(y1+own,y2+opp)]+=rp*Q(y1,tot)
        out[(y1+opp,y2+own)]+=rp*Q(y2,tot)
    return dict(out)

def first_two(probs):
    m1=m2=Q(0)
    for (y,z),q in probs.items():
        v=Q(y-z,2*(y+z))
        m1+=q*v
        m2+=q*v*v
    return m1,m2

def brute(y1,y2,a,b,c,eps,nmax):
    states={(y1,y2):Q(1)}
    for n in range(1,nmax+1):
        out=defaultdict(Q)
        for (i,j),prob in states.items():
            trans=step_probs(i,j,a,b,c,eps)
            check(sum(trans.values())==1)
            tot=i+j
            v=Q(i-j,2*tot)
            # One-step conditional drift is a mixture of Pólya and Friedman.
            E=sum(p*Q(y-z,2*(y+z)) for (y,z),p in trans.items())
            check(E==v*(1-Q(2*b)*eps/Q(tot+a+b)))
            # Mean squared deviation directly agrees with independently computed branch formula.
            E2=sum(p*Q(y-z,2*(y+z))**2 for (y,z),p in trans.items())
            res=Q(0)
            for rp,own,opp in [(1-eps,c,0),(eps,a,b)]:
                denom=tot+own+opp
                am=Q(1)-Q(2*opp,denom)
                h=own-opp
                res+=rp*(am*am*v*v+Q(h*h,denom*denom)*(Q(1,4)-v*v))
            check(E2==res)
            for target,p in trans.items():out[target]+=prob*p
        states=dict(out)
        check(sum(states.values())==1)
    return states

for par in [(1,1,1,1,2,Q(1,3)),(2,1,1,2,3,Q(2,5)),
            (1,2,1,2,1,Q(1,7)),(2,3,0,2,2,Q(1,4))]:
    y1,y2,a,b,c,eps=par
    states=brute(*par,12)
    check(all(p>=0 for p in states.values()))
    print('finite_exact',par, 'terminal_states',len(states),'mean_var',*[str(v) for v in first_two(states)])

# Compare independent exact distribution recursion with closed first- and second-moment
# recursions in the balanced a+b=c family.
for y1,y2,a,b,c,eps in [(1,1,1,1,2,Q(1,3)),(2,1,1,2,3,Q(2,5)),
                          (2,3,0,2,2,Q(1,4)),(1,3,2,1,3,Q(1,8))]:
    states={(y1,y2):Q(1)}
    mean=Q(y1-y2,2*(y1+y2))
    sq=mean*mean
    for k in range(1,12):
        states2=defaultdict(Q)
        for (i,j),prob in states.items():
            for target,p in step_probs(i,j,a,b,c,eps).items():
                states2[target]+=prob*p
        states=dict(states2)
        T=y1+y2+c*k
        shrink=Q(1)-Q(2*b)*eps/T
        mean*=shrink
        acoef=(1-eps)+eps*(Q(1)-Q(2*b,T))**2
        noise=((1-eps)*c*c+eps*(a-b)**2)/T**2
        sq=acoef*sq+noise*(Q(1,4)-sq)
        direct_m,direct_s=first_two(states)
        check(mean==direct_m)
        check(sq==direct_s)
        check(sq>=mean*mean)
    print('balanced_exact',y1,y2,a,b,c,eps,'checks',checks)

# Numeric high-n deterministic moments in the balanced family, diagonal to an
# affine Beta limit with the predicted mean and variance.
def moments(n,lam,y1,y2,a,b,c):
    eps=lam/log(n+1)
    m=(y1-y2)/(2*(y1+y2))
    sq=m*m
    for k in range(1,n+1):
        T=y1+y2+c*k
        acoef=(1-eps)+eps*(1-2*b/T)**2
        noise=((1-eps)*c*c+eps*(a-b)**2)/T**2
        sq=acoef*sq+noise*(.25-sq)
        m*=(1-2*b*eps/T)
    return .5+m,sq-m*m
for par in [(1,1,1,1,2,1.0),(2,1,1,2,3,.5),(2,3,0,2,2,1.2)]:
    y1,y2,a,b,c,lam=par
    n=200000
    observed=moments(n,lam,y1,y2,a,b,c)
    alpha,beta=y1/c,y2/c
    d=exp(-2*b*lam/c)
    target=(.5+d*(alpha/(alpha+beta)-.5),d*d*alpha*beta/((alpha+beta)**2*(alpha+beta+1)))
    check(0<=observed[0]<=1 and 0<=observed[1]<=.25)
    check(abs(observed[0]-target[0])<.025)
    check(abs(observed[1]-target[1])<.025)
    print('triangular_numeric',par,'n',n,'observed_mean_var',observed,'limit_mean_var',target)

print('ALL_ASSERTIONS_PASSED',checks)
