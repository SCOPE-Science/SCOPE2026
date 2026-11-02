"""Exact checks for reciprocal-slope four-branch interval dynamics.

Run with python verify.py. Requires Python 3.9+ and SymPy.
The global theorem is proved in RESULT.md; this program checks its
critical algebra and finitely many independently computed rational cases.
"""
from fractions import Fraction as Q
from sympy import symbols, simplify

k, u = symbols('k u', positive=True, finite=True)
t = 1 - 1 / k
p = k / (k + 1)
outer_minus = (u + 1) / k
inner_minus = k * (u + 1)
inner_plus = k * (u - 1)
outer_plus = (u - 1) / k

def compose(affine, expression):
    return simplify(affine.subs(u, expression))

# The sequence is J0 -> J1 -> J2 -> J3 -> J0.
a = compose(inner_plus, u)
a = compose(outer_minus, a)
a = compose(inner_minus, a)
a = compose(outer_plus, a)
assert simplify(a - u) == 0
assert simplify(inner_plus.subs(u,p) + p) == 0
assert simplify(inner_minus.subs(u,-p) - p) == 0
assert simplify(p-t - 1/(k*(k+1))) == 0
assert simplify(compose(inner_minus, inner_plus) - (k*k*u-k*k+k)) == 0

# Check the exact disjoint interval images using rational parameters.
def G(x, K):
    assert -K <= x <= K
    if x <= -1:
        return (x+1)/K
    if x < 0:
        return K*(x+1)
    if x < 1:
        return K*(x-1)
    return (x-1)/K

N = 0
for K in [Q(6,5), Q(3,2), Q(2), Q(5,2), Q(3), Q(5), Q(11)]:
    T = 1 - 1/K
    P = K/(K+1)
    intervals = [(Q(0), T), (-K,Q(-1)), (-T,Q(0)), (Q(1),K)]
    for idx,(L,R) in enumerate(intervals):
        for j in range(21):
            x = L + (R-L)*Q(j,21)
            y = G(x,K)
            LL,RR = intervals[(idx+1)%4]
            assert LL <= y < RR,(K,idx,x,y)
            z=x
            for _ in range(4): z=G(z,K)
            assert z==x,(K,x,z)
            N += 2
    assert G(P,K)==-P and G(-P,K)==P
    assert -1 < -P < -T < 0 < T < P < 1
    assert G(-1,K)==0 and G(T,K)==-1 and G(K,K)==T
    N+=6
    # Two survivor strips have exact widths K^(-n-1) after n steps.
    Eminus=(-Q(1),-T)
    Eplus=(T,Q(1))
    for n in range(10):
        for side in (-1,+1):
            lo,hi = Eplus if side==1 else Eminus
            target_side = side*(-1 if n%2 else 1)
            for step in range(n):
                # Preimage of alternate strip under affine branch.
                curr_side=side*(-1 if (n-step-1)%2 else 1)
                if curr_side==1:
                    lo,hi = 1+lo/K,1+hi/K
                else:
                    lo,hi = -1+lo/K,-1+hi/K
            assert hi-lo==1/K**(n+1), (K,n,side,lo,hi)
            N+=1
    # Independently simulate a rational mesh, excluding the true repelling pair.
    for i in range(1,80):
        x=-K+2*K*Q(i,80)
        if x in (-P,P): continue
        for j in range(160):
            if any(L<=x<R for L,R in intervals): break
            x=G(x,K)
        else:
            raise AssertionError(('transient did not enter periodic grid',K,i,x))
        N+=1
print('Exact algebra and',N,'finite rational tests passed')
