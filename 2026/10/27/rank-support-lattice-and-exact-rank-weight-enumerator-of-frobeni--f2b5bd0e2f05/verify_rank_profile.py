"""Independent finite-field enumeration of Frobenius-consistent spectral rank supports.

No external data required. Uses prime-base finite fields in reproducibility cases;
the accompanying theorem applies to every prime-power base field.
"""
from itertools import product
from collections import Counter
from math import prod
import sympy as sp


def field(p, modulus):
    m = len(modulus) - 1
    order = p**m
    def digits(z):
        a=[]
        for _ in range(m):
            a.append(z%p); z//=p
        return a
    def encoded(a):
        return sum(int(v)*p**i for i,v in enumerate(a))
    vec=[digits(i) for i in range(order)]
    def mul(a,b):
        x=vec[a]; y=vec[b]; z=[0]*(2*m-1)
        for i in range(m):
            for j in range(m): z[i+j]=(z[i+j]+x[i]*y[j])%p
        for k in range(2*m-2,m-1,-1):
            v=z[k]
            if v:
                for j in range(m):z[k-m+j]=(z[k-m+j]-v*modulus[j])%p
        return encoded(z[:m])
    def power(a,e):
        b=1
        while e:
            if e&1:b=mul(b,a)
            a=mul(a,a); e//=2
        return b
    # Certificate field is indeed a field, via exhaustive inverse check.
    assert all(any(mul(a,b)==1 for b in range(1,order)) for a in range(1,order))
    return order,vec,power


def orbits(q,n):
    seen=set(); ans=[]
    for s in range(n):
        if s in seen:continue
        c=[]; t=s
        while t not in seen:
            seen.add(t);c.append(t);t=t*q%n
        assert t==s
        ans.append(tuple(c))
    assert sum(map(len,ans))==n
    return ans


def rref(vectors,p):
    if not vectors:return ()
    width=len(vectors[0]); mat=[list(row) for row in vectors if any(row)]
    row=0
    for col in range(width):
        k=next((k for k in range(row,len(mat)) if mat[k][col]%p),None)
        if k is None:continue
        mat[row],mat[k]=mat[k],mat[row]
        inv=pow(mat[row][col],-1,p)
        mat[row]=[(inv*u)%p for u in mat[row]]
        for i in range(len(mat)):
            if i==row:continue
            a=mat[i][col]
            if a: mat[i]=[(u-a*v)%p for u,v in zip(mat[i],mat[row])]
        row+=1
        if row==len(mat):break
    return tuple(tuple(r) for r in mat[:row])


def predicted(q,n):
    # This computational factorization deliberately covers prime q only.
    X=sp.Symbol('X')
    cls=orbits(q,n)
    d=len(next(c for c in cls if 1 in c))
    factors=sp.factor_list(X**d-1,modulus=q)[1]
    ranks=Counter({0:1}); exp_divisor_count=1
    for f,e in factors:
        f=sp.Poly(f,X,modulus=q); degree=f.degree()
        exps=[]
        for c in cls:
            v=sp.Poly(X**len(c)-1,X,modulus=q)
            j=0
            while not v.rem(f).as_expr():
                v=v.exquo(f);j+=1
            exps.append(j)
        local=Counter({0:1})
        for j in range(1,e+1):
            b=lambda k:sum(min(k,v) for v in exps)
            local[j*degree]=q**(degree*b(j))-q**(degree*b(j-1))
            assert local[j*degree]>0
        new=Counter()
        for a,u in ranks.items():
            for b,v in local.items():new[a+b]+=u*v
        ranks=new;exp_divisor_count*=e+1
    assert sum(ranks.values())==q**n
    return dict(sorted(ranks.items())),exp_divisor_count,d


def check_case(p,modulus,n):
    order,vec,power=field(p,modulus)
    m=len(modulus)-1
    classes=orbits(p,n)
    seeds=[]
    for cl in classes:
        ell=len(cl)
        allowed=tuple(a for a in range(order) if power(a,p**ell)==a)
        assert len(allowed)==p**ell
        seeds.append([(a,tuple(power(a,p**j) for j in range(ell))) for a in allowed])
    observed=Counter();supports=set()
    for choices in product(*seeds):
        vectors=[vec[x] for a,cl in choices for x in cl]
        basis=rref(vectors,p)
        observed[len(basis)]+=1
        supports.add(basis)
    expected,subspaces,d=predicted(p,n)
    observed=dict(sorted(observed.items()))
    assert observed==expected,(p,m,n,observed,expected)
    assert len(supports)==subspaces,(len(supports),subspaces)
    assert sum(observed.values())==p**n
    print(f'q={p} m={m} n={n} d={d} size={p**n} Frobenius_supports={len(supports)} distribution={observed}')


if __name__=='__main__':
    for p,mod,n in [
        (2,[1,1,1],3),
        (2,[1,1,0,1],7),
        (2,[1,1,0,0,1],5),
        (2,[1,1,0,0,1],15),
        (3,[1,0,1],8),
        (5,[2,0,1],6),
    ]: check_case(p,mod,n)
    print('RANK_PROFILE_VERIFY_OK')

# Independent DFT-based noncyclic test: A=(Z/3Z)^2, base F2, extension F4.
def check_noncyclic():
    _, vec, power = field(2,[1,1,1])
    chars=[(a,b) for a in range(3) for b in range(3)]
    counts=Counter();supports=set()
    for mask in range(1<<9):
        spectral=[]
        for a,b in chars:
            val=0
            for idx,(u,v) in enumerate(chars):
                if mask>>idx&1:
                    val ^= power(2,(a*u+b*v)%3)
            spectral.append(val)
        basis=rref([vec[v] for v in spectral],2)
        counts[len(basis)]+=1;supports.add(basis)
    assert dict(sorted(counts.items()))=={0:1,1:31,2:480}
    assert len(supports)==3
    print('NONCYCLIC_DFT q=2 A=C3xC3 size=512 supports=3 distribution={0: 1, 1: 31, 2: 480}')
    print('NONCYCLIC_DFT_VERIFY_OK')

if __name__ == '__main__':
    check_noncyclic()
