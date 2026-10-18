"""Reproduce exact finite-grid and asymptotic checks for the cyclic-block rate law.
Python 3 standard library only; run: python3 verify.py
These finite tests support, but do not replace, the analytic theorem.
"""
from fractions import Fraction as F
from math import acosh, cosh, sinh, tanh, exp, isclose


def matmul(A, B):
    return [[sum(a * B[k][j] for k, a in enumerate(row))
             for j in range(len(B[0]))] for row in A]


def mv(A, v):
    return [sum(a * x for a, x in zip(row, v)) for row in A]


def inner(a, b):
    return sum(x*y for x, y in zip(a,b))


def inverse(A):
    n=len(A)
    z=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        row=next(j for j in range(k,n) if z[j][k])
        z[k],z[row]=z[row],z[k]
        pivot=z[k][k]
        z[k]=[x/pivot for x in z[k]]
        for i in range(n):
            if i==k: continue
            a=z[i][k]
            if a: z[i]=[x-a*y for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]


def cyclic_matrix(n,t):
    A=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        A[j][(j+1)%n]-=t
        A[(j+1)%n][j]-=t
    return A


def inverse_block(q,t):
    T=[[F(int(i==j))-(t if abs(i-j)==1 else F(0)) for j in range(q)] for i in range(q)]
    return inverse(T)


def embed_blocks(n,q,Tinv,p):
    B=[[F(0) for j in range(n)] for i in range(n)]
    for j,pj in enumerate(p):
        inds=[(j+k)%n for k in range(q)]
        for i in range(q):
            for k in range(q):
                B[inds[i]][inds[k]]+=pj*Tinv[i][k]
    return B


def rate(n,q,t):
    alpha=acosh(1/(2*float(t)))
    r=exp(-alpha)
    return (q-2*r*(-__import__('math').expm1(-q*alpha))/((1-r)*(1+r**(q+1))))/n

checks=0
for n in range(3,13):
    for q in range(1,n):
        for t in (F(1,10),F(1,4),F(2,5),F(49,100)):
            G=cyclic_matrix(n,t)
            H=inverse_block(q,t)
            ones=[F(1)]*n
            v=[sum(row) for row in H]
            s=sum(v)
            c=1-2*t
            target=c*s/n
            p=[F(1,n)]*n
            B=embed_blocks(n,q,H,p)
            P=matmul(B,G)
            M=[[F(int(i==j))-P[i][j] for j in range(n)] for i in range(n)]
            assert all(M[i][j]>=0 for i in range(n) for j in range(n))
            assert all(M[i][j]==M[j][i] for i in range(n) for j in range(n))
            assert all(sum(row)==1-target for row in M)
            assert isclose(float(target),rate(n,q,t),rel_tol=1e-11,abs_tol=1e-11)
            checks+=n*n+3
            # For any fixed distribution the constant Fourier mode has exactly the same energy loss.
            weights=[F(j+1,n*(n+1)//2) for j in range(n)]
            Bp=embed_blocks(n,q,H,weights)
            assert inner(ones,mv(matmul(G,matmul(Bp,G)),ones))/inner(ones,mv(G,ones))==target
            checks+=1
            # Check exact block minimization and energy-drop identity for a nonconstant vector.
            e=[F(2*i-n,3) for i in range(n)]
            inds=[k for k in range(q)]
            ge=mv(G,e)
            upd=mv(H,[ge[i] for i in inds])
            e1=list(e)
            for i in inds: e1[i]-=upd[i]
            loss=inner(e,mv(G,e))-inner(e1,mv(G,e1))
            assert loss==inner([ge[i] for i in inds],upd)
            assert loss>=0
            checks+=2
            if q==1: assert target==c/n;checks+=1
            if q==2: assert target==2*c/(n*(1-t));checks+=1
            if q==3: assert target==c*(3+4*t)/(n*(1-2*t*t));checks+=1

# Critical screened-Poisson block-length scaling: q*alpha tends to s.
for s in (0.1,0.7,2.,5.,12.):
    limit=1-2*tanh(s/2)/s
    assert 0<limit<1
    for q in (400,1600,6400):
        alpha=s/q
        ratio=1-sinh(q*alpha/2)/(q*sinh(alpha/2)*cosh((q+1)*alpha/2))
        assert abs(ratio-limit)<2*s/q
        checks+=2

# Boundary deficit for fixed t as q grows.
for t in (0.04,0.2,0.45):
    alpha=acosh(1/(2*t))
    r=exp(-alpha)
    limit=2*r/(1-r)
    q=150
    deficit=sinh(q*alpha/2)/(sinh(alpha/2)*cosh((q+1)*alpha/2))
    assert isclose(deficit,limit,rel_tol=1e-10,abs_tol=1e-10)
    checks+=1

print('PASS',checks,'exact-fraction matrix identity and asymptotic checks')
