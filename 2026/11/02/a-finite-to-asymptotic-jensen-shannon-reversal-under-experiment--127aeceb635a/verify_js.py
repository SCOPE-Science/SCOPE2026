from fractions import Fraction as F
from math import comb
from decimal import Decimal, getcontext

getcontext().prec=36
N=48
assert N>=20

def log_interval(x):
    assert x>0
    r=x;k=0
    while r>=2: r/=2;k+=1
    while r<1: r*=2;k-=1
    def series(v):
        z=(v-1)/(v+1)
        y=z*z
        term=z
        total=F(0)
        for j in range(N):
            total+=2*term/F(2*j+1)
            term*=y
        remainder=2*term/(F(2*N+1)*(1-y))
        return total,total+remainder
    lo,hi=series(r)
    lo2,hi2=series(F(2))
    return (lo+k*(lo2 if k>=0 else hi2),hi+k*(hi2 if k>=0 else lo2))

def scale(v,interval):
    lo,hi=interval
    return (v*lo,v*hi) if v>=0 else (v*hi,v*lo)

def add(*things):
    return (sum(x[0] for x in things),sum(x[1] for x in things))

def neg(x):return (-x[1],-x[0])

def xlogx(x):return scale(x,log_interval(x)) if x else (F(0),F(0))

def h(a,b): return add(xlogx(a+b),neg(xlogx(a)),neg(xlogx(b)))

def delta(t,m):
    n=2*m
    entropy=(F(0),F(0))
    for k in range(n+1):
        a=F(comb(n,k))*F(t,2)**k*(1-F(t,2))**(n-k)
        b=F(comb(n,k))*F(1,2)**k*F(t,2)**(n-k)
        entropy=add(entropy,scale(F(1,2),h(a,b)))
    return add(scale(t**m,log_interval(F(2))),neg(entropy))

def show(label,x):
    lo,hi=x
    dlo=Decimal(lo.numerator)/Decimal(lo.denominator)
    dhi=Decimal(hi.numerator)/Decimal(hi.denominator)
    print(f'{label} in [{dlo}, {dhi}]')
    assert hi>=lo

for m in (1,2,3,4):
    d=delta(F(1,10),m)
    show(f'Delta(m={m}, t=1/10)',d)
    if m<=2:assert d[0]>0
    else:assert d[1]<0
print('PASS: rigorous rational log intervals certify reversal at m=3')
