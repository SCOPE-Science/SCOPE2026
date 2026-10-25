"""Independent exact checks of rank-one Fourier formulas for small finite fields.
No external dependencies.  Includes every squarefree monic fibre in the tested sizes.
"""
from itertools import product, permutations
from collections import defaultdict
from fractions import Fraction


def monic_charpoly(mat, p, n):
    ans = [0] * (n + 1)
    for perm in permutations(range(n)):
        inversion = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        coeff = [1]
        for i,j in enumerate(perm):
            t = [-mat[i*n+j] % p, 1] if i == j else [-mat[i*n+j] % p]
            res = [0]*(len(coeff)+len(t)-1)
            for a,x in enumerate(coeff):
                for b,y in enumerate(t):
                    res[a+b] = (res[a+b]+x*y)%p
            coeff=res
        for k, val in enumerate(coeff):
            ans[k] = (ans[k]+(-1 if inversion%2 else 1)*val)%p
    return tuple(ans)


def degree(f):
    for i in range(len(f)-1,-1,-1):
        if f[i]:return i
    return -1


def divmodpoly(f,g,p):
    f=list(f)
    while f and f[-1]==0:f.pop()
    g=list(g)
    while g and g[-1]==0:g.pop()
    if not g:raise ZeroDivisionError
    while len(f)>=len(g):
        fac=f[-1]*pow(g[-1],-1,p)%p
        k=len(f)-len(g)
        for j,b in enumerate(g):f[j+k]=(f[j+k]-fac*b)%p
        while f and f[-1]==0:f.pop()
    return tuple(f)


def squarefree(f,p):
    h=tuple((i*f[i])%p for i in range(1,len(f)))
    if degree(h)<0:return False
    a,b=f,h
    while degree(b)>=0:
        a,b=b,divmodpoly(a,b,p)
    return degree(a)==0


def test_case(p,n):
    fibres=defaultdict(list)
    for mat in product(range(p),repeat=n*n):
        fibres[monic_charpoly(mat,p,n)].append(mat)
    tested=0
    total=0
    # use exact cyclotomic polynomials as coefficient vectors rather than floats
    def cyc_power(k):return tuple(1 if j==(k%p) else 0 for j in range(p))
    def add_scaled(v,poly,mult):
        for j in range(p):v[j]+=mult*poly[j]
    def canon(poly):
        # quotient by 1+z+...+z^(p-1)=0: subtract coefficient at z^(p-1)
        return tuple(poly[j]-poly[p-1] for j in range(p-1))
    for f,mats in fibres.items():
        if not squarefree(f,p):continue
        tested+=1
        roots=[a for a in range(p) if sum(coeff*pow(a,i,p) for i,coeff in enumerate(f))%p==0]
        S=len(mats)
        # Use the fixed nonzero vector u=e_1; every nonzero dual v gives a rank-one probe.
        for v in product(range(p),repeat=n):
            if not any(v):continue
            c=v[0]
            lhs=[0]*p
            for mat in mats:
                z=sum(v[i]*mat[i*n] for i in range(n))%p
                add_scaled(lhs,cyc_power(z),1)
            rhs=[0]*p
            if c:
                # F=(q-1)|V_f|/(q^n-1)*sum_{r rational root} psi(cr)
                k=Fraction((p-1)*S,p**n-1)
                for lam in roots:
                    assert k.denominator==1
                    add_scaled(rhs,cyc_power(c*lam),int(k))
            else:
                k=Fraction((p-1)*S,p**n-1)
                N=Fraction(S-len(roots)*k,p**n-p)
                z=len(roots)*k-p*N
                assert z.denominator==1
                rhs[0]=int(z)
            assert canon(lhs)==canon(rhs),(p,n,f,v,canon(lhs),canon(rhs))
            total+=1
    return tested,total

if __name__=='__main__':
    total=0
    for p,n in [(2,3),(3,2),(5,2)]:
        fibres,probes=test_case(p,n)
        print('p=%d n=%d squarefree_fibres=%d rank_one_probes=%d'%(p,n,fibres,probes))
        total+=probes
    print('CERTIFICATE_OK total_probes=%d'%total)
