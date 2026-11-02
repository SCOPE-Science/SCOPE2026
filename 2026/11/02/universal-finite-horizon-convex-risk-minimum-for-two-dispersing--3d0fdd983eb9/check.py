"""Exact direct-path verification of the two-habitat convex-risk theorem.

This is finite verification of examples and formulas, not a proof of the
infinite-horizon or all-convex-function assertions.
"""
from fractions import Fraction as F
from itertools import product

CASES = [
    {(F(1),F(1)):F(1,4),(F(1),F(3)):F(1,4),(F(3),F(1)):F(1,4),(F(3),F(3)):F(1,4)},
    {(F(1),F(3)):F(1,2),(F(3),F(1)):F(1,2)},
    {(F(1),F(1)):F(2,5),(F(3),F(3)):F(2,5),(F(1),F(3)):F(1,10),(F(3),F(1)):F(1,10)},
    {(F(1),F(2)):F(1,5),(F(2),F(1)):F(1,5),(F(1),F(4)):F(1,10),(F(4),F(1)):F(1,10),(F(2),F(2)):F(2,5)},
    {(F(1),F(1)):F(1,2),(F(4),F(4)):F(1,2)},
    {(F(1),F(1)):F(1,5),(F(1),F(5)):F(3,10),(F(5),F(1)):F(3,10),(F(5),F(5)):F(1,5)},
]
S_VALS = [F(1),F(1,2),F(3,4)]
Q_VALS = [F(0),F(1,4),F(1,2),F(2,3),F(3,4),F(1)]
STRIKES = [F(0),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2),F(3)]
CHECKS = 0

def check(expr, label):
    global CHECKS
    assert expr, label
    CHECKS += 1

def mean_and_d(law):
    mu = sum(p*(a+b)/2 for (a,b),p in law.items())
    diff2 = sum(p*(a-b)**2 for (a,b),p in law.items())
    av2 = sum(p*((a+b)/2)**2 for (a,b),p in law.items())
    return mu,diff2,av2

def dist(law,s,q,t):
    """Enumerate environmental paths from the original two-patch recurrence."""
    mu,_,_ = mean_and_d(law)
    c = 1-q+s*q
    states = [(F(1),F(1),F(1))]
    for _ in range(t):
        next_states = []
        for x,y,prob in states:
            for (g1,g2),p in law.items():
                nx=(1-q)*g1*x+s*q*g2*y
                ny=s*q*g1*x+(1-q)*g2*y
                next_states.append((nx,ny,prob*p))
        states=next_states
    norm=2*(mu*c)**t
    return [(prob,(x+y)/norm) for x,y,prob in states]

def expectation(D,fun):
    return sum(prob*fun(val) for prob,val in D)

for case_number,law in enumerate(CASES,1):
    check(sum(law.values())==1,('probability',case_number))
    for (a,b),p in law.items():
        check(law.get((b,a),0)==p,('exchangeability',case_number,a,b))
    mu,d,K_num=mean_and_d(law)
    K=K_num/mu**2
    for s in S_VALS:
        q0=1/(1+s)
        for t in [1,2,3]:
            base=dist(law,s,q0,t)
            check(expectation(base,lambda x:x)==1,('mean benchmark',case_number,s,t))
            check(expectation(base,lambda x:x*x)==K**t,('second moment benchmark',case_number,s,t))
            for q in Q_VALS:
                D=dist(law,s,q,t)
                check(expectation(D,lambda x:x)==1,('mean',case_number,s,q,t))
                for k in STRIKES:
                    gap=expectation(D,lambda x:max(x-k,0))-expectation(base,lambda x:max(x-k,0))
                    check(gap>=0,('call convex order',case_number,s,q,t,k,gap))
                    gap2=expectation(D,lambda x:max(k-x,0))-expectation(base,lambda x:max(k-x,0))
                    check(gap2>=0,('put convex order',case_number,s,q,t,k,gap2))
                if t==1:
                    check(expectation(D,lambda x:x*x)==K,('first year q independent',case_number,s,q))
                if t==2:
                    theta=(1-q-s*q)/(1-q+s*q)
                    exact=K*K+theta*theta*d*d/(16*mu**4)
                    check(expectation(D,lambda x:x*x)==exact,('two year exact gap',case_number,s,q))
                    if d and q!=q0:
                        check(exact>K*K,('strict second moment',case_number,s,q))
                if t==3 and d and q!=q0:
                    check(expectation(D,lambda x:x*x)>K**3,('strict third moment',case_number,s,q))

# A separate closed-form finite witness: independent equal-probability (1,3) site growth.
case=CASES[0]
mu,d,K_num=mean_and_d(case)
check(mu==2 and d==2 and K_num/mu**2==F(9,8),'binary parameters')
D1=dist(case,F(1),F(1,2),2)
D2=dist(case,F(1),F(0),2)
check(expectation(D1,lambda x:(x-1)**2)==F(17,64),'wellmixed example variance')
check(expectation(D2,lambda x:(x-1)**2)==F(9,32),'no dispersal example variance')
print('EXACT_CHECKS_PASSED',CHECKS)
