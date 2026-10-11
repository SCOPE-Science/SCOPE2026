import sympy as sp

q = sp.sqrt(2)
r = q - 1
t = sp.symbols('t', real=True)
a = sp.symbols('a', real=True)

V = [(1,r),(r,1),(-r,1),(-1,r),(-1,-r),(-r,-1),(r,-1),(1,-r)]

def supports(z):
    x,y=z
    return [x,-x,y,-y,(x+y)/q,(x-y)/q,(-x+y)/q,(-x-y)/q]

def nonneg(expr):
    expr=sp.simplify(expr)
    ans=sp.ask(sp.Q.nonnegative(expr))
    if ans is None:
        ans = bool(expr.is_nonnegative)
    assert ans is True, f'nonnegativity not certified: {expr}'

def dominates_affine(z, expected, lo, hi):
    for s in supports(z):
        d=sp.expand(expected-s)
        # d is affine in t, so endpoint nonnegativity is sufficient.
        assert sp.Poly(d,t).degree() <= 1
        nonneg(d.subs(t,lo))
        nonneg(d.subs(t,hi))

# Every listed octagon vertex is on the unit sphere.
for x,y in V:
    vals=[sp.simplify(s) for s in supports((x,y))]
    assert any(sp.simplify(v-1)==0 for v in vals)
    for v in vals:
        nonneg(1-v)

v0=V[0]
t1=1/q
# Exact support certificates for the five dihedral vertex separations.
expected={
  0:[((0,1),1+t,1-t)],
  1:[((0,t1),1+t,1-r*t),((t1,1),1+t,r*(1+t))],
  2:[((0,1),1+r*t,1+r*t)],
  3:[((0,t1),1-r*t,1+t),((t1,1),r*(1+t),1+t)],
  4:[((0,1),1-t,1+t)],
}
for k,pieces in expected.items():
    vk=V[k]
    zp=(v0[0]+t*vk[0],v0[1]+t*vk[1])
    zm=(v0[0]-t*vk[0],v0[1]-t*vk[1])
    for (lo,hi),ep,em in pieces:
        dominates_affine(zp,ep,lo,hi)
        dominates_affine(zm,em,lo,hi)

F0=1+t**2
F1a=1+(2-q)*(t+t**2)
F1b=(2-q)*(1+t)**2
F2=(1+r*t)**2

t0=2-q
assert sp.simplify(F1a-F2-r*t*(t-t0))==0
assert sp.simplify(F2-F0-2*r*t*(1-t))==0
assert sp.simplify(F1a-F0-t*((2-q)-r*t))==0
nonneg(t0); nonneg(t1-t0); nonneg(1-t1)
# After t1, F1b stays above F2 and F0 because both differences
# are positive at t1 and have positive derivatives on [t1,1].
D12=sp.expand(F1b-F2)
D10=sp.expand(F1b-F0)
nonneg(D12.subs(t,t1)); nonneg(D10.subs(t,t1))
nonneg(sp.diff(D12,t).subs(t,t1)); nonneg(sp.diff(D12,t).subs(t,1))
nonneg(sp.diff(D10,t).subs(t,t1)); nonneg(sp.diff(D10,t).subs(t,1))

# Yang--Li's identity: Omega(a)=(1+a)^2/2 * gamma((1-a)/(1+a)).
s=(1-a)/(1+a)
a0=3-2*q
a1=(2*q-1)/7
assert sp.simplify((1-t1)/(1+t1)-a0)==0
assert sp.simplify((1-t0)/(1+t0)-a1)==0
nonneg(a0); nonneg(a1-a0); nonneg(1-a1)

O0=4-2*q
O1=(a**2+2*(q-1)*a+5-2*q)/2
O2=1+2*(q-1)*a+(3-2*q)*a**2
assert sp.simplify((1+a)**2*F1b.subs(t,s)/2-O0)==0
assert sp.simplify((1+a)**2*F1a.subs(t,s)/2-O1)==0
assert sp.simplify((1+a)**2*F2.subs(t,s)/2-O2)==0
assert sp.simplify(O0-O1.subs(a,a0))==0
assert sp.simplify(O1.subs(a,a1)-O2.subs(a,a1))==0
assert sp.simplify(O2.subs(a,1)-2)==0
print('SUPPORT_INTERVALS=7')
print('GAMMA_BRANCHES=3')
print('OMEGA_BREAKPOINTS=', a0, a1)
print('VERIFY_OK')
