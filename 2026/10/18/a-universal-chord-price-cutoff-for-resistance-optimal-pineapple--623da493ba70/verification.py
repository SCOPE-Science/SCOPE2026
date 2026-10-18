"""Standalone finite checks for priced pineapple resistance design.
Run: python3 verification.py (Python 3 standard library only).
The exact all-parameter theorem is proved in RESULT.md, not by these samples.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def inverse(matrix):
    n = len(matrix)
    augmented = [[F(matrix[i][j]) for j in range(n)] +
                 [F(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if augmented[r][col]), None)
        if pivot is None:
            raise ValueError('disconnected network')
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        value = augmented[col][col]
        augmented[col] = [x / value for x in augmented[col]]
        for row in range(n):
            if row != col:
                value = augmented[row][col]
                if value:
                    augmented[row] = [x - value*y for x, y in zip(augmented[row], augmented[col])]
    return [r[n:] for r in augmented]


def edges(k, m):
    E = [(0,i,'hub_core') for i in range(1,k+1)]
    E += [(i,j,'core') for i in range(1,k+1) for j in range(i+1,k+1)]
    E += [(0,i,'leaf') for i in range(k+1,k+m+1)]
    return E


def kirchhoff(k, m, weights):
    n = k+m+1
    E = edges(k,m)
    assert len(weights)==len(E)
    mat=[[F(0) for _ in range(n)] for __ in range(n)]
    for (i,j,_),w in zip(E,weights):
        w=F(w)
        mat[i][i]+=w;mat[j][j]+=w
        mat[i][j]-=w;mat[j][i]-=w
    inv=inverse([r[:-1] for r in mat[:-1]])
    ans=F(0)
    for i in range(n):
        for j in range(i+1,n):
            if j==n-1:
                ans+=inv[i][i]
            else:
                ans+=inv[i][i]+inv[j][j]-2*inv[i][j]
    return ans


def closed_kirchhoff(k,m,a,b,c):
    n=k+m+1
    return F(m*(n-1),1)/b + F(m+1,1)/a + F((k-1)*n,1)/(a+k*c)


def optimum(k,m,t,B=1.):
    n=k+m+1
    threshold=2*n/(n-1)
    if t>=threshold:
        s=B/(n-1)
        return s,s,0.,(n-1)**3/B
    beta=t*(k-1)/2
    alpha=k-beta
    assert alpha>0
    Z=m*sqrt(n-1)+sqrt((m+1)*alpha)+sqrt((k-1)*n*beta)
    a=B*sqrt((m+1)/alpha)/Z
    b=B*sqrt(n-1)/Z
    v=B*sqrt((k-1)*n/beta)/Z
    c=(v-a)/k
    return a,b,c,Z*Z/B


def run():
    rng=Random(26021016)
    checks=0
    # Reconstruct all pair resistances from exact rational matrices; no spectral
    # or orbit formulas are used in the matrix calculation.
    for k in range(2,6):
        for m in range(1,4):
            for trial in range(15):
                a=F(rng.randint(1,9),rng.randint(1,8))
                b=F(rng.randint(1,9),rng.randint(1,8))
                c=F(rng.randint(0,9),rng.randint(1,8))
                E=edges(k,m)
                w=[a if typ=='hub_core' else b if typ=='leaf' else c for _,_,typ in E]
                actual=kirchhoff(k,m,w)
                expected=closed_kirchhoff(k,m,a,b,c)
                assert actual==expected,(k,m,a,b,c,actual,expected)
                checks+=1
    for k in range(2,6):
        for m in range(1,4):
            n=k+m+1
            cut=F(2*n,n-1)
            prices=[F(1,4),F(1),F(2),cut-F(1,1000),cut,cut+F(1,1000),F(4)]
            for t in prices:
                a,b,c,val=optimum(k,m,float(t))
                assert a>0 and b>0 and c>=0
                assert isclose(k*a+m*b+float(t)*k*(k-1)*c/2,1.,abs_tol=1e-12)
                assert isclose(float(closed_kirchhoff(k,m,a,b,c)),val,rel_tol=1e-11)
                assert (c>0) == (t<cut)
                checks+=4
                if t>=cut:
                    assert isclose(a,b,rel_tol=1e-13)
                    assert isclose(val,(n-1)**3,rel_tol=1e-13)
                    # Budget-multiplier inequality at an inactive chord.
                    assert (n-1)*t >= 2*n
                    checks+=3
                else:
                    alpha=k-float(t)*(k-1)/2
                    beta=float(t)*(k-1)/2
                    v=a+k*c
                    assert isclose(m*(n-1)/b**2/m, (m+1)/a**2/alpha,rel_tol=1e-10)
                    assert isclose((m+1)/a**2/alpha, (k-1)*n/v**2/beta,rel_tol=1e-10)
                    checks+=2
            # Compare against unrestricted, independently non-symmetric weights:
            # this is corroboration, not a certificate of global optimality.
            for t in (F(1,2), F(1), cut, F(3)):
                best=optimum(k,m,float(t))[-1]
                E=edges(k,m)
                for trial in range(20):
                    raw=[F(rng.randint(1,18),rng.randint(1,10)) for _ in E]
                    budget=sum(w*(t if typ=='core' else 1) for (_,_,typ),w in zip(E,raw))
                    w=[x/budget for x in raw]
                    result=kirchhoff(k,m,w)
                    assert float(result)>=best-1e-8
                    checks+=1
    print(f'VERIFY_OK {checks} checks')

if __name__=='__main__':
    run()
