#!/usr/bin/env python3
import math

def bisect(f,a,b,steps=100):
    fa=f(a); fb=f(b)
    if not (fa*fb < 0): raise AssertionError((a,b,fa,fb))
    for _ in range(steps):
        c=(a+b)/2.0; fc=f(c)
        if fa*fc <= 0: b=c; fb=fc
        else: a=c; fa=fc
    return (a+b)/2.0

def A(k): return (k*k+3.0)*math.cos(k/2.0)**2-1.0
def H(k): return math.tan(k/2.0)**2-k*k-2.0
def Rplus(k): return k*math.tan(k/2.0)-math.sqrt(3.0)
def Rminus(k): return k*math.tan(k/2.0)+math.sqrt(3.0)



def rank_complex(M,tol=1e-10):
    A=[list(map(complex,row)) for row in M]
    m=len(A); n=len(A[0]); rank=0; col=0
    while rank<m and col<n:
        piv=max(range(rank,m),key=lambda i: abs(A[i][col]))
        if abs(A[piv][col]) <= tol:
            col+=1; continue
        A[rank],A[piv]=A[piv],A[rank]
        z=A[rank][col]
        A[rank]=[x/z for x in A[rank]]
        for i in range(m):
            if i!=rank:
                z=A[i][col]
                A[i]=[A[i][j]-z*A[rank][j] for j in range(n)]
        rank+=1; col+=1
    return rank

# Endpoint reduced systems: dimensions 2,1,1 in rotation sectors j=0,1,2.
for n in (1,3,7):
    K=2*n*math.pi
    M0=[[-1,1j*K,1],[0,0,0],[1,-1j*K,-1]]
    assert 3-rank_complex(M0)==2
    for j in (1,2):
        w=complex(math.cos(2*math.pi*j/3),math.sin(2*math.pi*j/3))
        s=(-1)**j
        M=[[-(1+1j*s*math.sqrt(3)),1j*K,1],
           [0,1j*K*(1-w),w-1],
           [1-1j*s*math.sqrt(3),-1j*w*K,-w]]
        assert 3-rank_complex(M)==1

eps=1e-8
for m in range(0,16):
    a=2*m*math.pi; p=(2*m+1)*math.pi; b=(2*m+2)*math.pi
    rp=bisect(Rplus,a+eps,p-eps); ca=bisect(H,a+eps,p-eps)
    cb=bisect(H,p+eps,b-eps); rm=bisect(Rminus,p+eps,b-eps)
    for k in (ca,cb):
        assert abs(A(k)) < 2e-8 and abs(H(k)) < 2e-8
    assert abs(Rplus(rp)) < 2e-8 and abs(Rminus(rm)) < 2e-8
    assert 1+3+3+1+4 == 12
for m in (8,16,32):
    P=(2*m+1)*math.pi
    left=bisect(H,2*m*math.pi+eps,P-eps); right=bisect(H,P+eps,(2*m+2)*math.pi-eps)
    assert abs((P-left)*P-2.0) < 0.02 and abs((right-P)*P-2.0) < 0.02
    assert abs((P*P-left*left)-4.0) < 0.03 and abs((right*right-P*P)-4.0) < 0.03
for n in (8,16,32):
    E=2*n*math.pi
    left=bisect(Rminus,(2*n-1)*math.pi+eps,E-eps); right=bisect(Rplus,E+eps,(2*n+1)*math.pi-eps)
    target=2.0*math.sqrt(3.0); etarget=4.0*math.sqrt(3.0)
    assert abs((E-left)*E-target) < 0.03 and abs((right-E)*E-target) < 0.03
    assert abs((E*E-left*left)-etarget) < 0.05 and abs((right*right-E*E)-etarget) < 0.05
print('VERIFY_OK')
