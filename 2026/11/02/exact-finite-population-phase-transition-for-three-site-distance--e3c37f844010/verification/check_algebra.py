#!/usr/bin/env python3
"""Symbolic verification of the slope and branch identities in the theorem."""
import sympy as s
A,B,C,t,d=s.symbols('A B C t d', positive=True)
u=A*(B+C)
v=C*(A+B)
Rleft=A*B*(1+3*t)/(t*(u+v*t))
Rright=A*B*C*(1+3*t)/(d*(u+v*t))
assert s.simplify(s.diff(Rleft,t)+A*B*(u+2*v*t+3*v*t*t)/(t*t*(u+v*t)**2))==0
assert s.simplify(s.diff(Rright,t)-A*B*C*(3*u-v)/(d*(u+v*t)**2))==0
# Equal-gap count expression, with a singleton on one end.
assert s.simplify(4*A*B/(A*B+B+2*A)-4/(1+1/A+2/B))==0
N,a=s.symbols('N a',positive=True)
expr=1/a+2/(N-a)
assert s.simplify(s.diff(expr,a,2)-(2/a**3+4/(N-a)**3))==0
print('PASS symbolic derivative, exact-gap and convexity identities')
