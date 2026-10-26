#!/usr/bin/env python3
"""Exact finite checks for posterior reconstruction of binary additive shifts."""
from fractions import Fraction
from math import comb


def coefficients(poly):
    d=poly.bit_length()-1
    assert d>=1 and (poly&1) and (poly&(1<<d))
    return d,tuple((poly>>j)&1 for j in range(d))


def sequence_kernel(poly,seed):
    d,c=coefficients(poly)
    state=tuple((seed>>j)&1 for j in range(d))
    initial=state
    seq=[]
    for _ in range((1<<d)+1):
        seq.append(state[0])
        new=sum((state[j] if c[j] else 0) for j in range(d))%2
        state=state[1:]+(new,)
        if state==initial:
            return tuple(seq)
    raise AssertionError('nonperiodic kernel state')


def alpha(poly):
    d,_=coefficients(poly)
    vals=[]
    for seed in range(1,1<<d):
        w=sequence_kernel(poly,seed)
        vals.append(Fraction(sum(w),len(w)))
    return min(vals), vals


def outputs(poly,x,L):
    d,_=coefficients(poly)
    n=L-d
    return sum(((sum((x>>(i+j))&1 for j in range(d+1) if (poly>>j)&1)%2)<<i) for i in range(n))


def posterior_error(poly,N,q):
    d,_=coefficients(poly)
    L=N+d
    weights={}
    for x in range(1<<L):
        y=outputs(poly,x,L)
        w=x.bit_count()
        prob=q**w * (1-q)**(L-w)
        if prob>weights.get(y,Fraction(0)):
            weights[y]=prob
    return 1-sum(weights.values(),Fraction(0))


def strict_tail(n,q):
    return sum((Fraction(comb(n,k))*q**k*(1-q)**(n-k) for k in range(n//2+1,n+1)),Fraction(0))


def weak_tail(n,q):
    return sum((Fraction(comb(n,k))*q**k*(1-q)**(n-k) for k in range((n+1)//2,n+1)),Fraction(0))


def half_tie_error(n,q):
    e=strict_tail(n,q)
    if n%2==0:e+=Fraction(1,2)*Fraction(comb(n,n//2))*q**(n//2)*(1-q)**(n//2)
    return e


def run():
    density_checks=0
    for d in range(1,8):
        for interior in range(1<<(d-1)):
            poly=(1<<d)|(interior<<1)|1
            a,vals=alpha(poly)
            assert a>0 and all(v<=1 for v in vals)
            assert Fraction(1,d)<=a<=Fraction(1<<(d-1),(1<<d)-1)
            assert (a==Fraction(1,d))==(poly==((1<<d)|1))
            for seed in range(1<<d):
                v=sequence_kernel(poly,seed)
                assert 1<=len(v)<=((1<<d)-1 if seed else 1)
                assert v.count(1)>0 or seed==0
            density_checks+=1
    assert alpha(0b11)[0]==1
    assert alpha(0b101)[0]==Fraction(1,2)
    assert alpha(0b111)[0]==Fraction(2,3)
    for d in range(1,8):assert alpha((1<<d)|1)[0]==Fraction(1,d)

    binom_checks=0
    bounds_checks=0
    for q in (Fraction(1,4),Fraction(2,5)):
        for N in range(1,13):
            assert posterior_error(0b11,N,q)==half_tie_error(N+1,q)
            binom_checks+=1
        for N in range(1,9):
            e=posterior_error(0b101,N,q)
            N0=(N+1)//2+1
            N1=N//2+1
            expected=1-(1-half_tie_error(N0,q))*(1-half_tie_error(N1,q))
            assert e==expected,(q,N,e,expected)
            binom_checks+=1
    for poly in (0b11,0b101,0b111,0b1011,0b1001,0b1101,0b1111,0b10011):
        d,_=coefficients(poly)
        for N in range(1,9):
            L=N+d
            q=Fraction(1,4)
            e=posterior_error(poly,N,q)
            tails=[]
            for seed in range(1,1<<d):
                cycle=sequence_kernel(poly,seed)
                m=sum(cycle[i%len(cycle)] for i in range(L))
                tails.append((strict_tail(m,q),weak_tail(m,q)))
            lo=max(a for a,b in tails)
            hi=sum((b for a,b in tails),Fraction(0))
            assert lo<=e<=hi,(poly,N,lo,e,hi)
            bounds_checks+=1
    print('VERIFY_OK:',density_checks,'closed recurrence kernels;',binom_checks,
          'exact Bayesian errors;',bounds_checks,'exact error-sandwich checks;'
          ' alpha(1+z)=1, alpha(1+z^2)=1/2, alpha(1+z+z^2)=2/3')

if __name__=='__main__':run()
