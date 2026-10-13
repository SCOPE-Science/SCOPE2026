"""Independent finite-field checks for subalgebra and idempotent spectra.
Run with: python checker.py
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, p, q):
        self.p, self.q = p, q
        assert (p == q) or (p == 2 and q == 4)
    def add(self, a, b):
        return (a + b) % self.p if self.q == self.p else a ^ b
    def neg(self, a):
        return (-a) % self.p if self.q == self.p else a
    def mul(self, a, b):
        if self.q == self.p:
            return (a*b)%self.p
        v=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):v ^= (1<<(i+j))
        if v&8:v ^= 0b1110
        if v&4:v ^= 0b111
        assert 0 <= v <4
        return v
    def inv(self,a):
        assert a
        for x in range(1,self.q):
            if self.mul(a,x)==1:return x
        raise ValueError(a)

def plus(F, v, w):return tuple(F.add(x,y) for x,y in zip(v,w))
def mul_poly(F,u,v):
    p=F.p; out=[0]*p
    for i,a in enumerate(u):
        for j,b in enumerate(v[:p-i]):
            out[i+j]=F.add(out[i+j],F.mul(a,b))
    return tuple(out)
def derivative(F,u):
    return tuple(F.mul((i+1)%F.p, u[i+1]) if i+1<F.p else 0 for i in range(F.p))
def prod(F,a,f,g):
    return mul_poly(F,f,plus(F,derivative(F,g),mul_poly(F,a,g)))
def rec(F,a):
    p=F.p; h=[0]*p;g=[0]*p;h[0]=1
    for i in range(p-1):
        sh=sg=0
        for j in range(i+1):
            sh=F.add(sh,F.mul(a[j],h[i-j]))
            sg=F.add(sg,F.mul(a[j],g[i-j]))
        h[i+1]=F.mul(F.neg(sh),F.inv((i+1)%p))
        g[i+1]=F.mul(F.add((1 if i==0 else 0),F.neg(sg)),F.inv((i+1)%p))
    Lh=plus(F,derivative(F,h),mul_poly(F,a,h))
    Lg=plus(F,derivative(F,g),mul_poly(F,a,g))
    assert Lh[:-1] == (0,)*(p-1)
    assert Lg[:-1] == (1,)+(0,)*(p-2)
    return Lh[-1],Lg[-1],tuple(h),tuple(g)

def expected(F, a):
    sigma,tau,_,_=rec(F,a)
    d=(F.p-1)//2
    tail=(F.q**d-1)//(F.q-1)
    unit=F.q if sigma==tau==0 else (0 if tau==0 else 1)
    nlines=tail+1+unit
    nidemp=F.q if sigma==tau==0 else (2 if sigma!=0 and tau!=0 else 1)
    return (nlines,nidemp),(sigma,tau)

def direct(F,a):
    p,q=F.p,F.q
    lines=0; idem=0
    for f in product(range(q),repeat=p):
        if not any(f):continue
        y=prod(F,a,f,f)
        if y==f:idem+=1
        r=next(i for i,c in enumerate(f) if c)
        if f[r]!=1:continue
        lam=y[r]
        if all(y[i]==F.mul(lam,f[i]) for i in range(p)):
            lines+=1
    return lines,idem

def main():
    for p,q,full in [(2,2,True),(2,4,True),(3,3,True),(5,5,False)]:
        F=Field(p,q)
        params=list(product(range(q),repeat=p)) if full else None
        if params is None:
            params=[]
            # Four structural patterns and further deterministic test parameters.
            for c0 in range(min(q,3)):
                for c1 in range(min(q,3)):
                    for c2 in range(min(q,3)):
                        a=[0]*p;a[0]=c0;a[1]=c1;a[-1]=c2
                        params.append(tuple(a))
            for j in range(min(q,5)):
                params.append(tuple((j*i+i*i)%q for i in range(p)))
            params=list(dict.fromkeys(params))
        seen={}
        for a in params:
            exp,st=expected(F,a)
            got=direct(F,a)
            assert got==exp,(p,q,a,st,exp,got)
            seen[st]=True
        print('BRUTE_OK',p,q,'parameters',len(params),'pairs',len(seen))
        if q==p or (p==2 and q==4):
            dist=Counter()
            for a in product(range(q),repeat=p):
                exp,st=expected(F,a)
                dist[st]+=1
            assert len(dist)==q*q
            assert all(count==q**(p-2) for count in dist.values())
            print('UNIFORM_OK',p,q,len(dist),'each',q**(p-2))
    print('VERIFY_OK')

if __name__=='__main__':main()
