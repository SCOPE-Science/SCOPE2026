"""Exact three-round types for lattices of flats of uniform matroids.
No external packages. Finite computations corroborate the all-parameter proof.
"""
from itertools import product

def order(x, y, intersection):
    if intersection == x == y:
        return '='
    if intersection == x:
        return '<'
    if intersection == y:
        return '>'
    return '!'

def signature(h, a, b, c, d):
    # X=A+B, Y=A+C; top has size a+b+c+d.
    x, y, n = a+b, a+c, a+b+c+d
    xy = order(x, y, a)
    types = set()
    # Each cell is empty, full, or properly nonempty in Z.
    # For the last state, taking one element is cardinality-minimal.
    choices = []
    for z in (a,b,c,d):
        choices.append(tuple(set((0,z,1))) if z>=2 else ((0,z) if z else (0,)))
    for za,zb,zc,zd in product(*choices):
        z = za+zb+zc+zd
        if z <= h:
            types.add((xy,order(x,z,za+zb),order(y,z,za+zc)))
    types.add((xy,order(x,n,x),order(y,n,y))) # Z=top
    return xy,tuple(sorted(types))

def pointed(s,t):
    h=s+t; n=h+2
    ans=set()
    for a in range(s+1):
        b=s-a
        for c in range(min(b+t,t+2)+1):
            ans.add(signature(h,a,b,c,n-s-c))
    ans.add(signature(h,s,0,n-s,0)) # Y=top
    return frozenset(ans)

def top_type(h):
    n=h+2
    return frozenset([signature(h,k,n-k,0,0) for k in range(h+1)] +
                     [signature(h,n,0,0,0)])

def abstract(n,r):
    h=r-1
    unaries={s:set() for s in list(range(r))+[n]}
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                x=a+b; y=a+c
                if x in unaries and y in unaries:
                    unaries[x].add(signature(h,a,b,c,d))
    return frozenset(frozenset(v) for v in unaries.values())

def direct(n,r):
    universe=(1<<n)-1
    els=[s for s in range(1<<n) if s.bit_count()<r or s==universe]
    rel={(x,y):order(x.bit_count(),y.bit_count(),(x&y).bit_count())
         for x in els for y in els}
    point_types=set()
    for x in els:
        pair_types=set()
        for y in els:
            t=frozenset((rel[x,y],rel[x,z],rel[y,z]) for z in els)
            pair_types.add((rel[x,y],tuple(sorted(t))))
        point_types.add(frozenset(pair_types))
    return frozenset(point_types)

def checks():
    tests=0
    # True exhaustive comparison with direct set structures, not orbit assumptions.
    for n in range(3,8):
        for r in range(2,n):
            assert direct(n,r)==abstract(n,r),(n,r)
            tests+=1
    print('DIRECT_EQUIVALENCE: PASS',tests,'small matroid lattices')
    classes={}
    for n in range(3,17):
        for r in range(2,n):
            types=abstract(n,r)
            classes.setdefault(types,[]).append((n,r))
            assert types==abstract(r+1,r)
    assert len(classes)==5
    for group in classes.values():
        assert len({min(r,6) for n,r in group}) == 1
    assert {min(group[0][1],6) for group in classes.values()} == {2,3,4,5,6}
    assert all(abstract(n,r)==abstract(r+1,r) for n in range(3,17) for r in range(2,n))
    print('ORBIT_ROOTS: PASS 5 classes for 2<=r<n<=16')
    # Pair-profile finite-state compression rules. These are checks of the
    # exceptional configurations in the mathematical pumping proof.
    # All feasible clipped descriptors encountered through h=16 must be exact.
    descriptor_types={}
    for h in range(1,17):
        for a in range(h+1):
            for b in range(h-a+1):
                for c in range(h-a+1):
                    d=max(0,h+2-a-b-c)
                    t=h-a-b
                    desc=(min(a,2),min(b,2),min(c,2),min(t,2),
                          min(h-a-c,2),max(-1,min(h-a-b-c,2)))
                    v=signature(h,a,b,c,d)
                    assert desc not in descriptor_types or descriptor_types[desc]==v
                    descriptor_types[desc]=v
    print('CAPPED_SIGNATURE_TABLE: PASS',len(descriptor_types),'feasible descriptors')
    checks_n=checks_t=checks_s=0
    for s in range(0,16):
        for t in range(0,13):
            h=s+t
            if h<1:continue
            for a in range(s+1):
                b=s-a
                for c in range(t+3,b+t+1):
                    delta=c-(t+2)
                    if delta<1:continue
                    n=max(h+2,s+c)
                    assert signature(h,a,b,c,n-s-c)==signature(h,a+delta,b-delta,t+2,0)
                    checks_n+=1
    for s in range(0,14):
        for t in range(3,16):
            h=s+t;n=h+2
            for a in range(s+1):
                b=s-a
                for c in range(min(b+t,t+2)+1):
                    cp=c-1 if c>=3 else c
                    assert signature(h,a,b,c,n-s-c)==signature(h-1,a,b,cp,n-1-s-cp)
                    checks_t+=1
                for c in range(min(b+t-1,t+1)+1):
                    cp=c+1 if c>=2 else c
                    assert signature(h-1,a,b,c,n-1-s-c)==signature(h,a,b,cp,n-s-cp)
                    checks_t+=1
    for s in range(6,18):
        for t in range(0,13):
            h=s+t;n=h+2
            for a in range(s+1):
                b=s-a
                for c in range(min(b+t,t+2)+1):
                    ap,bp=(a-1,b) if a>=3 else (a,b-1)
                    assert signature(h,a,b,c,n-s-c)==signature(h-1,ap,bp,c,n-s-c)
                    checks_s+=1
            for a in range(s):
                b=(s-1)-a
                for c in range(min(b+t,t+2)+1):
                    ap,bp=(a+1,b) if a>=2 else (a,b+1)
                    assert signature(h-1,a,b,c,n-s-c)==signature(h,ap,bp,c,n-s-c)
                    checks_s+=1
    for t in range(3):
        assert pointed(3,t)==pointed(4,t)==pointed(5,t)
    assert all(top_type(h)==top_type(2) for h in range(2,20))
    print('PUMPING_BOUNDARY_CHECKS: PASS',checks_n,checks_t,checks_s)
    # Canonical unary profile table and stable class.
    profiles={(s,t):pointed(s,t) for s in range(4) for t in range(3) if s+t>=1}
    assert len(set(profiles.values()))==len(profiles)
    assert len({abstract(r+1,r) for r in range(2,15)})==5
    assert abstract(7,6)==abstract(10,9)==abstract(15,14)
    print('CANONICAL_POINTED_PROFILES: PASS',len(profiles),'distinct proper profiles')
    print('STABLE_CLASS_REPRESENTATIVE: r=6 n=7 121 flats')
    print('ALL_FINITE_VERIFICATION_CHECKS: PASS')

if __name__=='__main__':checks()
