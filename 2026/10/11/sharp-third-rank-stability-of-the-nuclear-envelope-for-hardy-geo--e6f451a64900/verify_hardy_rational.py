"""Exact rational certificates for elementary exponential inequalities in an analytical matrix-norm result.
This checker does not establish the infinite-dimensional or continuous integral steps.
"""
from fractions import Fraction as Q
from math import factorial

def interval_exp(p, q=1, order=32):
    x=Q(p,q)
    terms=[x**k / factorial(k) for k in range(order+2)]
    lo=sum(terms[:order+1],Q())
    tail=terms[order+1]/(1-x/Q(order+2))
    return lo,lo+tail

b={1:interval_exp(1),2:interval_exp(1,2),3:interval_exp(4,3),4:interval_exp(3,4)}
f1=(Q(1),Q(1))
f2=(Q(2),Q(2))
f3=b[1]
f4=tuple(2*v for v in b[2]);f5=b[3];f6=tuple(2*v for v in b[4])
rs=[f1,f2,f3,f4,f5,f6]
deltas=[(rs[i][0]-rs[i-1][1],rs[i][1]-rs[i-1][0]) for i in range(1,6)]
for i in range(1,len(deltas)):
    assert deltas[i-1][0]>deltas[i][1],(i,float(deltas[i-1][0]),float(deltas[i][1]))
print('EXACT_RATIONAL_CONSECUTIVE_PROJECTION_GAPS_OK')
for i,d in enumerate(deltas,2): print(i, float(d[0]), float(d[1]))
assert (Q(1)+Q(2,5))**2<Q(2) # concavity condition for x>=5/2
print('POLYGAMMA_COMPARISON_BOUND_OK')
