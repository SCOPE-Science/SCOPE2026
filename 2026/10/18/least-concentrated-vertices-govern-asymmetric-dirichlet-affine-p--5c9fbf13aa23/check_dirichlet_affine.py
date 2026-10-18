"""Finite reproducibility tests for Dirichlet-affine projection formulas.

Requires Python 3 and mpmath. All claims for arbitrary parameters are proven
analytically in RESULT.md; these are finite reproducibility tests only.
"""
from fractions import Fraction as F
from itertools import product
import mpmath as mp

mp.mp.dps=45
N=0

def check(condition, note):
    global N
    N+=1
    if not condition:
        raise AssertionError(note)


def Q(a,A):
    a,A=mp.mpf(str(a)),mp.mpf(str(A))
    t=a/(A+1)
    return 1+2*(A*mp.betainc(a,A-a,0,t,regularized=True)
                  -(A+1)*mp.betainc(a+1,A-a,0,t,regularized=True))

def quad_Q(a,A):
    a,A=mp.mpf(str(a)),mp.mpf(str(A))
    t=a/(A+1)
    denom=mp.beta(a,A-a)
    # y=t*u**(1/a) removes the beta-density endpoint singularity.
    f=lambda u: (A-A*(A+1)*(t*u**(1/a))/a)*(1-t*u**(1/a))**(A-a-1)*t**a/(a*denom)
    return 1+2*mp.quad(f,[0,1])

def inverse(matrix):
    n=len(matrix)
    a=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for j in range(n):
        t=next(t for t in range(j,n) if a[t][j]!=0)
        a[t],a[j]=a[j],a[t]
        z=a[j][j];a[j]=[q/z for q in a[j]]
        for i in range(n):
            if i==j:continue
            z=a[i][j]
            a[i]=[a[i][k]-z*a[j][k] for k in range(2*n)]
    return [row[n:] for row in a]

# Exact rational Gram-matrix, reproducing-kernel and affine-reproduction tests.
for alpha in [[F(1),F(2)], [F(1),F(2),F(3)], [F(1,2),F(3,2),F(5,2)], [F(3),F(1),F(1),F(2)]]:
    n=len(alpha);A=sum(alpha)
    G=[[(alpha[i]*alpha[j]+(alpha[i] if i==j else 0))/(A*(A+1)) for j in range(n)] for i in range(n)]
    inv=inverse(G)
    expected=[[(A*(A+1)/alpha[i] if i==j else F(0))-A for j in range(n)] for i in range(n)]
    for i,j in product(range(n),repeat=2):
        check(inv[i][j]==expected[i][j],f'Gram inverse {alpha} {i} {j}')
    for i,j in product(range(n),repeat=2):
        check(sum(inv[i][k]*G[k][j] for k in range(n))==F(int(i==j)),f'kernel reproduces {alpha} {i} {j}')
    for i in range(n):
        check(sum(inv[i][j]*alpha[j]/A for j in range(n))==1,f'constants {alpha} {i}')

# Direct quadrature, separate from the incomplete-beta antiderivative.
for A in (mp.mpf('1.7'),mp.mpf('3.1'),mp.mpf('9.4')):
    for fraction in (mp.mpf('0.09'),mp.mpf('0.25'),mp.mpf('0.45'),mp.mpf('0.76'),mp.mpf('0.91')):
        a=A*fraction
        err=abs(Q(a,A)-quad_Q(a,A))
        check(err<mp.mpf('3e-32'),f'beta-integral {a},{A}: {err}')

# Strict convex-order monotonicity on heterogeneous finite grids.
for A in (mp.mpf('0.8'),mp.mpf('2.5'),mp.mpf('10'),mp.mpf('33')):
    vals=[Q(A*mp.mpf(k)/20,A) for k in range(1,20)]
    for i in range(len(vals)-1):
        check(vals[i]>vals[i+1],f'shape order {A},{i}')

# Binary-simplex arbitrary evaluation-point norms cannot exceed best endpoint.
for a,b in ((mp.mpf('0.7'),mp.mpf('1.9')), (mp.mpf('2'),mp.mpf('5')), (mp.mpf('4.2'),mp.mpf('1.1'))):
    A=a+b
    beta_norm=mp.beta(a,b)
    for k in range(1,20):
        x=mp.mpf(k)/20
        f=lambda y: abs((A+1)*A*(x*y/a+(1-x)*(1-y)/b)-A)*y**(a-1)*(1-y)**(b-1)/beta_norm
        val=mp.quad(f,[0,mp.mpf('0.5'),1])
        check(val<max(Q(a,A),Q(b,A)),f'interior {a} {b} {x}')

# Large-total-concentration beta central-limit prediction (coarse tolerances).
for p in (mp.mpf('0.16'),mp.mpf('0.31'),mp.mpf('0.47')):
    for A in (mp.mpf('150'),mp.mpf('450')):
        target=mp.sqrt(2/mp.pi)*mp.sqrt((1-p)/p)
        observed=Q(p*A,A)/mp.sqrt(A)
        check(abs(observed/target-1)<mp.mpf('0.08'),f'large concentration {p} {A}')

# Boundary behavior in the fixed-A problem.
for A in (mp.mpf('0.6'),mp.mpf('2.3'),mp.mpf('8')):
    val=Q(A*mp.mpf('1e-9'),A)
    check(abs(val-(1+2*A))<mp.mpf('0.001'),f'vanishing shape {A}')

print(f'PASS: {N} deterministic finite checks')
print('Example alpha=(1,2,5): total=8, sharp norm =',mp.nstr(Q(1,8),18))
print('Balanced alpha=(8/3,8/3,8/3): norm =',mp.nstr(Q(mp.mpf(8)/3,8),18))
