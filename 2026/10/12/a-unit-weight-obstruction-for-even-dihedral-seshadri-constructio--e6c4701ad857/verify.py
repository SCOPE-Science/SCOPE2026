import sympy as sp

n,q,D=sp.symbols("n q D")
alpha=(n-D)/2
beta=(n+D)/2
a=n-q

# Intersection form on the blow-up of P1 x P1 at 2n points:
# H1^2=H2^2=0, H1.H2=1, E^2=-2n.
dot=sp.expand(alpha + q*beta - 2*n)
assert sp.expand(2*dot - (n*(q-3)+(q-1)*D)) == 0

# Reflection s_gamma(R)=R+(R.gamma)/(n-q)*gamma.
h1=sp.expand(alpha + q*dot/a)
h2=sp.expand(beta + dot/a)
e_mag=sp.expand(1 + dot/a)  # coefficient of -E
A=sp.expand(2*a*h1)
B=sp.expand(2*a*h2)
C=sp.expand(2*a*e_mag)
A_expected=n*(n+q**2-4*q)+(q**2-n)*D
B_expected=n*(n-3)+(n-1)*D
C_expected=q*(n-2)-n+(q-1)*D
assert sp.simplify(A-A_expected)==0
assert sp.simplify(B-B_expected)==0
assert sp.simplify(C-C_expected)==0

# If D is irrational, (a0+a1 D)/(b0+b1 D) is rational exactly when
# a0*b1-a1*b0 vanishes (B is positive for n>4, D>0).
a0=n*(n+q**2-4*q)
a1=q**2-n
b0=n*(n-3)
b1=n-1
cross=sp.factor(a0*b1-a1*b0)
assert cross == 2*n*(q-n)*(q-n+2)

# D=sqrt(n(n-4)) cannot be integral for integer n>4 because
# (n-2)^2-D^2=4.  The only same-parity positive factorization of 4
# with n-2-D and n-2+D is 2*2, forcing n=4.
assert sp.expand((n-2)**2 - n*(n-4)) == 4

# Finite arithmetic sanity sweep, not used as the proof.
import math
for N in range(5,101):
    roots=[]
    for Q in range(1,N):
        if 2*N*(Q-N)*(Q-N+2)==0:
            roots.append(Q)
    assert roots == [N-2]
    if N % 2 == 0:
        assert math.gcd(N,N-2)==2
        assert all(2*N*(Q-N)*(Q-N+2)!=0 for Q in range(1,N) if math.gcd(Q,N)==1)
    else:
        assert math.gcd(N,N-2)==1

print("reflected_H1_numerator=A_q")
print("reflected_H2_numerator=B")
print("rationality_determinant=2*n*(q-n)*(q-n+2)")
print("unique_in_range_root=q=n-2")
print("even_n_gcd(n,n-2)=2")
print("VERIFY_OK")
