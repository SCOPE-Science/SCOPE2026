#!/usr/bin/env python3
import math


def jacobi_eigenvalues(A, tol=1e-13, max_iter=20000):
    A=[row[:] for row in A]
    n=len(A)
    for _ in range(max_iter):
        p=q=0; m=0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(A[i][j])>m:
                    m=abs(A[i][j]); p=i; q=j
        if m<tol:
            return sorted(A[i][i] for i in range(n))
        app,aqq,apq=A[p][p],A[q][q],A[p][q]
        phi=0.5*math.atan2(2.0*apq, aqq-app)
        c,s=math.cos(phi),math.sin(phi)
        for r in range(n):
            if r==p or r==q: continue
            arp,arq=A[r][p],A[r][q]
            A[r][p]=A[p][r]=c*arp-s*arq
            A[r][q]=A[q][r]=s*arp+c*arq
        A[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        A[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        A[p][q]=A[q][p]=0.0
    raise RuntimeError('Jacobi iteration did not converge')


def B_matrix(k, gaps):
    n=len(gaps); B=[[0.0]*n for _ in range(n)]
    for j,d in enumerate(gaps):
        th=k*d
        w=k/math.sin(th)
        c=k/math.tan(th)
        r=(j+1)%n
        B[j][j]-=c; B[r][r]-=c
        B[j][r]+=w; B[r][j]+=w
    return B


def lammax(k,gaps):
    return jacobi_eigenvalues(B_matrix(k,gaps))[-1]


def ground_root(gaps, alpha):
    lo=1e-11
    hi=min(math.pi/d for d in gaps)*(1.0-1e-10)
    assert lammax(lo,gaps)<alpha
    assert lammax(hi,gaps)>alpha
    for _ in range(90):
        mid=(lo+hi)/2
        if lammax(mid,gaps)<alpha: lo=mid
        else: hi=mid
    return (lo+hi)/2


def equidistant_root(n, alpha):
    lo=0.0; hi=0.5*n*(1.0-1e-12)
    def F(k): return 2*k*math.tan(math.pi*k/n)
    for _ in range(90):
        mid=(lo+hi)/2
        if F(mid)<alpha: lo=mid
        else: hi=mid
    return (lo+hi)/2


def mmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def monodromy(k,gaps,alpha):
    M=[[1.0,0.0],[0.0,1.0]]
    D=[[1.0,0.0],[alpha,1.0]]
    for d in gaps:
        P=[[math.cos(k*d), math.sin(k*d)/k],[-k*math.sin(k*d), math.cos(k*d)]]
        M=mmul(D,mmul(P,M))
    return M


def jensen_rhs(k,gaps):
    return 2*k/len(gaps)*sum(math.tan(0.5*k*d) for d in gaps)


def test_case(n,alpha,weights):
    L=2*math.pi
    s=sum(weights); gaps=[L*w/s for w in weights]
    k=ground_root(gaps,alpha)
    keq=equidistant_root(n,alpha)
    assert all(0<k*d<math.pi for d in gaps)
    M=monodromy(k,gaps,alpha)
    assert abs((M[0][0]+M[1][1])-2.0)<2e-8
    assert jensen_rhs(k,gaps)<=alpha+2e-9
    assert 2*k*math.tan(math.pi*k/n)<=alpha+2e-9
    unequal=max(gaps)-min(gaps)>1e-12
    if unequal:
        assert k<keq-1e-8
    assert abs(alpha-2*keq*math.tan(math.pi*keq/n))<2e-10


def main():
    cases={
      2:[1.0,1.7],
      3:[1.0,1.3,1.9],
      4:[0.8,1.1,1.4,2.0],
      5:[0.7,1.0,1.2,1.6,2.1],
      6:[0.9,1.0,1.15,1.35,1.7,2.2],
      7:[0.8,0.95,1.1,1.3,1.55,1.9,2.4],
    }
    for n,w in cases.items():
        for alpha in (0.08,0.7,3.0,25.0):
            test_case(n,alpha,w)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
