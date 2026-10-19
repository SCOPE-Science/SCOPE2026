"""Independently enumerate anti-commuting involutions of small Jordan matrices.

Run: python3 verify.py ; uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def gl(k,q):
    out=1
    for j in range(k): out*=q**k-q**j
    return out


def types(parts):
    counts=Counter(parts)
    sizes=sorted(counts)
    for choice in product(*(range(counts[s]+1) for s in sizes)):
        plus=dict(zip(sizes,choice))
        yield counts,plus


def formula(parts,q):
    ans=Counter()
    for m,a in types(parts):
        b={s:m[s]-a[s] for s in m}
        D=sum(m[i]*m[j]*min(i,j) for i in m for j in m)
        rho=sum(m[i]**2 for i in m)
        G=q**(D-rho)
        for i in m:G*=gl(m[i],q)
        E=0
        for i in m:
            for j in m:
                lower=max(0,j-i)
                for x in (0,1):
                    for y in (0,1):
                        num=sum(1 for e in range(lower,j) if e%2 == (x-y)%2)
                        E+= (a[i] if x==0 else b[i])*(a[j] if y==0 else b[j])*num
        rho0=sum(a[i]**2+b[i]**2 for i in m)
        H=q**(E-rho0)
        for i in m:H*=gl(a[i],q)*gl(b[i],q)
        assert G%H==0,(parts,q,a,G,H)
        rankplus=sum(a[i]*((i+1)//2)+b[i]*(i//2) for i in m)
        ans[rankplus]+=G//H
    return ans


def jordan(parts):
    n=sum(parts); N=[[0]*n for _ in range(n)]
    k=0
    for d in parts:
        for i in range(d-1):N[k+i][k+i+1]=1
        k+=d
    return N


def kernel_basis(A,q):
    A=[row[:] for row in A]
    nr=len(A); nc=len(A[0]); r=0; piv=[]
    for c in range(nc):
        pivot=next((j for j in range(r,nr) if A[j][c]%q),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c]%q,-1,q)
        A[r]=[(x*inv)%q for x in A[r]]
        for j in range(nr):
            if j!=r and A[j][c]%q:
                f=A[j][c]
                A[j]=[(v-f*w)%q for v,w in zip(A[j],A[r])]
        piv.append(c);r+=1
        if r==nr:break
    free=[c for c in range(nc) if c not in piv]
    out=[]
    for f in free:
        v=[0]*nc;v[f]=1
        for i,p in enumerate(piv):v[p]=(-A[i][f])%q
        out.append(v)
    return out


def enumerate_small(parts,q):
    n=sum(parts);N=jordan(parts);I=[[int(i==j) for j in range(n)] for i in range(n)]
    # Coefficient rows of S N + N S = 0 for row-major S entries
    C=[]
    for i in range(n):
        for j in range(n):
            row=[]
            for a in range(n):
                for b in range(n):
                    row.append((int(i==a)*N[b][j]+N[i][a]*int(j==b))%q)
            C.append(row)
    basis=kernel_basis(C,q)
    ans=Counter()
    for coeff in product(range(q),repeat=len(basis)):
        vec=[sum(c*b[k] for c,b in zip(coeff,basis))%q for k in range(n*n)]
        M=[vec[i*n:(i+1)*n] for i in range(n)]
        if any(sum(M[i][k]*M[k][j] for k in range(n))%q != I[i][j] for i in range(n) for j in range(n)):
            continue
        tr=sum(M[i][i] for i in range(n))%q
        # trace mod q need recover signed trace between -n and +n for q <= n: use rank(S+I), since + eigenspace = image (S+I)
        P=[[(M[i][j]+I[i][j])%q for j in range(n)] for i in range(n)]
        rank=n-len(kernel_basis(P,q))
        ans[rank]+=1
    return ans,len(basis)




def gf9_add(x,y):
    return (x%3+y%3)%3+3*((x//3+y//3)%3)

def gf9_mul(x,y):
    a,b=x%3,x//3; c,d=y%3,y//3
    return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)

def enumerate_gf9_2(parts):
    N=jordan(parts); n=2; result=Counter()
    for vals in product(range(9),repeat=4):
        S=[list(vals[:2]),list(vals[2:])]
        prod=lambda X,Y,i,j: gf9_add(gf9_mul(X[i][0],Y[0][j]),gf9_mul(X[i][1],Y[1][j]))
        if any(prod(S,S,i,j)!=int(i==j) for i in range(2) for j in range(2)):continue
        if any(gf9_add(prod(S,N,i,j),prod(N,S,i,j))!=0 for i in range(2) for j in range(2)):continue
        if S==[[1,0],[0,1]]:k=2
        elif S==[[2,0],[0,2]]:k=0
        else:k=1
        result[k]+=1
    return result

def main():
    cases=[([1],3),([2],3),([3],3),([1,1],3),([2,1],3),([1,1,1],3),([4],3),([3,1],3),([2,2],3),([3,2],3),([2,1],5)]
    for parts,q in cases:
        expected=formula(parts,q)
        actual,dim=enumerate_small(parts,q)
        assert expected==actual,(parts,q,expected,actual)
        print('PASS',parts,q,'equation-space-dimension',dim,'rank-plus',dict(sorted(expected.items())))
    for p in ([1,1],[2]):
        act=enumerate_gf9_2(p);exp=formula(p,9)
        assert act==exp,(p,exp,act)
        print('PASS_GF9',p,dict(sorted(act.items())))
    print('ALL_EXACT_CHECKS_PASSED',len(cases)+2)
if __name__=='__main__': main()
