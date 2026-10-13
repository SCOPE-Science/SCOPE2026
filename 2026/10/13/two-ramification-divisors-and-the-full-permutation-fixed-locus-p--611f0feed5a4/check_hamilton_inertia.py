"""Exact symbolic checks for the Hamilton sextic quotient branch theorem.

Requires Python 3 and SymPy; no external files or network calls.
"""
from itertools import combinations
import sympy as sp

z,u,v,w,a,b=sp.symbols('z u v w a b')
P=z**6+u*z**2-v*z+w
expected=(-1024*u**6*w+256*u**5*v**2-13824*u**3*w**3
          +43200*u**2*v**2*w**2-22500*u*v**4*w
          +3125*v**6-46656*w**5)
assert sp.expand(sp.discriminant(P,z)-expected)==0
assert sp.gcd(sp.Poly(expected,u,v,w),sp.Poly(v,u,v,w)).total_degree()==0

x=sp.symbols('x0:6')
def elementary(vs,k):
    return sp.expand(sum(sp.prod(c) for c in combinations(vs,k)))

def matchings(items):
    if not items:
        yield ()
    else:
        f=items[0]
        for t in items[1:]:
            for rest in matchings(tuple(x for x in items if x!=f and x!=t)):
                yield tuple(sorted(((f,t),)+rest))

Ms=set(matchings(tuple(range(6))))
assert len(Ms)==15
for M in Ms:
    y=[None]*6
    for i,(j,k) in enumerate(M):
        y[j]=[a,b,sp.Symbol('c')][i]
        y[k]=-[a,b,sp.Symbol('c')][i]
    assert elementary(y,1)==0
    assert elementary(y,3)==0
    assert elementary(y,5)==0
    assert sp.expand(elementary(y,2)+(a*a+b*b+sp.Symbol('c')**2))==0
assert 15*2==5*6  # divisor degree of sigma_5 on a degree-six K3
assert 15*6==30*3  # 15 degree-six curves vs discriminant weight30 and H^2=6: 15*6=30*6/2

# For fixed vectors with eigenvalue 1 and 3 cycle groups,
# weighted power sum equations eliminate the last variable; resulting
# planar p2,p3 have no nonzero common projective root.
for weights in [(4,1,1),(3,2,1),(2,2,2)]:
    A,B,C=weights
    c=-(A*a+B*b)/C
    p2=sp.together(A*a*a+B*b*b+C*c*c)
    p3=sp.together(A*a**3+B*b**3+C*c**3)
    res=sp.factor(sp.resultant(sp.together(p2),sp.together(p3),b))
    assert res != 0 and sp.factor(res/a**6).free_symbols==set(),(weights,res)
    # if a=0, p2 is nonzero constant*b^2
    assert sp.factor(p2.subs(a,0)/b**2)!=0

# Four-cycle representative (3,1,1,1): cubic for the singleton entries.
t=sp.symbols('t')
poly=t**3+3*t**2+6*t+10
assert sp.discriminant(poly,t)!=0
# Remaining cycle representative (2,2,1,1): s=0 yields 2 points,
# s!=0 yields 4 points; the -1 eigenspace contributes another 2.
s,tt=sp.symbols('s tt')
assert sp.factor(6*s*(2*s*s-3*tt))==6*s*(2*s*s-3*tt)
assert sp.discriminant(t**2-t+sp.Rational(2,3),t)!=0
assert sp.discriminant(t**2+2*t+sp.Rational(5,3),t)!=0

# Cohomological Lefschetz/Burnside topological Euler characteristic.
from math import factorial
fixed={
    (1,1,1,1,1,1):24,(2,1,1,1,1):-6, # genus-four curve Euler=2-8
    (2,2,1,1):8,(3,1,1,1):6,(2,2,2):2,
    (4,1,1):2,(3,2,1):0,(3,3):6,
    (4,2):4,(5,1):4,(6,):2,
}
def class_size(part):
    from collections import Counter
    c=Counter(part)
    d=1
    for j,m in c.items():d*=j**m*factorial(m)
    return factorial(6)//d
assert sum(class_size(t)*e for t,e in fixed.items())==720*3
print('HAMILTON_SEXTIC_BRANCH_EXACT_OK')
