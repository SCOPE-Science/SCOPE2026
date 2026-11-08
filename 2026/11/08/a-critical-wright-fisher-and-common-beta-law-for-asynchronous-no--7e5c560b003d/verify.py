#!/usr/bin/env python3
"""Exact finite-state and generator checks for noisy voter dynamics on K_{a,b}."""
from fractions import Fraction as F
from itertools import product

checks = 0

def ck(condition, description=''):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description or f'assertion {checks}')

def chain(a,b,e):
    c=1-e
    states=list(product(range(a+1),range(b+1)))
    idx={s:t for t,s in enumerate(states)}
    q=[[F(0) for _ in states] for _ in states]
    for s,(i,j) in enumerate(states):
        paths=[(i+1,j,F(a-i)*(e/2+c*F(j,b))),
               (i-1,j,F(i)*(e/2+c*F(b-j,b))),
               (i,j+1,F(b-j)*(e/2+c*F(i,a))),
               (i,j-1,F(j)*(e/2+c*F(a-i,a)))]
        for ii,jj,r in paths:
            if r and 0<=ii<=a and 0<=jj<=b:
                q[s][idx[(ii,jj)]]+=r
                q[s][s]-=r
    return states,q

def stationary(q):
    n=len(q)
    a=[[q[j][i] for j in range(n)]+[F(0)] for i in range(n)]
    a[-1]=[F(1)]*n+[F(1)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        z=a[col][col]
        for j in range(col,n+1): a[col][j]/=z
        for i in range(n):
            if i==col: continue
            r=a[i][col]
            if r:
                for j in range(col,n+1): a[i][j]-=r*a[col][j]
    return [a[i][-1] for i in range(n)]

def gen(states,q,f):
    return [sum(row[j]*f(states[j]) for j in range(len(states))) for row in q]

for a,b,e in product(range(1,5),range(1,5),[F(1,2),F(1,3),F(2,3)]):
    states,q=chain(a,b,e)
    n=len(states); c=1-e; S=F(1,a)+F(1,b)
    for row in q: ck(sum(row)==0,'row zero')
    pi=stationary(q)
    ck(sum(pi)==1,'normalization')
    ck(all(p>0 for p in pi),'positivity')
    ck(all(sum(pi[i]*q[i][j] for i in range(n))==0 for j in range(n)),'stationarity')
    w=c*S/(2*(1-c*c)+c*c*S)
    x=lambda z:F(z[0],a)
    y=lambda z:F(z[1],b)
    zfun=lambda st:(x(st)+y(st))/2
    dfun=lambda st:x(st)-y(st)
    A=lambda st:e/2+c*(x(st)+y(st)-2*x(st)*y(st))
    LZ=gen(states,q,zfun)
    LD=gen(states,q,dfun)
    LZ2=gen(states,q,lambda st:zfun(st)**2)
    for t,s in enumerate(states):
        Z=zfun(s);D=dfun(s)
        ck(LZ[t]==e*(F(1,2)-Z),'Z drift')
        ck(LD[t]==-(1+c)*D,'D drift')
        ck(LZ2[t]-2*Z*LZ[t]==S*A(s)/4,'Z qv')
    cs=sum(pi[t]*(2*s[0]-a)*(2*s[1]-b) for t,s in enumerate(states))/F(a*b)
    ck(cs==w,'cross spin')
    if a>=2:
        ca=sum(pi[t]*((2*s[0]-a)**2-a) for t,s in enumerate(states))/F(a*(a-1))
        ck(ca==c*w,'A pair')
    if b>=2:
        cb=sum(pi[t]*((2*s[1]-b)**2-b) for t,s in enumerate(states))/F(b*(b-1))
        ck(cb==c*w,'B pair')
    VarZ=sum(pi[t]*(zfun(s)-F(1,2))**2 for t,s in enumerate(states))
    ck(VarZ==(S+(2+2*c-c*S)*w)/16,'Z variance')
print('VERIFY_OK',checks,'exact assertions')
