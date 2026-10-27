"""Independent exact checks for directed-cycle/triangle covariance in fair tournaments."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def cycles_on(n, k):
    """Each unoriented simple cycle exactly once, modulo rotation and reversal."""
    out = []
    for vertices in combinations(range(n), k):
        start = vertices[0]
        for tail in permutations(vertices[1:]):
            if tail[0] < tail[-1]:
                out.append((start,) + tail)
    assert len(out) == factorial(n) // (factorial(n-k) * 2*k)
    return out


def edge_spec(n, path):
    ix = {e:i for i,e in enumerate(combinations(range(n),2))}
    must_one = must_zero = 0
    for a, b in zip(path, path[1:] + path[:1]):
        t = 1 << ix[(min(a,b), max(a,b))]
        if a < b:
            must_one |= t
        else:
            must_zero |= t
    return must_one, must_zero


def oriented(mask, spec):
    yes, no = spec
    return (mask & yes) == yes and (mask & no) == 0


def reversed_spec(n, cycle):
    """Kept only to document the orientation convention."""
    return edge_spec(n, tuple(reversed(cycle)))


def verify():
    checked = 0
    for n in range(3,7):
        idx = {e:i for i,e in enumerate(combinations(range(n),2))}
        masks = {
            k:[(edge_spec(n,c),reversed_spec(n,c)) for c in cycles_on(n,k)]
            for k in range(3,n+1)
        }
        count = 1<<comb(n,2)
        S = {k:0 for k in masks}
        Sprod = {k:0 for k in masks}
        S3 = 0
        for mask in range(count):
            v = {
                k:sum(oriented(mask,s) or oriented(mask,t) for s,t in specs)
                for k,specs in masks.items()
            }
            x=v[3]
            S3+=x
            for k,y in v.items():
                S[k]+=y
                Sprod[k]+=x*y
        assert Fraction(S3,count)==Fraction(comb(n,3),4)
        checked += 1
        for k in masks:
            expectation=Fraction(factorial(n),factorial(n-k)*k*2**k)
            covariance=Fraction(Sprod[k],count)-Fraction(S3,count)*Fraction(S[k],count)
            desired=Fraction(factorial(n),factorial(n-k)*4*2**k)
            assert Fraction(S[k],count)==expectation,(n,k,'mean')
            assert covariance==desired,(n,k,covariance,desired)
            assert covariance == Fraction(k,4)*expectation
            checked += 3
    # Separate experiment: condition on one fixed directed k-cycle and average
    # triangle count over all unfixed arcs. This does not reuse cycle-count weights.
    n=7
    pairs=list(combinations(range(n),2))
    edge_id={p:i for i,p in enumerate(pairs)}
    triads=list(combinations(range(n),3))
    for k in (5,6,7):
        cyc=tuple(range(k))
        fixed={}
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            fixed[tuple(sorted((a,b)))] = int(a<b)
        free=[e for e in pairs if e not in fixed]
        acc=0
        for m in range(1<<len(free)):
            values=dict(fixed)
            values.update({e:(m>>j)&1 for j,e in enumerate(free)})
            def forward(a,b):
                t=values[tuple(sorted((a,b)))]
                return t if a<b else 1-t
            acc += sum((forward(a,b) and forward(b,c) and forward(c,a)) or
                       (forward(b,a) and forward(c,b) and forward(a,c))
                       for a,b,c in triads)
        observed=Fraction(acc,1<<len(free))
        assert observed==Fraction(comb(n,3),4)+Fraction(k,4),(n,k,observed)
        checked+=1
    return checked


if __name__=='__main__':
    print('PASS',verify(),'exact equalities')
