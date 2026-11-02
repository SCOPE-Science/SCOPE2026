#!/usr/bin/env python3
"""Finite checks for the bank-reserve boundary law in uniform debt-constrained exchange."""
import itertools, math
from fractions import Fraction

def exact(N,K,d):
    if d==0:
        return math.comb(K+N-1,N-1)
    return sum(math.comb(N,j)*math.comb(d-1,j-1)*math.comb(K+d+N-j-1,N-j-1)
               for j in range(1,min(d,N-1)+1))

def states(N,K,L):
    for xs in itertools.product(range(-L,K+L+1),repeat=N):
        if sum(xs)==K and sum(max(-x,0) for x in xs)<=L:
            yield xs

def params(k,d):
    D=math.sqrt(1+4*d*(k+d))
    a=(2*(k+d)+D-1)/(2*(k+d)+D+1)
    b=(2*d+D-1)/(2*d+D+1)
    p0=1/(k+2*d+D)
    return a,b,p0

def logcount(N,K,d):
    lg=math.lgamma
    def lc(a,b):return lg(a+1)-lg(b+1)-lg(a-b+1)
    if d==0:return lc(K+N-1,N-1)
    vals=[lc(N,j)+lc(d-1,j-1)+lc(K+d+N-j-1,N-j-1)
          for j in range(1,min(d,N-1)+1)]
    t=max(vals)
    return t+math.log(sum(math.exp(v-t) for v in vals))

def logsumexp(z):
    t=max(z)
    return t+math.log(sum(math.exp(v-t) for v in z))

def test():
    assertions=0
    for N in range(2,5):
        for K in range(0,4):
            for L in range(0,4):
                counts=[0]*(L+1)
                for xs in states(N,K,L):
                    counts[sum(max(-x,0) for x in xs)]+=1
                for d,count in enumerate(counts):
                    assert count==exact(N,K,d),(N,K,d,count,exact(N,K,d));assertions+=1
                assert sum(counts)==sum(exact(N,K,d) for d in range(L+1));assertions+=1
    for N,K,L in [(3,1,2),(4,2,2),(3,0,2)]:
        S=set(states(N,K,L))
        edges=[(i,i+1) for i in range(N-1)]
        for xs in S:
            for i,j in edges:
                for x,y in [(i,j),(j,i)]:
                    ys=list(xs);ys[x]-=1;ys[y]+=1
                    if tuple(ys) in S:
                        assert xs in S and tuple(ys) in S
                        back=list(ys);back[y]-=1;back[x]+=1
                        assert tuple(back)==xs;assertions+=1
    for N,K,L in [(3,1,2),(4,2,2),(3,0,2)]:
        q=Fraction(1,1);p=Fraction(1,2)
        S=set(states(N,K,L)); edges=[(i,i+1) for i in range(N-1)]
        def weight(xs):
            w=Fraction(1,1)
            for v in xs:
                if v>=0:w*=p**(-v)
                else:w*=q**(-v)
            return w
        def rate(v):return p if v>=1 else q
        for xs in S:
            for i,j in edges:
                for x,y in [(i,j),(j,i)]:
                    ys=list(xs);ys[x]-=1;ys[y]+=1;ys=tuple(ys)
                    if ys in S:
                        assert weight(xs)*rate(xs[x])==weight(ys)*rate(ys[y]);assertions+=1
    for k,d in [(1,1),(0.5,2),(2,0.3),(0.1,0.2),(3,5)]:
        a,b,p0=params(k,d)
        Z=1/(1-a)+b/(1-b)
        assert abs(p0*Z-1)<1e-12;assertions+=1
        assert abs(p0*a/(1-a)**2-(k+d))<1e-11;assertions+=1
        assert abs(p0*b/(1-b)**2-d)<1e-11;assertions+=1
        assert 0<a<1 and 0<b<1 and 0<a*b<1;assertions+=1
    for ratio in [1.0,0.5,0.25]:
      for N in [50,100,300]:
        K=L=N
        a,b,_=params(1,1);u=ratio*a*b
        logs=[logcount(N,K,d)+d*math.log(1/ratio) for d in range(L+1)]
        norm=logsumexp(logs)
        for s in range(5):
            p=math.exp(logs[L-s]-norm)
            target=(1-u)*u**s
            assert abs(p-target) < 0.02,(ratio,N,s,p,target)
            assertions+=1
        print('p/q=',ratio,'N=',N,'stationary_empty_bank_prob=',round(math.exp(logs[-1]-norm),12))
    print('CHECKS_OK',assertions)

if __name__=='__main__':test()
