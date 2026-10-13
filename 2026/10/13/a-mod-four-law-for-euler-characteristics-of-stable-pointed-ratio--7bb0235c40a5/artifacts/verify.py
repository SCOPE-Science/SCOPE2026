from fractions import Fraction
from math import comb

MAX = 150
b = {2: 1}
for m in range(2, MAX):
    conv = sum(comb(m,k)*b[k]*b[m-k+1] for k in range(2,m))
    b[m+1] = 2*b[m] + conv

for r in range(1, MAX//2):
    assert b[2*r] % 4 == (1 if (r+1)%2==0 else 3)
    if 2*r+1 <= MAX:
        assert b[2*r+1] % 4 == 2

published = [1,2,7,34,213,1630,14747,153946,1821473]
assert [b[m] for m in range(2,11)] == published

# Exact ordinary power-series arithmetic for exponential series.
N = 35
# g(x)=x+sum b_m x^m/m!
g = [Fraction(0) for _ in range(N+1)]
g[1] = Fraction(1)
fact = 1
for m in range(2,N+1):
    fact *= m
    g[m] = Fraction(b[m], fact)

# f(x)=2x-(1+x)log(1+x); coefficients f_m=-(-1)^m/(m(m-1)), m>=2.
f = [Fraction(0) for _ in range(N+1)]
f[1]=Fraction(1)
for m in range(2,N+1):
    f[m] = Fraction(-((-1)**m), m*(m-1))

def mul(a,c):
    out=[Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(c):
            if y and i+j<=N: out[i+j]+=x*y
    return out

powers=[[Fraction(0) for _ in range(N+1)] for __ in range(N+1)]
powers[0][0]=Fraction(1)
powers[1]=g[:]
for m in range(2,N+1): powers[m]=mul(powers[m-1],g)
comp=[Fraction(0) for _ in range(N+1)]
for m,coef in enumerate(f):
    if coef:
        for j in range(N+1): comp[j]+=coef*powers[m][j]
assert comp[1] == 1
assert all(comp[j] == 0 for j in range(N+1) if j != 1)
print('VERIFY_OK', MAX-1, N, [b[m] for m in range(2,11)])
