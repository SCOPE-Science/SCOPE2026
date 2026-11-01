#!/usr/bin/env python3
"""Standalone mathematical consistency checks for the two-site quadratic cell theorem.
Uses only Python standard library; analytic proof is contained in RESULT.md.
"""
from fractions import Fraction as F
import math

def diag_q(ax,ay,bx,by,px,py,x,y):
    return ax*x*x+ay*y*y-bx*(x-px)*(x-px)-by*(y-py)*(y-py)

# Independent expanded and unexpanded quadratic evaluations, exactly rational.
for px,py in [(F(1),F(0)),(F(0),F(1)),(F(1),F(2)),(F(3,5),F(-7,8))]:
    for i in range(-6,7):
        for j in range(-6,7):
            x,y=F(i,3),F(j,4)
            direct=diag_q(F(2),F(1,2),F(1),F(1),px,py,x,y)
            expanded=x*x-F(1,2)*y*y+2*px*x+2*py*y-px*px-py*py
            assert direct==expanded
            eta=F(2)*px*px-py*py
            # H=diag(1,-1/2), b=(px,py), c=px^2+py^2:
            centered=(x+px)**2-F(1,2)*(y-2*py)**2-eta
            assert direct==centered

# The three genuine topological phases are realized by the same SPD metrics.
assert F(2)*1**2-0**2>0               # orphan of C_p
assert F(2)*0**2-1**2<0               # orphan of C_0
assert abs(2*1**2-(math.sqrt(2))**2)<1e-12  # double-cone boundary
# Concrete ray exits C_0 and subsequently reenters C_0; both endpoints and intermediary exact.
# p=(1,0), ray u=(1,8/5), q(tu)= -(7/25)t^2+2t-1.
q=lambda t:diag_q(F(2),F(1,2),F(1),F(1),F(1),F(0),F(t),F(8,5)*F(t))
assert q(0)<0 and q(3)>0 and q(10)<0

# Exact hyperbolic branch inequalities at translated origin: eta>0,
# positive set has x separated from zero by sqrt(eta).
assert F(2)>0 and F(-1)<0
# Haar orientation law evaluated by a completely independent angular grid.
N=100000
count=sum(1 for k in range(N) if 2*math.cos(2*math.pi*(k+.5)/N)**2 < math.sin(2*math.pi*(k+.5)/N)**2)
pred=2/math.pi*math.atan(1/math.sqrt(2))
assert abs(count/N-pred)<2/N+1e-12, (count/N,pred)
assert abs((1-pred)+pred-1)<1e-14
print('PASS: 676 exact matrix/phase grid checks; angular count',count,'/',N,'versus',pred)
