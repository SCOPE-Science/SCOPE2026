"""Independent finite checks for three-seat sparse-approval JR/welfare compatibility.
Python 3 standard library.  The theorem itself is analytical; exhaustive tests
are restricted to specified finite candidate counts and anonymous profiles.
"""
from itertools import combinations
from math import comb
from collections import Counter


def all_weak_compositions(n, dim):
    if dim == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for tail in all_weak_compositions(n - first, dim - 1):
                yield (first,) + tail


def properties(ballots, counts, m, k=3):
    # ballots bit masks, counts of identical ballots, k=3.
    scores = [sum(c for b, c in zip(ballots, counts) if b & (1 << i)) for i in range(m)]
    welfare_opt = sorted(range(m), key=lambda c: scores[c], reverse=True)
    best = sum(scores[c] for c in welfare_opt[:k])
    quota = (sum(counts) + k - 1)//k
    exists = False
    for chosen in combinations(range(m), k):
        if sum(scores[c] for c in chosen) != best:
            continue
        wm = sum(1<<c for c in chosen)
        jr = True
        for cand in range(m):
            if wm & (1 << cand):
                continue
            num = sum(weight for b, weight in zip(ballots, counts)
                      if (b & wm)==0 and (b & (1<<cand)))
            if num >= quota:
                jr = False
                break
        if jr:
            exists = True
            break
    return exists, scores, best


def properties_k(ballots,counts,m,k):
    scores = [sum(c for b,c in zip(ballots,counts) if b & (1<<i)) for i in range(m)]
    top = sum(sorted(scores, reverse=True)[:k])
    q=(sum(counts)+k-1)//k
    for chosen in combinations(range(m),k):
        if sum(scores[c] for c in chosen)!=top: continue
        wm=sum(1<<c for c in chosen)
        if all(sum(c for b,c in zip(ballots,counts)
                   if not(b & wm) and b & (1<<j))<q for j in range(m) if not wm&(1<<j)):
            return True,scores,top
    return False,scores,top

def witness(n):
    q = (n+2)//3
    r = n-q
    bases = [r//3]*3
    for i in range(r%3): bases[i]+=1
    # 3 pair types AB, BC, AC; plus q singleton x voters.
    ballots = [0b0011, 0b0110, 0b0101, 0b1000]
    counts = bases + [q]
    e, sc, opt = properties(ballots, counts, 4)
    return q,r,bases,sc,opt,e


def test_exhaustive(m, limit_n):
    ballots = [sum(1<<j for j in indices) for l in (1,2) for indices in combinations(range(m),l)]
    total = 0
    for n in range(1,limit_n+1):
        q = (n+2)//3
        expected_every = 2*n < 5*q+3
        bad = 0
        witness_bad = False
        for c in all_weak_compositions(n,len(ballots)):
            good, scores, best = properties(ballots,c,m)
            total+=1
            if not good:
                bad+=1
                if expected_every:
                    raise AssertionError((m,n,c,scores,best))
                witness_bad=True
        # For n with a negative threshold m=4 already provides counterexample.
        if m==4 and not expected_every:
            assert witness_bad
        print('EXHAUSTIVE', 'm',m,'n',n,'profiles',comb(n+len(ballots)-1,len(ballots)-1),
              'no_optimal_JR',bad,'universal_guarantee',expected_every,flush=True)
    return total

if __name__=='__main__':
    for n in range(1,101):
        q,r,bases,scores,opt,compatible=witness(n)
        should_fail=2*n>=5*q+3
        if should_fail:
            assert not compatible and min(scores[:3])>scores[3],(n,q,scores)
        if n in [8,9,10,11,12,13,14,15,16,17,18,19,25,40,100]:
            print('WITNESS',n,'q',q,'pair_counts',bases,'approval_scores',scores,
                  'max_welfare',opt,'failure_condition',should_fail,flush=True)
    total=test_exhaustive(4,12)
    total+=test_exhaustive(5,6)
    # Separate exhaustive checks of the k=2 and one-approval positive guarantees.
    for m, k, maxn, max_ballot in [(4,2,9,2),(5,2,6,2),(5,3,10,1)]:
        bs = [sum(1<<j for j in ids)
              for l in range(1,max_ballot+1)
              for ids in combinations(range(m),l)]
        cnt = 0
        for n in range(1,maxn+1):
            for c in all_weak_compositions(n,len(bs)):
                good,_,_ = properties_k(bs,c,m,k)
                assert good,(m,k,n,c)
                cnt+=1
        total += cnt
        print('AUX_EXHAUSTIVE',m,k,maxn,max_ballot,cnt,flush=True)
    print('VERIFY_OK anonymous_profiles',total,'witness_range',100,flush=True)
