#!/usr/bin/env python3
"""Reproducible exact arithmetic tests for binary digit-shift variance."""
from fractions import Fraction
from itertools import combinations


def pair_variance(t):
    ps = [i for i in range(t.bit_length()) if (t >> i) & 1]
    energy = sum((Fraction(1, 1 << (b-a)) for a, b in combinations(ps, 2)), Fraction(0))
    return 2 * len(ps) - 2 * energy


def recurrence_variance(N):
    vals = [Fraction(0)] * (N+1)
    vals[1] = Fraction(2)
    for t in range(2, N+1):
        if t % 2 == 0:
            vals[t] = vals[t//2]
        else:
            vals[t] = 1 + (vals[t//2]+vals[t//2+1])/2
    return vals


def test():
    max_t=8191
    rec=recurrence_variance(max_t)
    for t in range(1,max_t+1):
        assert pair_variance(t) == rec[t], (t,pair_variance(t),rec[t])
    selections=0
    for width in range(2,12):
        for k in range(2,width+1):
            pos_lists=list(combinations(range(width),k))
            v=[(pair_variance(sum(1<<i for i in ps)), ps) for ps in pos_lists]
            minimum=Fraction(4)-Fraction(4,2**k)
            assert min(p for p,_ in v)==minimum
            minimizers=[ps for p,ps in v if p==minimum]
            assert all(tuple(ps)==tuple(range(ps[0],ps[0]+k)) for ps in minimizers)
            if width>k:
                outside=[(p,ps) for p,ps in v if p!=minimum]
                second=Fraction(5)-Fraction(6,2**k)
                assert min(p for p,_ in outside)==second,(width,k,second,min(p for p,_ in outside))
                second_minimizers=[ps for p,ps in outside if p==second]
                for ps in second_minimizers:
                    gaps=tuple(ps[i+1]-ps[i] for i in range(k-1))
                    assert gaps == (2,)+(1,)*(k-2) or gaps == (1,)*(k-2)+(2,),(width,k,ps)
            selections+=len(v)
    # a second, direct (non-recursive) finite sample of increment moments
    samples={}
    N=1<<18
    for t in (1,3,5,7,11,13,23,29,41,85):
        v=sum(( (n+t).bit_count()-n.bit_count() )**2 for n in range(N))/N
        samples[t]=(float(pair_variance(t)),v)
        assert abs(float(pair_variance(t))-v)<0.02, (t,v)
    print('VERIFY_OK',f'checked_t={max_t}',f'exhaustive_binary_subsets={selections}',f'direct_samples={len(samples)}',f'sample_size_each={N}',f'exact_rationals=yes', f'finite_sample_max_error={max(abs(x-y) for x,y in samples.values()):.6g}')

if __name__=='__main__':
    test()
