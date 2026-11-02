"""Independent finite-field checks for weighted cyclic evolution dynamics.
Run with Python 3.10+: python verify.py
Only standard library required.
"""
from itertools import product
from math import gcd, comb
from collections import Counter

class Field:
    def __init__(self, p, degree=1, modulus=None):
        self.p, self.degree, self.q = p, degree, p**degree
        self.modulus = modulus
        if degree>1:
            assert len(modulus)==degree+1 and modulus[-1]==1
        self.addtab = [[self.add(a,b) for b in range(self.q)] for a in range(self.q)]
        self.multab = [[self.mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.gen = next(g for g in range(1,self.q) if len({self.power(g,k) for k in range(self.q-1)})==self.q-1)
        self.explog = {self.power(self.gen,k):k for k in range(self.q-1)}
    def digits(self,x):
        ans=[]
        for _ in range(self.degree):
            ans.append(x%self.p);x//=self.p
        return ans
    def pack(self,d):
        return sum((v%self.p)*self.p**i for i,v in enumerate(d[:self.degree]))
    def add(self,a,b):
        return self.pack([u+v for u,v in zip(self.digits(a),self.digits(b))])
    def mul(self,a,b):
        p=self.p;n=self.degree
        aa=self.digits(a);bb=self.digits(b)
        out=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):out[i+j]=(out[i+j]+aa[i]*bb[j])%p
        if n>1:
            for j in range(2*n-2,n-1,-1):
                c=out[j]
                for i in range(n):out[j-n+i]=(out[j-n+i]-c*self.modulus[i])%p
        return self.pack(out)
    def power(self,x,e):
        a=1
        while e:
            if e&1:a=self.mul(a,x)
            x=self.mul(x,x);e//=2
        return a

def fixed_pred(m,n,b,t):
    g=gcd(n,t);R=n*t//g
    d=gcd(m,2**R-1)
    H=(2**R-1)//(2**n-1)
    B=(b[0]+sum(2**(n-i)*b[i] for i in range(1,n)))%gcd(m,2**n-1)
    good=(B*H)%d==0
    return (1+d)**g if good else 1

def fixed_support_pred(m,n,b,t):
    g=gcd(n,t);ell=n//g;R=t*ell
    d=gcd(m,2**R-1)
    H=(2**R-1)//(2**n-1)
    B=(b[0]+sum(2**(n-i)*b[i] for i in range(1,n)))%gcd(m,2**n-1)
    if (B*H)%d!=0:return {0:1}
    return {j*ell:comb(g,j)*d**j for j in range(g+1)}

def verify_config(F,n,b,T=30):
    q=F.q; m=q-1
    weights=[F.power(F.gen,x) for x in b]
    states=list(product(range(q),repeat=n))
    def step(x):
        return tuple(F.multab[weights[i]][F.multab[x[(i-1)%n]][x[(i-1)%n]]] for i in range(n))
    nxt={x:step(x) for x in states}
    # Independent state tracing for distance to eventual cycle; unrelated to predicted decomposition.
    memo={}
    for start in states:
        if start in memo:continue
        walk=[];ix={};v=start
        while v not in memo and v not in ix:
            ix[v]=len(walk);walk.append(v);v=nxt[v]
        if v in memo:
            depth,period=memo[v]
            for w in reversed(walk):depth+=1;memo[w]=(depth,period)
        else:
            j=ix[v];per=len(walk)-j
            for w in walk[j:]:memo[w]=(0,per)
            depth=0
            for w in reversed(walk[:j]):depth+=1;memo[w]=(depth,per)
    s=0;h=m
    while h%2==0 and h>0:s+=1;h//=2
    for t in range(s+1):
        actual=sum(depth<=t for depth,per in memo.values())
        predicted=(1+h*2**t)**n
        assert actual==predicted, ('tail',q,n,b,t,actual,predicted)
    assert max(v[0] for v in memo.values())==s,('max-tail',q,n,b)
    fibers=Counter(nxt.values())
    for x in states:
        depth,_=memo[x]
        r=sum(1 for xi in x if xi!=0)
        expected_indegree=1 if s==0 else ((2**r) if depth<s else 0)
        assert fibers[x]==expected_indegree, ('tree_fiber',q,n,b,x,depth,fibers[x],expected_indegree)
    current={x:x for x in states}
    for t in range(1,T+1):
        current={x:nxt[v] for x,v in current.items()}
        actual=sum(x==current[x] for x in states)
        expect=fixed_pred(m,n,b,t)
        assert actual==expect,('fixed',q,n,b,t,actual,expect)
        by_support=Counter(sum(1 for z in x if z) for x in states if x==current[x])
        support_expected=fixed_support_pred(m,n,b,t)
        assert dict(by_support)==support_expected,('support',q,n,b,t,dict(by_support),support_expected)
    return len(states)

if __name__=='__main__':
    fields=[Field(2),Field(3),Field(5),Field(7),Field(11),Field(2,2,[1,1,1]),Field(2,3,[1,1,0,1]),Field(3,2,[1,0,1])]
    cases=0;points=0
    for F in fields:
        for n in [1,2,3,4]:
            if F.q**n>1500:continue
            m=F.q-1
            all_weights=list(product(range(m),repeat=n))
            if len(all_weights)>85:
                all_weights=all_weights[:35]+all_weights[len(all_weights)//2:len(all_weights)//2+25]+all_weights[-25:]
            for b in all_weights:
                points+=verify_config(F,n,b,32)
                cases+=1
    print('WEIGHTED_CYCLIC_EVOLUTION_DYNAMICS_OK',cases,'weighted configurations',points,'states', '32 iterates per configuration')
