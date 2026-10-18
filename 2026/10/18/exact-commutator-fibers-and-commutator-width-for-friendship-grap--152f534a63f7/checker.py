"""Independent exhaustive checks of commutator-word fibers for friendship graphical groups.
Only finite-field vertex-coordinate pairs are needed: central coordinates multiply every fiber by q^(6m).
Run: python3 friendship_commutator_checker.py
"""
from itertools import product
from collections import Counter
from math import prod


def gf(q):
    if q in (2,3,5):
        return [[(a+b)%q for b in range(q)] for a in range(q)], [[(a*b)%q for b in range(q)] for a in range(q)]
    if q==4:
        # F_2[t]/(t^2+t+1): two-bit low-to-high polynomials
        def mul(a,b):
            out=0
            for i in range(2):
                if (a>>i)&1:out ^= b<<i
            for i in (2,):
                if (out>>i)&1:out ^= 7<<(i-2)
            return out
        return [[a^b for b in range(q)] for a in range(q)], [[mul(a,b) for b in range(q)] for a in range(q)]
    raise ValueError(q)


def predict(target,q,m):
    spokes=[target[3*i:3*i+2] for i in range(m)]
    cs=[target[3*i+2] for i in range(m)]
    allzero=all(a==0 and b==0 for a,b in spokes)
    out=0
    if allzero:
        out += prod(q*(q*q-1) if c else q**3+q*q-q for c in cs)
    if all((a or b or c==0) for (a,b),c in zip(spokes,cs)):
        active=sum(bool(a or b) for a,b in spokes)
        out += (q*q-1)*q**(2*m-active)
    return out


def verify(q,m):
    add,mul=gf(q)
    neg=[next(b for b in range(q) if add[a][b]==0) for a in range(q)]
    n=2*m+1
    vectors=list(product(range(q),repeat=n))
    counts=Counter()
    for x in vectors:
        for y in vectors:
            z=[]
            for i in range(m):
                a,b=2*i+1,2*i+2
                z.append(add[mul[x[0]][y[a]]][neg[mul[x[a]][y[0]]]])
                z.append(add[mul[x[0]][y[b]]][neg[mul[x[b]][y[0]]]])
                z.append(add[mul[x[a]][y[b]]][neg[mul[x[b]][y[a]]]])
            counts[tuple(z)] += 1
    assert sum(counts.values())==q**(4*m+2)
    expect_image=(q**3-q+1)**m+q**m-1
    assert len(counts)==expect_image,(q,m,len(counts),expect_image)
    for target in product(range(q),repeat=3*m):
        p=predict(target,q,m)
        assert counts[target]==p,(q,m,target,counts[target],p)
    # Independently obtain the zero-target count from the class equation.
    # For the chosen graph, rank ad_x follows from support neighborhoods.
    class_number=0
    for x in vectors:
        support=[i for i,u in enumerate(x) if u]
        if not support:
            rank=0
        elif x[0]:
            rank=2*m
        else:
            occupied=sum(bool(x[2*i+1] or x[2*i+2]) for i in range(m))
            rank=occupied+1
        class_number += q**(3*m-rank)
    assert class_number * q**(2*m+1) == counts[(0,)*(3*m)] * q**(3*m)
    zero=(0,)*(3*m)
    expect0=(q*q-1)*q**(2*m)+(q**3+q*q-q)**m
    assert counts[zero]==expect0
    # Width test. Width 1 for m=1, exactly 2 for m>1.
    assert (len(counts)==q**(3*m)) == (m==1)
    # Every central vector decomposes as a sum of one all-zero-blade-coordinate
    # commutator and another whose only possibly nonzero coordinates are the
    # per-blade internal edge coordinates.
    for target in product(range(q),repeat=3*m):
        hub=tuple(t if k%3!=2 else 0 for k,t in enumerate(target))
        internal=tuple(t if k%3==2 else 0 for k,t in enumerate(target))
        assert counts[hub]>0 and counts[internal]>0
        assert all(add[a][b]==c for a,b,c in zip(hub,internal,target))
    print('EXACT_CHECK_PASS',f'q={q}',f'm={m}',f'vertices={n}',f'targets={q**(3*m)}',f'pair_count={q**(4*m+2)}',f'image={expect_image}',f'zero_fiber={expect0}')

if __name__=='__main__':
    for q,m in [(2,1),(3,1),(2,2),(3,2),(4,2),(2,3),(5,1)]:
        verify(q,m)
    print('ALL_EXACT_CHECKS_PASSED')
