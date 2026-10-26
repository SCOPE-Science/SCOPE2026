from fractions import Fraction
from math import factorial
from collections import defaultdict

def friedman(N):
    dist={0: Fraction(1)}
    marg={0:dist}
    alive={1:Fraction(1)}
    survival={1:Fraction(1)}
    # initial single white, first draw deterministically white
    dist={1:Fraction(1)};marg[1]=dist
    for t in range(1,N):
        nextd=defaultdict(Fraction)
        nexta=defaultdict(Fraction)
        for x,p in dist.items():
            q=Fraction(t+2-x,2*(t+1))
            nextd[x+1]+=p*q;nextd[x-1]+=p*(1-q)
        for x,p in alive.items():
            q=Fraction(t+2-x,2*(t+1))
            nexta[x+1]+=p*q
            if x>1:nexta[x-1]+=p*(1-q)
        dist=dict(nextd);alive=dict(nexta);marg[t+1]=dist
        survival[t+1]=sum(alive.values())
    return marg,survival

def shifted_elephant(N):
    # time s=2, S_s=0; time-dependent p0 ERW P(+|S_s=y)=(s-y)/(2s)
    alive={0:Fraction(1)}; survival={2:Fraction(1)}
    for s in range(2,N+1):
        ans=defaultdict(Fraction)
        for y,p in alive.items():
            q=Fraction(s-y,2*s)
            ans[y+1]+=p*q
            if y>-0:ans[y-1]+=p*(1-q)
        alive=dict(ans);survival[s+1]=sum(alive.values())
    return survival

def eulerian(n,k):
    a=[[0]*(n+1) for _ in range(n+1)];a[1][0]=1
    for i in range(2,n+1):
        for j in range(i):a[i][j]=(i-j)*a[i-1][j-1]+(j+1)*a[i-1][j] if j>0 else a[i-1][0]
    return a[n][k]

m,fs=friedman(40); es=shifted_elephant(40)
for n in range(1,20):
 assert fs[n]==es[n+1],('shift law mismatch',n)
for n in range(1,10):
 assert m[2*n].get(0,0)==Fraction(eulerian(2*n,n),factorial(2*n))
assert all(fs[n]==fs[n+1] for n in range(2,40,2))
print('PASS: shifted-elephant hitting law exact through time 40; Eulerian marginal formula through 18.')
print('survival at n=20:',fs[20],float(fs[20]));print('survival at n=40:',float(fs[40]))
