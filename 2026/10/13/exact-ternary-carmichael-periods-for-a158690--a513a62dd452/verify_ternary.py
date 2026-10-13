"""Exact finite checks for the arithmetic congruence theorem (integer arithmetic)."""
from math import comb, factorial
from itertools import combinations

def exp_product_coefficients(N, mod):
    P=[1]+[0]*N
    a=[0]*(N+1)
    a[0]=1
    for m in range(1,N+1):
        d=2*m-1
        nxt=[0]*(N+1)
        for n in range(m,N+1):
            nxt[n]=sum(comb(n,k)*P[n-k]*(-1 if k%2==0 else 1)*pow(d,k,mod)
                       for k in range(1,n+1))%mod
        P=nxt
        for n in range(m,N+1):
            a[n]=(a[n]+P[n])%mod
    return a

def stirling_coefficients(N,mod):
    S=[[0]*(N+1) for _ in range(N+1)]
    S[0][0]=1
    for n in range(1,N+1):
        for k in range(1,n+1):
            S[n][k]=(k*S[n-1][k]+S[n-1][k-1])%mod
    fac=[factorial(k)%mod for k in range(N+1)]
    G=[0]*(N+1)
    a=[0]*(N+1);a[0]=1
    P=[1]+[0]*N
    for m in range(1,N+1):
        d=2*m-1
        F=[-comb(d,k) for k in range(1,min(N,d)+1)]
        nxt=[0]*(N+1)
        for i in range(m-1,N+1):
            if P[i]==0:continue
            for k in range(1,min(len(F),N-i)+1):
                nxt[i+k]=(nxt[i+k]+P[i]*F[k-1])%mod
        P=nxt
        for k in range(m,N+1):G[k]=(G[k]+P[k])%mod
    for n in range(1,N+1):
        a[n]=((-1)**n*sum(G[k]*fac[k]*S[n][k] for k in range(1,n+1)))%mod
    return a

def q3(k):
    if k%3==0:return 0
    return ((k*k-1)//3)%3

def shift_residue(parity):
    pieces=[]
    for m in range(1,8):
        d=[2*j-1 for j in range(1,m+1)]
        s=0
        for l in range(m+1):
            for chosen in combinations(d,l):
                v=sum(chosen)
                if v%3==0:continue
                s+=(-1)**(l+parity)*(v%3 if parity else 1)*q3(v)
        pieces.append(s%3)
    return pieces

def run(N=110,R=5):
    mod=3**R
    a=exp_product_coefficients(N,mod)
    b=stirling_coefficients(N,mod)
    assert a==b,(next((i for i in range(N+1) if a[i]!=b[i]),None))
    known=[1,1,5,55,1073,32671,1431665,85363615,6646603073,654896692351]
    assert a[:len(known)]==[v%mod for v in known]
    assert shift_residue(0)==[0,2,0,0,0,0,0]
    assert shift_residue(1)==[0,1,2,0,0,0,0]
    checks=0
    for r in range(1,R+1):
        q=3**r
        T=2*3**(r-1)
        for n in range(3*r,N-T+1):
            assert a[n+T]%q == a[n]%q,(r,n,'full')
            checks+=1
        if r==1:
            for n in range(3,N+1):
                assert a[n]%3==(-1)**(n+1)%3
                checks+=1
            continue
        h=2*3**(r-2)
        for n in range(3*r,N-h+1):
            expected=(2*3**(r-1)) if n%2==0 else 0
            assert (a[n+h]-a[n]-expected)%q==0,(r,n,'half',a[n+h],a[n],expected)
            checks+=1
    print(f'PASS: N={N}, modulus=3^{R}, two independent EGF algorithms, '
          f'shift congruence checks={checks}, derivative residues even={shift_residue(0)}, odd={shift_residue(1)};'
          ' general proof separate.')

if __name__=='__main__':run()
