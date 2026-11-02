"""Finite exact-arithmetic checks of the two-seat reciprocal-JR support frontier.
All comparisons use integers and no floating point.
"""
from itertools import product, combinations

def jr(maskset, q, W, n):
    covered = maskset[W[0]] | maskset[W[1]]
    uncovered = ((1<<n)-1) ^ covered
    for mask, val in zip(maskset, q):
        if 2*(mask & uncovered).bit_count()*val >= 12*n:
            return False
    return True

def frontier(n, d):
    if 2*d >= n: return (1,1)
    return 3*n - 2*d, 4*(n-d)

def check_case(n, masks, q, d):
    pairs = tuple(combinations(range(len(q)),2))
    top = max(sum(q[i] for i in p) for p in pairs)
    winners = [p for p in pairs if jr(masks,q,p,n)]
    assert winners, ('no_JR',n,masks,q)
    best = max(sum(q[i] for i in p) for p in winners)
    num,den = frontier(n,d)
    assert den*best >= num*top, ('ratio',n,d,masks,q,best,top)
    # Constructive one-replacement repair of a quality-maximizing committee.
    W=max(pairs,key=lambda p: sum(q[i] for i in p))
    if not jr(masks,q,W,n):
        cover=masks[W[0]]|masks[W[1]]
        U=((1<<n)-1)^cover
        hits=[i for i in range(len(q)) if i not in W and 2*(masks[i]&U).bit_count()*q[i]>=12*n]
        assert hits
        top1=max(W, key=lambda i:q[i]); chosen=(top1,hits[0])
        assert jr(masks,q,chosen,n),('repair',n,d,masks,q,W,chosen)
        assert den*sum(q[i] for i in chosen)>=num*top
    return best == top, best*den == num*top

def main():
    cases=0; tight=0; unaffected=0
    for n,m,vals in ((2,3,(6,8,9,12)),(3,3,(6,8,9,12)),(4,3,(6,8,9,12)),(3,4,(6,9,12))):
        allmasks=range(1,1<<n)
        for masks in product(allmasks,repeat=m):
            d=min(x.bit_count() for x in masks)
            for q in product(vals,repeat=m):
                u,t = check_case(n,masks,q,d)
                cases += 1; unaffected += u; tight += t
    # Every (n,d) in a grid has a canonical three-candidate extremizer.
    canonical=0
    for n in range(3,61):
        for d in range(1,n//2 + 1):
            supporters_high=(1<<d)-1
            supporters_low=((1<<n)-1)^supporters_high
            if d*2>=n: continue
            # Use quality q0=n/[2(n-d)], represented by exact fractions.
            from fractions import Fraction
            q0=Fraction(n,2*(n-d))
            Q=(Fraction(1),Fraction(1),q0)
            masks=(supporters_high,supporters_high,supporters_low)
            def qualifies(W):
                union=masks[W[0]]|masks[W[1]]
                U=((1<<n)-1)^union
                return all(2*(m&U).bit_count()*z<n for m,z in zip(masks,Q))
            legal=[p for p in combinations(range(3),2) if qualifies(p)]
            assert legal==[(0,2),(1,2)],(n,d,legal)
            a=Fraction(3*n-2*d,4*(n-d))
            assert max(sum(Q[i] for i in p) for p in legal)/2 == a
            canonical +=1
    print(f'VERIFY_OK exhaustive_profiles={cases} quality_optimal_profiles={unaffected} equality_profiles={tight} exact_canonical_pairs={canonical}')
if __name__=='__main__': main()
