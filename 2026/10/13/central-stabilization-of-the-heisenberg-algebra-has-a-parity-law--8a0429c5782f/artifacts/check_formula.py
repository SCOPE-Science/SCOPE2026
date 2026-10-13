from itertools import combinations, product
from fractions import Fraction


def qbinom(n,k,q):
    if k<0 or k>n: return 0
    num=den=1
    for i in range(k):
        num*=q**(n-i)-1
        den*=q**(k-i)-1
    return num//den

def closed_counts(q,r):
    z=r+1
    G=sum(qbinom(z,j,q) for j in range(z+1))
    A=sum(qbinom(z,j,q)*q**j for j in range(z+1))
    B=sum(qbinom(r,j,q)*q**(2*j) for j in range(r+1))
    N=G+(q+1)*A+B
    J=Fraction(0,1)
    for h in range(r+1):
        n=r-h
        for a in range(n+1):
            for b in range(n-a+1):
                count=qbinom(r,h,q)*qbinom(n,a,q)*(q**(a*b))*qbinom(n-a,b,q)
                J += Fraction(count,q**h)
    S = Fraction(q**(2*z),1)*J
    bad = Fraction(q*(q+1),1)*S
    good = Fraction(N*N,1)-bad
    return N, good, Fraction(good,N*N)

def rref_subspaces(n,p):
    out=[]
    for k in range(n+1):
        for piv in combinations(range(n),k):
            piv=set(piv)
            slots=[]
            for i,pc in enumerate(sorted(piv)):
                for j in range(pc+1,n):
                    if j not in piv:
                        slots.append((i,j))
            for vals in product(range(p), repeat=len(slots)):
                rows=[[0]*n for _ in range(k)]
                for i,pc in enumerate(sorted(piv)):
                    rows[i][pc]=1
                for (i,j),v in zip(slots,vals): rows[i][j]=v
                out.append(tuple(tuple(x%p for x in row) for row in rows))
    return out

def rank(mat,p):
    a=[list(r) for r in mat if any(x%p for x in r)]
    if not a: return 0
    m=len(a); n=len(a[0]); rr=0
    for c in range(n):
        piv=next((i for i in range(rr,m) if a[i][c]%p),None)
        if piv is None: continue
        a[rr],a[piv]=a[piv],a[rr]
        inv=pow(a[rr][c]%p,-1,p)
        a[rr]=[(x*inv)%p for x in a[rr]]
        for i in range(m):
            if i!=rr and a[i][c]%p:
                t=a[i][c]%p
                a[i]=[(a[i][j]-t*a[rr][j])%p for j in range(n)]
        rr+=1
        if rr==m: break
    return rr

def contains(rows,v,p):
    return rank(rows,p)==rank(list(rows)+[tuple(v)],p)

def bracket(u,v,p):
    n=len(u)
    w=[0]*n
    w[2]=(u[0]*v[1]-u[1]*v[0])%p
    return tuple(w)

def is_subalg(rows,p):
    for u in rows:
        for v in rows:
            if not contains(rows,bracket(u,v,p),p): return False
    return True

def permutes(A,B,p):
    AB=tuple(A)+tuple(B)
    for u in A:
        for v in B:
            if not contains(AB,bracket(u,v,p),p): return False
    return True

def brute(q,r):
    # q prime in this brute checker
    n=r+3
    subs=[S for S in rref_subspaces(n,q) if is_subalg(S,q)]
    good=sum(1 for A in subs for B in subs if permutes(A,B,q))
    return len(subs),good,Fraction(good,len(subs)**2)

def main():
    cases=[(2,0),(3,0),(2,1),(3,1),(2,2)]
    for q,r in cases:
        c=closed_counts(q,r)
        b=brute(q,r)
        assert c==b,(q,r,c,b)
        print(f"q={q} r={r} N={c[0]} good={c[1]} sd={c[2]} OK")
    # known specializations
    q=5
    N,good,sd=closed_counts(q,0)
    expected=Fraction(3*q**3+12*q**2+16*q+16,(q**2+2*q+4)**2)
    assert sd==expected
    N,good,sd=closed_counts(q,1)
    expected=Fraction((2*q**3+4*q**2+3*q+5)**2-q**4*(q+1)*(3*q+1),(2*q**3+4*q**2+3*q+5)**2)
    assert sd==expected
    print("specializations r=0 and r=1 OK")
    print("CHECK_OK")

if __name__=='__main__': main()
