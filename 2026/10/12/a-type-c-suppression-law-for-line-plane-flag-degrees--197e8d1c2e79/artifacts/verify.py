from fractions import Fraction
from math import factorial

def ordinary_root_degree(n):
    N = 2*n
    d = 4*n-3
    prod = Fraction(1,1)
    # Complementary A_{N-1} roots for flags 1<2.
    prod *= Fraction(1,1)  # e1-e2
    for j in range(3,N+1):
        prod *= Fraction(2,j-1)  # e1-ej
        prod *= Fraction(1,j-2)  # e2-ej
    return factorial(d)*prod

def symplectic_root_degree(n):
    d = 4*n-4
    lam = [2,1] + [0]*(n-2)
    rho = [n-i for i in range(n)]
    prod = Fraction(1,1)
    # Positive short roots e_i-e_j and e_i+e_j outside Levi C_{n-2}.
    for i in range(n):
        for j in range(i+1,n):
            if i < 2:
                prod *= Fraction(lam[i]-lam[j], rho[i]-rho[j])
                prod *= Fraction(lam[i]+lam[j], rho[i]+rho[j])
    # Positive long roots 2e_1 and 2e_2 have coroots e_1 and e_2.
    for i in range(2):
        prod *= Fraction(lam[i],rho[i])
    return factorial(d)*prod

def deg_a(n):
    return Fraction((2**(2*n-2))*factorial(4*n-3), factorial(2*n-1)*factorial(2*n-2))

def deg_c(n):
    return Fraction(3*(2**(2*n-3))*factorial(4*n-4), factorial(2*n-1)*factorial(2*n-3))

def euler_a(n):
    return 2*n*(2*n-1)

def euler_c(n):
    return 4*n*(n-1)

checks=0
for n in range(2,101):
    da=ordinary_root_degree(n)
    dc=symplectic_root_degree(n)
    assert da == deg_a(n)
    assert dc == deg_c(n)
    assert da.denominator == dc.denominator == 1
    assert Fraction(dc,da) == Fraction(3*(n-1),4*n-3)
    assert Fraction(euler_c(n),euler_a(n)) == Fraction(2*(n-1),2*n-1)
    q = Fraction(dc,euler_c(n)) / Fraction(da,euler_a(n))
    assert q == Fraction(3*(2*n-1),2*(4*n-3))
    checks += 1

for n in range(2,100):
    qn = Fraction(3*(2*n-1),2*(4*n-3))
    qnext = Fraction(3*(2*n+1),2*(4*n+1))
    assert qn > qnext
    assert qn-qnext == Fraction(3, (4*n-3)*(4*n+1))
    checks += 1

assert ordinary_root_degree(2) == 40
assert symplectic_root_degree(2) == 24
assert euler_a(2) == 12
assert euler_c(2) == 8
assert Fraction(24,8)/Fraction(40,12) == Fraction(9,10)
print('VERIFY_OK', checks)
