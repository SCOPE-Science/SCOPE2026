#!/usr/bin/env python3
"""Independent exact checks of the good-prime spectrum for cobalancing-square windows."""
from math import gcd

def primerange(lo,hi):
    for n in range(max(2,lo),hi):
        if all(n%d for d in range(2,int(n**0.5)+1)):
            yield n

def mul(x,y,p):
    a,b=x;c,d=y
    return ((a*c+2*b*d)%p,(a*d+b*c)%p)

def order_lambda(p):
    z=(1,0); l=(3%p,2%p)
    for d in range(1,2*p*p+1):
        z=mul(z,l,p)
        if z==(1,0): return d
    raise AssertionError(p)

def vp(n,p):
    v=0
    while n and n%p==0:
        n//=p;v+=1
    return v

def run():
    bs=[0,0]
    for _ in range(505): bs.append(6*bs[-1]-bs[-2]+2)
    assert bs[:7]==[0,0,2,14,84,492,2870]
    u=[b//2 for b in bs]
    sq=[x*x for x in u]
    prefix=[0]
    for x in sq: prefix.append(prefix[-1]+x)
    ps=[p for p in primerange(5,103) if p!=7]
    orders={p:order_lambda(p) for p in ps}
    assert orders[5]==6
    tested=0
    for k in range(1,301):
        # GCD of 5 windows is the global GCD because squares obey the order-five recurrence
        gs=[prefix[n+k]-prefix[n] for n in range(5)]
        g=0
        for x in gs: g=gcd(g,x)
        for p in ps:
            actual=vp(g,p)
            expected=(1+vp(k,5) if k%6==0 else 0) if p==5 else (vp(k,p) if k%orders[p]==0 else 0)
            assert actual==expected,(k,p,actual,expected,orders[p])
            tested+=1
    for n in range(0,219):
        assert sq[n+5]-41*sq[n+4]+246*sq[n+3]-246*sq[n+2]+41*sq[n+1]-sq[n]==0
    print('PASS: 300 window lengths, %d prime valuation comparisons, %d distinct primes, 219 recurrence checks'%(tested,len(ps)))
    print('orders mod 5, 11,13,17:',[(p,orders[p]) for p in (5,11,13,17)])

if __name__=='__main__':run()
