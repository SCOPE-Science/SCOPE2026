"""Independent finite-field checks for random generated subalgebras of products of fields.
Run: python3 checker.py (Python 3, standard library only)."""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def field(q, m):
    # Irreducible monic coefficient arrays in ascending order.
    polys = {(2,1):(1,1), (2,2):(1,1,1), (2,3):(1,1,0,1),
             (3,1):(1,1), (3,2):(1,0,1)}
    f = polys[q,m]
    N = q**m
    digits = {x:tuple((x//(q**i))%q for i in range(m)) for x in range(N)}
    enc = lambda aa:sum((a%q)*(q**i) for i,a in enumerate(aa))
    def plus(a,b):return enc([(u+v)%q for u,v in zip(digits[a],digits[b])])
    def mul(a,b):
        a,b=digits[a],digits[b]
        c=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):c[i+j]=(c[i+j]+a[i]*b[j])%q
        for k in range(2*m-2,m-1,-1):
            lead=c[k]
            for i in range(m):c[k-m+i]=(c[k-m+i]-lead*f[i])%q
        return enc(c[:m])
    def power(a,k):
        v=1
        while k:
            if k%2:v=mul(v,a)
            a=mul(a,a);k//=2
        return v
    return N,digits,plus,mul,power


def rank_basis_q(vectors,q,m,r):
    pivots={}
    indep=[]
    for v in vectors:
        a=v[:]
        for col in sorted(pivots):
            z=a[col]
            if z:
                p=pivots[col]
                a=[(x-z*y)%q for x,y in zip(a,p)]
        if any(a):
            col=next(j for j,x in enumerate(a) if x)
            inv=pow(a[col],-1,q)
            a=[x*inv%q for x in a]
            pivots[col]=a
            indep.append(v)
    return len(pivots),indep


def generated_basis(gens,q,m,r,field_data):
    N,digits,plus,mul,power=field_data
    flatten=lambda x:[a for c in x for a in digits[c]]
    basis=[(1,)*r]
    for g in gens:
        cand=basis+[g]
        if rank_basis_q([flatten(x) for x in cand],q,m,r)[0]>len(basis):basis.append(g)
    cursor=0
    while cursor<len(basis):
        v=basis[cursor];cursor+=1
        for g in gens:
            w=tuple(mul(a,b) for a,b in zip(v,g))
            if rank_basis_q([flatten(x) for x in basis+[w]],q,m,r)[0]>len(basis):
                basis.append(w)
    assert len(basis)<=m*r
    return basis


def count_idempotents(basis,q,field_data):
    N,digits,plus,mul,power=field_data
    r=len(basis[0]);one=0
    num=0
    for coef in product(range(q),repeat=len(basis)):
        x=(0,)*r
        for v,c in zip(basis,coef):
            for _ in range(c):x=tuple(plus(a,b) for a,b in zip(x,v))
        if tuple(mul(a,a) for a in x)==x:num+=1
    return num


def orbit_profile(gens,r,q,field_data):
    N,digits,plus,mul,power=field_data
    occ=defaultdict(set)
    for i in range(r):
        t=tuple(g[i] for g in gens)
        seq=[];p=t
        while p not in seq:
            seq.append(p)
            p=tuple(power(a,q) for a in p)
        assert p==t
        occ[len(seq)].add(min(seq))
    return tuple((d,len(occ[d])) for d in sorted(occ))


def mobius(n):
    if n==1:return 1
    num=0;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;num+=1
            if n%p==0:return 0
        p+=1
    if n>1:num+=1
    return -1 if num%2 else 1


def predicted(q,m,l,r):
    div=[d for d in range(1,m+1) if m%d==0]
    h={d:sum(mobius(e)*q**(d*l//e) for e in range(1,d+1) if d%e==0)//d for d in div}
    dp={(0,(0,)*len(div)):1}
    for j,d in enumerate(div):
        for _ in range(h[d]):
            ndp=defaultdict(int)
            for (sz,counts),v in dp.items():
                ndp[sz,counts]+=v
                for k in range(1,r-sz+1):
                    newcounts=list(counts);newcounts[j]+=1
                    ndp[sz+k,tuple(newcounts)]+=v*comb(sz+k,k)*d**k
            dp=ndp
    out={tuple((d,s) for d,s in zip(div,counts) if s):v for (sz,counts),v in dp.items() if sz==r}
    assert sum(out.values())==q**(m*l*r)
    return out


def run():
    cases=[(2,1,2,3),(2,2,1,3),(2,2,2,3),(2,3,1,2),(2,3,2,2),
           (3,1,2,3),(3,2,1,3),(3,2,2,2)]
    total=0
    for q,m,l,r in cases:
        f=field(q,m);N=f[0]
        observed=Counter()
        for items in product(range(N),repeat=l*r):
            gens=[tuple(items[j*r:(j+1)*r]) for j in range(l)]
            prof=orbit_profile(gens,r,q,f)
            B=generated_basis(gens,q,m,r,f)
            dim_expected=sum(d*s for d,s in prof)
            components=sum(s for d,s in prof)
            assert len(B)==dim_expected,(q,m,l,r,gens,prof,B)
            # Enumerate the generated algebra and verify its primitive idempotents count.
            assert count_idempotents(B,q,f)==2**components,(q,m,l,r,gens,prof,B)
            observed[prof]+=1
            total+=1
        formula=predicted(q,m,l,r)
        assert dict(observed)==formula,(q,m,l,r,observed,formula)
        print('PASS',q,m,l,r,'sample arrays',N**(l*r),'subalgebra types',len(observed))
    print('ALL_FINITE_ETALE_SUBALGEBRA_CHECKS_PASSED',len(cases),total)

if __name__=='__main__':run()
