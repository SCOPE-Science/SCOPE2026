#!/usr/bin/env python3
"""Independent finite-size numerical diagnostics for path-map flip onset (not an infinite proof)."""
import math

def matvec(N, x):
    return [2*x[i]-(x[i-1] if i else 0)-(x[i+1] if i+1<N else 0) for i in range(N)]

def solve(A,b):
    M=[list(row)+[val] for row,val in zip(A,b)]
    n=len(M)
    for k in range(n):
        p=max(range(k,n), key=lambda j:abs(M[j][k]))
        M[k],M[p]=M[p],M[k]
        assert abs(M[k][k])>1e-15
        pivot=M[k][k]
        for j in range(k,n+1):M[k][j]/=pivot
        for i in range(n):
            if i==k:continue
            f=M[i][k]
            for j in range(k,n+1):M[i][j]-=f*M[k][j]
    return [M[i][-1] for i in range(n)]

def check(N,delta):
    lam=2+2*math.cos(math.pi/(N+1)); h=2/lam+delta
    v=[(-1)**i*math.sqrt(2/(N+1))*math.sin((i+1)*math.pi/(N+1)) for i in range(N)]
    S=sum(t**4 for t in v)
    root=math.sqrt(3*lam*delta/S)
    x=[root*t for t in v]
    for _ in range(40):
        val=[2*x[i]-h*w for i,w in enumerate(matvec(N,[math.sin(t) for t in x]))]
        jac=[]
        for i in range(N):
            row=[]
            for j in range(N):
                kij=(2 if i==j else -1 if abs(i-j)==1 else 0)
                row.append(2*(i==j)-h*kij*math.cos(x[j]))
            jac.append(row)
        change=solve(jac,val)
        x=[a-b for a,b in zip(x,change)]
        if max(map(abs,change))<1e-12:break
    residual=max(abs(2*x[i]-h*matvec(N,[math.sin(t) for t in x])[i]) for i in range(N))
    # Half orbit sends x to -x under F(x)=x-hK sin(x)
    image=[x[i]-h*matvec(N,[math.sin(t) for t in x])[i] for i in range(N)]
    assert residual<3e-11 and max(abs(image[i]+x[i]) for i in range(N))<3e-11
    assert min((1 if a*b>0 else -1) for a,b in zip(x,v))>0
    proj=sum(a*b for a,b in zip(x,v))
    scaled=proj/root
    assert abs(scaled-1)<0.006
    # Spectral stability of single-step DF=I-h K diag(cos x), tested via power iteration
    # Gershgorin alone is not enough, so use symmetric Jacobi iteration.
    d=[math.sqrt(math.cos(t)) for t in x]
    Q=[[float(i==j)-h*d[i]*(2 if i==j else -1 if abs(i-j)==1 else 0)*d[j] for j in range(N)] for i in range(N)]
    for sweep in range(100*N*N):
        p,q=max(((i,j) for i in range(N) for j in range(i+1,N)),key=lambda ij:abs(Q[ij[0]][ij[1]]),default=(0,0))
        if N==1 or abs(Q[p][q])<1e-12:break
        phi=0.5*math.atan2(2*Q[p][q],Q[q][q]-Q[p][p])
        c,s=math.cos(phi),math.sin(phi)
        app,aqq,apq=Q[p][p],Q[q][q],Q[p][q]
        Q[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        Q[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        Q[p][q]=Q[q][p]=(c*c-s*s)*apq+s*c*(app-aqq)
        for r in range(N):
            if r!=p and r!=q:
                ar,br=Q[r][p],Q[r][q]
                Q[r][p]=Q[p][r]=c*ar-s*br
                Q[r][q]=Q[q][r]=s*ar+c*br
    eig=[Q[i][i] for i in range(N)]
    assert max(map(abs,eig))<1-1e-8,(N,delta,eig)
    return max(abs(a) for a in x),proj/root, eig

if __name__=='__main__':
    nchecks=0
    for N in range(1,11):
        for delta in [0.00005,0.0002,0.0008]:
            a,b,eig=check(N,delta)
            print(f'N={N:2d} d={delta:.5g} maxabs={a:.9g} amplitude_ratio={b:.9g} max|multipliers|={max(map(abs,eig)):.9g}')
            nchecks+=1
    print(f'VERIFY_OK {nchecks} parameter cases; each root satisfies F(x)=-x and has all single-step multipliers inside unit disk.')
