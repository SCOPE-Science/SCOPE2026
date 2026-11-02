"""Reproducible finite checks for looped layered temporal transits.

The finite checks are independent of the general mathematical proof:
(1) a direct subset test for archival upsets;
(2) a direct graph computation of Z reachability;
(3) ordered-partition and power-series counting methods.
Run: python3 checker.py
"""
from itertools import product
from math import factorial, comb, prod
from fractions import Fraction


def compositions(n):
    if n == 0:
        yield ()
    else:
        for a in range(1, n+1):
            for rest in compositions(n-a):
                yield (a,)+rest


def fubini(n):
    if n == 0: return 1
    return sum(comb(n,k)*fubini(n-k) for k in range(1,n+1))


def composition_counts(n):
    # Labelled counts are multinomial-weighted. Unlabelled counts
    # regard only each layer size and its number of reflexive points.
    total=2**n * fubini(n)
    simple=2 if n==1 else 0
    si=2 if n==1 else 0
    orbit_total=orbit_simple=orbit_si=0
    for sizes in compositions(n):
        h=len(sizes)
        multinomial=factorial(n)//prod(factorial(s) for s in sizes)
        arbitrary_orbits=prod(s+1 for s in sizes)
        orbit_total+=arbitrary_orbits
        if h==1:
            if n==1:orbit_simple+=2;orbit_si+=2
            continue
        simple+=multinomial*2**sizes[0]*prod(2**s-1 for s in sizes[1:-1])
        if sizes[0]==1:
            si+=multinomial*2**n
        else:
            si+=multinomial*2**(n-sizes[1])*(2**sizes[1]-1)
        orbit_simple+=(sizes[0]+1)*prod(s for s in sizes[1:-1])
        orbit_si+=(arbitrary_orbits if sizes[0]==1 else
                   (sizes[0]+1)*sizes[1]*prod(s+1 for s in sizes[2:]))
    return total,simple,si,orbit_total,orbit_simple,orbit_si


def all_rank_vectors(n):
    for h in range(1,n+1):
        for ranks in product(range(h),repeat=n):
            if len(set(ranks))==h:yield ranks


def archival_sets(ranks,refl):
    """Direct test of upsets satisfying the finite archival condition."""
    n=len(ranks)
    result=[]
    for mask in range(1<<n):
        good=True
        for x in range(n):
            if (mask>>x)&1:
                if any(ranks[x]<ranks[z] and not(mask>>z&1)
                       for z in range(n)):
                    good=False;break
            else:
                for z in range(n):
                    if (mask>>z)&1 and ranks[x]<ranks[z]:
                        # A reflexive witness y in S with x <= y <= z.
                        if not any((mask>>y)&1 and (refl>>y)&1
                                   and (y==x or ranks[x]<ranks[y])
                                   and (y==z or ranks[y]<ranks[z])
                                   for y in range(n)):
                            good=False;break
                if not good:break
        if good:result.append(mask)
    return set(result)


def normal_form_archival(ranks,refl):
    """Independent explicit formula for the complete congruence poset."""
    n=len(ranks);h=max(ranks)+1
    layer=[sum(1<<i for i,v in enumerate(ranks) if v==j) for j in range(h)]
    refs=[s&refl for s in layer]
    answer={0}
    for j in range(h):
        suffix=0
        for m in layer[j+1:]:suffix|=m
        for t in range(1<<n):
            if not t or t&~layer[j]:continue
            if j==0:
                allowed=(h==1 or t==layer[j] or refs[1]==layer[1])
            else:
                allowed=not(t&~refs[j]) and (
                   j==h-1 or t==layer[j] or refs[j+1]==layer[j+1])
            if allowed:answer.add(suffix|t)
    return answer


def closure_Z(ranks,refl):
    n=len(ranks);allmask=(1<<n)-1
    step=[0]*n
    for x in range(n):
        for w in range(n):
            if ranks[w]>ranks[x] or (ranks[w]==ranks[x] and w!=x):
                continue
            interval=0
            if w!=x:
                for y in range(n):
                    if y==x or ranks[w]<ranks[y]<ranks[x]:
                        interval|=1<<y
            if interval&refl:continue
            for y in range(n):
                if y==w or ranks[y]>ranks[w]:step[x]|=1<<y
    rows=[(1<<x)|step[x] for x in range(n)]
    for k in range(n):
        for x in range(n):
            if rows[x]>>k&1:rows[x]|=rows[k]
    return all(row==allmask for row in rows),any(row==allmask for row in rows)


