#!/usr/bin/env python3
"""Exact GF(2) checks for sequential neighbor-parity on K_n minus one edge.
Uses independent bit-matrix dynamics and a polynomial invariant-factor census.
"""
from itertools import permutations
from math import gcd, lcm, factorial


def deg(p): return p.bit_length()-1

def pmul(a,b):
    v=0
    while b:
        if b&1:v^=a
        a<<=1;b>>=1
    return v

def pdivmod(a,b):
    if b==0:raise ZeroDivisionError
    q=0
    while deg(a)>=deg(b):
        d=deg(a)-deg(b);a^=b<<d;q^=1<<d
    return q,a

def pgcd(a,b):
    while b:a,b=b,pdivmod(a,b)[1]
    return a

def pexact(a,b):
    q,r=pdivmod(a,b)
    assert r==0,(a,b,r)
    return q

def idmat(n):return [1<<i for i in range(n)]

def mmul(A,B):
    C=[]
    for a in A:
        b=0
        while a:
            lo=a&-a;b^=B[lo.bit_length()-1];a^=lo
        C.append(b)
    return C

def matpow(A,t):
    N=len(A);P=idmat(N)
    while t:
        if t&1:P=mmul(A,P)
        A=mmul(A,A);t>>=1
    return P

def rank(A):
    rows=A.copy();r=0;n=len(rows)
    for c in range(n):
        j=next((j for j in range(r,n) if (rows[j]>>c)&1),None)
        if j is None:continue
        rows[r],rows[j]=rows[j],rows[r]
        for i in range(n):
            if i!=r and ((rows[i]>>c)&1):rows[i]^=rows[r]
        r+=1
    return r

def sweep_matrix(n,order):
    rows=idmat(n)
    for v in order:
        neighbors=(1<<n)-1 - (1<<v)
        if v==0:neighbors^=1<<1
        if v==1:neighbors^=1<<0
        x=neighbors
        while x:
            low=x&-x;rows[v]^=rows[low.bit_length()-1];x^=low
    return rows

def cycle_sweep_matrix(n,order):
    rows=idmat(n)
    for v in order:
        for u in ((v-1)%n,(v+1)%n):
            rows[v]^=rows[u]
    return rows

def fixed_dimension(A,t):
    P=matpow(A,t)
    return len(A)-rank([P[i]^(1<<i) for i in range(len(A))])

def formula_dim(n,k,t):
    m=n-k;g=gcd(k,t);h=gcd(m,t)
    z=n*t
    assert z%(g*h)==0
    return g+h-((z//(g*h))&1)

def invariant_factors(n,k):
    m=n-k;f_k=(1<<k)|1;f_m=(1<<m)|1
    A_n=((1<<n)|1)
    A_n=pexact(A_n,3) # (x^n+1)/(x+1)
    d1=pgcd(f_k,A_n)
    d2=pexact(pmul(f_k,f_m),d1)
    assert pdivmod(d2,d1)[1]==0
    return d1,d2

def polynomial_dim(n,k,t):
    d1,d2=invariant_factors(n,k)
    q=(1<<t)|1
    return deg(pgcd(d1,q))+deg(pgcd(d2,q))

def max_order(n,k):
    a=k;b=n-k
    def v2(x):return (x&-x).bit_length()-1
    L=lcm(a,b)
    return L if v2(a)==v2(b) else 2*L

def brute_period_spectrum(A):
    n=len(A);N=1<<n;visited=set();counts={}
    def step(state):
        out=0
        for i,row in enumerate(A):
            if (state&row).bit_count()&1:out|=1<<i
        return out
    for x in range(N):
        if x in visited:continue
        seen=[];y=x
        while y not in visited:
            visited.add(y);seen.append(y);y=step(y)
        assert y==x,'Map failed to be a permutation'
        counts[len(seen)]=counts.get(len(seen),0)+len(seen)
    return counts

def mobius(d):
    p=2;v=1
    while p*p<=d:
        if d%p==0:
            d//=p;v=-v
            if d%p==0:return 0
            while d%p==0:d//=p
        p+=1
    return -v if d>1 else v

def expected_spectrum(n,k):
    L=max_order(n,k); out={}
    for d in range(1,L+1):
        if L%d:continue
        exact=sum(mobius(d//t)*(1<<formula_dim(n,k,t)) for t in range(1,d+1) if d%t==0)
        assert exact>=0 and exact%d==0
        if exact:out[d]=exact
    return out


def run():
    scanned=0;states=0;mat_tests=0;poly_tests=0;gap_tests=0;cycle_scans=0;cycle_states=0
    for n in range(3,8):
        gaps={k:0 for k in range(1,n)}
        for order in permutations(range(n)):
            k=(order.index(1)-order.index(0))%n
            gaps[k]+=1
            A=sweep_matrix(n,order)
            got=brute_period_spectrum(A)
            want=expected_spectrum(n,k)
            assert got==want,(n,k,order,got,want)
            scanned+=1;states+=1<<n
            positions=[order.index(i) for i in range(n)]
            kc=sum(positions[i]<positions[(i+1)%n] for i in range(n))
            C=cycle_sweep_matrix(n,order)
            cycle_actual=brute_period_spectrum(C)
            cycle_predicted=expected_spectrum(n,kc)
            assert cycle_actual==cycle_predicted,(n,kc,order,cycle_actual,cycle_predicted)
            cycle_scans+=1;cycle_states+=1<<n
        assert all(v==n*factorial(n-2) for v in gaps.values()),(n,gaps)
        gap_tests+=n-1
    for n in range(3,25):
        for k in range(1,n):
            order=[0]+list(range(2,k+1))+[1]+list(range(k+1,n))
            assert len(order)==n and len(set(order))==n
            A=sweep_matrix(n,order)
            L=max_order(n,k)
            assert matpow(A,L)==idmat(n),(n,k,'order upper')
            for p in (2,3,5,7,11,13):
                if L%p==0:
                    assert matpow(A,L//p)!=idmat(n),(n,k,'order sharp')
            for t in range(1,min(2*L,72)+1):
                want=formula_dim(n,k,t)
                got=fixed_dimension(A,t)
                assert want==got,(n,k,t,got,want)
                assert polynomial_dim(n,k,t)==got,(n,k,t,'Smith')
                mat_tests+=1;poly_tests+=1
    print('DENSE_SPARSE_CYCLE_EQUIVALENCE_VERIFIED')
    print('all_order_scans_n3_to7',scanned)
    print('independent_cycle_rule150_scans',cycle_scans)
    print('independent_cycle_rule150_states',cycle_states)
    print('configuration_states_classified',states)
    print('uniform_gap_counts_checked',gap_tests)
    print('exact_fixed_space_and_smith_checks',mat_tests)
    print('polynomial_cross_checks',poly_tests)

if __name__=='__main__':run()
