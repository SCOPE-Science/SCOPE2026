"""Independent finite checks for the Bernoulli near-maximum stopping certificate.

The analytical theorem is proved in RESULT.md; finite checks do not establish
its infinite range or historical priority.
"""
import math
from fractions import Fraction

CHECKS=0

def test(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def probability_no_two(n,p):
    """Exact first passage distribution for a walk not visiting level 2."""
    q=1-p
    t=p*p
    hit=0.0
    for k in range(1,n//2+1):
        hit+=t
        t*=((2*k+2)*(2*k+1))/((k+1)*(k+2))*p*q
    return 1-hit


def values(n,p):
    """Full Bellman recursion for starting drawdown 1, plus continuation."""
    q=1-p
    prev=[0.]*(n+3)
    prev[0]=prev[1]=1.
    # pi_0,j is indicator that j <= 1.
    continuation=0.
    immediate=0.
    for k in range(1,n+1):
        uk=probability_no_two(k,p)
        curr=[0.]*(n+3)
        curr[0]=max(uk,p*prev[0]+q*prev[1])
        ck=p*prev[0]+q*prev[2]
        curr[1]=max(uk,ck)
        for j in range(2,n+2):
            curr[j]=p*prev[j-1]+q*prev[j+1]
        prev=curr
        if k==n:
            immediate=uk
            continuation=ck
    return immediate,continuation


def bound(n, p):
    d=1-2*p
    q=1-p
    rho=p/q
    L=n//3
    return (d*d/(q*q)
            -math.exp(d)*(2*p*rho*rho*math.exp(-d*d*L/2)
                          +L*math.exp(-d*d*(n-L)/2)))

# Independent dynamic-programming verification for the exact win recursion.
# For early horizons all path probabilities can also be evaluated as rationals.
for n in range(2,10):
    for pn, qn in [(1,2),(2,5),(3,7)]:
        p=Fraction(pn,qn); q=1-p
        old=[Fraction(0)]*(n+3);old[0]=old[1]=1
        # Compute immediate-stop probability by killed walk on {S<=1}.
        killed={0:Fraction(1)}
        for k in range(1,n+1):
            new={}
            for x,w in killed.items():
                new[x-1]=new.get(x-1,0)+q*w
                if x+1<=1:
                    new[x+1]=new.get(x+1,0)+p*w
            killed=new
            u=sum(killed.values())
            cur=[Fraction(0)]*(n+3)
            cur[0]=max(u,p*old[0]+q*old[1])
            c=p*old[0]+q*old[2]
            cur[1]=max(u,c)
            for j in range(2,n+2):
                cur[j]=p*old[j-1]+q*old[j+1]
            old=cur
        U,W=values(n,float(p))
        test(abs(U-float(u))<2e-11, ('exact U',n,p,U,float(u)))
        # Exact independent Bellman recurrence and floating recurrence agree.
        exact_W=float(c)
        test(abs(W-exact_W)<2e-11, ('exact W',n,p,W,exact_W))

# Check the all-n closed-form error majorant, including the floor effects.
for n in range(32,6000):
    d=math.sqrt(6*math.log(n)/n)
    p=(1-d)/2
    L=n//3
    test(0<d<1 and d*L>1, ('conditions',n))
    original_error=math.exp(d)*(math.exp(-d*d*L/2)
                              +L*math.exp(-d*d*(n-L)/2))
    abstract_error=math.exp(1.5)/n+math.e/(3*n)
    test(original_error<=abstract_error*(1+2e-12), ('envelope',n))
    test(abstract_error<6/n < d*d, ('strict',n))
    test(bound(n,p)>0, ('certificate',n))

# Compare genuine optimal continuation and stopping in moderate horizons.
for n in (32,40,50,64,80,100,125,200,300,500,800,1200):
    d=math.sqrt(6*math.log(n)/n)
    p=(1-d)/2
    U,W=values(n,p)
    test(U-W>0, ('dynamic choice',n,U,W))
    test(U-W>=bound(n,p)-2e-9, ('rigorous domination',n,U,W,bound(n,p)))

# Check a continuum of p at each of several sample horizons, wherever the
# sufficient analytic inequality is positive and its prerequisites hold.
for n in (32,64,100,300,700):
    for i in range(1,100):
        p=i/200
        d=1-2*p
        if d*(n//3)>=1 and bound(n,p)>0:
            U,W=values(n,p)
            test(U-W>=bound(n,p)-2e-9, ('arbitrary-p certificate',n,p))

print('PASSED',CHECKS,'finite assertions')
print('Verified: exact rational Bellman recursions, explicit finite-horizon certificate,')
print('closed-form log-horizon envelope, and finite optimal stopping comparisons.')
print('Unproved by computation: the universal n>=32 claim, large-n asymptotics, originality.')
