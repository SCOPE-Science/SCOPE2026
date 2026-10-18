"""Exact integer checks for fourth-power Pell reciprocal-tail formula.

The infinite assertion is proved in RESULT.md; finite rational brackets
below are independent spot checks, not a substitute for that proof.
"""
from fractions import Fraction
from math import isqrt

def pell_tables(limit):
    p = [0, 1]
    q = [2, 2]
    while len(p) <= limit:
        p.append(2*p[-1] + p[-2])
        q.append(2*q[-1] + q[-2])
    return p, q

def t_numerator(n, p, q):
    return 5*(3*p[4*n]-q[4*n])+4*(-1)**n*(2*p[2*n]-q[2*n])

def bracket(n, p, cutoff):
    partial = sum((Fraction(1,p[k]**4) for k in range(n, cutoff+1)),Fraction())
    upper = partial + Fraction(16,15*p[cutoff+1]**4)
    return partial,upper

def check():
    N=40
    p,q=pell_tables(max(4*N,3*N+16))
    count=0
    for n in range(1,N+1):
        num=t_numerator(n,p,q)
        assert (num%20)=={0:2,1:18,2:10}[n%3],(n,num%20)
        g=num//20
        lo,hi=bracket(n,p,2*n+12)
        if g==0:
            assert lo>1
        else:
            assert lo > Fraction(1,g+1),(n,'lower')
            assert hi < Fraction(1,g),(n,'upper')
        count+=1
    # The special n=2 rational bounds quoted in the proof.
    assert Fraction(1,16)+Fraction(1,625)+Fraction(1,20736)>Fraction(5,78)
    assert Fraction(1,16)+Fraction(1,625)+Fraction(16,15*20736)<Fraction(2,31)
    # In the recurrence ring Z[sqrt(2)] reduce alpha^6 modulo 5:
    a,b=1,0
    for _ in range(6):
        a,b=a+2*b,a+b
    assert (a,b)==(99,70)
    assert a%5==4 and b%5==0
    # The expansion coefficients can be proved directly over Q(sqrt(2)).
    from fractions import Fraction as F
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def inv(x):
        den=x[0]**2-2*x[1]**2
        return (x[0]/den,-x[1]/den)
    def div(x,y): return mul(x,inv(y))
    def scale(x,s): return (x[0]*s,x[1]*s)
    one=(F(1),F(0));alpha_inv_sq=(F(3),F(-2))
    def power(x,k):
        o=one
        for _ in range(k): o=mul(o,x)
        return o
    a=alpha_inv_sq
    c0=inv(add(one,scale(power(a,2),-1)))
    c1=scale(inv(add(one,power(a,3))),4)
    c2=scale(inv(add(one,scale(power(a,4),-1))),10)
    A=div(one,scale(c0,64))
    B=scale(div(c1,mul(c0,c0)),-F(1,64))
    C=scale(add(div(mul(c1,c1),power(c0,3)),scale(div(c2,mul(c0,c0)),-1)),F(1,64))
    assert A == (F(-1,4),F(3,16)),A
    assert B == (F(-1,5),F(1,10)),B
    assert C == (F(0),F(67,1200)),C
    print('VERIFY_OK: 40 exact rational reciprocal-tail brackets; 40 residue checks; Pell congruence; surd coefficients')

if __name__=='__main__':
    check()
