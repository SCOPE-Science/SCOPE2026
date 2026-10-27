"""Reproduce finite matrix checks for biharmonic kernels on triangle-free strongly regular graphs.
Only finite cases are checked; the general assertions require the accompanying proof.
"""
from fractions import Fraction as Q
from math import sqrt, exp, log

count = 0

def check(condition, msg):
    global count
    count += 1
    if not condition:
        raise AssertionError(msg)

def graphs():
    yield 'pentagon', [((i-j) % 5 in (1, 4)) for i in range(5) for j in range(5)], 5, 2, 1
    pairs = [(a, b) for a in range(5) for b in range(a+1, 5)]
    yield 'Petersen', [not set(pairs[i]) & set(pairs[j]) for i in range(10) for j in range(10)], 10, 3, 1
    S={1,2,4,8,15}
    yield 'Clebsch', [((i ^ j) in S) for i in range(16) for j in range(16)], 16, 5, 2

def mul(A, B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def matrix_power(M, p):
    n=len(M)
    R=identity(n)
    for _ in range(p):
        R=mul(R,M)
    return R

def run():
    global count
    for name, flat, n,k,mu in graphs():
        A=[[int(flat[i*n+j]) for j in range(n)] for i in range(n)]
        I=identity(n)
        check(n==1+k+k*(k-1)//mu, (name,'n formula'))
        for i in range(n):
            check(sum(A[i])==k,(name,'degree',i))
            for j in range(n):
                check(A[i][j]==A[j][i],(name,'symmetric',i,j))
                check(A[i][i]==0,(name,'loop',i))
        AA=mul(A,A)
        for i in range(n):
            for j in range(n):
                check(AA[i][j] == (k-mu)*I[i][j] - mu*A[i][j] + mu,(name,'SRG identity',i,j))
        L=[[k*I[i][j]-A[i][j] for j in range(n)] for i in range(n)]
        L2=mul(L,L)
        for i in range(n):
            for j in range(n):
                if i!=j and not A[i][j]:
                    check(L2[i][j] == mu,(name,'bi-Laplacian nonedge',i,j))
        d=sqrt(mu*mu+4*(k-mu))
        r=(-mu+d)/2;s=(-mu-d)/2
        alpha=lambda t:(r*exp(-(k-s)**2*t)-s*exp(-(k-r)**2*t))/d
        beta=lambda t:(exp(-(k-r)**2*t)-exp(-(k-s)**2*t))/d
        hh=lambda t:alpha(t)+k*beta(t)
        a=(k-r)**2;b=(k-s)**2
        tpk=log((k-r)*b/((k-s)*a))/(b-a)
        check(0<tpk<1,(name,'tpk'))
        check(hh(tpk)>1,(name,'positive bump'))
        low=tpk;high=3.
        for _ in range(60):
            mid=(low+high)/2
            if hh(mid)>1:low=mid
            else:high=mid
        ts=(low+high)/2
        check(ts>tpk,(name,'positivity cutoff'))
        for t in (0.001,0.01,0.03,0.1,0.2,ts,1.0):
            u=exp(-a*t);w=exp(-b*t)
            al=alpha(t);be=beta(t);ga=(1-al-k*be)/n
            T=[[al*I[i][j]+be*A[i][j]+ga for j in range(n)] for i in range(n)]
            for i in range(n):
                check(abs(sum(T[i])-1)<1.e-12,(name,'stochastic sum',i,t))
                check(T[i][i]>0,(name,'positive diagonal',i,t))
                for j in range(n):
                    if A[i][j]:
                        check(T[i][j]>0,(name,'positive neighbor',i,j,t))
                    if i!=j and not A[i][j]:
                        check(abs(T[i][j]-ga)<1.e-12,(name,'nonedge coefficient',i,j,t))
                norm=sum(abs(z) for z in T[i]);target=1+2*(n-k-1)/n*max(hh(t)-1,0)
                check(abs(norm-target)<1.e-11,(name,'sharp row sum',i,t,norm,target))
            # Independent spectral reconstruction: exact matrix polynomial projectors.
            P0=[[1/n for j in range(n)] for i in range(n)]
            Pr=[[(A[i][j]-s*I[i][j]-(k-s)/n)/d for j in range(n)] for i in range(n)]
            Ps=[[(r*I[i][j]-A[i][j]-(r-k)/n)/d for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    val=P0[i][j]+u*Pr[i][j]+w*Ps[i][j]
                    check(abs(T[i][j]-val)<1.e-12,(name,'spectral reconstruct',i,j,t))
        hprime=(b*(k-r)-a*(k-s))/d
        check(abs(hprime-n*mu)<1.e-10,(name,'initial h slope'))
        slope=2*(n-k-1)/n*hprime
        check(abs(slope-2*k*(k-1))<1.e-10,(name,'initial norm slope'))
    print(f'CHECKED {count} finite algebraic / floating comparison assertions')

if __name__=='__main__':
    run()
