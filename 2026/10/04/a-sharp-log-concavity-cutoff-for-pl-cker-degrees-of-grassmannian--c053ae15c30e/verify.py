from math import factorial, prod
from fractions import Fraction

def degree(n,k):
    assert 1 <= k <= n-1
    m=k*(n-k)
    return factorial(m)*prod(factorial(i) for i in range(k))//prod(factorial(j) for j in range(n-k,n))

def log_concave(ds):
    return all(ds[i]*ds[i] >= ds[i-1]*ds[i+1] for i in range(1,len(ds)-1))

# Formula consequences, symmetry, and strict central growth.
for n in range(2,101):
    ds=[degree(n,k) for k in range(1,n)]
    assert ds == ds[::-1]
    for k in range(1,(n-1)//2 + 1):
        if k < (n-1)/2:
            assert degree(n,k+1) > degree(n,k)

# Exact finite side of the log-concavity cutoff.
for n in range(2,12):
    assert log_concave([degree(n,k) for k in range(1,n)])
assert not log_concave([degree(12,k) for k in range(1,12)])
assert degree(12,2)**2 < degree(12,1)*degree(12,3)

# Edge ratios used in the infinite proof.
assert Fraction(degree(11,3), degree(11,2)**2) == Fraction(437,442)
assert Fraction(degree(12,3), degree(12,2)**2) == Fraction(3795,2584)
for n in range(5,1001):
    qn=Fraction(2*(n-2)*factorial(n-1)*factorial(3*n-9), factorial(2*n-4)**2)
    qnext=Fraction(2*(n-1)*factorial(n)*factorial(3*n-6), factorial(2*n-2)**2)
    assert qnext > qn
    p=11*n**3-71*n**2+84*n+36
    assert p == 11*(n-5)**3+94*(n-5)**2+199*(n-5)+56
    assert p > 0

print('VERIFY_OK')
print('n=11:', degree(11,2), degree(11,3), Fraction(degree(11,3),degree(11,2)**2))
print('n=12:', degree(12,2), degree(12,3), Fraction(degree(12,3),degree(12,2)**2))
