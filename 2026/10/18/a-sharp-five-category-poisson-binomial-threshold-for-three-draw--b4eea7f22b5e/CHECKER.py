"""Exact-rational checks accompanying the three-draw occupancy theorem.

Finite grid checks are diagnostics only; the proof in RESULT.md treats every
real probability vector and does not rely on exhaustive testing.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb

def add(a,b):
    return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))))

def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return tuple(z)

def scale(a,s): return tuple(s*x for x in a)

def eq_poly(a,b):
    m=max(len(a),len(b))
    return all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0)
               for i in range(m))

# Coefficients of u and v for the five-category extremal family.
t=(Q(0),Q(1))
one=(Q(1),)
q0=add(one,scale(t,-4))
u=add(mul(q0,q0),scale(mul(t,t),4))
v=add(mul(mul(q0,q0),q0),scale(mul(mul(t,t),t),4))
a=v
b=scale(add(u,scale(v,-1)),3)
c=add(add(one,scale(u,-3)),scale(v,2))
D=add(mul(b,b),scale(mul(a,c),-4))
H=(Q(4),Q(-27),Q(30),Q(75))
expected=(Q(0),Q(0),Q(0))+scale(H,48)
assert eq_poly(D,expected), (D,expected)

# Verify the independent extremal branches in the centered cubic inequality.
# Their positive coefficients are proportional to (5-2k)/sqrt(5k(5-k)).
# Squaring shows k=1 dominates all k with positive third moment.
for k in range(2,5):
    if 5-2*k>0:
        assert Q((5-2*k)**2,5*k*(5-k)) <= Q(9,20)

# Enumerate integer probability numerators summing to a small denominator.
def compositions(total,parts):
    if parts==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first,parts-1):
                yield (first,)+rest

vector_checks=0
triple_checks=0
for m in range(1,6):
    for d in range(1,10):
        for parts in compositions(d,m):
            p=[Q(k,d) for k in parts]
            u=sum(x*x for x in p)
            v=sum(x*x*x for x in p)
            aa=v
            bb=3*(u-v)
            cc=1-3*u+2*v
            assert aa>=0 and bb>=0 and cc>=0
            assert aa+bb+cc==1
            assert bb*bb>=4*aa*cc, (m,d,parts,aa,bb,cc)
            vector_checks+=1
            if vector_checks%13==0:
                probs=[Q(0),Q(0),Q(0)]
                for i,j,k in product(range(m),repeat=3):
                    probs[len({i,j,k})-1]+=p[i]*p[j]*p[k]
                assert probs==[aa,bb,cc]
                triple_checks+=1

p=[Q(5,6)]+[Q(1,30)]*5
u=sum(x*x for x in p)
v=sum(x*x*x for x in p)
(a,b,c)=(v,3*(u-v),1-3*u+2*v)
assert (a,b,c)==(Q(521,900),Q(109,300),Q(13,225))
assert b*b-4*a*c==Q(-1439,810000)

print('PASS polynomial identity: D(t)=48 t^3(75 t^3+30 t^2-27 t+4)')
print('PASS five-coordinate maximal-skewness branch comparison')
print(f'PASS {vector_checks} exact simplex grid vectors')
print(f'PASS {triple_checks} independent triple-enumeration comparisons')
print('PASS six-category strict complex-root counterexample')
print('Scope: finite checks support, but do not replace, the analytical proof.')
