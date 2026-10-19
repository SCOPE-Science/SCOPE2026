#!/usr/bin/env python3
"""Independent exhaustive finite-field check of truncated-substitution commutants."""
from itertools import product
from collections import Counter


def gf_ops(p,k,mod=None):
    q=p**k
    if k==1:
        return q,lambda x,y:(x+y)%p,lambda x,y:(x*y)%p
    if mod is None: raise ValueError('irreducible polynomial coefficients are required')
    def digits(x):
        out=[]
        for _ in range(k):
            out.append(x%p);x//=p
        return out
    def pack(z): return sum((c%p)*p**i for i,c in enumerate(z[:k]))
    def add(x,y):
        a,b=digits(x),digits(y)
        return pack([(u+v)%p for u,v in zip(a,b)])
    def mul(x,y):
        a,b=digits(x),digits(y)
        z=[0]*(2*k-1)
        for i in range(k):
            for j in range(k): z[i+j]=(z[i+j]+a[i]*b[j])%p
        for i in range(2*k-2,k-1,-1):
            c=z[i]
            for j in range(k): z[i-k+j]=(z[i-k+j]-c*mod[j])%p
        return pack(z)
    return q,add,mul

def check(p,k,mod=None):
    q,add,mul=gf_ops(p,k,mod)
    els=list(product(range(q),repeat=3))
    def compose(f,g):
        # f(g(t)) modulo t^4; do not use the derived commutation equations
        result=[0]*4
        gp=[1,0,0,0]
        for a in (0,)+f:
            for j in range(4): result[j]=add(result[j],mul(a,gp[j]))
            nextp=[0]*4
            for i in range(4):
                for j,x in enumerate(g,1):
                    if i+j<4: nextp[i+j]=add(nextp[i+j],mul(gp[i],x))
            gp=nextp
        return tuple(result[1:])
    count=Counter()
    for f in els:
        cen=sum(compose(f,g)==compose(g,f) for g in els)
        count[cen]+=1
    if p==2:
        expected=Counter({q**3:2,2*q*q:2*(q*q-1),q:(q-2)*q*q})
    else:
        expected=Counter({q**3:2,3*q*q:2*(q-1),q*q+q:2*q*(q-1),q*q:q,3*q:q*(q-1),q:(q-3)*q*q})
    expected=Counter({s:n for s,n in expected.items() if n})
    # merge colliding centralizer sizes correctly!
    if p==2:
        exp=Counter()
        exp[q**3]+=2;exp[2*q*q]+=2*(q*q-1);exp[q]+=(q-2)*q*q
    else:
        exp=Counter()
        for s,n in [(q**3,2),(3*q*q,2*(q-1)),(q*q+q,2*q*(q-1)),(q*q,q),(3*q,q*(q-1)),(q,(q-3)*q*q)]: exp[s]+=n
    exp=Counter({s:n for s,n in exp.items() if n})
    assert count==exp, (p,k,count,exp)
    num=sum(c*n for c,n in count.items())
    predicted=5*q**4-4*q*q if p==2 else 3*q**4+9*q**3-11*q*q
    assert num==predicted,(p,k,num,predicted)
    print(f'PASS p={p} k={k} q={q}: centralizers={dict(sorted(count.items()))} commuting_pairs={num}')

if __name__=='__main__':
    check(2,1);check(3,1);check(2,2,[1,1]);check(5,1);check(7,1)
    print('CHECKER_OK')
