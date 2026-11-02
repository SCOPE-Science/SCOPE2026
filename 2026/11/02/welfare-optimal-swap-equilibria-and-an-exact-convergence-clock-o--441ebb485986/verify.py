"""Reproduce the equal-part Schelling-swap theorem by exact finite enumeration.

All computations use integer counts and rational utilities; no floating-point
approximations enter the comparisons. Finite checks corroborate, rather than
replace, the all-size proof in RESULT.md.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial


def occupations(mask, parts):
    return tuple(sum((mask >> v) & 1 for v in part) for part in parts)


def welfare(mask, parts, neighbours):
    return sum(Fraction(sum(((mask >> x) & 1) == ((mask >> j) & 1)
                            for j in neighbours[x]), len(neighbours[x]))
               for x in range(len(neighbours)))


def graph(parts):
    n = sum(len(p) for p in parts)
    which = {v: i for i,p in enumerate(parts) for v in p}
    return tuple(tuple(w for w in range(n) if which[w] != which[v])
                 for v in range(n))


def improvement(mask, u, v, neighbours):
    if ((mask >> u) & 1) == ((mask >> v) & 1):
        return False
    old_u = Fraction(sum(((mask >> u)&1) == ((mask >> x)&1) for x in neighbours[u]),len(neighbours[u]))
    old_v = Fraction(sum(((mask >> v)&1) == ((mask >> x)&1) for x in neighbours[v]),len(neighbours[v]))
    new_mask = mask ^ (1 << u) ^ (1 << v)
    new_u = Fraction(sum(((new_mask >> u)&1) == ((new_mask >> x)&1) for x in neighbours[u]),len(neighbours[u]))
    new_v = Fraction(sum(((new_mask >> v)&1) == ((new_mask >> x)&1) for x in neighbours[v]),len(neighbours[v]))
    return new_v > old_u and new_u > old_v


def stable(mask, neighbours):
    for u in range(len(neighbours)):
        for v in range(u+1,len(neighbours)):
            if improvement(mask,u,v,neighbours):
                return False
    return True


def formula_count(m,k,R):
    q,s=divmod(R,m)
    return comb(m,s)*comb(k,q+1)**s*comb(k,q)**(m-s)


def finite_equal_part():
    profiles=0; counts=0; utilitychecks=0
    for m,k in ((3,2),(4,2),(5,2),(3,3),(4,3),(3,4)):
        n=m*k
        parts=[list(range(i*k,(i+1)*k)) for i in range(m)]
        adj=graph(parts)
        for R in range(n+1):
            eq=0; optimum=None; results=[]
            for chosen in combinations(range(n),R):
                mask=sum(1<<v for v in chosen)
                occupancy=occupations(mask,parts)
                ex=max(occupancy)-min(occupancy)<=1
                actual=stable(mask,adj)
                assert ex==actual,(m,k,R,chosen,occupancy,ex,actual)
                W=welfare(mask,parts,adj)
                results.append((actual,W))
                optimum=W if optimum is None or W>optimum else optimum
                eq+=actual; profiles+=1
            assert eq==formula_count(m,k,R),(m,k,R,eq,formula_count(m,k,R))
            assert all((W==optimum)==actual for actual,W in results)
            counts+=1
    return profiles,counts


def finite_cocktail_party():
    profiles=0; classes=0; jumps=0
    for m in range(3,7):
        parts=[(2*i,2*i+1) for i in range(m)]
        adj=graph(parts);n=2*m
        for s in range(m+1):
            observed={}
            expected=[]
            for t in range(s//2+1):
                num=factorial(m)*2**(s-2*t)//(factorial(t)*factorial(s-2*t)*factorial(m-s+t))
                expected.append(num)
            for chosen in combinations(range(n),s):
                mask=sum(1<<v for v in chosen)
                occ=occupations(mask,parts)
                t=occ.count(2)
                observed[t]=observed.get(t,0)+1
                for u in range(n):
                    for v in range(u+1,n):
                        if improvement(mask,u,v,adj):
                            after=occupations(mask^(1<<u)^(1<<v),parts)
                            assert after.count(2)==t-1
                            jumps+=1
                assert stable(mask,adj)==(t==0)
                profiles+=1
            assert [observed.get(t,0) for t in range(s//2+1)]==expected,(m,s,observed,expected)
            assert sum(expected)==comb(n,s)
            lhs=Fraction(sum(t*expected[t] for t in range(len(expected))),comb(n,s))
            rhs=Fraction(s*(s-1),2*(2*m-1))
            assert lhs==rhs,(m,s,lhs,rhs)
            variance=Fraction(sum(t*t*expected[t] for t in range(len(expected))),comb(n,s))-lhs*lhs
            p2=Fraction(s*(s-1),n*(n-1))
            p4=(Fraction(s*(s-1)*(s-2)*(s-3),n*(n-1)*(n-2)*(n-3)) if s>=4 else Fraction(0))
            expected_variance=m*p2*(1-p2)+m*(m-1)*(p4-p2*p2)
            assert variance==expected_variance,(m,s,variance,expected_variance)
            classes+=1
    return profiles,classes,jumps


def unequal_witness():
    sizes=(1,3,3)
    parts=[]; j=0
    for size in sizes:
        parts.append(list(range(j,j+size)));j+=size
    adj=graph(parts)
    R=3; candidates=[]
    for chosen in combinations(range(7),R):
        mask=sum(1<<v for v in chosen)
        candidates.append((occupations(mask,parts),welfare(mask,parts,adj),stable(mask,adj)))
    bad=[(r,w) for r,w,st in candidates if st and w<max(w0 for _,w0,_ in candidates)]
    assert bad, 'unequal-part counterexample expected'
    return len(bad),bad[0],max(w0 for _,w0,_ in candidates)



def nonunique_three_seat_clock():
    parts=[(0,1,2),(3,4,5),(6,7,8)]
    adj=graph(parts)
    start=sum(1<<v for v in (0,1,2,3))
    assert occupations(start,parts)==(3,1,0)
    assert improvement(start,0,6,adj)
    short=start^(1<<0)^(1<<6)
    assert occupations(short,parts)==(2,1,1) and stable(short,adj)
    assert improvement(start,0,4,adj)
    mid=start^(1<<0)^(1<<4)
    assert occupations(mid,parts)==(2,2,0)
    assert improvement(mid,1,6,adj)
    long=mid^(1<<1)^(1<<6)
    assert occupations(long,parts)==(1,2,1) and stable(long,adj)
    return (1,2)

if __name__=='__main__':
    a=finite_equal_part()
    b=finite_cocktail_party()
    c=unequal_witness()
    d=nonunique_three_seat_clock()
    print('Equal-part profiles and parameter classes:',a)
    print('Cocktail-party profiles, parameter classes, profitable switches:',b)
    print('Unequal-part counterexample:',c)
    print('Three-seat nonunique improvement lengths:',d)
    print('ALL EXACT CHECKS PASSED')
