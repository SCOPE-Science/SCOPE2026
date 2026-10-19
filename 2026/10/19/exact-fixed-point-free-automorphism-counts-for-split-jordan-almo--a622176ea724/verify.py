"""Independent finite checks for a split-Jordan almost-abelian Lie algebra theorem.
Run with Python 3 and no third-party packages.
"""
from itertools import product
from fractions import Fraction


def ident(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matmul(A, B, p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) % p
                       for j in range(len(B[0]))) for i in range(len(A)))


def rank(A, p):
    if not A: return 0
    B=[list(row) for row in A]; n=len(B); m=len(B[0]); r=0
    for j in range(m):
        k=next((k for k in range(r,n) if B[k][j]%p),None)
        if k is None: continue
        B[r],B[k]=B[k],B[r]
        f=pow(B[r][j],-1,p)
        B[r]=[(x*f)%p for x in B[r]]
        for i in range(n):
            if i!=r:
                z=B[i][j]
                B[i]=[(x-z*y)%p for x,y in zip(B[i],B[r])]
        r+=1
        if r==n:break
    return r


def invertible(A,p): return rank(A,p)==len(A)
def nofixed(A,p):
    return rank(tuple(tuple((A[i][j] - (i==j))%p for j in range(len(A)))
                      for i in range(len(A))),p)==len(A)


def allmat(n,p):
    for x in product(range(p),repeat=n*n):
        yield tuple(tuple(x[i*n:(i+1)*n]) for i in range(n))


def gl(n,q):
    z=1
    for i in range(n): z*=q**n-q**i
    return z


def derangement(n,q):
    z=sum((Fraction((-1)**j*q**(j*(j-1)//2),gl(j,q)) for j in range(n+1)),Fraction(0))
    v=z*gl(n,q)
    assert v.denominator==1
    return int(v)


def hsize(part,q):
    d=sum(min(i,j)*a*b for i,a in part.items() for j,b in part.items())
    u=sum(a*a for a in part.values())
    z=q**(d-u)
    for a in part.values(): z*=gl(a,q)
    return z


def types_from_blocks(blocks):
    ty={}
    for lam,length in blocks:
        ty.setdefault(lam,{})[length]=ty.setdefault(lam,{}).get(length,0)+1
    return ty


def predicted(blocks,q):
    ty=types_from_blocks(blocks)
    n=sum(s for _,s in blocks)
    support=set(ty)
    group=[a for a in range(1,q) if all(ty.get((lam*pow(a,-1,q))%q)==typ for lam,typ in ty.items())]
    prodH=1
    for typ in ty.values():prodH*=hsize(typ,q)
    aut=q**n*len(group)*prodH
    fpf=Fraction(0)
    for a in group:
        if a==1:continue
        rem=set(support); rho=Fraction(1)
        while rem:
            lam=min(rem); cyc=[]; x=lam
            while x not in cyc:
                cyc.append(x); x=(x*pow(a,-1,q))%q
            for y in cyc:rem.remove(y)
            for m in ty[lam].values():rho*=Fraction(derangement(m,q),gl(m,q))
        fpf+=rho
    fpf*=q**n*prodH
    assert fpf.denominator==1
    return aut,int(fpf)


def jordan(blocks,q):
    n=sum(s for _,s in blocks)
    T=[[0]*n for _ in range(n)];j=0
    for lam,s in blocks:
        for i in range(s):
            T[j+i][j+i]=lam
            if i+1<s:T[j+i][j+i+1]=1
        j+=s
    return tuple(map(tuple,T))


def full_linear_count(blocks,q):
    T=jordan(blocks,q); n=len(T);N=n+1
    # Independently check multiplication on all basis pairs, without assuming block shape.
    brackets={}
    for i in range(N):
        for j in range(N):
            z=[0]*N
            if i==0 and j>0:
                for k in range(n):z[k+1]=T[k][j-1]
            elif j==0 and i>0:
                for k in range(n):z[k+1]=-T[k][i-1]
            brackets[i,j]=tuple(x%q for x in z)
    total=fpf=0
    for F in allmat(N,q):
        if not invertible(F,q):continue
        good=True
        for i in range(N):
            for j in range(N):
                lhs=tuple(sum(F[k][h]*brackets[i,j][h] for h in range(N))%q for k in range(N))
                rhs=tuple(sum(F[r][i]*F[s][j]*brackets[r,s][k]
                              for r in range(N) for s in range(N))%q for k in range(N))
                if lhs!=rhs:
                    good=False;break
            if not good:break
        if good:
            total+=1
            fpf+=nofixed(F,q)
    return total,fpf


def intertwiner_pairs(lam1,lam2,s,q):
    A=jordan([(lam1,s)],q);B=jordan([(lam2,s)],q)
    a=(lam1*pow(lam2,-1,q))%q
    assert a!=1
    X=[x for x in allmat(s,q) if invertible(x,q) and matmul(x,A,q)==tuple(tuple(a*v%q for v in row) for row in matmul(B,x,q))]
    Y=[y for y in allmat(s,q) if invertible(y,q) and matmul(y,B,q)==tuple(tuple(a*v%q for v in row) for row in matmul(A,y,q))]
    # Cyclic matrix S has off-diagonal blocks X and Y; its fixed points correspond to eigenvalue 1 of YX.
    return len(X),len(Y),sum(nofixed(matmul(y,x,q),q) for x in X for y in Y)


def centralizer_census(blocks,q):
    T=jordan(blocks,q); n=len(T)
    cent=[X for X in allmat(n,q) if matmul(X,T,q)==matmul(T,X,q) and invertible(X,q)]
    return len(cent),sum(nofixed(X,q) for X in cent)


def main():
    for blocks,q in [([(1,1),(2,1)],3), ([(1,1),(1,1)],3), ([(1,1),(2,1)],5), ([(1,1),(1,1)],2)]:
        assert full_linear_count(blocks,q)==predicted(blocks,q),(blocks,q)
        print('FULL_LIE_LINEAR_ENUMERATION',q,blocks,predicted(blocks,q),'OK')
    for blocks,q in [([(1,2)],3), ([(1,2),(1,1)],3), ([(1,1),(1,1)],3), ([(1,1),(1,1)],2)]:
        h,d=centralizer_census(blocks,q)
        typ=types_from_blocks(blocks)[1]
        want=hsize(typ,q)
        rho=Fraction(1)
        for m in typ.values():rho*=Fraction(derangement(m,q),gl(m,q))
        assert h==want and d==h*rho,(blocks,h,d,want,rho)
        print('CENTRALIZER_AND_EIGENFREE_ENUMERATION',q,blocks,h,d,'OK')
    for s in (1,2):
        x,y,free=intertwiner_pairs(1,2,s,3)
        expect=predicted([(1,s),(2,s)],3)
        assert x==y==hsize({s:1},3)
        assert expect[1]==3**(2*s)*free,(s,x,y,free,expect)
        print('JORDAN_ORBIT_INTERTWINERS',s,x,y,free,'OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
