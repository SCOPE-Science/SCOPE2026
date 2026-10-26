"""Independent finite checks for catenary degrees of consecutive tetrahedral semigroups.

Run: python3 verify.py.  The published infinite argument is separate from
these deliberately bounded exhaustive critical-fiber computations.
"""
from math import gcd
from functools import reduce


def tetra(m):
    return m * (m + 1) * (m + 2) // 6


def proposed(n):
    if n % 6 in (3, 5):
        return n + 5
    if n % 6 == 0:
        return n + 4
    return n + 3


def relations(n):
    r = n % 6
    e = lambda i, k: tuple(k if j == i else 0 for j in range(4))
    add = lambda *xs: tuple(sum(x[j] for x in xs) for j in range(4))
    if r == 0:
        return [
            (e(3,(n+2)//2),add(e(2,2),e(1,(n+4)//2))),
            (e(2,n+1),e(1,n+4)),
            (e(1,n//3),e(0,(n+3)//3)),
        ]
    if r == 1:
        return [
            (e(3,(n+2)//3),e(2,(n+5)//3)),
            (e(2,(n+1)//2),add(e(1,2),e(0,(n+3)//2))),
            (e(1,n),e(0,n+3)),
        ]
    if r == 2:
        return [
            (e(3,(n+2)//2),add(e(2,2),e(1,(n+4)//2))),
            (e(2,(n+1)//3),e(1,(n+4)//3)),
            (e(1,n),e(0,n+3)),
        ]
    if r == 3:
        return [
            (e(3,n+2),e(2,n+5)),
            (e(2,(n+1)//2),add(e(1,2),e(0,(n+3)//2))),
            (e(1,n//3),e(0,(n+3)//3)),
        ]
    if r == 4:
        return [
            (e(0,n+3),e(1,n)),
            (e(1,(n+4)//2),add(e(2,(n-1)//3),e(3,(n+2)//6))),
            (e(2,(n+5)//3),e(3,(n+2)//3)),
        ]
    return [
        (e(0,(n+3)//2),add(e(1,(n-2)//3),e(2,(n+1)//6))),
        (e(1,(n+4)//3),e(2,(n+1)//3)),
        (e(2,n+5),e(3,n+2)),
    ]


def all_factors(a, target):
    out = []
    for x in range(target//a[0]+1):
        rem = target-x*a[0]
        for y in range(rem//a[1]+1):
            rem2=rem-y*a[1]
            for z in range(rem2//a[2]+1):
                rem3=rem2-z*a[2]
                if rem3 % a[3] == 0:
                    out.append((x,y,z,rem3//a[3]))
    return out


def distance(x,y):
    common = sum(min(i,j) for i,j in zip(x,y))
    return max(sum(x)-common,sum(y)-common)


def fiber_catenary(facts):
    """Minimum bottleneck spanning tree (Prim), exact finite-factorization calculation."""
    count=len(facts)
    if count<=1:return 0
    reached={0}
    nearest=[distance(facts[0],z) for z in facts]
    maximum=0
    for _ in range(count-1):
        j=min((j for j in range(count) if j not in reached),key=lambda j:nearest[j])
        maximum=max(maximum,nearest[j])
        reached.add(j)
        for k in range(count):
            if k not in reached:
                nearest[k]=min(nearest[k],distance(facts[j],facts[k]))
    return maximum


def presentation_connects(facts, relations):
    """Check presentation moves connect the full critical fiber."""
    available=set(facts)
    pending=[facts[0]]
    seen={facts[0]}
    while pending:
        current=pending.pop()
        for left,right in relations:
            for start,finish in ((left,right),(right,left)):
                if all(v >= need for v,need in zip(current,start)):
                    following=tuple(v-need+add for v,need,add in zip(current,start,finish))
                    assert following in available
                    if following not in seen:
                        seen.add(following)
                        pending.append(following)
    return len(seen)==len(available)


def run():
    checked_fibers=0
    max_fiber=0
    for n in range(4,34):
        a=[tetra(i) for i in range(n,n+4)]
        assert reduce(gcd,a)==1
        expected=proposed(n)
        rel=relations(n)
        assert len(rel)==3
        betti=set()
        for left,right in rel:
            w1=sum(i*j for i,j in zip(left,a))
            w2=sum(i*j for i,j in zip(right,a))
            assert w1==w2, (n,left,right)
            betti.add(w1)
            assert max(sum(left),sum(right))<=expected,(n,left,right)
        largest=0
        for b in sorted(betti):
            facts=all_factors(a,b)
            assert len(facts)>1,(n,b)
            assert presentation_connects(facts,rel),(n,b)
            actual=fiber_catenary(facts)
            largest=max(largest,actual)
            checked_fibers+=1
            max_fiber=max(max_fiber,len(facts))
        assert largest==expected,(n,largest,expected)
    print('PASS: n=4..33, 30 semigroup parameters; '
          f'{checked_fibers} distinct critical fibers; '
          f'maximum fiber cardinality {max_fiber}; '
          'all presentation identities, critical-fiber connectivity, and catenary formulas match.')


if __name__=='__main__':
    run()
