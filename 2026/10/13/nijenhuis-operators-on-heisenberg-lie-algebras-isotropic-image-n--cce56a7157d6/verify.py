"""Direct finite-field checks for a symplectic classification of Nijenhuis operators.
Standard-library only; Python 3.9+.
"""
from itertools import product
from collections import Counter
from math import prod


def rank(M,q):
    A=[list(x) for x in M]
    if not A: return 0
    rows, cols=len(A),len(A[0]); p=0
    for j in range(cols):
        k=next((k for k in range(p,rows) if A[k][j]%q),None)
        if k is None: continue
        A[p],A[k]=A[k],A[p]
        inv=pow(A[p][j]%q,-1,q)
        A[p]=[(x*inv)%q for x in A[p]]
        for i in range(rows):
            if i!=p:
                f=A[i][j]
                if f: A[i]=[(x-f*y)%q for x,y in zip(A[i],A[p])]
        p+=1
        if p==rows: break
    return p


def omega(v,w,m,q):
    return sum(v[i]*w[m+i]-v[m+i]*w[i] for i in range(m))%q


def iso_rank(S,m,q):
    n=2*m
    cols=list(zip(*S))
    for i in range(n):
        for j in range(i+1,n):
            if omega(cols[i],cols[j],m,q): return None
    return rank(S,q)


def gauss(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for i in range(k):
        a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b


def iso_subspaces(m,r,q):
    return gauss(m,r,q)*prod(q**(m-i)+1 for i in range(r))


def expected_S(m,q):
    n=2*m
    return {r:iso_subspaces(m,r,q)*prod(q**n-q**i for i in range(r)) for r in range(m+1)}


def check_S(m,q):
    n=2*m; cnt=Counter()
    for a in product(range(q),repeat=n*n):
        S=[a[i*n:(i+1)*n] for i in range(n)]
        r=iso_rank(S,m,q)
        if r is not None:cnt[r]+=1
    expect=expected_S(m,q)
    assert dict(cnt)==expect,(m,q,dict(cnt),expect)
    print('S_RANKS',m,q,dict(sorted(cnt.items())))
    return sum(cnt.values())


def bracket(u,v,m,q):
    return [0]*(2*m)+[omega(u,v,m,q)]


def matvec(N,v,q):
    return [sum(a*b for a,b in zip(row,v))%q for row in N]


def torsion_zero(N,m,q):
    n=2*m+1
    for i in range(n):
        e=[0]*n;e[i]=1
        Ne=matvec(N,e,q)
        for j in range(i+1,n):
            f=[0]*n;f[j]=1
            Nf=matvec(N,f,q)
            t=bracket(Ne,Nf,m,q)
            r=bracket(Ne,f,m,q)
            s=bracket(e,Nf,m,q)
            v=bracket(e,f,m,q)
            Nv=matvec(N,v,q)
            w=[(r[k]+s[k]-Nv[k])%q for k in range(n)]
            Nw=matvec(N,w,q)
            if t!=Nw:return False
    return True


def canonical(N,m,q):
    n=2*m
    d=N[n][n]
    if any(N[i][n] for i in range(n)):
        return False
    S=[[((N[i][j]-int(i==j)*d)%q) for j in range(n)] for i in range(n)]
    return iso_rank(S,m,q) is not None


def brute_m1(q):
    n=3; count=0; rank_counts=Counter()
    for x in product(range(q),repeat=9):
        N=[x[3*i:3*(i+1)] for i in range(3)]
        direct=torsion_zero(N,1,q)
        reduced=canonical(N,1,q)
        assert direct==reduced,(q,N,direct,reduced)
        if direct:count+=1
    expected=q**3*sum(expected_S(1,q).values())
    assert count==expected,(q,count,expected)
    print('NIJENHUIS_M1',q,count)


def sample(m,q):
    import random
    gen=random.Random(271828)
    n=2*m+1
    for _ in range(2500):
        N=[[gen.randrange(q) for _ in range(n)] for _ in range(n)]
        assert canonical(N,m,q)==torsion_zero(N,m,q)
    print('RANDOM_EQUIVALENCE',m,q,2500)


def main():
    for q in (2,3):brute_m1(q)
    for q in (2,3,5): check_S(1,q)
    check_S(2,2)
    for m,q in ((1,5),(2,2),(2,3),(3,2)):
        sample(m,q)
    print('VERIFY_OK')

if __name__=='__main__':main()
