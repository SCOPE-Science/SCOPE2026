from fractions import Fraction
from itertools import combinations


def ceil_frac(q):
    return -((-q.numerator) // q.denominator)


def profile_support(m,n,a,b,lam):
    if a == m and b == n:
        return None, None
    if a == m:
        return None, lam
    if b == n:
        return lam, None
    D = m*n - lam*lam*(m-a)*(n-b)
    x = (lam*m*b + lam*lam*a*(n-b))/D
    y = (lam*n*a + lam*lam*b*(m-a))/D
    return x,y


def formula(m,n,lam,tau):
    if tau > lam:
        return m+n
    if tau == lam:
        return min(m,n)
    vals=[]
    for a in range(m):
        cx = lam*m - lam*lam*a - tau*lam*lam*(m-a)
        cy = lam*lam*(m-a)*(1-tau)
        rx = n*(tau*(m-lam*lam*(m-a)) - lam*lam*a)/cx
        ry = n*(tau*(m-lam*lam*(m-a)) - lam*a)/cy
        b = min(n, max(0, ceil_frac(rx), ceil_frac(ry)))
        vals.append(a+b)
    vals.append(m) # all vertices of the m-side are sources
    return min(vals)


def brute_profiles(m,n,lam,tau):
    best=m+n
    pairs=[]
    for a in range(m+1):
        for b in range(n+1):
            x,y=profile_support(m,n,a,b,lam)
            ok=(x is None or x>=tau) and (y is None or y>=tau)
            if ok:
                s=a+b
                if s<best:
                    best=s; pairs=[(a,b)]
                elif s==best:
                    pairs.append((a,b))
    return best,pairs


def solve_fraction(A,b):
    n=len(A)
    if n==0: return []
    M=[list(A[i])+[b[i]] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c] != 0)
        M[c],M[p]=M[p],M[c]
        z=M[c][c]
        M[c]=[v/z for v in M[c]]
        for r in range(n):
            if r==c: continue
            z=M[r][c]
            if z:
                M[r]=[M[r][j]-z*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]


def direct_support(m,n,S,lam):
    N=m+n
    S=set(S)
    U=[v for v in range(N) if v not in S]
    idx={v:i for i,v in enumerate(U)}
    A=[[Fraction(int(i==j),1) for j in range(len(U))] for i in range(len(U))]
    rhs=[Fraction(0,1) for _ in U]
    for v in U:
        i=idx[v]
        if v < m:
            nbrs=range(m,m+n); deg=n
        else:
            nbrs=range(0,m); deg=m
        for w in nbrs:
            coeff=lam/Fraction(deg,1)
            if w in S: rhs[i]+=coeff
            else: A[i][idx[w]]-=coeff
    sol=solve_fraction(A,rhs)
    h=[Fraction(1,1) if v in S else sol[idx[v]] for v in range(N)]
    return h


def brute_subsets(m,n,lam,tau):
    N=m+n
    for k in range(N+1):
        for S in combinations(range(N),k):
            h=direct_support(m,n,S,lam)
            if min(h)>=tau:
                return k
    raise AssertionError('all-source set should be feasible')


def main():
    lambdas=[Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(4,5)]
    profile_cases=0
    for m in range(1,9):
        for n in range(1,9):
            for lam in lambdas:
                taus={Fraction(1,10),lam,lam/2,(lam+1)/2}
                for tau in sorted(t for t in taus if 0<t<=1):
                    f=formula(m,n,lam,tau)
                    b,_=brute_profiles(m,n,lam,tau)
                    assert f==b,(m,n,lam,tau,f,b)
                    profile_cases+=1

    subset_cases=0
    for m,n in [(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        for lam,tau in [
            (Fraction(1,2),Fraction(1,4)),
            (Fraction(2,3),Fraction(1,3)),
            (Fraction(3,4),Fraction(3,4)),
            (Fraction(3,4),Fraction(4,5)),
        ]:
            f=formula(m,n,lam,tau)
            b=brute_subsets(m,n,lam,tau)
            assert f==b,(m,n,lam,tau,f,b)
            subset_cases+=1

    f,pairs=brute_profiles(10,10,Fraction(3,5),Fraction(3,10))
    assert f==6 and pairs==[(3,3)],(f,pairs)
    print(f'ALL CHECKS PASSED; profile_cases={profile_cases}; subset_cases={subset_cases}; split_example=K10,10:(3,3)')

if __name__=='__main__':
    main()
