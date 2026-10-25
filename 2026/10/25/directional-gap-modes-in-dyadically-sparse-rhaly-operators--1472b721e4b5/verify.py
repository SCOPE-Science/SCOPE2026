"""Reproducibility checks for the dyadic sparse Rhaly singular-spectrum theorem.

Finite calculations are supplementary checks, not certificates of the
infinite-dimensional spectrum.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks=0

def check(condition):
    global checks
    assert condition
    checks+=1

# Exact finite-dimensional Gram and inverse covariance identities.
for N in range(2,13):
    for u,v in ((F(1),F(2)),(F(3),F(2)),(F(1),F(1)),(F(2),F(5))):
        b=[u if k%2==0 else v for k in range(N)]
        # Replace irrational Gram by exact factorization with q=sqrt(2) symbolic:
        # normalize G by b's: Toeplitz covariance with a=1/sqrt(2).
        # Check via a^2=1/2 and exact multiplication of T_a and T_a^-1
        # in formal polynomials c0+c1*a, a*a=1/2.
        def smul(x,y):
            x0,x1=x;y0,y1=y
            return x0*y0+x1*y1/F(2),x0*y1+x1*y0
        def sadd(x,y):return x[0]+y[0],x[1]+y[1]
        def tp(k,l):
            d=abs(k-l)
            if d%2:return F(0),F(1,2**(d//2))
            return F(1,2**(d//2)),F(0)
        def ip(k,l):
            if k==l:return (F(2) if k==0 else F(3), F(0))
            if abs(k-l)==1:return (F(0),-F(2))
            return F(0),F(0)
        for k in range(N):
            for l in range(N):
                z=(F(0),F(0))
                for j in range(N):z=sadd(z,smul(tp(k,j),ip(j,l)))
                # Last finite inverse has exceptional right endpoint diag2.
                # So focus on all columns <=N-2.
                if l<N-1:check(z==(F(k==l),F(0)))
        # Isolated edge vector solves first Jacobi row and all interior rows.
        rho=u*u/(v*v); eigen=F(2)/(u*u)+F(1)/(v*v)
        # Symbolic offdiag sqrt2/(uv), odd eigenvector=-u/(sqrt2 v) r^k.
        # split even/odd recurrence directly after multiplying sqrt2.
        r=-rho
        for k in range(1,9):
            even=r**k
            prevodd=-(u/(2*v))*r**(k-1)  # coefficient of sqrt2
            nextodd=-(u/(2*v))*r**k
            actual=(F(3)/(u*u))*even - F(2)/(u*v)*(prevodd+nextodd)
            check(actual==eigen*even)
        for k in range(0,9):
            oddcoeff=-u/(2*v)*r**k
            # odd coefficient of sqrt2 in vector; diagonal acts on sqrt2 coeff,
            # -sqrt2/(uv) times even neighbors gives sqrt2 coeff -1/(uv).
            actual=(F(3)/(v*v))*oddcoeff-F(1)/(u*v)*(r**k+r**(k+1))
            check(actual==eigen*oddcoeff)
        boundary=(F(2)/(u*u))*F(1)-F(2)/(u*v)*(-u/(2*v))
        check(boundary==eigen)
        if u<v:check(abs(float(r))<1)
        else:check(abs(float(r))>=1)

# Inspect band edges and position of the boundary state in exact rational cases.
for ui,vi in ((1,2),(2,1),(2,3),(3,2),(1,1),(2,2),(1,4),(4,1)):
    A=3/ui**2;B=3/vi**2;t=sqrt(2)/(ui*vi)
    L=(A+B-sqrt((A-B)**2+16*t*t))/2
    U=(A+B+sqrt((A-B)**2+16*t*t))/2
    check(L>0 and U>=max(A,B))
    check(isclose(L*U,1/(ui*ui*vi*vi),rel_tol=1e-12))
    edge=2/ui**2+1/vi**2
    if ui<vi:check(min(A,B)<edge<max(A,B))
    if ui==vi:check(isclose(edge,A))
    if ui>vi:check(min(A,B)<edge<max(A,B))
    r=-ui*ui/vi**2
    check((abs(r)<1)==(ui<vi))

# Direct matrix coefficient tests: sparse triangular rows vs analytic Gram.
for N in range(1,9):
    for ui,vi in ((1.,2.),(2.,1.),(1.3,2.7)):
        b=[ui if j%2==0 else vi for j in range(N)]
        rows=[]
        for j in range(N):
            row=[(b[j]/sqrt(2**j) if m<2**j else 0.) for m in range(2**(N-1))]
            rows.append(row)
        for i in range(N):
            for j in range(N):
                measured=sum(x*y for x,y in zip(rows[i],rows[j]))
                expected=b[i]*b[j]*2**(-abs(i-j)/2)
                check(isclose(measured,expected,rel_tol=1e-12,abs_tol=1e-12))

print('PASS',checks,'supplementary checks')
