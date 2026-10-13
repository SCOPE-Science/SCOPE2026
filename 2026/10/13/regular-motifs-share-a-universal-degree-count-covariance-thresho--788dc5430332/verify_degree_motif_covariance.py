#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb


def ff(x,d):
    z=1
    for j in range(d):
        z*=x-j
    return z


def binom_pmf(N,k,p):
    if k<0 or k>N:
        return Fraction(0)
    return Fraction(comb(N,k))*p**k*(1-p)**(N-k)


def edge_index(n):
    E=list(combinations(range(n),2))
    return E,{e:i for i,e in enumerate(E)}


def motif_counts(n, mask, idx):
    def has(a,b):
        if a>b: a,b=b,a
        return bool(mask & (1<<idx[(a,b)]))

    edge_count=mask.bit_count()
    tri=0
    p3=0
    for a,b,c in combinations(range(n),3):
        ab,ac,bc=has(a,b),has(a,c),has(b,c)
        tri += int(ab and ac and bc)
        p3 += int(ab and ac) + int(ab and bc) + int(ac and bc)

    c4=0
    k4=0
    for a,b,c,d in combinations(range(n),4):
        verts=(a,b,c,d)
        all6=all(has(x,y) for x,y in combinations(verts,2))
        k4 += int(all6)
        # Three undirected Hamilton cycles on a fixed 4-set.
        c4 += int(has(a,b) and has(b,c) and has(c,d) and has(d,a))
        c4 += int(has(a,b) and has(b,d) and has(d,c) and has(c,a))
        c4 += int(has(a,c) and has(c,b) and has(b,d) and has(d,a))
    return {'K2':edge_count,'K3':tri,'C4':c4,'K4':k4,'P3':p3}


def degrees(n, mask, E):
    ds=[0]*n
    for i,(a,b) in enumerate(E):
        if mask & (1<<i):
            ds[a]+=1; ds[b]+=1
    return ds


def potential_copies(n,name):
    if name=='K2': return comb(n,2), 1, [1,1]
    if name=='K3': return comb(n,3), 3, [2,2,2]
    if name=='C4': return 3*comb(n,4), 4, [2,2,2,2]
    if name=='K4': return comb(n,4), 6, [3,3,3,3]
    if name=='P3': return 3*comb(n,3), 2, [2,1,1]
    raise KeyError(name)


def exact_test(n,p):
    E,idx=edge_index(n)
    m=len(E)
    names=['K2','K3','P3'] + (['C4','K4'] if n>=4 else [])
    # Precompute graph statistics once; then weight by p.
    rows=[]
    for mask in range(1<<m):
        ds=degrees(n,mask,E)
        Nk=[ds.count(k) for k in range(n)]
        mc=motif_counts(n,mask,idx)
        rows.append((mask.bit_count(),Nk,mc))

    formula_checks=0
    regular_checks=0
    sign_checks=0
    triangle_checks=0
    for name in names:
        copies,e,degs=potential_copies(n,name)
        EX=Fraction(copies)*p**e
        for k in range(n):
            EN=Fraction(n)*binom_pmf(n-1,k,p)
            ENX=Fraction(0)
            for ec,Nk,mc in rows:
                pr=p**ec*(1-p)**(m-ec)
                ENX += pr*Nk[k]*mc[name]
            cov=ENX-EN*EX
            b=binom_pmf(n-1,k,p)
            bracket=sum((Fraction(ff(k,d),ff(n-1,d))*p**(-d) if d else Fraction(1)) for d in degs)-len(degs)
            target=EX*b*bracket
            assert cov==target,(n,p,name,k,cov,target)
            formula_checks+=1

            if len(set(degs))==1:
                d=degs[0]; h=len(degs)
                target2=h*EX*b*(Fraction(ff(k,d),ff(n-1,d))*p**(-d)-1)
                assert cov==target2
                regular_checks+=1
                raw=Fraction(ff(k,d),1)-Fraction(ff(n-1,d),1)*p**d
                if b>0 and EX>0:
                    assert (cov>0)-(cov<0)==(raw>0)-(raw<0)
                sign_checks+=1

            if name=='K3':
                target3=3*comb(n,3)*p**3*b*(Fraction(k*(k-1),(n-1)*(n-2))*p**(-2)-1)
                assert cov==target3
                triangle_checks+=1
    return len(rows),formula_checks,regular_checks,sign_checks,triangle_checks


def root_bisect(N,d,p):
    rhs=ff(N,d)*(p**d)
    lo=Fraction(d-1,1)
    hi=Fraction(N,1)
    # Use float bisection only for asymptotic sanity, not exact theorem.
    lo=float(lo); hi=float(hi); rhs=float(rhs)
    def f(x):
        z=1.0
        for j in range(d): z*=x-j
        return z-rhs
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def run():
    total_graphs=0
    formula_checks=regular_checks=sign_checks=triangle_checks=0
    parameter_sets=0
    for n in (4,5,6):
        for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
            g,a,b,c,d=exact_test(n,p)
            total_graphs+=g
            formula_checks+=a; regular_checks+=b; sign_checks+=c; triangle_checks+=d
            parameter_sets+=1

    asymptotic_checks=0
    for d in (1,2,3,4):
        for p in (0.2,0.5,0.8):
            errors=[]
            for n in (200,1000,5000):
                N=n-1
                r=root_bisect(N,d,p)
                approx=p*N+(d-1)*(1-p)/2
                errors.append(abs(r-approx))
                assert abs(r-approx)<0.05
                asymptotic_checks+=1
            assert errors[-1] <= errors[0] + 1e-12
            asymptotic_checks+=1

    print(
        'VERIFY_OK '
        f'parameter_sets={parameter_sets} '
        f'graphs_enumerated_weighted={total_graphs} '
        f'formula_checks={formula_checks} '
        f'regular_checks={regular_checks} '
        f'sign_checks={sign_checks} '
        f'triangle_checks={triangle_checks} '
        f'asymptotic_checks={asymptotic_checks}'
    )

if __name__=='__main__':
    run()
