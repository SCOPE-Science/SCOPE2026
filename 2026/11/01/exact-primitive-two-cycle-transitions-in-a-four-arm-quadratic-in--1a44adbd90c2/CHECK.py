"""Exact symbolic and rational Sturm verification of a four-arm quadratic interval map.

Requires Python 3 and SymPy. Every periodic root counted at the rational
sample parameters is isolated over Q; no numerical orbit search is used.
"""
import sympy as S

x, p = S.symbols('x p')
half = S.Rational(1, 2)

def q(z, t):
    return 2*z/t - z*z/(t*t)

def F(z, t):
    return q(z if z <= half else 1-z, t)

def numerator(expr):
    return S.Poly(S.cancel(expr).as_numer_denom()[0], x)

A = 4*p**4 + 8*p**3 - 2*p**2 - 4*p + 1
B = 4*p**4 - 8*p**3 + 6*p**2 - 4*p + 1
J = 27*p**5 + 288*p**3 - 288*p**2 + 512*p - 256
p0 = 1 - S.sqrt(2)/2
h = (4*p-1)/(4*p*p)
assert S.simplify(h.subs(p,p0)-half) == 0
assert S.simplify((q(h,p)-half) + (2*p*p-4*p+1)*A/(16*p**6)) == 0
assert S.simplify((q(1-h,p)-half) + (2*p*p-4*p+1)*B/(16*p**6)) == 0
assert S.expand(S.diff(B,p) - 4*(p-1)*(4*p*p-2*p+1)) == 0
assert S.simplify(S.diff(A,p).subs(p,p0)) == 68-50*S.sqrt(2)
assert S.expand(S.diff(A,p,2) - (48*p*p+48*p-4)) == 0
assert J.subs(p,half) == -S.Rational(1125,32)
assert S.expand(S.diff(J,p) - (135*p**4+864*(p-S.Rational(1,3))**2+416)) == 0

H = {
  'LL': S.cancel(p**6*(q(q(x,p),p)-x)),
  'LR': S.cancel(p**6*(q(1-q(x,p),p)-x)),
  'RL': S.cancel(p**6*(q(q(1-x,p),p)-x)),
  'RR': S.cancel(p**6*(q(1-q(1-x,p),p)-x)),
}
expected_discriminants = {
  'LL': -p**16*(p-2)**2*(p+2)**3*(3*p-2)**3,
  'LR': -p**19*J,
  'RL': -p**19*J,
  'RR': -p**20*(p+4)*(3*p-4)**3,
}
for tag, pol in H.items():
    assert S.simplify(S.discriminant(pol,x)-expected_discriminants[tag]) == 0, tag

# Exact rational isolating intervals and branch-domain verification.
def count(t):
    t = S.Rational(t)
    eps = S.Rational(1, 10**10)
    counts = {}
    for tag in ['LL','LR','RL','RR']:
        P = numerator(H[tag].subs(p,t))
        roots = S.intervals(P,eps=eps) # rational Sturm isolation
        num = 0
        for (a,b), mult in roots:
            assert mult == 1
            v = (a+b)/2
            if v < 0 or v > 1:
                continue
            assert abs(v-half) > (b-a) # root is away from x=1/2
            if (v < half) != (tag[0]=='L'):
                continue
            y = F(v,t)
            # F is globally 8-Lipschitz for 1/4 <= t <= 1/2.
            assert abs(y-half) > 8*(b-a)
            if (y < half) != (tag[1]=='L'):
                continue
            assert a >= 0 and b <= 1
            num += 1
        counts[tag] = num
    fixed = 0
    for tag, expr in [('L',q(x,t)-x),('R',q(1-x,t)-x)]:
        for (a,b), mult in S.intervals(numerator(expr),eps=eps):
            v=(a+b)/2
            if v<0 or v>1: continue
            assert abs(v-half)>b-a
            if (v<half)==(tag=='L'):
                fixed += 1
    total=sum(counts.values())
    assert (total-fixed)%2 == 0
    return tuple(counts[k] for k in ['LL','LR','RL','RR']),fixed,(total-fixed)//2

samples = {
    S.Rational(1,4): ((4,4,4,4),4,6),
    S.Rational(251,1000): ((4,4,4,4),4,6),
    S.Rational(27,100): ((2,3,3,4),4,4),
    S.Rational(1,3): ((1,2,2,3),2,3),
    S.Rational(2,5): ((1,1,1,1),2,1),
    S.Rational(1,2): ((1,1,1,1),2,1),
}
for t, expected in samples.items():
    result=count(t)
    assert result == expected, (t,result,expected)
    print('p=',t, 'branch(F^2)=',result[0],'fixed=',result[1], 'two-cycles=',result[2])

# Exact sign brackets for the only nontrivial boundary parameters.
p1a,p1b = S.Rational(25484,100000),S.Rational(25485,100000)
p2a,p2b = S.Rational(37548,100000),S.Rational(37549,100000)
assert A.subs(p,p1a)>0>A.subs(p,p1b)
assert B.subs(p,p2a)>0>B.subs(p,p2b)
assert p1b<p0<p2a
print('All symbolic identities, discriminants, isolating intervals, and parameter brackets verified.')
