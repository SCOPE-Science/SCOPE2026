"""Standalone exact checks and asymptotic sanity checks for growing-color urn trees."""
from fractions import Fraction
from collections import defaultdict
from math import log

ASSERTIONS=0

def check(x, description=''):
    global ASSERTIONS
    assert x, description
    ASSERTIONS += 1

def exact_activation_chain(steps, c, a):
    probs={0: Fraction(1)}
    expected=[]; vars_=[]; star=[]
    S=Fraction(1)
    product=Fraction(1)
    for t in range(1,steps+1):
        nxt=defaultdict(Fraction)
        for k,mass in probs.items():
            p=Fraction(t-k,1)/S
            check(0<=p<=1)
            nxt[k+1]+=mass*p
            nxt[k]+=mass*(1-p)
        probs={k:v for k,v in nxt.items() if v}
        if t>=2:
            product*=1-Fraction(t-1,1)/S
        check(sum(probs.values())==1)
        check(probs.get(1,0)==product)
        m=sum(k*x for k,x in probs.items())
        v=sum((k-m)**2*x for k,x in probs.items())
        expected.append(m); vars_.append(v); star.append(product)
        S+=1+Fraction(c)*(t**a)
    return probs,expected,vars_,star

def exact_full_history(steps, c, a):
    # weights and ever-selected indicators of each living vertex, independently
    # reconstructed without using the activation-count recurrence.
    states={((Fraction(1),False),):Fraction(1)}
    out=[]
    for t in range(1,steps+1):
        nxt=defaultdict(Fraction)
        for state, mass in states.items():
            total=sum(w for w,_ in state)
            for i,(w,flag) in enumerate(state):
                ss=list(state)
                ss[i]=(w+Fraction(c)*(t**a), True)
                ss.append((Fraction(1),False))
                nxt[tuple(ss)]+=mass*w/total
        states=dict(nxt)
        dist=defaultdict(Fraction)
        for state,mass in states.items():
            dist[sum(flag for _,flag in state)]+=mass
        out.append(dict(dist))
        check(sum(states.values())==1)
    return out

def moments_recurrence(steps,c,a):
    S=1.0; m=v=0.0; output=[]
    for t in range(1,steps+1):
        p=(t-m)/S
        v=(1-2/S)*v+p*(1-p)
        m+=p
        S+=1+c*t**a
        output.append((m,v))
    return output

def run():
    for c,a in [(1,1),(2,1),(1,2),(2,2),(1,3)]:
        probs, means,vars_,star=exact_activation_chain(9,c,a)
        histories=exact_full_history(6,c,a)
        for i,dist in enumerate(histories):
            chain,_,_,_=exact_activation_chain(i+1,c,a)
            check({k:v for k,v in dist.items() if v}==chain, ('full_history_mismatch',c,a,i))
        moments=moments_recurrence(9,c,a)
        for i,(m,v) in enumerate(moments):
            check(abs(float(means[i])-m)<1e-11)
            check(abs(float(vars_[i])-v)<1e-10)
    for a in [0.25,0.5,0.75,1.0]:
        n=200000; c=2.0
        m,v=moments_recurrence(n,c,a)[-1]
        target=((a+1)/(c*(1-a))*n**(1-a) if a<1 else 2/c*log(n))
        check(0.75<m/target<1.05, ('mean_asymptotic',a,m/target))
        check(0.70<v/m<1.01, ('variance_asymptotic',a,v/m))
    for a in [1.25,1.5,2.0,3.0]:
        n=200000; c=2.0
        m,v=moments_recurrence(n,c,a)[-1]
        check(1<=m<100, ('finite_mean',a,m))
        check(0<=v<m*m+5)
    print('VERIFIED',ASSERTIONS,'independent exact/numeric assertions')

if __name__=='__main__':run()
