#!/usr/bin/env python3
"""Numerical reproducibility for a Gaussian active harmonic lattice.
Standard-library-only independent Fourier, matrix and optimization checks.
All exact infinite-distance conclusions require the accompanying analytic proof.
"""
import math


def ensure(condition, desc):
    if not condition:
        raise AssertionError(desc)


def near(x, y, atol=1e-9, rtol=1e-8):
    return abs(x-y) <= atol + rtol*max(abs(x), abs(y))


def params(gamma, tau, omega, activity):
    return 1+gamma*tau+2*(omega*tau)**2, 2*(omega*tau)**2, activity


def laplacian_spectrum(A, B, a, t, q):
    return t + a/(A-B*math.cos(q))


def dft_matrix(n, symbol):
    return [[sum(symbol(2*math.pi*k/n)*math.cos(2*math.pi*k*(i-j)/n)
                 for k in range(n))/n for j in range(n)] for i in range(n)]


def inverse(m):
    n=len(m)
    b=[[float(m[i][j]) for j in range(n)] + [float(i==j) for j in range(n)]
       for i in range(n)]
    for j in range(n):
        k=max(range(j,n),key=lambda k:abs(b[k][j]))
        ensure(abs(b[k][j])>1e-12, 'singular finite covariance')
        b[j],b[k]=b[k],b[j]
        pivot=b[j][j]
        b[j]=[x/pivot for x in b[j]]
        for i in range(n):
            if i!=j:
                q=b[i][j]
                b[i]=[u-q*v for u,v in zip(b[i],b[j])]
    return [row[n:] for row in b]


def precision(A,B,a,t,n):
    if t==0:
        return A/a if n==0 else -B/(2*a) if n==1 else 0.0
    h=A+a/t
    delta=math.sqrt(h*h-B*B)
    r=B/(h+delta)
    return (1/t if n==0 else 0.0) - a/(t*t*delta)*r**n


def positive_partial(A,B,a,t,n):
    j0=precision(A,B,a,t,0)
    jn=precision(A,B,a,t,n)
    return -jn/j0


def critical_point(A,B,a,n):
    assert n>=2
    alpha=A/B
    r0=alpha-math.sqrt(alpha*alpha-1)
    def log_deriv(r):
        return ((n-1)/r - 1/(r0-r) - 1/(1/r0-r) + 1/(alpha-r))
    lo=r0*1e-12
    hi=r0*(1-1e-12)
    for _ in range(120):
        md=(lo+hi)/2
        if log_deriv(md)>0: lo=md
        else: hi=md
    r=(lo+hi)/2
    u=B/2*(r+1/r)-A
    return r,a/u


def lyapunov_mode_variance(gamma,tau,k,T,m,Ta):
    # Matrices for (position, velocity, active force divided by mass), k>0.
    # Active force acceleration has variance gamma*Ta/(m*tau).
    # (m gamma v0)^2/m^2 = gamma Ta/(m tau).
    p=1/tau
    M=[[0,1,0],[-k,-gamma,1],[0,0,-p]]
    Q=[[0,0,0],[0,2*gamma*T/m,0],[0,0,2*p*gamma*Ta/(m*tau)]]
    # Correction: stationary acceleration variance is gamma*Ta/(m*tau),
    # hence Q33 = 2/tau * gamma*Ta/(m*tau).
    vars_=[(i,j) for i in range(3) for j in range(i,3)]
    rows=[];rhs=[]
    for i,j in vars_:
        C=[]
        for h,l in vars_:
            E=[[0.0]*3 for _ in range(3)]
            E[h][l]=E[l][h]=1.0
            W=sum(M[i][s]*E[s][j]+E[i][s]*M[j][s] for s in range(3))
            C.append(W)
        rows.append(C);rhs.append(-Q[i][j])
    # Gaussian elimination for 6x6 inhomogeneous system.
    z=[rows[i][:]+[rhs[i]] for i in range(6)]
    for j in range(6):
        ii=max(range(j,6),key=lambda x:abs(z[x][j]))
        z[ii],z[j]=z[j],z[ii]
        ensure(abs(z[j][j])>1e-12,'Lyapunov matrix singular')
        c=z[j][j];z[j]=[p/c for p in z[j]]
        for i in range(6):
            if i!=j:
                c=z[i][j];z[i]=[p-c*q for p,q in zip(z[i],z[j])]
    return z[vars_.index((1,1))][-1]


