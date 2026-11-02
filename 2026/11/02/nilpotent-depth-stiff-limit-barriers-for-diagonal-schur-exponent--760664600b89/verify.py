"""Standalone arithmetic checks for two diagonal-split exponential integrators.

Run with Python 3.10 or later: python verify.py
Only Python's standard library is required.
The infinite stiff-limit and contraction claims are proved analytically in RESULT.md.
"""
import math

checks = 0

def assert_close(x, y, atol=2e-11, rtol=5e-11):
    global checks
    assert math.isfinite(x) and math.isfinite(y), (x, y)
    assert abs(x-y) <= atol + rtol*max(abs(x),abs(y)), (x,y)
    checks += 1

def identity(n):
    return [[float(i==j) for j in range(n)] for i in range(n)]

def zeros(n):
    return [[0.0 for j in range(n)] for i in range(n)]

def shift(n):
    return [[float(j==i+1) for j in range(n)] for i in range(n)]

def multiply(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def add_scaled(a,b,c):
    return [[a[i][j]+c*b[i][j] for j in range(len(a))] for i in range(len(a))]

def scaled(a,c):
    return [[c*v for v in row] for row in a]

def power(a,k):
    r=identity(len(a))
    for _ in range(k): r=multiply(r,a)
    return r

def maxdiff(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a)))

def matclose(a,b,atol=2e-10):
    global checks
    assert maxdiff(a,b)<atol,(maxdiff(a,b),a,b)
    checks+=1

def formulas(n,z,rho):
    j=shift(n); j2=multiply(j,j)
    a=math.exp(-z); p=-math.expm1(-z)
    u=p*p/z; v=p*(z-p)/z
    first=add_scaled(scaled(identity(n),a),j,rho*p)
    second=add_scaled(add_scaled(scaled(identity(n),a),j,rho*u),j2,rho*rho*v)
    exact=zeros(n); term=identity(n)
    for k in range(n):
        exact=add_scaled(exact,term,a)
        term=multiply(term,scaled(j,rho*z/(k+1)))
    return first,second,exact,(a,p,u,v)

def apply(m,v):
    return [sum(m[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]

def procedural_euler(n,z,rho):
    a=math.exp(-z); p=-math.expm1(-z)
    j=shift(n); zrho=z*rho
    phi1=p/z; phi2=(z-p)/(z*z)
    cols=[]
    for col in range(n):
        y=[float(i==col) for i in range(n)]
        Jy=apply(j,y)
        stage=[a*y[i]+zrho*phi1*Jy[i] for i in range(n)]
        Jstage=apply(j,stage)
        e1=stage
        e2=[a*y[i]+zrho*(phi1-phi2)*Jy[i]+zrho*phi2*Jstage[i] for i in range(n)]
        cols.append((e1,e2))
    return ([[cols[c][0][i] for c in range(n)] for i in range(n)],
            [[cols[c][1][i] for c in range(n)] for i in range(n)])

for n in range(1,10):
    for z in (0.05, 0.2, 0.8, 2.3, 9.5, 31.0):
        for rho in (0.15,0.5,0.9):
            e1,e2,exact,(a,p,u,v)=formulas(n,z,rho)
            p1,p2=procedural_euler(n,z,rho)
            matclose(e1,p1)
            matclose(e2,p2)
            assert_close(u+v,p)
            assert u>0 and v>0 and a>0 and p>0
            checks+=1
            for e in (e1,e2):
                assert all(x>=0 for row in e for x in row)
                assert max(sum(row) for row in e)<1+1e-12
                assert max(sum(e[i][j] for i in range(n)) for j in range(n))<1+1e-12
                checks+=3
            for k in (1,2,3):
                m=power(exact,k)
                x=scaled(identity(n),math.exp(-k*z))
                term=identity(n)
                for q in range(1,n):
                    term=multiply(term,scaled(shift(n),k*z*rho/q))
                    x=add_scaled(x,term,math.exp(-k*z))
                matclose(m,x,atol=3e-10)

# Exact limiting step maps and finite-horizon nilpotent cutoffs.
for n in range(1,11):
    for rho in (0.2, 0.5,0.9):
        e1,e2,exact,_=formulas(n,100000.0,rho)
        j=shift(n)
        matclose(e1,scaled(j,rho),atol=2e-5)
        matclose(e2,scaled(power(j,2),rho*rho),atol=2e-5)
        for k in (1,2,3,5,7):
            target1=scaled(power(j,k),rho**k)
            target2=scaled(power(j,2*k),rho**(2*k))
            matclose(power(e1,k),target1,atol=6e-5)
            matclose(power(e2,k),target2,atol=6e-5)
            assert max(abs(v) for row in target1 for v in row)==(rho**k if k<n else 0.0)
            assert max(abs(v) for row in target2 for v in row)==(rho**(2*k) if 2*k<n else 0.0)
            checks+=2

# For fixed stiffness the first method has O(z^2), the second O(z^3)
# one-step error at small dimensionless step z, before the stiff limit.
for n in (2,3,5):
    for rho in (0.2,0.7):
        e1,e2,exact,_=formulas(n,0.02,rho)
        ee1,ee2,exact2,_=formulas(n,0.01,rho)
        assert maxdiff(e1,exact)/maxdiff(ee1,exact2)>3.8
        checks+=1
        assert maxdiff(e2,exact)/maxdiff(ee2,exact2)>7.4
        checks+=1


# Finite checks for the precise leading algebraic residue when 2*k >= n,
# while k < n. These check matrix coefficients, not the infinite limit.
for n in range(2,10):
    for k in range((n+1)//2,n):
        m=2*k-n+1
        for rho in (0.2,0.6,0.9):
            e1,e2,exact,_=formulas(n,10000.0,rho)
            diff=add_scaled(power(e2,k),power(exact,k),-1.0)
            actual=diff[0][n-1]*(10000.0**m)
            predicted=math.comb(k,m)*(rho**(n-1))
            assert abs(actual-predicted) <= 0.005*predicted,(n,k,m,rho,actual,predicted)
            checks+=1

print('PASS:',checks,'deterministic arithmetic and structural checks')
