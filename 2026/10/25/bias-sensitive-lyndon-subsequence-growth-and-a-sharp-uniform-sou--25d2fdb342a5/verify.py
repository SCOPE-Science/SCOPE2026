from fractions import Fraction as Q
from itertools import product
from math import gcd

def lyndon(s):
    return bool(s) and all(s < s[i:]+s[:i] for i in range(1,len(s)))

def subseqs(s):
    r={()}
    for a in s:
        r|={t+(a,) for t in tuple(r)}
    return r

def direct(p,N):
    q=len(p);arr=[]
    for n in range(N+1):
        tot=Q(0)
        for s in product(range(q),repeat=n):
            v=sum(lyndon(x) for x in subseqs(s) if x)
            pr=Q(1)
            for a in s:pr*=p[a]
            tot+=pr*v
        arr.append(tot)
    return arr

def mul(a,b,N):
    return [sum((a[i]*b[k-i] for i in range(k+1)),Q(0)) for k in range(N+1)]
def power(a,d,N):
    x=[Q(1)]+[Q(0)]*N
    for _ in range(d):x=mul(x,a,N)
    return x

def mobius(n):
    x=n;k=0;d=2
    while d*d<=x:
        if x%d==0:
            x//=d;k+=1
            if x%d==0:return 0
            while x%d==0:x//=d
        d+=1
    if x>1:k+=1
    return (-1)**k

def gf(p,N):
    gs=[[Q(0)]+[v*(1-v)**(i-1) for i in range(1,N+1)] for v in p]
    h=[Q(0)]*(N+1)
    for d in range(1,N+1):
        mu=mobius(d)
        if not mu:continue
        s=[sum((power(g,d,N)[i] for g in gs),Q(0)) for i in range(N+1)]
        v=[Q(1)]+[Q(0)]*N
        for k in range(1,N//d+1):
            v=mul(v,s,N)
            for i in range(N+1):h[i]+=Q(mu,d*k)*v[i]
    return [sum(h[:i+1]) for i in range(N+1)]

for p,N in [((Q(1,2),Q(1,2)),11),((Q(1,3),Q(2,3)),10),((Q(1,3),)*3,8),((Q(1,2),Q(1,3),Q(1,6)),8)]:
    a=direct(p,N);b=gf(p,N)
    assert a==b,(p,[(i,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y])
    print('PASS',str(p),N,'coefficients',list(map(str,a[:7])))

# The uniform specialization also admits an independent closed-binomial formula.
from math import comb

def lyndon_length_count(q, m):
    return sum(mobius(d)*q**(m//d) for d in range(1,m+1) if m%d==0)//m

def published_uniform_mean(q,n):
    return sum(lyndon_length_count(q,m)*sum(comb(n,k)*(q-1)**(n-k) for k in range(m,n+1)) for m in range(1,n+1))/q**n

for q in (2,3,4):
    rate=2-Q(1,q)
    prefactor=Q(2*q-1,q-1)
    for n in (20,40,80):
        expected=published_uniform_mean(q,n)
        predicted=float(prefactor)*float(rate)**n/n
        assert 1 < expected/predicted < 1.2
    assert published_uniform_mean(q,2)>0

# Strict majorization for these pairs, checked numerically against the root equation.
def growth(ps):
    def S(z):return sum(float(p)*z/(1-(1-float(p))*z) for p in ps)
    lo,hi=0.0,1.0
    for _ in range(100):
        mid=(lo+hi)*0.5
        if S(mid)<1: lo=mid
        else:hi=mid
    return 2/(lo+hi)

assert growth((Q(1,2),Q(1,2)))>growth((Q(1,3),Q(2,3)))
assert growth((Q(1,3),)*3)>growth((Q(1,2),Q(1,3),Q(1,6)))
assert growth((Q(1,2),Q(1,3),Q(1,6)))>growth((Q(9,10),Q(1,20),Q(1,20)))
print('VERIFY_OK exhaustive_source_words=25824 bias_vectors=4 length_ranges=11,10,8,8 uniform_asymptotic_cases=9 strict_majorization_examples=3')
