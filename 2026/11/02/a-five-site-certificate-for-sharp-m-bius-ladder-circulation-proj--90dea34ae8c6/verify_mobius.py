#!/usr/bin/env python3
"""Exact-rational checks of antipodal ladder projection and dual certificate.
No third-party dependencies; analytic arguments for all integers are in RESULT.md.
"""
from fractions import Fraction as F

def data(n):
    assert n >= 10
    a = F(1, 2*n)
    if n <= 16:
        q = (3 + 22*a)/20
        u = F(1,2) - q
        x = [a,a,(3 - 58*a)/40]
        assert 0 <= x[2] <= a <= u
    else:
        u = F(1,5) + F(19,5)*a
        x = [F(3,20)-F(39,10)*a,a,a]
        assert a <= x[0] <= u
        q = F(1,2)-u
    assert F(1,2)-u == 2*sum(x)
    g = [F(0)]*n
    g[0] = -u
    for i in range(1,4):
        g[i] = -x[i-1]
        g[n-i] = x[i-1]
    return a,g

def formulas(n):
    a,g = data(n)
    S=[F(0)]*n
    for j in range(1,n): S[j]=S[j-1]+g[j]
    Rminus=[a-x for x in g]
    Rplus=[a+x for x in g]
    T=[g[0]-g[1]] + [g[i+1]-g[i] for i in range(1,n-1)]
    Z=[F(1,2)+g[0]+2*S[j] for j in range(n)]
    C=[1+2*g[0]]+g[1:]
    H=sum(abs(x)+abs(y) for x,y in zip(Rminus,Rplus))+2*abs(T[0])+sum(abs(x) for x in T[1:])
    V=2*sum(abs(z) for z in Z)+abs(C[0])+2*sum(abs(x) for x in C[1:])
    want = F(12,5)-F(16,5*n)
    assert H==want and V==want, (n,H,V,want)
    # Five-site signed supporting hyperplane; sign magnitudes <= absolute weights.
    s_minus=[4]*(n-2)+[0,-4]
    s_plus=[-4,-4,0]+[4]*(n-3)
    s_T=[-8]+[4 if i in (1,2,3,n-4,n-3,n-2) else 0 for i in range(1,n-1)]
    s_Z=[2 if j in (0,1,2,3,n-4,n-3,n-2,n-1) else (-2 if j==4 else 0) for j in range(n)]
    s_C=[1]+[-2 if i in (1,2,3,4) else (2 if i in (n-4,n-3,n-2,n-1) else 0) for i in range(1,n)]
    signed=(sum(s*x for s,x in zip(s_minus,Rminus))+
            sum(s*x for s,x in zip(s_plus,Rplus))+
            sum(s*x for s,x in zip(s_T,T))+
            sum(s*x for s,x in zip(s_Z,Z))+
            sum(s*x for s,x in zip(s_C,C)))
    assert signed==12-F(16,n), (n,signed)
    return H,V

def rotation(h,n,k):
    N=2*n
    out=[F(0)]*(3*n)
    for i in range(N):out[(i+k)%N]=h[i]
    for i in range(n):
        j=(i+k)%N
        if j<n:out[N+j]+=h[N+i]
        else:out[N+j-n]-=h[N+i]
    return out

def projection(n):
    N=2*n; E=3*n; a,g=data(n)
    h=[F(0)]*E
    h[0]=-(1-a+g[0])/2
    for i in range(1,n):h[i]=h[i-1]+a-g[i]
    for i in range(n,N):h[i]=-h[N-1-i]
    for i in range(n):h[N+i]=g[i]
    B=[[F(0)]*E for _ in range(N)]
    for i in range(N): B[i][i]=-1;B[(i+1)%N][i]=1
    for i in range(n):B[i][N+i]=-1;B[i+n][N+i]=1
    Kcols=[rotation(h,n,j) for j in range(N)]
    # P(e)=e-K(head)+K(tail)
    P=[[F(int(i==j)) for j in range(E)] for i in range(E)]
    for e in range(E):
        tail,head=(e,(e+1)%N) if e<N else (e-N,e-n)
        for row in range(E):P[row][e]+=Kcols[tail][row]-Kcols[head][row]
    # Range has zero divergence, and P acts as identity on ker B (via P^2=P).
    for v in range(N):
        for e in range(E):
            assert sum(B[v][j]*P[j][e] for j in range(E))==0, (n,'div',v,e)
    for i in range(E):
        for j in range(E):
            assert sum(P[i][k]*P[k][j] for k in range(E))==P[i][j],(n,'idemp',i,j)
    L=F(12,5)-F(16,5*n)
    assert all(sum(abs(P[i][j]) for i in range(E))==L for j in range(E))
    return L

if __name__=='__main__':
    for n in range(10,151):formulas(n)
    for n in range(10,19): projection(n)
    print('CHECK_OK rational_formula_orders=141 exact_matrix_projection_orders=9')
