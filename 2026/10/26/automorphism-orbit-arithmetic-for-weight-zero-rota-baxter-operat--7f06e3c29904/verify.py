#!/usr/bin/env python3
"""Independent finite-field checks for the chain-evolution operator orbit formula."""
from itertools import product
from math import gcd

def rb_family(n,q):
    inv2=pow(2,-1,q)
    for k in range(1,n):
        for dk in range(1,q):
            d=tuple(0 if i<k-1 else dk*pow(inv2,i-(k-1),q)%q for i in range(n))
            for b in product(range(q),repeat=k):
                yield d,tuple(b)+(0,)*(n-1-k)
    for dn in range(q):
        for b in product(range(q),repeat=n-1):
            yield (0,)*(n-1)+(dn,),tuple(b)

def rb_test(n,q,R):
    d,b=R
    def apply(x):
        y=[d[i]*x[i]%q for i in range(n)]
        y[-1]=(y[-1]+sum(b[i]*x[i] for i in range(n-1)))%q
        return tuple(y)
    def prod(x,y):
        return (0,)+tuple((x[i]*y[i])%q for i in range(n-1))
    E=[tuple(int(j==i) for j in range(n)) for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            u,v=E[i],E[j]
            ru,rv=apply(u),apply(v)
            lhs=prod(ru,rv)
            s=tuple((a+b)%q for a,b in zip(prod(ru,v),prod(u,rv)))
            if lhs!=apply(s):return False
    return True

def action(n,q,R,a,m):
    d,b=R
    L=1<<(n-1)
    bs=[0]*(n-1)
    bs[0]=(pow(a,L-1,q)*b[0]+(d[0]-d[-1])*m*pow(a,-1,q))%q
    for i in range(1,n-1):
        bs[i]=pow(a,L-(1<<i),q)*b[i]%q
    return (d,tuple(bs))

def orbit_formula(n,q):
    L=1<<(n-1)
    weights=[L-(1<<i) for i in range(n-1)]
    def scalar_orbits(ws):
        total=0
        for a in range(1,q):
            fixed=sum(pow(a,w,q)==1 for w in ws)
            total+=q**fixed
        assert total%(q-1)==0
        return total//(q-1)
    T=1 if (L-1)%q else 1+gcd(L-1,q-1)
    B=lambda k:scalar_orbits(weights[1:k])
    C=scalar_orbits(weights)
    return (q-1)*(T+sum(B(k) for k in range(2,n))+B(n-1))+C

def verify_conjugation_formula(n,q,R,a,t):
    d,b=R
    A=[pow(a,1<<i,q) for i in range(n)]
    def auto(v):
        w=[v[i]*A[i]%q for i in range(n)]
        w[-1]=(w[-1]+t*v[0])%q
        return tuple(w)
    def inv(v):
        w=[v[i]*pow(A[i],-1,q)%q for i in range(n)]
        w[-1]=((v[-1]-t*w[0])*pow(A[-1],-1,q))%q
        return tuple(w)
    def apply(v):
        w=[d[i]*v[i]%q for i in range(n)]
        w[-1]=(w[-1]+sum(b[i]*v[i] for i in range(n-1)))%q
        return tuple(w)
    result=action(n,q,R,a,t)
    def predicted(v):
        dd,bb=result
        w=[dd[i]*v[i]%q for i in range(n)]
        w[-1]=(w[-1]+sum(bb[i]*v[i] for i in range(n-1)))%q
        return tuple(w)
    for i in range(n):
        e=tuple(int(i==j) for j in range(n))
        assert auto(apply(inv(e)))==predicted(e), (n,q,R,a,t,e)

def check(n,q):
    allR=list(rb_family(n,q))
    assert len(allR)==2*q**n-q
    assert len(set(allR))==len(allR)
    for R in allR:
        assert rb_test(n,q,R),(n,q,R)
    if n<=4 and q<=7:
        for R in allR:
            for a in range(1,q):
                for t in range(q):
                    verify_conjugation_formula(n,q,R,a,t)
    unseen=set(allR); orbits=[]
    while unseen:
        r=next(iter(unseen))
        orb={action(n,q,r,a,m) for a in range(1,q) for m in range(q)}
        assert orb<=unseen
        orbits.append(len(orb));unseen-=orb
    assert len(orbits)==orbit_formula(n,q),(n,q,len(orbits),orbit_formula(n,q))
    print('N',n,'Q',q,'OPERATORS',len(allR),'ORBITS',len(orbits),'ORBIT_SIZES',sorted(set(orbits)),'VERIFY_OK')

def exhaustive_n3_q3():
    n=3;q=3
    family=set(rb_family(n,q))
    for entries in product(range(q),repeat=n*n):
        R=lambda x:tuple(sum(entries[j*n+i]*x[j] for j in range(n))%q for i in range(n))
        E=[tuple(int(i==j) for i in range(n)) for j in range(n)]
        def mul(a,b):return (0,a[0]*b[0]%q,a[1]*b[1]%q)
        good=True
        for i in range(n):
            for j in range(i,n):
                x,y=E[i],E[j];u,v=R(x),R(y)
                if mul(u,v)!=R(tuple((a+b)%q for a,b in zip(mul(u,y),mul(x,v)))):
                    good=False;break
            if not good:break
        if good:
            d=tuple(entries[i*n+i] for i in range(n))
            b=(entries[0*n+2],entries[1*n+2])
            assert all(entries[j*n+i]==0 for j in range(n) for i in range(n) if i!=j and (i!=2 or j==2))
            assert (d,b) in family
    print('EXHAUSTIVE_ALL_LINEAR_MAPS_N3_Q3_VERIFY_OK')
if __name__=='__main__':
    for n,q in [(3,3),(3,5),(4,3),(4,5),(5,3),(5,5),(4,7),(5,7)]:check(n,q)
    exhaustive_n3_q3()