def predicted(ranks,refl):
    h=max(ranks)+1
    if h==1:return len(ranks)==1,len(ranks)==1
    a1=ranks.count(0)
    top_free=all(not(refl>>i&1) for i,v in enumerate(ranks) if v==h-1)
    internal_free=all(any(not(refl>>i&1) for i,v in enumerate(ranks) if v==j)
                      for j in range(1,h-1))
    second_free=any(not(refl>>i&1) for i,v in enumerate(ranks) if v==1)
    return top_free and internal_free, a1==1 or second_free


def series_mul(f,g,N):
    return [sum(f[j]*g[k-j] for j in range(k+1)) for k in range(N+1)]


def series_geometric(f,N):
    assert f[0]==0
    result=[Fraction(0) for _ in range(N+1)];result[0]=Fraction(1)
    for k in range(1,N+1):
        result[k]=sum(f[j]*result[k-j] for j in range(1,k+1))
    return result


def series_counts(N,labelled):
    zero=[Fraction(0)]*(N+1)
    z=zero.copy();z[1]=Fraction(1)
    if labelled:
        U=[Fraction(0)]+[Fraction(2**k,factorial(k)) for k in range(1,N+1)]
        V=[Fraction(0)]+[Fraction(2**k-1,factorial(k)) for k in range(1,N+1)]
        W=[Fraction(0)]+[Fraction(1,factorial(k)) for k in range(1,N+1)]
    else:
        U=[Fraction(0)]+[Fraction(k+1) for k in range(1,N+1)]
        V=[Fraction(0)]+[Fraction(k) for k in range(1,N+1)]
        W=[Fraction(0)]+[Fraction(1) for k in range(1,N+1)]
    G_U=series_geometric(U,N);G_V=series_geometric(V,N)
    total=series_mul(U,G_U,N)
    simple=series_mul(series_mul(U,W,N),G_V,N)
    si=series_mul([2*el for el in series_mul(z,U,N)] + [],G_U,N)
    vterm=series_mul([U[j]-2*z[j] for j in range(N+1)],V,N)
    si=[si[j]+val for j,val in enumerate(series_mul(vterm,G_U,N))]
    simple=[simple[j]+2*z[j] for j in range(N+1)]
    si=[si[j]+2*z[j] for j in range(N+1)]
    if labelled:
        return [(int(total[k]*factorial(k)),int(simple[k]*factorial(k)),
                 int(si[k]*factorial(k))) for k in range(1,N+1)]
    return [(int(total[k]),int(simple[k]),int(si[k])) for k in range(1,N+1)]


def main():
    N=8
    lbl=series_counts(N,True)
    unlbl=series_counts(N,False)
    for n in range(1,N+1):
        e=composition_counts(n)
        assert (*lbl[n-1],*unlbl[n-1])==e,(n,e,lbl[n-1],unlbl[n-1])
        print('COEFFICIENT',n,*e)
    for n in range(1,6):
        counts=[0,0,0]
        orbits=[set(),set(),set()]
        for ranks in all_rank_vectors(n):
            h=max(ranks)+1
            sizes=tuple(ranks.count(j) for j in range(h))
            for refl in range(1<<n):
                arcs=archival_sets(ranks,refl)
                assert arcs==normal_form_archival(ranks,refl),(n,ranks,refl,arcs)
                is_simple=(len(arcs)==2)
                proper=arcs-{(1<<n)-1}
                maximal=[x for x in proper if not any(x!=y and x&y==x for y in proper)]
                is_si=len(maximal)==1
                assert (is_simple,is_si)==closure_Z(ranks,refl)==predicted(ranks,refl),(
                    n,ranks,refl,is_simple,is_si)
                counts[0]+=1;counts[1]+=is_simple;counts[2]+=is_si
                signature=(sizes,tuple(sum(bool(refl>>i&1) for i,v in enumerate(ranks) if v==j)
                                       for j in range(h)))
                orbits[0].add(signature)
                if is_simple:orbits[1].add(signature)
                if is_si:orbits[2].add(signature)
        assert (*counts,*(len(s) for s in orbits))==composition_counts(n)
        print('EXHAUSTIVE',n,'labelled',counts,'isomorphism',*[len(s) for s in orbits])
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
