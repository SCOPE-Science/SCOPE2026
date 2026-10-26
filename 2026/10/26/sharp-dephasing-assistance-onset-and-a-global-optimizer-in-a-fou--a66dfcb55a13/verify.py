"""Exact finite-chain steady-current and phase-boundary verification.

Dependencies: Python 3 and SymPy. Independently solving the full Lindblad
master equation is implemented in crosscheck_lindblad.py.
"""
import sympy as S

G, u, g, W = S.symbols('G u g W', real=True)

def stationary_coefficients(L):
    h = {(r, j): S.Symbol('h%d_%d' % (r,j))
         for r in range(1, L+1) for j in range(1,L-r+2)}
    b = {(r, j): S.Symbol('b%d_%d' % (r,j))
         for r in range(2, L+1) for j in range(1,L-r+2)}
    def H(r,j): return h.get((r,j), S.Integer(0))
    def B(r,j): return b.get((r,j), S.Integer(0))
    eq = [G*(1+H(1,1))-4*B(2,1), G*(1-H(1,L))-4*B(2,L-1)]
    eq += [B(2,j)-B(2,j-1) for j in range(2,L)]
    for r in range(2,L+1):
        for j in range(1,L-r+2):
            damping = g + G*S.Rational(1,4)*(int(j==1)+int(j+r-1==L))
            eq += [H(r-1,j)-H(r-1,j+1)+H(r+1,j)-H(r+1,j-1)
                   +(r-1)*u*H(r,j)+damping*B(r,j)]
            eq += [B(r-1,j)-B(r-1,j+1)+B(r+1,j)-B(r+1,j-1)
                   +(r-1)*u*B(r,j)-damping*H(r,j)]
    variables=list(h.values())+list(b.values())
    A,rhs=S.linear_eq_to_matrix(eq, variables)
    return A,rhs,variables

def current(L):
    A,rhs,variables=stationary_coefficients(L)
    col=variables.index(S.Symbol('b2_1'))
    replacement=A.copy()
    replacement[:,col]=rhs
    return S.factor(4*replacement.det(method='domain-ge')/A.det(method='domain-ge'))

F2,F3,F4=(current(n) for n in (2,3,4))
assert S.cancel(F2-16*G*(2*g+G)/(16*(2*g+G)+4*G*u**2+G*(2*g+G)**2))==0
assert S.cancel(F3-16*G*(4*g+G)/(16*(4*g+G)+16*G*u**2+G*(4*g+G)**2))==0

P = (5308416*W**5+(460800*G**2+3538944)*W**4
     +(14608*G**4+513024*G**2+9547776)*W**3
     +(200*G**6+16128*G**4+157696*G**2+5603328)*W**2
     +(G**8+128*G**6-1536*G**4+90112*G**2+2293760)*W
     -192*G**2*(G**2+16)**2)
E = G**2+64*u**2+16
T = G**2*u**2+4*G**2+36*u**4+48*u**2+64
assert S.cancel(F4.subs(g,0)-64*G*(G**2+36*u**2+16)/(E*T))==0
assert S.cancel(S.diff(F4,g).subs(g,0)-8*P.subs(W,u**2)/(E*T)**2)==0

# Exact one-threshold certificate for each positive boundary coupling G.
assert S.factor(S.Poly(P,W).coeff_monomial(W)) == (G**2+16)*(G**6+112*G**4-3328*G**2+143360)
assert 3328**2-4*112*143360<0
for exponent in range(2,6):
    cc=S.Poly(P,W).coeff_monomial(W**exponent)
    assert all(x>0 for x in S.Poly(cc,G).all_coeffs() if x!=0)
assert S.factor(P.subs(W,0)) == -192*G**2*(G**2+16)**2

# Check positive coefficients of the exact rational current.
N,D=S.fraction(F4)
for expr in [N/G,D]:
    expanded=S.Poly(S.expand(expr).subs(u**2,W),G,g,W)
    assert all(x>=0 for x in expanded.coeffs())

# Global unimodality, rigorously on the equal-rates Γ=J=1 section.
N1,D1=S.fraction(S.factor(F4.subs(G,1)))
Q=S.expand(S.diff(N1,g)*D1-N1*S.diff(D1,g))
q=S.Poly(S.expand(Q).subs(u**2,W),g)
assert q.degree()==12
cs=[S.factor(q.coeff_monomial(g**k)) for k in range(13)]
P1=S.factor(P.subs(G,1))
assert S.expand(cs[0]-32*P1)==0
assert all(S.Poly(cs[i],W).degree() in [4,5] for i in range(4))
# For k=0,1,2,3, each coefficient crosses zero once and in this order.
brackets=[(S.Rational(22,1000),S.Rational(23,1000)),
          (S.Rational(72,1000),S.Rational(74,1000)),
          (S.Rational(244,1000),S.Rational(246,1000)),
          (S.Rational(104,100),S.Rational(106,100))]
for i,(lo,hi) in enumerate(brackets):
    c=cs[i]
    assert S.sign(c.subs(W,0))<0
    assert S.sign(c.subs(W,lo))<0 and S.sign(c.subs(W,hi))>0
    # Exactly one positive zero by Descartes' rule of signs.
    coeff=S.Poly(c,W).all_coeffs()
    nonzero=[S.sign(x) for x in coeff if x!=0]
    assert sum(nonzero[k]!=nonzero[k+1] for k in range(len(nonzero)-1))==1
# g^4 coefficient is strictly negative: its positive bracket is a
# quadratic of negative discriminant plus a positive linear polynomial.
assert S.expand(cs[4]+256*(8847360*W**4-2954752*W**3+18913120*W**2+4417642*W+7015467))==0
assert 2954752**2-4*8847360*18913120<0
for i in range(5,13):
    pol=S.Poly(-cs[i],W)
    assert all(x>=0 for x in pol.all_coeffs()) and pol.eval(0)>0
# The g polynomial thus has all negative coefficients below Wc;
# above Wc, exactly one sign change in ascending g order.

c=S.symbols('c',positive=True)
assert S.simplify(S.limit(u*F4.subs({G:1,g:c*u}),u,S.oo)-8*c/(3*(1+c**2)))==0

assert S.factor(F4.subs({G:1,u:0})) == 16/(6*g+17)
print('PASS exact current: L=2,3 crosschecks; L=4 positivity and response')
print('PASS unique onset: all positive boundary couplings')
print('PASS global one-maximum theorem: Γ=1; root isolation and coefficient signs')
print('PASS strong-tilt scaling current and optimal ratio')
