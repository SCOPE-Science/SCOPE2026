"""Final consolidated verification: Monsky F2 ranks + Tunnell counts (stdlib only)."""
import math

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
phi = lambda s: 0 if s==1 else 1

def monsky_odd(primes):
    m=len(primes)
    D2=[[phi(legendre(2,p)) if i==j else 0 for j in range(m)] for i,p in enumerate(primes)]
    Dm2=[[phi(legendre(-2,p)) if i==j else 0 for j in range(m)] for i,p in enumerate(primes)]
    E=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i!=j: E[i][j]=phi(legendre(primes[j],primes[i]))
    for i in range(m): E[i][i]=sum(E[i][j] for j in range(m) if j!=i)%2
    N=2*m; M=[[0]*N for _ in range(N)]
    for i in range(m):
        for j in range(m):
            M[i][j]=D2[i][j]; M[i][j+m]=(E[i][j]+D2[i][j])%2
            M[i+m][j]=(E[i][j]+Dm2[i][j])%2; M[i+m][j+m]=D2[i][j]
    return M

def rank_f2(M):
    M=[r[:] for r in M]; n=len(M); m=len(M[0]); r=0
    for c in range(m):
        p=next((i for i in range(r,n) if M[i][c]==1),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(n):
            if i!=r and M[i][c]==1: M[i]=[(a+b)%2 for a,b in zip(M[i],M[r])]
        r+=1
    return r

def tunnell(n):
    A=sum(1 for x in range(-100,101) for y in range(-200,201) for z in range(-100,101) if 2*x*x+y*y+8*z*z==n)
    B=sum(1 for x in range(-100,101) for y in range(-200,201) for z in range(-100,101) if 2*x*x+y*y+32*z*z==n)
    return A,B

out=[]
for n,pr in [(51,[3,17]),(219,[3,73])]:
    M=monsky_odd(pr); rk=rank_f2(M); m=len(pr)
    s=2*m-rk; out.append(f"n={n}: rank(Mo)={rk} s={s} dimSel={s+2}")
    A,B=tunnell(n); out.append(f"n={n}: A(8z2)={A} B(32z2)={B} A-2B={A-2*B} Tunnell-cert-noncongruent={A!=2*B}")
# controls: known non-congruent n=1,3 (expect A!=2B); known congruent n=5,7 (expect A==2B)
for n in [1,3,5,7]:
    A,B=tunnell(n); out.append(f"control n={n}: A={A} B={B} A==2B -> {A==2*B}")
# Legendre table
for a,p in [(2,3),(2,17),(2,73),(-2,3),(-2,17),(-2,73),(17,3),(3,17),(73,3),(3,73)]:
    out.append(f"({a}/{p})={legendre(a,p)}")
print("\n".join(out))
open("output/artifacts/tables.txt","w").write("\n".join(out)+"\n")
