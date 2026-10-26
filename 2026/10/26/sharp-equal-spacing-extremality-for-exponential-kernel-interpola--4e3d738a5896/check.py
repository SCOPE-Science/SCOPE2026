"""Exact identities and numerical sanity tests for exponential-kernel Gram matrices.

Run: python check.py
Only the Python standard library is required. Finite checks supplement an analytical proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, sqrt


def product_kernel(a):
    n = len(a) + 1
    K = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = F(1)
        for j in range(i+1,n):
            p *= a[j-1]
            K[i][j] = K[j][i] = p
    return K


def precision(a):
    n = len(a) + 1
    q = [[F(0) for j in range(n)] for i in range(n)]
    q[0][0] = 1 / (1-a[0]*a[0])
    q[-1][-1] = 1 / (1-a[-1]*a[-1])
    for i in range(1, n-1):
        q[i][i] = 1 / (1-a[i-1]*a[i-1]) + a[i]*a[i] / (1-a[i]*a[i])
    for i,t in enumerate(a):
        q[i][i+1] = q[i+1][i] = -t / (1-t*t)
    return q


def matmul(A, B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def eigen_extremes(M):
    # Symmetric Jacobi eigenvalue algorithm; finite diagnostic, not a theorem.
    a=[[float(t) for t in row] for row in M]
    n=len(a)
    for _ in range(200*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        b=a[p][q]
        if abs(b)<2e-14:
            break
        t0=(a[q][q]-a[p][p])/(2*b)
        t=(1 if t0>=0 else -1)/(abs(t0)+sqrt(1+t0*t0))
        c=1/sqrt(1+t*t);s=t*c
        app=a[p][p];aqq=a[q][q]
        a[p][p]=app-t*b
        a[q][q]=aqq+t*b
        a[p][q]=a[q][p]=0.
        for k in range(n):
            if k!=p and k!=q:
                v=a[k][p];w=a[k][q]
                a[k][p]=a[p][k]=c*v-s*w
                a[k][q]=a[q][k]=s*v+c*w
    else:
        raise AssertionError('Jacobi eigensolver failed')
    d=[a[i][i] for i in range(n)]
    return min(d),max(d)


def main():
    count=0
    opts=[F(1,7),F(1,3),F(1,2),F(2,3),F(3,4)]
    for n in range(2,8):
        for k in range(90):
            a=[opts[(k+3*i*i+i)%len(opts)] for i in range(n-1)]
            K=product_kernel(a);Q=precision(a)
            assert matmul(K,Q)==[[F(int(i==j)) for j in range(n)] for i in range(n)]
            for j in range(n-1):
                b=a[:]
                b[j]=(a[j]+1)/2
                KB=product_kernel(b);QB=precision(b)
                assert all(KB[i][k]>=K[i][k] for i in range(n) for k in range(n))
                assert all((-1)**(i+k)*QB[i][k] >= (-1)**(i+k)*Q[i][k]
                           for i in range(n) for k in range(n))
                assert any(KB[i][k]>K[i][k] for i in range(n) for k in range(n))
                assert any(QB[i][i]>Q[i][i] for i in range(n))
                low,high=eigen_extremes(K)
                low2,high2=eigen_extremes(KB)
                assert high2>high+1e-10 and low2<low-1e-10
                count+=1
    for n in range(2,15):
        for r in (0.1,0.35,0.6,0.83):
            r0=F(str(r));T=product_kernel([r0]*(n-1))
            eiglo,eighi=eigen_extremes(T)
            bound=((1+r)/(1-r))**2
            assert eighi/eiglo<bound*(1+1e-11)
            if n==2:
                assert abs(eighi/eiglo-(1+r)/(1-r))<1e-11
            count+=1
    print('PASS: {} exact matrix/precision and spectral comparison configurations'.format(count))
    print('Boundary n=14, r=0.83: condition {:.8f} < asymptotic {:.8f}'.format(
        (lambda x: x[1]/x[0])(eigen_extremes(product_kernel([F(83,100)]*13))),((1+0.83)/(1-0.83))**2))


if __name__=='__main__':
    main()
