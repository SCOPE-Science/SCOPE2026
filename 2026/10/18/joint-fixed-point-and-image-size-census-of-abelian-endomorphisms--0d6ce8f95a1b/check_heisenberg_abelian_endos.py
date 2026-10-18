"""Independent finite-field checks of abelian fixed-point-free endomorphism counts.

Run with Python 3.9 or newer. No external dependencies.
"""
from itertools import product
from fractions import Fraction
from math import prod


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    ans = Fraction(1)
    for i in range(k):
        ans *= Fraction(q**(n-i)-1, q**(k-i)-1)
    return int(ans)


def isotropic_count(n, r, q):
    ans = Fraction(1)
    for i in range(r):
        ans *= Fraction(q**(2*n-2*i)-1, q**(r-i)-1)
    return int(ans)


def predicted_X(n, r, s, q):
    N = 2*n
    return sum((-1)**(t-s) * q**((t-s)*(t-s-1)//2) * gaussian(t,s,q) *
               gaussian(r,t,q) * q**(t*(N-t)) *
               prod(q**(N-t)-q**i for i in range(r-t))
               for t in range(s,r+1))


def predicted_F(n,r,q):
    return predicted_X(n,r,0,q)


def rank(matrix, p):
    if not matrix:
        return 0
    x = [list(row) for row in matrix]
    m, n = len(x), len(x[0]); j = 0
    for i in range(m):
        while j < n and not any(x[k][j] % p for k in range(i,m)):
            j += 1
        if j == n: return i
        k = next(k for k in range(i,m) if x[k][j] % p)
        x[i],x[k] = x[k],x[i]
        inv = pow(x[i][j] % p, -1, p)
        x[i] = [inv*u % p for u in x[i]]
        for k in range(m):
            if k != i:
                f = x[k][j]
                x[k] = [(a-f*b)%p for a,b in zip(x[k],x[i])]
        j += 1
    return m


def sympl(a,b,n,p):
    return sum(a[i]*b[n+i]-a[n+i]*b[i] for i in range(n)) % p


def direct_fixed_lagrangian(n,r,p):
    N=2*n; ans=[0]*(r+1)
    # Image lies in span of the first r standard e vectors.
    for digits in product(range(p), repeat=r*N):
        B = [digits[i*N:(i+1)*N] for i in range(r)]
        if rank(B,p) != r:
            continue
        s=r-rank([[(1 if i==j else 0)-B[i][j] for j in range(r)] for i in range(r)],p)
        ans[s]+=1
    return ans


def rref_tuple(rows,p):
    x=[list(row) for row in rows]
    n=len(x[0]); i=0
    for j in range(n):
        k=next((k for k in range(i,len(x)) if x[k][j] % p),None)
        if k is None:continue
        x[i],x[k]=x[k],x[i]
        inv=pow(x[i][j] % p,-1,p)
        x[i]=[inv*z%p for z in x[i]]
        for k in range(len(x)):
            if k!=i:
                f=x[k][j]
                x[k]=[(a-f*b)%p for a,b in zip(x[k],x[i])]
        i+=1
        if i==len(x):break
    return tuple(tuple(row) for row in x)


def count_lagrangian_planes(p):
    vs=[v for v in product(range(p),repeat=4) if any(v)]
    isotropic=set()
    for a in vs:
        for b in vs:
            if sympl(a,b,2,p)==0 and rank([a,b],p)==2:
                isotropic.add(rref_tuple([a,b],p))
    return len(isotropic)


def n1_bruteforce(p):
    tally={(r,s):0 for r in (0,1) for s in range(r+1)}
    # A arbitrary 2x2, image isotropic exactly det A=0; no fixed vectors iff det(I-A) !=0.
    for a,b,c,d in product(range(p),repeat=4):
        if (a*d-b*c)%p !=0:continue
        r=0 if a==b==c==d==0 else 1
        s=2-rank([[(1-a)%p,(-b)%p],[(-c)%p,(1-d)%p]],p)
        tally[r,s]+=1
    for (r,s),count in tally.items():
        assert count==isotropic_count(1,r,p)*predicted_X(1,r,s,p),(p,r,s,count)
    return tally


def group_law(v,z,w,t,p):
    # For n=1 the symplectic form is v_0*w_1-v_1*w_0.
    return ((v[0]+w[0])%p,(v[1]+w[1])%p,(z+t+((v[0]*w[1]-v[1]*w[0])*pow(2,-1,p)))%p)


def group_hom_check(p):
    # Choose a nonzero rank-one map whose restriction to its image has eigenvalue 0.
    A=((0,1),(0,0)); ell=(1,2)
    def phi(g):
        x,y,z=g
        return ((A[0][0]*x+A[0][1]*y)%p,(A[1][0]*x+A[1][1]*y)%p,(ell[0]*x+ell[1]*y)%p)
    elems=list(product(range(p),repeat=3))
    for g in elems:
        assert phi(g)!=g or g==(0,0,0)
        for h in elems:
            lhs=phi(group_law(g[:2],g[2],h[:2],h[2],p))
            x=phi(g);y=phi(h)
            rhs=group_law(x[:2],x[2],y[:2],y[2],p)
            assert lhs==rhs
    return len(elems)**2


def main():
    for p in (3,5,7):
        t=n1_bruteforce(p)
        total=p**2*sum(c for (r,s),c in t.items() if s==0)
        assert total == p**5-2*p**3
        print('n=1 p=',p,'projected-ranks=',t,'group-endomorphisms=',total)
    assert group_hom_check(3)==729
    for p in (3,5):
        for r in (1,2):
            observed=direct_fixed_lagrangian(2,r,p)
            expected=[predicted_X(2,r,s,p) for s in range(r+1)]
            assert observed==expected,(p,r,observed,expected)
            print('n=2 p=',p,'image-rank=',r,'fixed-space-dimensional-strata=',observed)
    assert count_lagrangian_planes(3)==isotropic_count(2,2,3)==40
    print('ALL_FPF_AB_IMAGE_COUNTS_PASSED')

if __name__=='__main__':
    main()
