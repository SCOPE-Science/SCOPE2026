"""Exact arithmetic verification of local three-by-three Fourier-minor census."""
import itertools, math, random
from collections import Counter
from math import comb

def valuation(d,p,k):
    n=p**k
    d%=n
    if d==0:return k
    t=0
    while d%p==0:
        t+=1;d//=p
    return t

def profile(triple,p,k):
    vv=[valuation(x-y,p,k) for x,y in itertools.combinations(triple,2)]
    return min(vv),max(vv)

def local_counts(p,k,t,s):
    n=p**k
    l=lambda a:p**(k-a)*comb(p**a,3) if p**a>=3 else 0
    q=p**t
    c1=l(t)
    c2=l(s)-l(t)+p**(k-t)*comb(q,2)*(n-p**s)
    return c1,c2,comb(n,3)-c1-c2

def type_counts(p,k):
    n=p**k; out=Counter()
    for t in range(k):
        out[(t,t)]=p**t*comb(p,3)*p**(3*(k-t-1)) if p>=3 else 0
        for s in range(t+1,k):
            out[(t,s)]=n*(p**(k-s)-p**(k-s-1))*(p**(k-t)-p**(k-t-1))//2
    assert sum(out.values())==comb(n,3)
    return out

def global_counts(p,k):
    total=[0,0,0]
    for (t,s),ways in type_counts(p,k).items():
        v=local_counts(p,k,t,s)
        for i in range(3):total[i]+=ways*v[i]
    assert sum(total)==comb(p**k,3)**2
    return tuple(total)

def exact_cyclotomic_zero(p,k,r,c):
    n=p**k; f=n//p
    a=(r[1]-r[0])%n;b=(r[2]-r[0])%n
    u=(c[1]-c[0])%n;v=(c[2]-c[0])%n
    pos=[(a*u+b*v)%n,(a*v)%n,(b*u)%n]
    neg=[(a*v+b*u)%n,(a*u)%n,(b*v)%n]
    coeff=[0]*n
    for x in pos:coeff[x]+=1
    for x in neg:coeff[x]-=1
    return all(coeff[t+j*f]==coeff[t] for t in range(f) for j in range(1,p))

def exact_rank(p,k,R,C):
    if not exact_cyclotomic_zero(p,k,R,C):return 3
    n=p**k
    if all((r-r0)*(c-c0)%n==0 for r in R for c in C for r0 in R for c0 in C): return 1
    return 2

for p,k in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:
    n=p**k
    triples=list(itertools.combinations(range(n),3))
    groups=Counter(profile(r,p,k) for r in triples)
    assert groups==Counter({a:b for a,b in type_counts(p,k).items() if b})
    exp=global_counts(p,k)
    actual=Counter()
    for R in triples:
        t,s=profile(R,p,k)
        local=Counter()
        for C in triples:
            r=exact_rank(p,k,R,C)
            actual[r]+=1
            local[r]+=1
        x=local_counts(p,k,t,s)
        assert tuple(local[j] for j in (1,2,3))==x,(p,k,R,x,local)
    assert tuple(actual[j] for j in (1,2,3))==exp
    print('EXHAUSTIVE_PASS',p,k,'triples',len(triples),'rank_counts',exp,flush=True)
random.seed(1729)
for p,k in [(3,4),(5,3),(7,2),(2,6)]:
    n=p**k
    for trial in range(9000):
        R=sorted(random.sample(range(n),3));C=sorted(random.sample(range(n),3))
        t,s=profile(R,p,k);tc,sc=profile(C,p,k)
        predicted=1 if t+tc>=k else 2 if s+tc>=k or sc+t>=k else 3
        got=exact_rank(p,k,R,C)
        assert predicted==got,(p,k,R,C,predicted,got)
    print('SAMPLE_PASS',p,k,'cases',9000,'global',global_counts(p,k),flush=True)
print('VERIFY_OK')