def main():
    count=0
    def check(cond, why):
        nonlocal count
        ensure(cond,why)
        count+=1
    for gamma,tau,omega,m,Ta,T in [
        (1.0,1.0,1.0,1.0,1.0,0.7),
        (0.7,2.0,0.4,1.7,1.2,0.2),
        (3.3,0.6,2.1,0.5,0.3,2.8),
        (0.2,0.15,0.9,1.1,4.0,0.9)]:
        A,B,a=params(gamma,tau,omega,Ta/m)
        t=T/m
        for q in [0.1,0.37,1.0,2.4,math.pi]:
            k=4*omega*omega*math.sin(q/2)**2
            by_lyap=lyapunov_mode_variance(gamma,tau,k,T,m,Ta)
            expected=laplacian_spectrum(A,B,a,t,q)
            check(near(by_lyap,expected,rtol=5e-9),f'mode variance q={q}, {by_lyap} {expected}')
        for N in [7,11,18]:
            C=dft_matrix(N,lambda q:laplacian_spectrum(A,B,a,t,q))
            Ji=inverse(C)
            Jf=dft_matrix(N,lambda q:1/laplacian_spectrum(A,B,a,t,q))
            for i in range(N):
                for j in range(N):
                    check(near(Ji[i][j],Jf[i][j],atol=2e-10),f'finite inverse {N} ({i},{j})')
                    if i!=j and Jf[i][j]<-1e-11:
                        check(Ji[i][j]<0,f'nonlocal precision sign N={N}')
            # Cold-field nearest-neighbor precision on the periodic ring.
            C0=dft_matrix(N,lambda q:laplacian_spectrum(A,B,a,0,q))
            J0=inverse(C0)
            for i in range(N):
                for j in range(N):
                    d=min((i-j)%N,(j-i)%N)
                    check(near(J0[i][j],precision(A,B,a,0,d),atol=1e-9),f'cold Markov ring {N}')
        N=100
        Jf=dft_matrix(N,lambda q:1/laplacian_spectrum(A,B,a,t,q))
        for n in range(0,8):
            check(near(Jf[0][n],precision(A,B,a,t,n),atol=1e-8,rtol=3e-5),f'infinite Fourier coefficient {n}')
        alpha=A/B
        r0=alpha-math.sqrt(alpha*alpha-1)
        prev=0
        for n in [2,3,4,5,7,10,20,40,100]:
            r,tstar=critical_point(A,B,a,n)
            check(tstar>prev, 'unique optimizer should increase with distance')
            prev=tstar
            p=positive_partial(A,B,a,tstar,n)
            check(0<p<1, f'conditional correlation is valid at n={n}')
            for factor in [0.01,0.1,0.5,0.9,1.1,2.0,10.0,100.0]:
                check(p>positive_partial(A,B,a,tstar*factor,n),f'global optimum {n} factor {factor}')
        r100,t100=critical_point(A,B,a,100)
        check(abs(t100/100-a/math.sqrt(A*A-B*B))<0.015*a/math.sqrt(A*A-B*B), 'temperature slope n100')
        optimal=positive_partial(A,B,a,t100,100)
        asym=r0**100/(math.e*100)
        check(abs(optimal/asym-1)<0.02,'universal large-distance coefficient')
    print(f'PASSED {count} independent numerical and algebraic-reconstruction checks')

if __name__=='__main__':
    main()
