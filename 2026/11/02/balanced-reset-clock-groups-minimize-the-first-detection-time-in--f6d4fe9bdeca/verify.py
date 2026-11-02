#!/usr/bin/env python3
"""Reproducible finite numerical checks for grouped Brownian reset search.
These checks do not replace the analytic moment/ordering proof.
"""
from fractions import Fraction
from math import erf, exp, sqrt


def moments(T, h=0.005, r=1.3, x0=1.0, D=1.0, max_n=6):
    steps = round(T/h)
    assert abs(steps*h-T)<1e-12
    s = [1.0] + [erf(x0/sqrt(4*D*h*i)) for i in range(1,steps+1)]
    output = {}
    for n in range(1,max_n+1):
        base = [exp(-r*h*i)*s[i]**n for i in range(steps+1)]
        kernel = [r*v for v in base]
        m = [1.0]
        for i in range(1,steps+1):
            summation = 0.5*kernel[i]
            summation += sum(kernel[j]*m[i-j] for j in range(1,i))
            m.append((base[i]+h*summation)/(1-0.5*h*kernel[0]))
        output[n] = m[-1]
    return output


def checks():
    checks_run = 0
    for p in [Fraction(1,7),Fraction(2,5),Fraction(3,4)]:
        for b in range(1,5):
            for a in range(b+2,8):
                def M(j):
                    return p*Fraction(1,3)**j + (1-p)*Fraction(4,5)**j
                delta = M(a)*M(b)-M(a-1)*M(b+1)
                assert delta>0
                # Direct finite-support expectation of nonnegative swap kernel.
                rhs = sum(w1*w2*(x*y)**b*(x**(a-b-1)-y**(a-b-1))*(x-y)/2
                          for x,w1 in [(Fraction(1,3),p),(Fraction(4,5),1-p)]
                          for y,w2 in [(Fraction(1,3),p),(Fraction(4,5),1-p)])
                assert delta == rhs
                checks_run += 1
    print('Finite-support exact transfer identities checked:',checks_run)
    for T in [0.25,0.5,1.0,2.0]:
        m=moments(T)
        for n in range(2,6):
            assert m[n-1]*m[n+1]-m[n]*m[n]>1e-10
            checks_run += 1
        balanced=m[2]**2
        imbalanced=m[3]*m[1]
        all_shared=m[4]
        all_independent=m[1]**4
        assert all_independent < balanced < imbalanced < all_shared
        checks_run += 3
        print(f'T={T:.2f} independent={all_independent:.9f} balanced_2+2={balanced:.9f} uneven_3+1={imbalanced:.9f} shared={all_shared:.9f} gap={imbalanced-balanced:.9g}')
    print('TOTAL numerical/algebraic assertions:',checks_run)

if __name__=='__main__':
    checks()
