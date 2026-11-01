"""Exact arithmetic and finite consistency tests for neutral periodic Blaschke schedules.
Run: python3 verify.py (Python standard library only)."""
from fractions import Fraction as F
from itertools import permutations
from math import log, isfinite

def t_of_a(a):
    r = (1 + a) / (2 * (1 - a))
    return r*r

def coefficient_data(word):
    R = F(1)
    B = C = F(0)
    for a in word:
        R *= t_of_a(a)
        B += F(1, 2) / R
        C += F(1, 16) / (R*R)
    if R != 1:
        raise ValueError('word is not neutral')
    return B, C

def formal_composition(word):
    P, A, D = F(1), F(0), F(0)
    for a in word:
        t = t_of_a(a)
        D = t*D + F(1, 16)/(t*P)
        A = t*A + F(1, 2)
        P = t*P
    return P, A, D

def map_x(x, a):
    return ((x+a)/(1+a*x))**2

def map_y(y, a):
    t=t_of_a(a)
    return t*y+F(1,2)+F(1,16)/(t*y)

def y_of_x(x):
    return ((1+x)/(1-x))**2

def iterate_float_y(y, word):
    for a in word:
        t=float(t_of_a(a))
        y=t*y+0.5+1/(16*t*y)
    return y

def main():
    aa,bb=F(1,7),F(1,2)
    words=set(permutations((aa,aa,bb,bb)))
    assert len(words)==6
    count=0
    for word in words:
        B,C=coefficient_data(word)
        P,A,D=formal_composition(word)
        assert P==1 and A==B and D==C
        for x in (F(0),F(1,3),F(2,3),F(9,10)):
            y=y_of_x(x)
            for a in word:
                x=map_x(x,a)
                y=map_y(y,a)
                assert y==y_of_x(x)
                count+=1
    w_group=(aa,aa,bb,bb)
    w_alt=(aa,bb,aa,bb)
    assert coefficient_data(w_group)[0] == F(169,32)
    assert coefficient_data(w_alt)[0] == F(13,4)
    Bs=[coefficient_data(w)[0] for w in words]
    Cs=[coefficient_data(w)[1] for w in words]
    assert max(Bs)==coefficient_data(w_group)[0]
    assert min(Bs)==coefficient_data((bb,bb,aa,aa))[0]
    assert max(Cs)==coefficient_data(w_group)[1]
    assert min(Cs)==coefficient_data((bb,bb,aa,aa))[1]
    assert coefficient_data(w_group)[0]>coefficient_data(w_alt)[0]
    q=F(4,9)
    for k in range(1,10):
        gr=[aa]*k+[bb]*k
        al=[aa,bb]*k
        bg,cg=coefficient_data(gr)
        ba,ca=coefficient_data(al)
        assert bg==F(13,10)*(q**(-k)-1)
        assert ba==F(13,8)*k
        assert bg>=ba
        assert cg>=ca
        count+=8
    for word in (w_group,w_alt):
        B,C=map(float,coefficient_data(word))
        y=1.0
        residuals=[]
        for n in range(1,100001):
            y=iterate_float_y(y,word)
            if n in (25000,50000,100000):
                residuals.append(y-B*n-(C/B)*log(n))
        assert all(isfinite(z) for z in residuals)
        assert abs(residuals[-1]-residuals[-2])<0.002, residuals
        count+=2
    print('PASS:',count,'exact/finite checks; 6 distinct balanced words; 2 logarithmic residual convergence checks.')
    print('grouped: B,C=',coefficient_data(w_group))
    print('alternating: B,C=',coefficient_data(w_alt))

if __name__=='__main__':
    main()
