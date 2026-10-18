"""Reproduce finite checks for the circular-design outlier projection theorem.
Python 3 standard library only. Tests are finite consistency checks, not a proof
of the stated universal and asymptotic theorems.
"""
import math

PI = math.pi
CHECKS = 0

def close(a, b, tol=3e-10):
    global CHECKS
    if not abs(a-b) <= tol * max(1., abs(a), abs(b)):
        raise AssertionError((a,b,tol))
    CHECKS += 1

def inv3(a):
    """Gauss-Jordan inversion, independent of the low-rank hat formulas."""
    z = [list(map(float,row))+[float(i==j) for j in range(3)] for i,row in enumerate(a)]
    for p in range(3):
        q=max(range(p,3),key=lambda k:abs(z[k][p]))
        z[p],z[q] = z[q],z[p]
        pivot=z[p][p]
        if abs(pivot) < 1e-14: raise ArithmeticError('singular design')
        z[p]=[v/pivot for v in z[p]]
        for i in range(3):
            if i!=p:
                f=z[i][p]
                z[i]=[z[i][j]-f*z[p][j] for j in range(6)]
    return [row[3:] for row in z]

def direct_hat(n,r,phase):
    x = [[1.,math.cos(2*PI*j/n),math.sin(2*PI*j/n)] for j in range(n)]
    x.append([1.,r*math.cos(phase),r*math.sin(phase)])
    gram=[[sum(x[k][i]*x[k][j] for k in range(n+1)) for j in range(3)] for i in range(3)]
    iv=inv3(gram)
    return [[sum(x[i][p]*iv[p][q]*x[j][q] for p in range(3) for q in range(3)) for j in range(n+1)] for i in range(n+1)]

def outlier_norm(n,r,phase):
    return (1+2*r*r+sum(abs(1+2*r*math.cos(2*PI*j/n-phase)) for j in range(n)))/(n+1+2*r*r)

def mean_abs_cosine(r):
    if r<=.5: return 1.
    return (2/PI)*(math.sqrt(4*r*r-1)+math.asin(1/(2*r)))

def mean_abs_cosine_prime(r):
    assert r>.5
    return (4/PI)*math.sqrt(1-1/(4*r*r))

def optimize(n,phase):
    # Finite numerical search, not used in the mathematical proof.
    low,high=0.,3*math.sqrt(n)
    ratio=(math.sqrt(5)-1)/2
    x=high-ratio*(high-low);y=low+ratio*(high-low)
    fx=outlier_norm(n,x,phase);fy=outlier_norm(n,y,phase)
    for _ in range(105):
        if fx<fy:
            low=x;x=y;fx=fy;y=low+ratio*(high-low);fy=outlier_norm(n,y,phase)
        else:
            high=y;y=x;fy=fx;x=high-ratio*(high-low);fx=outlier_norm(n,x,phase)
    radius=(low+high)/2
    return radius,outlier_norm(n,radius,phase)

# Direct Gram-matrix inversions and full projection matrices.
for n in range(3,20):
    for phase in (0.,PI/(3*n),PI/7):
        for r in (0.,.4,.9,1.5,math.sqrt(n/2)+PI/4,3*math.sqrt(n)):
            h=direct_hat(n,r,phase)
            d=n+1+2*r*r
            for j in range(n):
                close(h[-1][j],(1+2*r*math.cos(2*PI*j/n-phase))/d)
                close(h[j][-1],h[-1][j])
            close(h[-1][-1],(1+2*r*r)/d)
            close(sum(abs(v) for v in h[-1]),outlier_norm(n,r,phase))
            for i in range(n):
                close(sum(h[i]),1.,1e-9)
                if sum(abs(v) for v in h[i])>math.sqrt(3*(n+1)/n)+1e-9:
                    raise AssertionError('ordinary row bound')
                CHECKS+=1
            for i in range(n+1):
                close(sum(h[i]),1.,1e-9)
                close(sum(h[i][j]*h[j][i] for j in range(n+1)),h[i][i],1e-9)

# Sharp circle-quadrature bounds, including shifted phases.
for n in (7,10,21,60,121,500):
    for phase in (0.,PI/(2*n),PI/17):
        for r in (.6,1.2,4.,math.sqrt(n/2),3*math.sqrt(n)):
            c=[math.cos(2*PI*j/n-phase) for j in range(n)]
            s=sum(abs(1+2*r*z) for z in c)
            assert abs(s-n*mean_abs_cosine(r))<=8*r+1e-7
            CHECKS+=1
            if r>=1.:
                sprime=sum(2*z*(1 if 1+2*r*z>0 else -1) for z in c)
                assert abs(sprime-n*mean_abs_cosine_prime(r))<=30.
                CHECKS+=1

# Optimal radius / maximal norm asymptotics, uniformly over outlier phase.
for n in (40,100,400,1000,3000):
    for phase in (0.,PI/(2*n),PI/7,2*PI/13):
        r, value=optimize(n,phase)
        correction=r-math.sqrt(n/2)-PI/4
        residue=value-(math.sqrt(2*n)/PI+.5)
        assert abs(correction)<4/math.sqrt(n)+.07,(n,phase,correction)
        assert abs(residue)<1.4/math.sqrt(n)+.018,(n,phase,residue)
        assert value>math.sqrt(3*(n+1)/n)
        CHECKS+=3
print('PASS:',CHECKS,'independent finite assertions')
