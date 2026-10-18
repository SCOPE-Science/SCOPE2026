"""Reproducible checks for a two-bin thinning covariance transition."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, pi


def central_ratio(k):
    r = k // 2
    return Fraction(comb(2*r, r), 4**r)


def bernstein_average(L, t):
    return sum(Fraction(comb(L-1, b)) * t**b * (1-t)**(L-1-b)
               * central_ratio(b+1) for b in range(L))


def covariance_formula(L, t):
    # E|D| = L*t*E[g(1+B)/(1+B)], B~Bin(L-1,t).
    return (1-t/2)**L * L*t * (t/(2-t) - bernstein_average(L, t))


def exact_enumeration(L, t):
    e = h = eh = Fraction(0)
    for states in product((0, 1, 2), repeat=L):
        p = Fraction(1)
        for a in states:
            p *= (1-t if a == 0 else t/2)
        x = states.count(1)
        y = states.count(2)
        empty = int(x == 0) + int(y == 0)
        peak = max(x, y)
        e += p*empty
        h += p*peak
        eh += p*empty*peak
    return eh-e*h


def bernstein_average_float(L,t):
    if t == 1: return float(central_ratio(L))
    if t == 0: return 1.
    probs=(1.-t)**(L-1)
    h=1.
    out=0.
    for b in range(L):
        if b and (b+1)%2==0:
            r=(b+1)//2
            h*= (2*r-1)/(2*r)
        out+=probs*h
        if b+1<L:
            probs*= (L-1-b)/(b+1)*t/(1.-t)
    return out

def transition(L):
    low, high = 0., 1.
    for i in range(80):
        t = (low+high)/2
        val = t/(2-t) - bernstein_average_float(L,t)
        if val < 0: low = t
        else: high = t
    return (low+high)/2


def checks():
    count=0
    for L in range(2, 8):
        for t in (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4), Fraction(9, 10), Fraction(1)):
            lhs=exact_enumeration(L,t)
            rhs=covariance_formula(L,t)
            assert lhs==rhs,(L,t,lhs,rhs)
            count+=1
    for L in range(2,70):
        h=[central_ratio(k) for k in range(1,L+1)]
        assert all(h[k+1] <= h[k] for k in range(L-1))
        assert h[0] > h[1]
        t0=Fraction(0);t1=Fraction(1)
        assert t0/(2-t0)-bernstein_average(L,t0) <0
        assert t1/(2-t1)-bernstein_average(L,t1)>0
        count+=3
    for L in (2,3,4,5,10,20,50,100,200,500,1000):
        root=transition(L)
        assert 0<root<1
        assert (root*0.99)/(2-root*0.99)-bernstein_average_float(L,root*0.99)<0
        assert (root+(1-root)*0.01)/(2-root-(1-root)*0.01)-bernstein_average_float(L,root+(1-root)*0.01)>0
        print('L',L,'root',round(root,10),'scaled',round(root*L**(1/3),9))
        count+=3
    print('checks:',count,'limit constant:',(8/pi)**(1/3))

if __name__=='__main__':checks()
