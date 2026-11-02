#!/usr/bin/env python3
"""Independent finite checks for three-stage earthquake-triggering mean-rate echoes."""
import math
import sympy as S
import mpmath as M
M.mp.dps = 55
b, q, x = S.symbols('b q x', positive=True)
a = S.symbols('a', positive=True)
t = S.symbols('t', positive=True)
th = S.sqrt(3)*a*t/2
closed = a*S.exp(-t)*(S.exp(a*t)-S.exp(-a*t/2)*(S.cos(th)+S.sqrt(3)*S.sin(th)))/3
F = S.sqrt(3)*S.sin(th)-(1-a)/(1+a)*(S.exp(S.sqrt(3)*th)-S.cos(th))
# Exact derivative identity, no numerical surrogate.
residual = S.simplify(S.expand_trig(S.diff(closed,t) - a*(1+a)*S.exp(-(1+a/S.Integer(2))*t)*F/S.Integer(3)))
assert residual == 0, residual
# Independently sum Erlang convolution generations.
for Q in ['0.1', '0.7', '0.99999']:
 A=M.root(M.mpf(Q), 3)
 for T in ['0.1','1','3','8','14']:
  T=M.mpf(T)
  direct=M.exp(-T)*sum((M.mpf(Q)**n*T**(3*n-1)/M.factorial(3*n-1)) for n in range(1,140))
  predicted=A/3*(M.exp(-(1-A)*T)-M.exp(-(1+A/2)*T)*(M.cos(M.sqrt(3)*A*T/2)+M.sqrt(3)*M.sin(M.sqrt(3)*A*T/2)))
  assert M.fabs(direct-predicted)<M.mpf('1e-42'), (Q,T,direct,predicted)
# Unique-root certified analytically in the accompanying proof; numerical checks below only.
thresholds=[]
for j in [1,2,3]:
 lo=2*M.pi*j
 hi=(2*j+1)*M.pi
 f=lambda z:M.exp(M.sqrt(3)*z)*(M.cos(z)-M.sqrt(3)*M.sin(z))-1
 root=M.findroot(f, (lo+M.pi/6-M.mpf('.08'),lo+M.pi/6+M.mpf('.08')))
 assert lo<root<hi
 d=M.sqrt(3)*M.sin(root)/(M.exp(M.sqrt(3)*root)-M.cos(root))
 thresholds.append(((1-d)/(1+d))**3)
assert thresholds[0]<M.mpf('0.99999')<thresholds[1]<thresholds[2]<1
assert M.fabs(thresholds[0]-M.mpf('0.99996060180549372590647916699'))<M.mpf('1e-28')
assert M.fabs(thresholds[1]-M.mpf('0.99999999926014997572712679173'))<M.mpf('1e-28')
# Sign reversals for the added echo in the interval (2*pi,3*pi).
A=M.root(M.mpf('0.99999'),3)
delta=(1-A)/(1+A)
f=lambda z:M.sqrt(3)*M.sin(z)-delta*(M.exp(M.sqrt(3)*z)-M.cos(z))
assert f(2*M.pi)<0 and f(2*M.pi+M.pi/6)>0 and f(3*M.pi)<0
print('All symbolic, renewal-series, and threshold checks passed.')
print('thresholds:',*(M.nstr(y,25) for y in thresholds))
