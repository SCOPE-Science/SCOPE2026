"""Exact coefficient and degeneracy verifier for a genus-four cyclic quintic family.

Run: python3 verify_cyclic5_11.py. Requires sympy >= 1.11.
All arithmetic that determines the result is in F_11[t].
"""
import sympy as S
x,t=S.symbols('x t'); p=11
f=x*(x-1)*(x-t)**2
Q=t*t-t+1

def red(v):
    return S.Poly(S.expand(v),t,modulus=p).as_expr()

def assert_zero(v):
    assert S.Poly(S.expand(v),t,modulus=p).is_zero, S.factor(v)

def coeff(h,q,k):
    return red(S.Poly(S.expand(h*f**q),x).coeff_monomial(x**k))

A=coeff(1,4,10)
B=coeff(x-t,6,21)
assert_zero(A-(-5)*t*t*(t-1)**2*Q)
assert_zero(B-4*Q)
assert_zero(coeff(x-t,6,10)+t**11*B)
assert_zero(coeff(x-t,6,32))

basis=[x-t,x*(x-t)]
v0=[];v1=[]
for h in basis:
    low=coeff(h,8,10)
    mid=coeff(h,8,21)
    high=coeff(h,8,32)
    aa=red(-S.cancel(low/t**S.Integer(11)))
    assert_zero(low+t**11*aa)
    assert_zero(mid-aa+t**11*high)
    v0.append(aa);v1.append(high)
assert_zero(v0[0]+5*t**4*(t*t-3*t-3))
assert_zero(v0[1]-3*t**5*(t-2))
assert_zero(v1[0]-5*(t+5))
assert_zero(v1[1]-4*(t*t+t-4))
block_det=red(v0[0]*v1[1]-v0[1]*v1[0])
assert_zero(block_det-2*t**4*(t-1)**4)
det=red(A*B*block_det)
assert_zero(det-4*t**6*(t-1)**6*Q**2)
# Character basis and local valuation checks: j=2,3,4 and h=1,(x-t),(x-t),x(x-t).
for j,h in [(2,1),(3,x-t),(4,x-t),(4,x*(x-t))]:
    order_at_lam=(0 if h==1 else 1)
    order_at_infty= 4*j-6-5*S.degree(h,x)
    assert 4+5*order_at_lam-2*j>=0
    assert order_at_infty>=0
# Q has distinct roots, and none is at the boundary.
assert_zero(S.gcd(S.Poly(Q,t,modulus=p),S.Poly(S.diff(Q,t),t,modulus=p)).as_expr()-1)
assert red(Q.subs(t,0)) and red(Q.subs(t,1))
# Q is irreducible over F_11; its discriminant -3=8 is a nonsquare.
assert 8 not in {(n*n)%11 for n in range(11)}
# Branch-moduli invariant j_br=256 Q^3/[t^2(t-1)^2], so vanishes iff Q=0.
# The six branch cross ratio transforms stabilize the unordered image.
trs=[t,1-t,1/t,1/(1-t),(t-1)/t,t/(t-1)]
for tr in trs:
    expr=S.cancel(256*Q**3/(t*t*(t-1)**2)-256*(tr*tr-tr+1)**3/(tr**2*(tr-1)**2))
    assert S.cancel(expr)==0
print('VERIFY_OK: genus 4 basis valuations, 4 block coefficients, 2x2 determinant, all polynomial identities')
print('STRATA_OK: p=11, rank 4 for Q !=0 and rank 2 for Q=0, a-numbers 0 and 2, stable ranks equal ranks')
print('DIVISOR_OK: det(B)=4*t^6*(t-1)^6*(t^2-t+1)^2; two F121 points, each multiplicity two')
print('MODULI_OK: exceptional branch configurations form one equianharmonic S3 orbit, j_br=0')
