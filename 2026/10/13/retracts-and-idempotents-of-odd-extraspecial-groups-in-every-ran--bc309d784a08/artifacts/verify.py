"""Replays idempotent-endomorphism counts for extraspecial groups of odd order.
Requires only Python 3.10+. No external data or dependencies.
"""
from itertools import product
from math import prod


def gaussian(n,k,p):
    if k<0 or k>n: return 0
    top=prod(p**(n-j)-1 for j in range(k))
    bot=prod(p**(k-j)-1 for j in range(k))
    assert top%bot==0
    return top//bot


def isotropic(n,r,p):
    if r<0 or r>n: return 0
    return gaussian(n,r,p)*prod(p**(n-j)+1 for j in range(r))


def isotropic_hyperplane(n,r,p):
    return isotropic(n-1,r-1,p)+p**r*isotropic(n-1,r,p)


def rank_counts(n,p,kind):
    iso=isotropic if kind=='exponent_p' else isotropic_hyperplane
    return [iso(n,r,p)*p**(r*(2*n-r+1)) for r in range(n+1)]


def H_mul(a,b,p):
    u,v,z=a; U,V,Z=b
    return ((u+U)%p,(v+V)%p,(z+Z+u*V)%p)


def E_mul(a,b,p):
    u,v=a; U,V=b
    return ((u+U+p*u*V)%(p*p),(v+V)%p)


def power(a,k,mul,unit,p):
    acc=unit
    while k:
        if k&1: acc=mul(acc,a,p)
        a=mul(a,a,p)
        k>>=1
    return acc


def enumerate_H(p):
    G=list(product(range(p),repeat=3))
    one=(0,0,0)
    def exponent(x,k): return power(x,k,H_mul,one,p)
    is_idempotent=0
    total=0
    for A in G:
        invA=exponent(A,p-1)
        for B in G:
            invB=exponent(B,p-1)
            comm=H_mul(H_mul(H_mul(A,B,p),invA,p),invB,p)
            # The map specified by generator images A,B sends z to [A,B].
            # Since x^u y^v z^w=(u,v,uv+w), evaluate it on A and B.
            def phi(g):
                u,v,z=g
                ans=H_mul(exponent(A,u),exponent(B,v),p)
                return H_mul(ans,exponent(comm,(z-u*v)%p),p)
            total+=1
            if phi(A)==A and phi(B)==B:
                is_idempotent+=1
    assert total==p**6
    return is_idempotent


def enumerate_E(p):
    G=list(product(range(p*p),range(p)))
    one=(0,0)
    def exponent(x,k): return power(x,k,E_mul,one,p)
    is_idempotent=0
    homomorphisms=0
    for A in G:
        for B in G:
            if exponent(B,p)!=one: continue
            # [x,y]=x^p; relations impose [A,B]=A^p.
            invA=exponent(A,p*p-1)
            invB=exponent(B,p*p-1)
            comm=E_mul(E_mul(E_mul(A,B,p),invA,p),invB,p)
            if comm!=exponent(A,p): continue
            homomorphisms+=1
            def phi(g):
                U,v=g
                u=(U-p*(U%p)*v)%(p*p)
                return E_mul(exponent(A,u),exponent(B,v),p)
            if phi(A)==A and phi(B)==B:
                is_idempotent+=1
    assert homomorphisms==2*p**4-p**3, (p,homomorphisms)
    return is_idempotent


# Independent finite field subspace enumeration verifies the isotropic-count formulas.
def rankmod(vectors,p):
    a=[list(v) for v in vectors]; rank=0
    for col in range(len(a[0]) if a else 0):
        j=next((i for i in range(rank,len(a)) if a[i][col]%p),None)
        if j is None: continue
        a[rank],a[j]=a[j],a[rank]
        inv=pow(a[rank][col]%p,-1,p)
        a[rank]=[(x*inv)%p for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                factor=a[i][col]
                a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank


def orth(v,w,n,p):
    return sum((v[i]*w[n+i]-v[n+i]*w[i]) for i in range(n))%p


def count_iso_lines_and_planes(n,p):
    m=2*n
    vs=[v for v in product(range(p),repeat=m) if any(v)]
    # r=1: every line is isotropic; hyperplane is v[0]==0.
    lines=len(vs)//(p-1)
    hlines=sum(v[0]==0 for v in vs)//(p-1)
    assert lines==isotropic(n,1,p)
    assert hlines==isotropic_hyperplane(n,1,p)
    if n==1: return (lines,hlines)
    # Ordered independent symplectic-orthogonal bases of planes / GL(2,p).
    count=0; hcount=0
    for u in vs:
        for v in vs:
            if orth(u,v,n,p)!=0 or rankmod((u,v),p)!=2: continue
            count+=1
            if u[0]==0 and v[0]==0: hcount+=1
    gl2=(p*p-1)*(p*p-p)
    assert count%gl2==hcount%gl2==0
    planes=count//gl2
    hplanes=hcount//gl2
    assert planes==isotropic(n,2,p)
    assert hplanes==isotropic_hyperplane(n,2,p)
    return lines,hlines,planes,hplanes


for p in (3,5):
    rank_H=rank_counts(1,p,'exponent_p')
    rank_E=rank_counts(1,p,'exponent_p2')
    direct_H=enumerate_H(p)
    direct_E=enumerate_E(p)
    assert direct_H==1+sum(rank_H)
    assert direct_E==1+sum(rank_E)
    assert rank_H==[1,p*p*(p+1)]
    assert rank_E==[1,p*p]
    print('order_p3',{'p':p,'exp_p_idempotents':direct_H,'exp_p2_idempotents':direct_E})

for n,p in ((2,3),(2,5)):
    counts=count_iso_lines_and_planes(n,p)
    h=rank_counts(n,p,'exponent_p')
    e=rank_counts(n,p,'exponent_p2')
    assert h[1]-e[1]==p**(4*n-1)
    print('higher_rank',{'n':n,'p':p,'isotropic_counts':counts,
                         'exp_p_rank_profile':h,
                         'exp_p2_rank_profile':e,
                         'exp_p_total':1+sum(h),
                         'exp_p2_total':1+sum(e)})
print('VERIFY_OK')
