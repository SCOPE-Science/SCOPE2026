"""Finite-state exact checks for regular-hypergraph fixation comparison.

Requires Python 3 and sympy.  Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix, Rational


def transitions(n, edges, r, mask, weights=None):
    if weights is None:
        weights = [F(1)]*len(edges)
    degrees = [sum(w for e,w in zip(edges,weights) if v in e) for v in range(n)]
    if min(degrees) < 1:
        raise ValueError('isolated vertex')
    total = sum(r if ((mask >> v) & 1) else F(1) for v in range(n))
    out = {}
    for v in range(n):
        fitness = r if ((mask >> v) & 1) else F(1)
        for edge, weight in zip(edges, weights):
            if v not in edge:
                continue
            new = mask
            for w in edge:
                if ((mask >> v) & 1):
                    new |= (1 << w)
                else:
                    new &= ~(1 << w)
            out[new] = out.get(new, F(0)) + fitness * weight / total / degrees[v]
    assert sum(out.values()) == 1
    return out


def fixation(n, edges, r, weights=None):
    k = (1 << n)-2
    M = [[Rational(int(i == j)) for j in range(k)] for i in range(k)]
    b = [Rational(0) for _ in range(k)]
    for mask in range(1, (1 << n)-1):
        for new,prob in transitions(n, edges, r, mask, weights).items():
            p = Rational(prob.numerator, prob.denominator)
            if new == (1 << n)-1:
                b[mask-1] += p
            elif new != 0:
                M[mask-1][new-1] -= p
    sol = Matrix(M).LUsolve(Matrix(b))
    return {mask:F(int(sol[mask-1].p),int(sol[mask-1].q))
            for mask in range(1,(1 << n)-1)}


def moran(n,m,r):
    if r==1:
        return F(m,n)
    return (1-r**(-m))/(1-r**(-n))


def check(n,edges,r,strict,weights=None):
    if weights is None:
        weights = [F(1)]*len(edges)
    degs=[sum(w for e,w in zip(edges,weights) if v in e) for v in range(n)]
    assert len(set(degs)) == 1
    probs=fixation(n,edges,r,weights)
    num_states=0
    for mask, p in probs.items():
        m=mask.bit_count()
        baseline=moran(n,m,r)
        if r==1 or not strict:
            assert p==baseline, (n,edges,r,mask,p,baseline)
        elif r>1:
            assert p<baseline, (n,edges,r,mask,p,baseline)
        else:
            assert p>baseline, (n,edges,r,mask,p,baseline)
        drift=sum(prob*r**(-new.bit_count()) for new, prob in transitions(n,edges,r,mask,weights).items())-r**(-m)
        d=degs[0]
        W=r*m+n-m
        defect=F(0)
        for e,w in zip(edges,weights):
            a=sum((mask >> v)&1 for v in e)
            b=len(e)-a
            defect+=w*(a*r*(r**(-b)-1)+b*(r**a-1))
        assert drift==r**(-m)*defect/(d*W), (n,edges,weights,r,mask,drift,defect)
        assert drift>=0
        num_states+=1
    return num_states


def edge_family(n,kind):
    if kind=='complete3':
        return [frozenset(e) for e in combinations(range(n),3)]
    if kind=='cyclic3':
        return list(dict.fromkeys(frozenset(((v+j)%n for j in range(3))) for v in range(n)))
    if kind=='mixed4':
        return [frozenset(range(n))] + [frozenset((v,(v+1)%n)) for v in range(n)]
    if kind=='paircycle':
        return [frozenset((v,(v+1)%n)) for v in range(n)]
    if kind=='oneedge':
        return [frozenset(range(n))]
    raise ValueError(kind)


def main():
    reps = [
        (3,'oneedge',[F(1,2),F(1),F(2),F(3)]),
        (4,'complete3',[F(1,2),F(1),F(2)]),
        (5,'cyclic3',[F(1,2),F(1),F(2)]),
        (4,'mixed4',[F(1,2),F(1),F(2)]),
        (5,'paircycle',[F(1,2),F(1),F(2)]),
    ]
    total=0
    for n,kind,rs in reps:
        for r in rs:
            count=check(n,edge_family(n,kind),r,kind!='paircycle')
            total += count
            print(kind,n,r,'states',count,'OK')
    weighted_edges=edge_family(4,'mixed4')
    weighted_weights=[F(3), F(1), F(2), F(1), F(2)]
    for r in (F(1,2),F(1),F(2)):
        count=check(4,weighted_edges,r,True,weighted_weights)
        total+=count
        print('balanced weighted mixed4',4,r,'states',count,'OK')
    for a in range(1,8):
        for b in range(1,8):
            for r in [F(1,5),F(1,2),F(2,3),F(3,2),F(2),F(4)]:
                q = a*r*(r**(-b)-1)+b*(r**a-1)
                assert q > 0 if a+b>=3 else q==0
    print('PASS: exact fixation comparison on', total, 'nonabsorbing states; 294 exact mixed-hyperedge drift checks.')

if __name__=='__main__':
    main()
