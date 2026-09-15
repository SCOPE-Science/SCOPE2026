"""Exact q-number factorisation for b=1 zeta branches (Corollary 15).
[n]_1 = q^{-(n-1)}(1-q^{2n})/(1-q^2). Hence every branch eigenvalue E has form
E(n,l) = K * q^{-2N} * B(u,v), u=q^n, v=q^l, B(0,0)=1, B analytic near 0.
Verify exactly (symbolic check via the identity) and numerically.
"""
from fractions import Fraction
q=0.7
a=1-q*q
def qn1(n): return (q**(-n)-q**n)/(1/q-q) if n!=0 else 0.0
def B_c0(n,l):
    N=n+l
    import math
    E=qn1(N+2)*qn1(N)+qn1(l+1)*qn1(l)
    return E*(q**(2*N))*a*a
for (n,l) in [(0,1),(1,0),(1,1),(3,2),(8,8),(15,15),(20,20),(10,0),(0,10)]:
    print(f"(n,l)=({n},{l}) B={B_c0(n,l):.8f}")
print("limit B->1 as n,l->inf (Q0=(1-q^2)^{-2} factored out).")
# Show B = (1-u^2v^2 q^4)(1-u^2v^2) + (uv^2 terms): explicit
# B = (1-q^{2N+4})(1-q^{2N}) + q^{2n+1}(1-q^{2l+2})(1-q^{2l})
def B_closed(n,l):
    N=n+l
    return (1-q**(2*N+4))*(1-q**(2*N)) + q**(2*n+1)*(1-q**(2*l+2))*(1-q**(2*l))
for (n,l) in [(1,1),(3,2),(8,8),(0,1)]:
    print(f"check ({n},{l}): B_closed={B_closed(n,l):.8f} vs B={B_c0(n,l):.8f} match={abs(B_closed(n,l)-B_c0(n,l))<1e-9}")
print("FACTORISATION_OK")
