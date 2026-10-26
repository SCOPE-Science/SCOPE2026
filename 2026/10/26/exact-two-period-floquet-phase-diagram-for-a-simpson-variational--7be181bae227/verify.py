"""Exact polynomial checks for the alternating-step Simpson harmonic integrator.

Only the Python standard library is required. The analytic stability
classification and boundary asymptotics are proved in RESULT.md.
"""
from fractions import Fraction as Q
from collections import defaultdict

# A two-variable polynomial: dictionary of (degree_s, degree_t) -> rational.
def mon(i=0, j=0, c=1):
    return {(i, j): Q(c)} if c else {}

def plus(*ps):
    out = defaultdict(Q)
    for p in ps:
        for k, v in p.items(): out[k] += v
    return {k: v for k, v in out.items() if v}

def neg(p): return {k: -v for k,v in p.items()}
def sub(p,q): return plus(p,neg(q))
def mul(p,q):
    out = defaultdict(Q)
    for (i,j),a in p.items():
        for (k,l),b in q.items(): out[(i+k,j+l)] += a*b
    return {k:v for k,v in out.items() if v}
def pw(p,n):
    out=mon()
    for _ in range(n): out=mul(out,p)
    return out

def zero(p, msg):
    assert not p, (msg, p)

S,T,ONE=mon(1),mon(0,1),mon()
def k(c): return mon(c=c)
def add(x,y):return plus(x,y)

def A(x):return plus(pw(x,4),neg(mul(k(22),pw(x,2))),k(48))
def B(x):return mul(x,mul(sub(k(12),pw(x,2)),sub(k(24),pw(x,2))))
def C(x):return mul(x,sub(k(8),pw(x,2)))
def D(x):return add(pw(x,2),k(24))
def F(x,y):
    return plus(mul(pw(x,2),pw(y,2)),neg(mul(k(8),pw(x,2))),mul(x,pw(y,3)),neg(mul(k(24),mul(x,y))),neg(mul(k(12),pw(y,2))),k(96))

# det M(s)=1: A^2 + BC = 4 D^2.
zero(sub(add(pw(A(S),2),mul(B(S),C(S))),mul(k(4),pw(D(S),2))), 'determinant')

# The two-step trace is N / (4 D(s) D(t)).
N = sub(mul(k(2),mul(A(S),A(T))),
        add(mul(B(S),C(T)),mul(B(T),C(S))))
DEN = mul(k(4),mul(D(S),D(T)))
Qpoly = plus(mul(pw(S,2),pw(T,2)),neg(mul(k(8),pw(S,2))),
             neg(mul(k(16),mul(S,T))),neg(mul(k(8),pw(T,2))),k(192))
zero(sub(add(N,mul(k(2),DEN)),mul(F(S,T),F(T,S))), 'trace plus two')
zero(sub(sub(N,mul(k(2),DEN)),
         mul(mul(pw(add(S,T),2),sub(mul(S,T),k(12))),Qpoly)), 'trace minus two')
zero(sub(sub(F(S,T),F(T,S)),
         neg(mul(mul(sub(S,T),add(S,T)),sub(mul(S,T),k(4))))), 'F antisymmetry')

# Test a nontrivial rational hyperbolic pair and a reciprocal-product safe pair.
def evalpoly(p,s,t):
    return sum(v*s**i*t**j for (i,j),v in p.items())
def tr(s,t):return evalpoly(N,s,t)/evalpoly(DEN,s,t)
s,t=Q(5,3),Q(22,15)
assert 0<s*s<8 and 0<t*t<8 and tr(s,t)<-2
s,t=Q(3,2),Q(8,3)
assert s*t==4 and -2<tr(s,t)<2
print('VERIFY_OK: four exact polynomial identities and two rational witnesses')
