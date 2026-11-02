"""Exact-rational spot checks for a closed second Cesàro commutator moment."""
from fractions import Fraction as F
from decimal import Decimal, localcontext

N_ASSERT = 0
def verify(cond):
    global N_ASSERT
    assert cond
    N_ASSERT += 1

def harmonic(n): return sum((F(1,k) for k in range(1,n+1)), F(0))
def m(n,j): return F(2*(n-j+1),(n+1)*(n+2)) if j<=n else F(0)
def r(n): return F(4*n+10,(n+3)*(n+4))
def gram(n,l):
    a,b=max(n,l),min(n,l)
    return F(2*(3*a-b+3),3*(a+1)*(a+2))
def coeffs(n):
    x=F(n)
    A=(F(104,9)/(x+4)-F(8,3)/(x+3)+F(136,3)/(x+2)+F(16,3)/(x+2)**2-F(488,9)/(x+1)+F(208,3)/(x+1)**2)
    B=(-F(56)/(x+4)+F(100,9)/(x+4)**2+F(464,9)/(x+3)-F(20,3)/(x+3)**2-F(40,9)/(x+2)-F(4)/(x+2)**2+F(80,9)/(x+1)-F(628,9)/(x+1)**2)
    return A,B
for n in range(21):
    for j in range(n+1): verify(m(n,j) == F(2*(n-j+1),(n+1)*(n+2)))
    for l in range(n+1):
        verify(sum((m(n,j)*m(l,j) for j in range(l+1)),F(0))==gram(n,l))
    h=harmonic(n+2)
    S0=4*h+F(6,n+3)-8
    S1=4*n-18*h-F(24,n+3)+35
    S2=2*n*n-20*n+78*h+F(96,n+3)-149
    verify(S0==sum((r(l) for l in range(n)),F(0)))
    verify(S1==sum((l*r(l) for l in range(n)),F(0)))
    verify(S2==sum((l*l*r(l) for l in range(n)),F(0)))
    term=F(4,9)*r(n)/F((n+1)**2*(n+2)**2)*(r(n)*(2*n+3)**2+2*((3*n+3)**2*S0-2*(3*n+3)*S1+S2))
    direct=r(n)**2*gram(n,n)**2+2*sum((r(l)*r(n)*gram(n,l)**2 for l in range(n)),F(0))
    verify(term==direct)
    A,B=coeffs(n)
    verify(A*h+B==term)
print('PASS:',N_ASSERT,'exact-rational identities; no assertion about infinite summation from these finite tests.')
