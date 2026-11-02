"""Reproducible finite checks for colored-hypercube star-event identities.
Run with Python 3 (standard library only). This is a finite verification,
not a substitute for the asymptotic proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict


def neighbors(d, x):
    return tuple(x ^ (1 << j) for j in range(d))


def exact_joint(d, probs, x, S, c, y, T, e):
    """Independent-site exact probability via intersection of constraints."""
    n = 1 << d
    allows = [set(range(len(probs))) for _ in range(n)]
    allows[x] &= {c}
    allows[y] &= {e}
    for z in neighbors(d, x):
        allows[z] &= set(S)
    for z in neighbors(d, y):
        allows[z] &= set(T)
    out = F(1)
    for a in allows:
        out *= sum((probs[z] for z in a), F(0))
    return out


def enumerate_events(d, q, probs):
    n = 1 << d
    palettes = [frozenset(S) for k in range(1,q) for S in combinations(range(q),k)]
    names = [(S,c) for S in palettes for c in range(q)]
    count_checks=0
    # Exhaustive two-event probabilities on small cubes, for uniform and biased colors.
    for S,c in names:
        a = sum((probs[z] for z in S),F(0))
        for x in range(n):
            assert exact_joint(d,probs,x,S,c,x,S,c)==probs[c]*a**d
            count_checks+=1
    for S,c in names:
        a = sum((probs[z] for z in S),F(0))
        for T,e in names:
            b = sum((probs[z] for z in T),F(0))
            for x in range(n):
                for y in range(n):
                    val=exact_joint(d,probs,x,S,c,y,T,e)
                    dist=(x^y).bit_count()
                    if dist>=3:
                        assert val==(probs[c]*a**d)*(probs[e]*b**d)
                    if dist==0:
                        wanted=(probs[c]*sum((probs[z] for z in S&T),F(0))**d) if c==e else F(0)
                        assert val==wanted
                    if a==F(1,2) and b==F(1,2) and x!=y and dist<=2:
                        assert val <= F(1,2)**(2*d-2)
                    count_checks+=1
    return count_checks


def enumerate_count_distribution(d, q, critical):
    n=1<<d
    hist=defaultdict(int)
    for assignment in product(range(q), repeat=n):
        counts=[]
        for S,c in critical:
            s=0
            for x in range(n):
                if assignment[x]==c and all(assignment[y] in S for y in neighbors(d,x)):
                    s+=1
            counts.append(s)
        hist[tuple(counts)]+=1
    assert sum(hist.values())==q**n
    # Means equal p_c independently of dimension for uniform, half-mass palettes.
    for i,(_,c) in enumerate(critical):
        observed=sum(cnt[i]*freq for cnt,freq in hist.items())
        assert observed*q == q**n
    return len(hist)


def main():
    checks=0
    for d,q,ps in [
        (1,2,[F(1,2)]*2),(2,2,[F(1,2)]*2),
        (3,2,[F(1,2)]*2),(4,2,[F(1,2)]*2),
        (2,3,[F(1,2),F(1,3),F(1,6)]),
        (3,3,[F(1,2),F(1,3),F(1,6)]),
        (2,4,[F(1,4)]*4),
    ]:
        checks+=enumerate_events(d,q,ps)
        print('exact-event-pairs: d=%d q=%d PASS'%(d,q))
    states=0
    for d,q in [(1,2),(2,2),(3,2),(4,2),(2,4)]:
        palettes=[frozenset(S) for k in range(1,q) for S in combinations(range(q),k) if k*2==q]
        critical=[(S,c) for S in palettes for c in range(q)]
        states+=enumerate_count_distribution(d,q,critical)
        print('full-star-count-law: d=%d q=%d PASS'%(d,q))
    # Supports exact maximum cross-palette overlap < 1/2 for a strictly positive palette.
    ps=[F(1,2),F(1,3),F(1,6)]
    H=[frozenset(S) for k in range(1,3) for S in combinations(range(3),k) if sum(ps[i] for i in S)==F(1,2)]
    assert len(H)==2 and max(sum((ps[i] for i in S&T),F(0)) for S in H for T in H if S!=T)==0
    print('ALL_CHECKS_OK exact_pair_checks=%d joint_histogram_states=%d'%(checks,states))

if __name__ == '__main__': main()
