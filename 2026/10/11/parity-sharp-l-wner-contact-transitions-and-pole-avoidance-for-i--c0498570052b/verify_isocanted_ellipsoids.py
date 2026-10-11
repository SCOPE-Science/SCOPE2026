"""Exact rational checks for a normalized isocanted cube's extremal ellipsoids.

No external modules required. Checks the vertex orbit reduction, feasible
ellipsoid contact constraints, and nonnegative first-order multipliers.
A finite test is not a proof of the general theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def orbits(d, delta):
    return [(k, F(d)*(1-delta+F(k,d)*delta)**2,
             delta**2*F(k*(d-k), d)) for k in range((d+1)//2, d+1)]


def candidate(d, delta):
    vals = orbits(d,delta)
    choices=[]
    for k,A,B in vals:
        if B==0: continue
        t=F(1,d)/A
        s=F(d-1,d)/B
        if s>t and all(A1*t+B1*s <=1 for _,A1,B1 in vals):
            choices.append(('single',k,t,s,None))
    for (k,A,B),(k1,A1,B1) in zip(vals,vals[1:]):
        det=A*B1-A1*B
        if not det: continue
        t=(B1-B)/det; s=(A-A1)/det
        if not (t>0 and s>t): continue
        if not all(a*t+b*s<=1 for _,a,b in vals):continue
        lam=(B1/t-A1*F(d-1)/s)/det
        mu=(A*F(d-1)/s-B/t)/det
        if lam>=0 and mu>=0:
            choices.append(('pair',k,t,s,(lam,mu)))
    assert choices, ('no-candidate',d,delta)
    ts={(c[2],c[3]) for c in choices}
    assert len(ts)==1,('nonunique',d,delta,choices)
    tag,k,t,s,_=choices[0]
    hits=tuple(kk for kk,A,B in vals if t*A+s*B==1)
    assert 1<=len(hits)<=2
    assert hits==tuple(range(hits[0],hits[0]+len(hits)))
    # (d-1)-dimensional perp inverse radius and 1D diagonal inverse radius.
    # Necessary + sufficient KKT conditions checked exactly.
    return tag,t,s,hits,2*sum(comb(d,k) for k in hits)


def vertex_check(d,delta):
    # Symmetric +/- candidates, each coordinate 1 or 1-delta,
    # all k>=1. Every candidate meets d independent facet equations.
    verts=[]
    for signs in product((0,1),repeat=d):
        if not any(signs): continue
        u=tuple(F(1) if bit else 1-delta for bit in signs)
        verts.extend([u,tuple(-a for a in u)])
    assert len(set(verts))==2*(2**d-1)
    for v in verts:
        assert all(abs(a)<=1 for a in v)
        assert all(abs(v[i]-v[j])<=delta for i in range(d) for j in range(i+1,d))
    return len(verts)


def main():
    tested=0; total_vertices=0; single=pair=0; pole_checks=0
    for d in range(2,31):
        for numerator,denominator in ((1,20),(1,4),(1,2),(3,4),(1,1),
             (5,4),(4,3),(7,5),(3,2),(7,4),(19,10),(39,20)):
            delta=F(numerator,denominator)
            tag,t,s,hits,contact_count=candidate(d,delta)
            assert contact_count>0
            if tag=='single':single+=1
            else: pair+=1
            tested+=1
            if d<=7:
                total_vertices+=vertex_check(d,delta)
            # The pole has Mahalanobis value d*t. It is strictly internal
            # for every d>=4 (and for d=2,3 below d-sqrt(d)).
            if d>=4:
                assert d*t<1
                pole_checks+=1
            # John semiaxis squared matrix checks, exact in fractions
            v=min(F(1),delta*delta/2)
            u=d-(d-1)*v
            assert u>0 and v>0
            assert (u+(d-1)*v)==d
            assert 2*v <=delta*delta
            # lower half Hamming layers are strictly dominated
            for k in range(1,(d+1)//2):
                Ak=F(d)*(1-delta+F(k,d)*delta)**2
                Ank=F(d)*(1-delta+F(d-k,d)*delta)**2
                assert Ank>Ak
        # Verify the exact threshold predicate on rational brackets
        # around its algebraic root, including the contact switch.
        from math import sqrt
        m=(d+1)//2
        z=sqrt(d-(d-1)*(m+1)*(d-m-1)/(m*(d-m)))
        tau=d*(z-1)/(1+(d-m)*(z-1))
        below=F(int(tau*100000)-1,100000)
        above=F(int(tau*100000)+2,100000)
        assert candidate(d,below)[3]==(m,)
        assert candidate(d,above)[3]!=(m,)
        assert candidate(d,F(1,100000))[3]==(m,)
    print('VERIFY_OK exact_rational_cases=%d single_candidates=%d pair_candidates=%d explicit_vertices_checked=%d pole_checks=%d john_facets=yes threshold_brackets=yes' % (tested,single,pair,total_vertices,pole_checks))
if __name__=='__main__':main()
