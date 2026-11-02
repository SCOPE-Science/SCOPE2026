"""Standalone checks for a rank-one IMEX Euler Euclidean contractivity theorem.

Only the Python standard library is required. Analytical proof is in RESULT.md;
these computations check exact witnesses and deterministic numerical examples.
"""
from fractions import Fraction
from itertools import combinations
import math
import random


def eye(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def trans(A):
    return [list(z) for z in zip(*A)]


def mm(A, B):
    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def solve(A, b):
    n = len(A)
    T = [list(A[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(T[i][k]))
        T[k], T[p] = T[p], T[k]
        q = T[k][k]
        assert abs(q) > 1.e-16
        T[k] = [v/q for v in T[k]]
        for i in range(n):
            if i != k:
                v = T[i][k]
                T[i] = [a-v*b for a,b in zip(T[i],T[k])]
    return [row[-1] for row in T]


def inverse(A):
    n = len(A)
    return trans([solve(A,[float(i==j) for i in range(n)]) for j in range(n)])


def det(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))


def psd(A, tol=2.e-8):
    n=len(A)
    for k in range(1,n+1):
        for ix in combinations(range(n),k):
            minor=[[A[i][j] for j in ix] for i in ix]
            if det(minor) < -tol:
                return False
    return True


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def instance(B, rho, u, h):
    n=len(B)
    A=[[B[i][j]+rho*u[i]*u[j] for j in range(n)] for i in range(n)]
    S=[[float(i==j)+h*A[i][j] for j in range(n)] for i in range(n)]
    T=[[float(i==j)-h*B[i][j] for j in range(n)] for i in range(n)]
    M=mm(inverse(S),T)
    G=mm(M,trans(M))
    H=[[float(i==j)-G[i][j] for j in range(n)] for i in range(n)]
    return psd(H), M


def threshold(B,rho,u):
    alpha=dot(u,[dot(row,u) for row in B])
    x=solve(B,u)
    lam=alpha-1/dot(u,x)
    if lam < 0 and lam > -1e-10:
        lam=0.
    assert lam>=0
    k=2*lam/(2*alpha+rho)
    assert 0 <= k < 1
    if k<1e-12:
        return float('inf')
    delta=math.sqrt(1-k)
    return 4*delta/(rho*(1-delta))


def check_exact_rational_witness():
    F=Fraction
    B=[[F(1), F(0)], [F(0), F(9)]]
    A=[[F(2), F(1)], [F(1), F(10)]]
    h=F(5)
    A2=[[sum(A[i][k]*A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    B2=[[sum(B[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    H=[[2*(A[i][j]+B[i][j])+h*(A2[i][j]-B2[i][j]) for j in range(2)] for i in range(2)]
    assert H == [[F(26),F(62)],[F(62),F(138)]]
    assert H[0][0]*H[1][1]-H[0][1]*H[1][0]==-256
    u=[1/math.sqrt(2)]*2
    hstar=threshold([[1.,0.],[0.,9.]],2.,u)
    expected=2*math.sqrt(7/15)/(1-math.sqrt(7/15))
    assert math.isclose(hstar,expected,rel_tol=1e-12)
    assert instance([[1.,0.],[0.,9.]],2.,u,4.)[0]
    assert not instance([[1.,0.],[0.,9.]],2.,u,5.)[0]
    return hstar


def check_randomized():
    rng=random.Random(20261027)
    count=0
    for n in [2,3,4]:
        for z in range(160):
            C=[[rng.uniform(-1.,1.) for j in range(n)] for i in range(n)]
            B=mm(trans(C),C)
            for i in range(n):
                B[i][i] += rng.uniform(.5,2.)
            u=[rng.uniform(-1.,1.) for i in range(n)]
            norm=math.sqrt(dot(u,u));u=[x/norm for x in u]
            rho=rng.uniform(.2,3.)
            hc=threshold(B,rho,u)
            alpha=dot(u,[dot(row,u) for row in B])
            gap=alpha-1/dot(u,solve(B,u))
            k=2*gap/(2*alpha+rho)
            if k < .025 or hc > 1.e4:
                continue
            assert math.isfinite(hc) and hc>0
            for factor,expected in [(0.3,True),(0.7,True),(1.3,False),(2.,False)]:
                h=hc*factor
                got,_=instance(B,rho,u,h)
                assert got==expected,(n,z,hc,factor,got,expected)
                count+=1
    return count


def check_small_angle():
    B=[[1.,0.],[0.,9.]]
    rho=2.
    results=[]
    for theta in [.04,.02,.01]:
        u=[math.cos(theta),math.sin(theta)]
        hstar=threshold(B,rho,u)
        asymptotic=4*9*(2*1+rho)/(rho*(9-1)**2*theta**2)
        ratio=hstar/asymptotic
        assert abs(ratio-1)<.003
        results.append(ratio)
    return results


if __name__=='__main__':
    hc=check_exact_rational_witness()
    n=check_randomized()
    ratios=check_small_angle()
    print('VERIFY_OK exact_witness_det=-256 cutoff=%.12f randomized_cases=%d angle_ratios=%s'%
          (hc,n,','.join('%.7f'%q for q in ratios)))
