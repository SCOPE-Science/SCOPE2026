"""Direct finite exhaustive verification for equivariant retractions.
All comparisons are made from maps, not from the claimed counting formula.
"""
from itertools import product, permutations
from collections import Counter, defaultdict
from math import factorial

def space(n):
    pts=list(product(range(n), repeat=2))
    idx={x:i for i,x in enumerate(pts)}
    flip=[idx[b,a] for (a,b) in pts]
    fixed=[idx[a,a] for a in range(n)]
    free=[idx[a,b] for a in range(n) for b in range(a+1,n)]
    return pts, flip, fixed, free

def expand(n, vals):
    pts, flip, fixed, free=space(n)
    out=[None]*len(pts)
    for j,z in zip(fixed+free,vals):
        out[j]=z
        out[flip[j]]=flip[z]
    return tuple(out)

def all_maps(n):
    pts, flip, fixed, free=space(n)
    for v in product(fixed,repeat=n):
        for w in product(range(n*n),repeat=len(free)):
            yield expand(n,v+w)

def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def profile(n,e):
    pts,flip,fixed,free=space(n)
    roots_f=sorted(set(e[z] for z in fixed))
    roots_o=sorted(set(min(e[z],flip[e[z]]) for z in free if e[z]!=flip[e[z]]))
    fixed_types=[]; free_types=[]
    for root in roots_f:
        b=sum(e[z]==root for z in fixed)-1
        c=sum(e[z]==root for z in free)
        fixed_types.append((b,c))
    for root in roots_o:
        d=sum(min(e[z],flip[e[z]])==root for z in free)-1
        free_types.append(d)
    return tuple(sorted(fixed_types)),tuple(sorted(free_types))

def predicted_centralizer(profile):
    fixed_types,free_types=profile
    first=1
    for b,c in fixed_types:
        first*=sum((1+bb)**b*(1+bb+2*cc)**c for bb,cc in fixed_types)
    for d in free_types:
        first*=sum((1+bb+2*cc)**d for bb,cc in fixed_types)+2*sum((1+dd)**d for dd in free_types)
    return first

def predicted_orbit(n,profile):
    fixed_types,free_types=profile
    N=n*(n-1)//2
    denom=1
    for b,c in fixed_types:
        denom*=factorial(b)*2**c*factorial(c)
    for d in free_types:
        denom*=2*factorial(d)
    for multiplicity in Counter(fixed_types).values():
        denom*=factorial(multiplicity)
    for multiplicity in Counter(free_types).values():
        denom*=factorial(multiplicity)
    assert factorial(n)*2**N*factorial(N)%denom==0
    return factorial(n)*2**N*factorial(N)//denom

def units(n):
    pts,flip,fixed,free=space(n)
    for fi in permutations(fixed):
        for fo in permutations(free):
            for signs in product((0,1),repeat=len(free)):
                vals=fi+tuple(flip[fo[i]] if signs[i] else fo[i] for i in range(len(free)))
                yield expand(n,vals)

def check(n):
    maps=list(all_maps(n))
    idem=[e for e in maps if compose(e,e)==e]
    uniq=defaultdict(list)
    for e in idem:
        uniq[profile(n,e)].append(e)
    expected=0
    for p,v in uniq.items():
        orbit_size=predicted_orbit(n,p)
        assert len(v)==orbit_size,(n,p,orbit_size,len(v))
        expected+=orbit_size
    assert expected==len(idem)
    U=list(units(n))
    assert len(U)==factorial(n)*2**(n*(n-1)//2)*factorial(n*(n-1)//2)
    for p,v in uniq.items():
        e=v[0]
        sample_orbit={compose(compose(u,e),inverse_perm(u)) for u in U}
        assert sample_orbit==set(v),(n,p,len(sample_orbit),len(v))
    # Exhaustive centralizer verification for every n=2 idempotent; one per n=3 orbit.
    samples=idem if n==2 else [v[0] for v in uniq.values()]
    for e in samples:
        x=predicted_centralizer(profile(n,e))
        brute=sum(1 for f in maps if compose(f,e)==compose(e,f))
        assert brute==x,(n,profile(n,e),x,brute)
    print('n',n,'magma_monoid_order',len(maps),'idempotents',len(idem),'unit_orbits',len(uniq),'unit_group',len(U),'centralizer_samples',len(samples),'VERIFY_OK')

def inverse_perm(a):
    inv=[None]*len(a)
    for i,j in enumerate(a):inv[j]=i
    return tuple(inv)

if __name__=='__main__':
    check(2)
    check(3)
