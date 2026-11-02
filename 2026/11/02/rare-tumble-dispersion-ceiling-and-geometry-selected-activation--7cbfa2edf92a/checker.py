#!/usr/bin/env python3
"""Reproduce finite checks of periodic rocking-diffusion identities.
All code uses only the Python standard library. These are diagnostics,
not a substitute for the analytic proof of the infinite-time limits.
"""
import math


def triangle(x, L, a, h):
    x = x % L
    return h*x/a if x<a else h*(L-x)/(L-a)


def drift(F, D, L, U, steps=360):
    dx=L/steps
    acc=0.0
    for j in range(steps):
        x=(j+.5)*dx
        ux=U(x)
        for k in range(steps):
            s=(k+.5)*dx
            acc+=math.exp((U(x+s)-ux-F*s)/D)
    integ=acc*dx*dx
    return -D*L*math.expm1(-F*L/D)/integ


def linear_solve(A, b):
    n=len(b);A=[list(row) for row in A];b=list(b)
    for k in range(n):
        p=max(range(k,n),key=lambda j:abs(A[j][k]))
        if abs(A[p][k])<1e-13: raise AssertionError('singular')
        A[p],A[k]=A[k],A[p];b[p],b[k]=b[k],b[p]
        ak=A[k];pivot=ak[k]
        for j in range(k+1,n):
            t=A[j][k]/pivot
            if t:
                A[j][k]=0.
                for l in range(k+1,n): A[j][l]-=t*ak[l]
                b[j]-=t*b[k]
    z=[0.]*n
    for k in range(n-1,-1,-1):
        z[k]=(b[k]-sum(A[k][j]*z[j] for j in range(k+1,n)))/A[k][k]
    return z


def finite_generator_diffusivity(gamma,D=.7,amp=.5,v=1.,L=2*math.pi,M=44):
    dx=L/M;n=2*M;A=[[0.]*n for _ in range(n)]
    b=[0.]*n;rp=[0.]*n;rm=[0.]*n
    for sig in range(2):
        F=v if sig==0 else -v
        for j in range(M):
            i=sig*M+j
            b[i]=F-amp*math.cos((j+.5)*dx)
            rp[i]=D/dx**2+b[i]/(2*dx)
            rm[i]=D/dx**2-b[i]/(2*dx)
            assert min(rp[i],rm[i])>0
            A[i][sig*M+(j+1)%M]+=rp[i]
            A[i][sig*M+(j-1)%M]+=rm[i]
            A[i][(1-sig)*M+j]+=gamma
            A[i][i]-=rp[i]+rm[i]+gamma
    AT=[[A[i][j] for i in range(n)] for j in range(n)]
    AT[0]=[1.]*n;rhs=[0.]*n;rhs[0]=1.
    pi=linear_solve(AT,rhs)
    assert abs(sum(pi)-1)<1e-8 and min(pi)>0
    mean=sum(pi[i]*b[i] for i in range(n))
    B=[list(row) for row in A];B[0]=list(pi)
    rhs=[mean-b[i] for i in range(n)];rhs[0]=0.
    phi=linear_solve(B,rhs)
    qv=0.
    for sig in range(2):
        for j in range(M):
            i=sig*M+j; ip=sig*M+(j+1)%M; im=sig*M+(j-1)%M; other=(1-sig)*M+j
            qv+=pi[i]*(rp[i]*(dx+phi[ip]-phi[i])**2
                       +rm[i]*(-dx+phi[im]-phi[i])**2
                       +gamma*(phi[other]-phi[i])**2)
    return qv/2,mean


def verify():
    checks=0
    L=1.;h=1.;v=.5;a=.6
    for D in [.05,.08,.1,.2,1.,3.]:
        for b in [.4,.5,.6]:
            U=lambda x,b=b:triangle(x,L,b,h)
            p=drift(v,D,L,U)
            m=drift(-v,D,L,U)
            assert 0<p<v and -v<m<0
            assert 0<(p-m)**2/8<v*v/2
            checks+=4
    # Analytical cusp-Laplace amplitude and its geometry-dependent barrier.
    for a in [.4,.5,.6]:
        s1=h/a; s2=h/(L-a)
        Bp=1/(s1-v)+1/(s2+v)
        Bm=1/(s1+v)+1/(s2-v)
        D=.055
        U=lambda x:triangle(x,L,a,h)
        p=drift(v,D,L,U,steps=750)
        m=drift(-v,D,L,U,steps=750)
        pp=L*math.exp(-(h-v*a)/D)/(D*Bp*Bp)
        mm=-L*math.exp(-(h-v*(L-a))/D)/(D*Bm*Bm)
        assert abs(p/pp-1)<.025,(a,p,pp)
        assert abs(m/mm-1)<.025,(a,m,mm)
        checks+=2
    # For a flat landscape the full finite-rate law is D + v**2/(2*gamma).
    for gamma in [.1,.4,1.]:
        deff,mean=finite_generator_diffusivity(gamma,D=.7,amp=0.,v=1.)
        assert abs(deff-(.7+1/(2*gamma)))<1e-8
        assert abs(mean)<1e-8
        checks+=2
    # Check an independent finite-state winding-martingale discretization.
    D=.7;amp=.5;v=1.;L=2*math.pi
    U=lambda x:amp*math.sin(x)
    p=drift(v,D,L,U,steps=600)
    m=drift(-v,D,L,U,steps=600)
    K=(p-m)**2/8
    errors=[]
    for gamma in [.25,.125,.0625,.03125]:
        deff,velocity=finite_generator_diffusivity(gamma,D,amp,v,L)
        rel=abs(gamma*deff/K-1)
        assert abs(velocity)<1e-8
        errors.append(rel)
        checks+=2
    assert errors[-1]<.1 and all(errors[j+1]<errors[j] for j in range(len(errors)-1)),errors
    checks+=1
    print('PASS',checks,'diagnostic assertions. Small-gamma scaled error:',errors,
          'asymptotic K:',K)


if __name__=='__main__':verify()
