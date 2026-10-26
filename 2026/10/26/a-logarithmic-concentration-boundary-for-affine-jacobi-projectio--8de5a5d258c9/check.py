"""Exact finite checks for affine Dirichlet projection stability.

Run with: python3 check.py
Uses only the Python standard library. Analytical asymptotics are proved in RESULT.md;
finite checks do not certify their universal scope.
"""
from fractions import Fraction as Q
from math import comb, factorial

ASSERTIONS=0

def check(condition, description):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(description)

def beta_integer(a,b):
    return Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def polynomial_negative_mass(n,a):
    """Exact integral of negative vertex kernel against Beta(a,(n-1)a)."""
    b=(n-1)*a
    c=Q(a,n*a+1)
    total=Q(0)
    for j in range(b):
        total += (-1)**j * comb(b-1,j) * (Q(a)*c**(a+j)/Q(a+j)
                    -Q(n*a+1)*c**(a+j+1)/Q(a+j+1))
    return n*total/beta_integer(a,b)

def beta_cdf_integer(a,b,c):
    total=Q(0)
    for j in range(b):
        total += (-1)**j*comb(b-1,j)*c**(a+j)/Q(a+j)
    return total/beta_integer(a,b)

def boundary_expression(n,a):
    b=(n-1)*a
    c=Q(a,n*a+1)
    return Q(n*a+1,a)*c**a*(1-c)**b/beta_integer(a,b) - beta_cdf_integer(a,b,c)

def kernel(n,a,x,y):
    return -n*a + n*(n*a+1)*sum(u*v for u,v in zip(x,y))

def expectation_kernel_product(n,a,x,z):
    # independently integrate the bilinear expansion using Dirichlet moments
    m1=[Q(1,n)]*n
    m2=[[Q(a+1,n*(n*a+1)) if i==j else Q(a,n*(n*a+1))
         for j in range(n)] for i in range(n)]
    c=-n*a; t=n*(n*a+1)
    return (c*c+c*t*(sum(x[i]*m1[i] for i in range(n))+
                       sum(z[i]*m1[i] for i in range(n)))+
            t*t*sum(x[i]*z[j]*m2[i][j] for i in range(n) for j in range(n)))

for n in range(2,11):
    for a in range(1,5):
        d=polynomial_negative_mass(n,a)
        check(d==boundary_expression(n,a),f'Beta recurrence n={n} a={a}')
        check(d>0,f'positivity defect n={n} a={a}')
        check(Q(1)+2*d>1,f'sharp norm n={n} a={a}')
        if a==1:
            check(d==n*Q(n,n+1)**(n-1)-1,f'Lebesgue reduction n={n}')
        for k in range(n):
            v=[Q(int(i==k)) for i in range(n)]
            u=[Q(1,n)]*n
            w=[Q(int(i in (0,k)),1+(k==0)) if k!=0 else Q(int(i==0)) for i in range(n)]
            # for k>0 w is half the sum of the first and k-th vertices
            if k>0:
                w=[Q(int(i==0)+int(i==k),2) for i in range(n)]
            for x,z in ((v,v),(v,u),(w,v),(w,u)):
                check(expectation_kernel_product(n,a,x,z)==kernel(n,a,x,z),
                      f'kernel reproduction n={n} a={a} index={k}')
        check(d<=n*a,f'boundary easy bound n={n} a={a}')

print(f'PASS: {ASSERTIONS} independent exact-rational assertions')
