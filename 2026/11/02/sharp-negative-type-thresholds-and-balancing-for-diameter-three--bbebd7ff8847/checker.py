"""Supplementary finite checks for a double-star negative-type threshold.

Requires numpy; this script tests, but does not replace, the analytic proof.
No external files, network, or private dependencies are required.
"""
import math
import random
import numpy as np


def threshold(m, n):
    assert m >= 1 and n >= 1
    if m == n == 1:
        return 2.0
    upper = math.log2(2.0 + 2.0 / max(m, n))
    lo, hi = 1.0, upper
    for _ in range(90):
        mid = (lo + hi) / 2.0
        q = 2.0**mid
        F = 2.0 * 3.0**mid - 2.0 - q*q
        g = q * math.sqrt(max(0.0, (2+2/m-q)*(2+2/n-q)))
        if F > g:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2.0


def distance_matrix(m, n):
    # A leaves, first center, second center, B leaves.
    N = m+n+2
    edges = [(i,m) for i in range(m)]
    edges += [(m,m+1)]
    edges += [(m+1,j) for j in range(m+2,N)]
    D = np.full((N,N), 99, dtype=int)
    np.fill_diagonal(D, 0)
    for i,j in edges:
        D[i,j] = D[j,i] = 1
    for k in range(N):
        D = np.minimum(D, D[:,[k]]+D[[k],:])
    return D


def zero_sum_form_eigs(m,n,p):
    d=distance_matrix(m,n)
    powered=d.astype(float)**p
    B=np.vstack((np.eye(m+n+1),-np.ones((1,m+n+1))))
    return np.linalg.eigvalsh(-0.5 * B.T @ powered @ B)


checks=0
# Correctness of explicit three-coordinate quadratic decomposition.
rng=random.Random(1203)
for m in range(1,9):
    for n in range(1,9):
        D=distance_matrix(m,n)
        for p in (0.7,1.0,1.25,1.51,1.9):
            q,r=2**p,3**p
            for _ in range(3):
                a,b,z=[rng.uniform(-1,1) for _ in range(3)]
                ea=np.array([rng.uniform(-1,1) for _ in range(m)]);ea-=ea.mean()
                eb=np.array([rng.uniform(-1,1) for _ in range(n)]);eb-=eb.mean()
                v=np.r_[a/m+ea,z-a,-z-b,b/n+eb]
                lhs=v @ (D.astype(float)**p) @ v
                Q=(q-2-q/m)*a*a+(q-2-q/n)*b*b+2*(r+1-2*q)*a*b-2*z*z+2*(2-q)*(a-b)*z
                rhs=Q-q*(ea@ea+eb@eb)
                assert abs(lhs-rhs)<3e-10*(1+abs(lhs))
                checks+=1

# Threshold and inertia tests independent of the 2x2 matrix computation.
for m in range(1,11):
    for n in range(1,11):
        p=threshold(m,n)
        for p0,expected in [(min(0.95,p-.08),1), ((p+1)/2,1), (p,0), (p+.07,-1)]:
            ev=zero_sum_form_eigs(m,n,p0)
            if expected==1: assert ev.min()>1e-8, (m,n,p0,ev.min())
            elif expected==-1: assert ev.min()<-1e-8, (m,n,p0,ev.min())
            else: assert abs(ev.min()) < 1e-7, (m,n,p0,ev.min())
            checks+=1
        if m+n>2:
            q=2**p
            f=2*3**p-2-q*q
            g=q*math.sqrt(max(0,(2+2/m-q)*(2+2/n-q)))
            assert abs(f-g)<2e-10, (m,n,p,f,g)
            checks+=1

# At a fixed leaf budget balancing strictly raises the threshold.
for S in range(3,41):
    values=[threshold(m,S-m) for m in range(1,S//2+1)]
    assert all(x+1e-10<y for x,y in zip(values,values[1:])), (S,values)
    checks+=max(0,len(values)-1)

# Balanced closed relation and large-degree first-order coefficient.
for k in range(1,21):
    p=threshold(k,k)
    assert abs(3**p-(1+1/k)*2**p-1)<1e-9
    checks+=1
for k in [50,100,200,400,800]:
    p=threshold(k,k)
    coefficient=2/(3*math.log(3)-2*math.log(2))
    assert abs(k*(p-1)-coefficient)<0.06
    checks+=1
print(f"PASS: {checks} supplementary numerical assertions")
print("(m,n)=(1,3):", threshold(1,3))
print("(m,n)=(2,2):", threshold(2,2))
print("(m,n)=(3,3):", threshold(3,3))
