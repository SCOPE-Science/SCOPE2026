"""Independent finite-field checks for derived-ideal-valued restricted Rota--Baxter operators.
Run: python3 verify.py.  No third-party dependencies.
"""
from itertools import product
from math import prod

def add(x,y,q): return (x^y) if q==4 else (x+y)%q
def neg(x,q): return x if q==4 else (-x)%q
def mul(x,y,q):
    if q!=4: return x*y%q
    r=0
    for _ in range(2):
        if y&1:r^=x
        y>>=1
        x<<=1
        if x&4:x^=7
    return r

def powq(x,k,q):
    y=1
    for _ in range(k):y=mul(y,x,q)
    return y

def matvec(S,v,q):return tuple(sum_field((mul(a,b,q) for a,b in zip(row,v)),q) for row in S)
def sum_field(items,q):
    s=0
    for x in items:s=add(s,x,q)
    return s

def iszero(x):return all(y==0 for y in x)

def rb_basis(u,S,T,q):
    n=len(u)
    # On (e,v_i), RHS R([e,R(v_i)]) and LHS zero.
    for i in range(n):
        ei=tuple(int(i==j) for j in range(n))
        z=matvec(S,ei,q)
        if not iszero(matvec(S,matvec(T,z,q),q)): return False
    return True

def restricted_direct(u,S,T,q,p):
    n=len(u)
    for x in product(range(q),repeat=n+1):
        v=x[1:]; t=x[0]
        Sv=matvec(S,v,q)
        Rx=tuple(add(mul(t,u[i],q),Sv[i],q) for i in range(n))
        # Iteratively form (ad_(Rx))^(p-1)(x) using original Lie brackets.
        curr_t,curr_v=t,v
        for _ in range(p-1):
            curr_v=tuple(neg(mul(curr_t,z,q),q) for z in matvec(T,Rx,q))
            curr_t=0
        lhs=matvec(S,curr_v,q)
        # The full restricted p-map on L sends every element of V to zero.
        # Consequently R(x)^[p] = 0, and the graph must be p-closed.
        if not iszero(lhs):return False
    return True

def rank(S,q):
    a=[list(row) for row in S];n=len(a); r=0
    for col in range(n):
        pivot=next((i for i in range(r,n) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=next(k for k in range(1,q) if mul(k,a[r][col],q)==1)
        a[r]=[mul(inv,z,q) for z in a[r]]
        for i in range(n):
            if i==r or a[i][col]==0:continue
            k=a[i][col]
            a[i]=[add(a[i][j],neg(mul(k,a[r][j],q),q),q) for j in range(n)]
        r+=1
    return r

def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k)) if k else 1

def gl(k,q):return prod(q**k-q**j for j in range(k))

def formula(n,q,p):
    ordinary=restricted=0
    for r in range(n//2+1):
        count=gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)
        ordinary+=count*q**n
        restricted+=count*q**(n-r if p==2 else n)
    return ordinary,restricted

def check(n,q,p,T_diag):
    T=tuple(tuple(T_diag[i] if i==j else 0 for j in range(n)) for i in range(n))
    # All eigenvalues must lie in F_p^* so T^p=T and T is invertible.
    assert all(1<=x<p for x in T_diag)
    ordinary=restricted=0
    by_rank={}
    for entries in product(range(q),repeat=n*n):
        S=tuple(tuple(entries[i*n+j] for j in range(n)) for i in range(n))
        for u in product(range(q),repeat=n):
            rb=rb_basis(u,S,T,q)
            # Independent direct basis computation + direct restricted graph p-th power.
            if rb:
                ordinary+=1
                is_restricted=restricted_direct(u,S,T,q,p)
                if is_restricted:
                    restricted+=1
                    r=rank(S,q)
                    by_rank[r]=by_rank.get(r,0)+1
    exp_o,exp_r=formula(n,q,p)
    assert (ordinary,restricted)==(exp_o,exp_r),(n,q,T_diag,ordinary,restricted,exp_o,exp_r)
    print('PASS',f'n={n}',f'q={q}',f'p={p}',f'T={T_diag}',f'ordinary={ordinary}',f'restricted={restricted}',f'rank_distribution={dict(sorted(by_rank.items()))}')

if __name__=='__main__':
    check(1,2,2,[1]);check(2,2,2,[1,1]);check(3,2,2,[1,1,1]);
    check(2,4,2,[1,1]);check(2,3,3,[1,2]);check(2,5,5,[1,2]);
    print('VERIFY_OK')
