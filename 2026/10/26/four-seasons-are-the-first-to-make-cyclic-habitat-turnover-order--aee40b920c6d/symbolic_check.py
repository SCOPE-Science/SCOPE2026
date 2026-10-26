"""Standalone exact symbolic expansion for the two four-block difference formulas.

Requires SymPy (see requirements.txt). Run: python symbolic_check.py
"""
import sympy as s

q = s.symbols('q1:5')
u = s.symbols('u1:5')

def excess(order):
    U = s.prod(u[i] for i in order)
    b = s.Integer(0)
    for i in order:
        b = u[i]*b + (1-u[i])*q[i]
    p = b/(1-U)
    total = s.Integer(0)
    for i in order:
        delta = (1-u[i])*(q[i]-p)
        total += q[i]*delta
        p += delta
    return total

A = excess((0,1,2,3))
B = excess((0,2,1,3))
C = excess((0,1,3,2))
R = s.prod(1-x for x in u)/(1-s.prod(u))
assert s.cancel(A-B+R*(q[0]-q[3])*(q[1]-q[2])) == 0
assert s.cancel(A-C-R*(q[0]-q[1])*(q[2]-q[3])) == 0
print('PASS: both four-block exchange formulas are exact rational-function identities in independent q and u variables')
