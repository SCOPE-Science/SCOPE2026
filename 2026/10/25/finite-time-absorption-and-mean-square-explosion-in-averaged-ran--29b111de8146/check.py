"""Standalone exact-arithmetic checks for a minibatch randomized Kaczmarz theorem."""
from collections import defaultdict
from fractions import Fraction as F
from math import comb

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

def kernel(q, a):
    assert isinstance(a, F)
    return [(k, F(comb(q,k), 2**q), 1-a*F(k,q), 1-a*F(q-k,q))
            for k in range(q+1)]

def moment_factor(q, a):
    return sum((p*u*u for _,p,u,_ in kernel(q,a)), F(0))

def distribution(q, a, n):
    current = {(F(1), F(1)):F(1)}
    for _ in range(n):
        following = defaultdict(F)
        for (x,y),mass in current.items():
            for _,p,u,v in kernel(q,a):
                following[(x*u,y*v)] += mass*p
        current = dict(following)
    return current

for q in range(2,10):
    for j in range(1,q+1):
        a=F(q,j)
        ker=kernel(q,a)
        z1=sum((p for _,p,u,_ in ker if u==0),F(0))
        z2=sum((p for _,p,_,v in ker if v==0),F(0))
        p=F(comb(q,j),2**q)
        check(z1==p and z2==p)
        both=sum((prob for _,prob,u,v in ker if u==0 and v==0),F(0))
        check(both==(p if 2*j==q else F(0)))
        for n in range(5):
            still1 = (1-p)**n
            neither = (1-(p if 2*j==q else 2*p))**n
            survived = 2*still1-neither
            check(F(0)<=survived<=1)
    a=F(2*q+1,2*q)
    check(all(u and v for _,_,u,v in kernel(q,a)))

for a in [F(4),F(19,5)]:
    q=4
    lam=moment_factor(q,a)
    check(lam==1-a+a*a*F(q+1,4*q))
    for n in range(6):
        d=distribution(q,a,n)
        check(sum(d.values(),F(0))==1)
        risk=sum((prob*(x*x+y*y) for (x,y),prob in d.items()),F(0))
        check(risk==2*lam**n)
        if a==4:
            dead=d.get((F(0),F(0)),F(0))
            check(1-dead == 2*F(3,4)**n - F(1,2)**n)

check(moment_factor(4,F(4))==2)
check(moment_factor(4,F(19,5))==F(137,80))
product=F(1)
for k,p,u,_ in kernel(4,F(19,5)):
    product *= abs(u)**comb(4,k)
check(product==F(6972041972007,64000000000000000))
check(0<product<1)
print('PASS:',checks,'independent exact-rational assertions')
