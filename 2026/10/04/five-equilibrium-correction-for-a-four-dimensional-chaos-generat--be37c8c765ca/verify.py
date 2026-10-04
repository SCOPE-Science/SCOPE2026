from fractions import Fraction as Q
from math import sqrt

# Polynomial coefficients are stored from constant term upward.
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); out=[Q(0)]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(out)

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def scale(a,c): return trim([Q(c)*x for x in a])

def deriv(p): return trim([Q(i)*p[i] for i in range(1,len(p))] or [Q(0)])

def divmod_poly(a,b):
    a=trim([Q(x) for x in a]); b=trim([Q(x) for x in b])
    if b == [0]: raise ZeroDivisionError
    q=[Q(0)]*max(1,len(a)-len(b)+1); r=a[:]
    while r != [0] and len(r) >= len(b):
        k=len(r)-len(b); c=r[-1]/b[-1]; q[k]+=c
        for j in range(len(b)): r[j+k]-=c*b[j]
        r=trim(r)
    return trim(q),trim(r)

def sturm(p):
    seq=[trim([Q(x) for x in p]), deriv(p)]
    while True:
        _,r=divmod_poly(seq[-2],seq[-1])
        if r == [0]: break
        seq.append(scale(r,-1))
    return seq

def evalp(p,x):
    v=Q(0)
    for c in reversed(p): v=v*x+c
    return v

def sgn(v): return (v>0)-(v<0)

def variations(signs):
    ss=[s for s in signs if s]
    return sum(a!=b for a,b in zip(ss,ss[1:]))

def V(seq,x): return variations([sgn(evalp(p,x)) for p in seq])

def inf_sign(p,plus):
    lc=sgn(p[-1]); d=len(p)-1
    return lc if plus or d%2==0 else -lc

def Vinf(seq,plus): return variations([inf_sign(p,plus) for p in seq])

def bisect(p,a,b,steps=100):
    a=float(a); b=float(b)
    fa=float(evalp(p,Q(str(a))))
    for _ in range(steps):
        m=(a+b)/2
        fm=sum(float(c)*(m**i) for i,c in enumerate(p))
        if fa*fm <= 0: b=m
        else: a=m; fa=fm
    return (a+b)/2

# Published parameter vector:
# a1=-12, a2=1/20, a3=-2/5, a4=8, a5=-45, a6=-10.
# Eliminating z=xy/45 and w=2xy/9 and writing s=|y| gives
# s=(x^2-360)/(10x), and the first equilibrium equation becomes P(x)=0.
x2_minus_360=[Q(-360),Q(0),Q(1)]
left=mul(mul(x2_minus_360,x2_minus_360),[Q(9),Q(1)])
# 40500*x*(12*x+2/5)
right=mul([Q(0),Q(40500)],[Q(2,5),Q(12)])
P=add(left,scale(right,-1))
expected=[Q(1166400),Q(113400),Q(-492480),Q(-720),Q(9),Q(1)]
assert P == expected, (P,expected)

S=sturm(P)
assert Vinf(S,False)-Vinf(S,True) == 3
intervals=[(Q(-143,100),Q(-142,100)),(Q(33,20),Q(83,50)),(Q(1973,25),Q(7893,100))]
for a,b in intervals:
    assert V(S,a)-V(S,b) == 1
# No fourth real root, because the three isolating intervals already account for all three real roots.

# Admissibility condition s>0 is equivalent to (x^2-360)/x>0.
# Since 18^2<360<19^2, the negative isolating interval is admissible,
# the small positive interval is inadmissible, and the large positive interval is admissible.
assert 18*18 < 360 < 19*19
assert intervals[0][0] > -Q(18) and intervals[0][1] < 0
assert intervals[1][0] > 0 and intervals[1][1] < Q(18)
assert intervals[2][0] > Q(19)

# The y=0 branch gives the fifth equilibrium exactly.
x0=Q(-1,30)
assert -12*x0 - Q(2,5) == 0

# Correct characteristic polynomial at E0.
# det(J-lambda I)=(-12-lambda)(1-lambda)(lambda^2+37 lambda-323999/900).
# The quadratic has one positive and one negative root because its product is negative.
quad_const=-Q(323999,900)
assert quad_const < 0
# exact discriminant and approximate roots
D=Q(37*37) - 4*quad_const
assert D == Q(2528096,900)
rplus=(-37 + sqrt(float(D)))/2
rminus=(-37 - sqrt(float(D)))/2
assert rplus > 0 and rminus < 0
assert abs(rplus-7.9999790356) < 1e-9
assert abs(rminus+44.9999790356) < 1e-9

# Approximate the two admissible x-roots and reconstruct the four nonzero equilibria.
roots=[]
for idx in (0,2):
    a,b=intervals[idx]
    xr=bisect(P,a,b)
    sr=(xr*xr-360)/(10*xr)
    assert sr>0
    for eps in (1,-1):
        y=eps*sr; z=xr*y/45; w=2*xr*y/9
        # residuals of the printed vector field
        f1=-12*xr+y*z+0.05*w*w-0.4
        f2=8*y-xr*z+w*abs(y)
        f3=xr*y-45*z
        f4=w-10*z
        assert max(abs(f1),abs(f2),abs(f3),abs(f4)) < 2e-8
        roots.append((xr,y,z,w))

print('STURM_TOTAL_REAL_ROOTS=3')
print('ADMISSIBLE_NONZERO_X_ROOTS=2')
print('TOTAL_EQUILIBRIA=5')
print('E0_SPECTRUM_APPROX=-12,1,{:.10f},{:.10f}'.format(rplus,rminus))
for i,e in enumerate(roots,1):
    print('E{}=({:.12f},{:.12f},{:.12f},{:.12f})'.format(i,*e))
print('VERIFY_OK')
