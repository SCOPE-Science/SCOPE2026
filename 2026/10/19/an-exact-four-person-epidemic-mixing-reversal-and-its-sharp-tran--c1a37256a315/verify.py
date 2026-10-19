"""Exact finite-state verification for a two-community Markovian SIR model.

Run with Python 3 and SymPy (see requirements.txt). All transition recursions
are computed from the stated infection/recovery rates rather than fitted data.
"""
from functools import lru_cache
from fractions import Fraction
from sympy import (Integer, Rational, Poly, S, cancel, diff, expand, factor,
                   simplify, symbols)

b, e, t = symbols('b e t', positive=True)


def expected(beta, leak):
    """Expected total infected from one introduction; exact 30-state recursion."""
    @lru_cache(None)
    def future(s0, i0, s1, i1):
        if i0 + i1 == 0:
            return S.Zero
        events = []
        if s0:
            rate = beta*s0*((1-leak)*i0+leak*i1)/2
            events.append((rate, (s0-1, i0+1, s1, i1), 1))
        if s1:
            rate = beta*s1*(leak*i0+(1-leak)*i1)/2
            events.append((rate, (s0, i0, s1-1, i1+1), 1))
        if i0:
            events.append((Integer(i0), (s0, i0-1, s1, i1), 0))
        if i1:
            events.append((Integer(i1), (s0, i0, s1, i1-1), 0))
        total = sum(rate for rate, state, cost in events)
        return cancel(sum(rate*(cost+future(*state))
                          for rate, state, cost in events)/total)
    ans = cancel(1 + future(1, 1, 2, 0))
    assert future.cache_info().currsize <= 30
    return ans


def endpoint_derivative(endpoint):
    """Differentiate the transition recursion exactly at a fixed endpoint."""
    @lru_cache(None)
    def future_and_derivative(s0, i0, s1, i1):
        if i0+i1 == 0:
            return S.Zero, S.Zero
        events = []
        if s0:
            events.extend([
                (b*s0*i0*(1-endpoint)/2, -b*s0*i0/2,
                 (s0-1,i0+1,s1,i1),1),
                (b*s0*i1*endpoint/2, b*s0*i1/2,
                 (s0-1,i0+1,s1,i1),1)])
        if s1:
            events.extend([
                (b*s1*i0*endpoint/2, b*s1*i0/2,
                 (s0,i0,s1-1,i1+1),1),
                (b*s1*i1*(1-endpoint)/2, -b*s1*i1/2,
                 (s0,i0,s1-1,i1+1),1)])
        if i0:
            events.append((Integer(i0), S.Zero,(s0,i0-1,s1,i1),0))
        if i1:
            events.append((Integer(i1), S.Zero,(s0,i0,s1,i1-1),0))
        total = sum(r for r,dr,st,c in events)
        totalprime = sum(dr for r,dr,st,c in events)
        num = S.Zero
        numprime = S.Zero
        for rate,dr,state,c in events:
            next_f,next_fp = future_and_derivative(*state)
            num += rate*(c+next_f)
            numprime += dr*(c+next_f)+rate*next_fp
        value = cancel(num/total)
        derivative = cancel((numprime-totalprime*value)/total)
        return value,derivative
    val, deriv = future_and_derivative(1,1,2,0)
    return cancel(1+val),factor(deriv)


q = 5*b**4-8*b**3-32*b**2-32*b-16
v0,d0 = endpoint_derivative(0)
v1,d1 = endpoint_derivative(1)
assert simplify(v0 - 2*(b+1)/(b+2)) == 0
assert simplify(d0 - 2*b*(2*b*b+4*b+1)/(b+2)**2) == 0
assert simplify(v1 - (4*b**4+25*b**3+38*b*b+28*b+8)/((b+1)*(b+2)**3)) == 0
assert simplify(d1 + b*q/(2*(b+1)**2*(b+2)**4)) == 0
assert q.subs(b,3) < 0 < q.subs(b,4)
assert [int(bool(x>0)) for x in Poly(q,b).all_coeffs()] == [1,0,0,0,0]

F4 = factor(expected(Integer(4),e))
F4_expected = ((8192*e**6+10880*e**5-11744*e**4-23672*e**3
                -12444*e**2-2502*e-135)/
               (9*(2*e-3)*(2*e+1)**2*(2*e+3)*(4*e+1)**2))
assert simplify(F4-F4_expected)==0
Q = (22528*e**8-17920*e**7-74880*e**6-68960*e**5-11344*e**4
     +57600*e**3+60840*e**2+25542*e+3969)
D = 9*(2*e-3)**2*(2*e+1)**3*(2*e+3)**2*(4*e+1)**3
assert simplify(diff(F4,e)-2*Q/D)==0
T = Poly(expand(sum(coeff*t**mon[0]*(1+t)**(8-mon[0])
                    for mon,coeff in Poly(Q,e).terms())),t)
assert T == Poly(-2625*t**8+443650*t**7+1786290*t**6
                 +2794698*t**5+2361056*t**4+1181286*t**3
                 +350766*t**2+57294*t+3969,t)
assert [int(bool(c>0)) for c in T.all_coeffs()] == [0,1,1,1,1,1,1,1,1]
assert simplify(F4.subs(e,0)-Rational(5,3))==0
assert simplify(F4.subs(e,1)-Rational(419,135))==0
assert simplify(diff(F4,e).subs(e,1)+Rational(14,2025))==0
assert simplify(F4.subs(e,Rational(99,100))-F4.subs(e,1)
                -Rational(295591073,32512225144680))==0


def individual_process(leak):
    """Independent four-labelled-individual exact recursion at beta=4."""
    @lru_cache(None)
    def future(state):
        if 1 not in state:
            return Fraction(0)
        moves=[]
        for a in range(4):
            if state[a] != 1:
                continue
            rec=list(state);rec[a]=2
            moves.append((Fraction(1),tuple(rec),0))
            for j in range(4):
                if state[j] != 0:
                    continue
                mixing=1-leak if a//2==j//2 else leak
                if mixing==0:
                    continue
                inf=list(state);inf[j]=1
                moves.append((2*mixing,tuple(inf),1))
        total=sum(rate for rate,s,c in moves)
        return sum((rate*(c+future(s)) for rate,s,c in moves),Fraction(0))/total
    return 1+future((1,0,0,0))

for leak in (Fraction(0),Fraction(1,2),Fraction(99,100),Fraction(1)):
    exact = individual_process(leak)
    assert exact == F4.subs(e,Rational(leak.numerator,leak.denominator))
print('PASS: exact endpoint identities, quartic sign, unique-optimum Descartes certificate,')
print('      4-person full rational law, positive rational reversal and independent labelled CTMC.')
