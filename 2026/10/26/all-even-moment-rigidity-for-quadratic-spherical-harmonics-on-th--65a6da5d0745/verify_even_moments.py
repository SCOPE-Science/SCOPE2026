"""Exact checks for even moments of quadratic spherical harmonics on S^2.

This program uses only Python's standard library. Its finite checks are
supplementary to the general algebraic proof.
"""
from fractions import Fraction as F
from math import factorial, comb

ASSERTIONS = 0

def check(statement, why):
    global ASSERTIONS
    if not statement:
        raise AssertionError(why)
    ASSERTIONS += 1

def poch(a,n):
    q=F(1)
    for k in range(n): q*=a+k
    return q

def odddf(k):
    out=1
    for j in range(k,0,-2): out*=j
    return out

def sphere_even(exps):
    if any(e%2 for e in exps): return F(0)
    a,b,c=(e//2 for e in exps)
    return poch(F(1,2),a)*poch(F(1,2),b)*poch(F(1,2),c)/poch(F(3,2),a+b+c)

def mul(p,q):
    out={}
    for i,ci in p.items():
        for j,cj in q.items():
            e=tuple(x+y for x,y in zip(i,j))
            out[e]=out.get(e,F(0))+ci*cj
    return {k:v for k,v in out.items() if v}

def add(p,q):
    r=dict(p)
    for k,v in q.items():r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}

def power(p,n):
    out={(0,0,0):F(1)}
    for _ in range(n):out=mul(out,p)
    return out

def integrate(p):
    return sum((c*sphere_even(k) for k,c in p.items()),F(0))

def qpoly(diagonal):
    return {(2,0,0):F(diagonal[0]),(0,2,0):F(diagonal[1]),(0,0,2):F(diagonal[2])}

def beta_polynomial(m,delta):
    q=F(0)
    for h in range(m//3+1):
        coeff=poch(F(1,2),m-h)/F(factorial(m-3*h)*factorial(2*h))
        q+=coeff*(F(4,27)*delta)**h
    return F(15**m*factorial(2*m),odddf(4*m+1))*q

def lower(m): return beta_polynomial(m,F(0))
def upper(m): return beta_polynomial(m,F(1))

def invariant_ratio(a):
    S=sum(x*x for x in a); T=sum(x*x*x for x in a)
    return F(6*T*T,S*S*S)

# Verify the claimed normalized fourth/sixth moments and transition.
check(lower(1)==1 and upper(1)==1,'L2 normalization')
check(lower(2)==upper(2)==F(15,7),'quartic invariance')
check(lower(3)==F(5625,1001),'sextic lower constant')
check(upper(3)==F(6625,1001),'sextic upper constant')
check(upper(3)-lower(3)==F(1000,1001),'sextic gap')

# Independently integrate Legendre zonal powers for the maximizing class.
for m in range(1,14):
    leg=F(0)
    for j in range(2*m+1):
        leg+=F(comb(2*m,j)*3**j*(-1)**(2*m-j),2**(2*m)*(2*j+1))
    check(upper(m)==15**0 * 5**m*leg, f'zonal Legendre moment m={m}')
    if m>=3:
        check(upper(m)>lower(m), f'positive biaxial gap m={m}')

# Independent exact Dirichlet integration of diagonal quadratics.
for a in [(1,0,-1),(2,-1,-1),(3,-1,-2),(7,2,-9),(-2,5,-3)]:
    S=sum(x*x for x in a)
    check(sum(a)==0,f'tracezero {a}')
    delta=invariant_ratio(a)
    check(F(0)<=delta<=F(1),f'delta domain {a}')
    p=qpoly(a)
    L2=integrate(power(p,2))
    check(L2==F(2*S,15), f'quadratic norm {a}')
    for m in range(2,11):
        direct=integrate(power(p,2*m))
        predicted=beta_polynomial(m,delta)*(L2**m)
        check(direct==predicted,f'full moment formula m={m} a={a}')

# Strict ordering and equality regimes across the coefficient polynomials.
for m in range(3,20):
    for t in [F(0),F(1,20),F(1,3),F(1,2),F(3,4),F(1)]:
        val=beta_polynomial(m,t)
        check(lower(m)<=val<=upper(m),f'interval monotonicity m={m}, t={t}')
        if F(0)<t<F(1):
            check(lower(m)<val<upper(m),f'strict interior m={m}, t={t}')

# Generic complex matrices: F=U+iV, integrate |F|^{2m} exactly.
# Cross-term factors of two follow from x^T A x.
def real_q(mat):
    p={}
    for i in range(3):
        for j in range(i,3):
            e=[0,0,0];e[i]+=1;e[j]+=1
            v=F(mat[i][j])*(1 if i==j else 2)
            if v:p[tuple(e)]=v
    return p

def complex_ratio(matA,matB,m):
    U=real_q(matA); V=real_q(matB)
    mass=add(mul(U,U),mul(V,V))
    return integrate(power(mass,m)),integrate(mass)

samples=[
 ([[1,2,0],[2,-1,1],[0,1,0]], [[0,0,1],[0,2,-1],[1,-1,-2]]),
 ([[2,1,1],[1,-1,0],[1,0,-1]], [[-1,0,2],[0,0,0],[2,0,1]]),
 ([[1,0,0],[0,1,0],[0,0,-2]], [[2,0,0],[0,-1,0],[0,0,-1]]),
 ([[0,1,0],[1,0,0],[0,0,0]], [[1,0,1],[0,-1,0],[1,0,0]]),
]
for A,B in samples:
    check(sum(A[i][i] for i in range(3))==0 and sum(B[i][i] for i in range(3))==0,'traceless matrices')
    for m in (3,4,5):
        value,norm=complex_ratio(A,B,m)
        check(value<=upper(m)*(norm**m),f'complex bound m={m}')

# Equality examples, with complex global phase and real biaxial minima.
for m in range(3,11):
    a=(2,-1,-1); b=(1,0,-1)
    check(integrate(power(qpoly(a),2*m))==upper(m)*integrate(power(qpoly(a),2))**m,'uniaxial')
    check(integrate(power(qpoly(b),2*m))==lower(m)*integrate(power(qpoly(b),2))**m,'biaxial')

print(f'PASS: {ASSERTIONS} exact rational assertions; m=1..19; real and complex checks.')
print('R_3(delta)=(5625+1000 delta)/1001.')
print('All finite checks support, but do not replace, the all-order proof.')
