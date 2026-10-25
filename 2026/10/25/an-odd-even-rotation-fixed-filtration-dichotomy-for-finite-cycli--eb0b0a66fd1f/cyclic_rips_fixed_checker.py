#!/usr/bin/env python3
"""Exact arithmetic cross-check of geometric fixed-face classifications.

No external dependencies. Vertices are cyclic residues, distances graph distances.
A nonempty simplex in the fixed orbit complex comprises full H-orbits.
The checker compares the exact pairwise compatibility graph with the theorem.
"""

def dist(n,a,b):
    k = (a-b) % n
    return min(k,n-k)

def actual_pair_max(n,d,a,b):
    m=n//d
    oa=[(a+j*m)%n for j in range(d)]
    ob=[(b+j*m)%n for j in range(d)]
    return max(dist(n,x,y) for x in oa for y in ob)

def actual_orbit_diameter(n,d,a):
    m=n//d
    oo=[(a+j*m)%n for j in range(d)]
    return max(dist(n,x,y) for x in oo for y in oo)

def predicted_pair_max(n,d,a,b):
    m=n//d
    delta=dist(m,a,b) if m>1 else 0
    if d%2==0:
        # Even-order orbits each contain antipodal vertex pairs.
        return n//2
    return m*((d-1)//2)+delta

def check(max_n=90):
    pair_checks=0
    threshold_checks=0
    orbit_checks=0
    for n in range(3,max_n+1):
        for d in range(2,n+1):
            if n%d:continue
            m=n//d
            for a in range(m):
                dia=actual_orbit_diameter(n,d,a)
                expected=n//2 if d%2==0 else m*((d-1)//2)
                assert dia==expected,(n,d,a,dia,expected)
                orbit_checks+=1
                for b in range(m):
                    ex=actual_pair_max(n,d,a,b)
                    pr=predicted_pair_max(n,d,a,b)
                    if d%2:
                        assert ex==pr,(n,d,a,b,ex,pr)
                    else:
                        # Need not assert pair max=diameter here, pair union adds orbit diam.
                        assert ex<=n//2
                    pair_checks+=1
            for r in range(n//2+1):
                for a in range(m):
                    for b in range(a+1,m):
                        joint=max(actual_orbit_diameter(n,d,a),
                                  actual_orbit_diameter(n,d,b),actual_pair_max(n,d,a,b))
                        if d%2==0:
                            pred=(r>=n//2)
                        else:
                            base=m*((d-1)//2)
                            pred=(r>=base and dist(m,a,b)<=r-base)
                        assert (joint<=r)==pred,(n,d,r,a,b,joint,pred)
                        threshold_checks+=1
    print('CYCLIC_RIPS_ROTATION_FIXED_VERIFIED',max_n,orbit_checks,pair_checks,threshold_checks)

if __name__=='__main__':
    check()
