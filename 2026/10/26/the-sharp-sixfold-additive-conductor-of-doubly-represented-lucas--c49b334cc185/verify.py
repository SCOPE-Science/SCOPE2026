"""Exact stand-alone check for additive covering of doubly represented Lucas integers.

Requires Python 3.9+, standard library only.  All arithmetic is exact.
"""
from math import isqrt


def floor_alpha_times(m):
    """floor(m*(sqrt(5)-1)/2) for positive integer m, exactly."""
    assert isinstance(m, int) and m >= 1
    return (isqrt(5 * m * m) - m) // 2


def k(n):
    assert n >= 0
    return 5 + 4*n + 3*floor_alpha_times(n+1)


WITNESSES_5 = {
    997:(5,12,30,30,920),
    998:(5,5,5,5,978),
    999:(5,16,16,121,841),
    1000:(200,200,200,200,200),
    1001:(5,5,12,30,949),
    1002:(5,5,5,5,982),
    1003:(121,121,121,320,320),
    1004:(5,77,200,200,522),
    1005:(5,5,5,12,978),
    1006:(5,5,16,16,964),
}


def bitset_no_1001():
    arr = []
    n = 0
    while k(n) <= 1001:
        arr.append(k(n))
        n += 1
    bound_mask = (1 << 1002) - 1
    reachable = 1  # bit 0
    for _ in range(6):
        following = 0
        for a in arr:
            following |= reachable << a
        reachable = following & bound_mask
    return not ((reachable >> 1001) & 1)


def candidates_fractional():
    # A: frac(alpha*m) < 170*alpha-105.
    # Rearranged as (170-m)*alpha > 105-floor(alpha*m),
    # compared by squaring (170-m)*sqrt(5) with 170-m+2*d.
    A=[]
    for m in range(1,170):
        c, d = 170-m, 105-floor_alpha_times(m)
        if d >= 0 and 5*c*c > (c+2*d)**2:
            A.append(m)
    # B: 1-frac(alpha*m) < 107-173*alpha.
    # Rearranged as (173-m)*alpha < 106-floor(alpha*m).
    B=[]
    for m in range(1,173):
        c, d = 173-m, 106-floor_alpha_times(m)
        if d >= 0 and 5*c*c < (c+2*d)**2:
            B.append(m)
    assert A == [13,34,47,68,81,89,102,123,136,157], A
    assert B == [8,21,29,42,55,63,76,97,110,118,131,144,152,165], B
    return A,B


def coefficient_is_zero(values, target):
    # Count every ordered sum of six values, with repetition permitted.
    coeff = [0]*(target+1)
    coeff[0] = 1
    for _ in range(6):
        nxt = [0]*(target+1)
        for a in values:
            for s in range(target-a+1):
                nxt[s+a] += coeff[s]
        coeff = nxt
    return coeff[target] == 0


def direct_lucas_partition_check():
    # A second independent construction of the underlying set using
    # all subsets of pairwise nonconsecutive Lucas indices.
    lucas=[2,1]
    while lucas[-1] <= 1006:
        lucas.append(lucas[-1]+lucas[-2])
    lim = len(lucas)-2
    counts=[0]*1007
    def visit(i, prev_used, total):
        if total>1006:
            return
        if i == lim+1:
            counts[total] += 1
            return
        visit(i+1, False, total)
        if not prev_used:
            visit(i+1, True, total+lucas[i])
    visit(0,False,0)
    assert max(counts[1:]) == 2
    ambiguous={n for n in range(1,1007) if counts[n]==2}
    seq=set()
    i=0
    while k(i)<=1006:
        seq.add(k(i));i+=1
    assert ambiguous==seq, (sorted(ambiguous^seq)[:15])
    return len(ambiguous)


def main():
    values=[];i=0
    while k(i)<=1006:
        values.append(k(i));i+=1
    assert values[0]==5
    assert all(k(n+1)-k(n) in (4,7) for n in range(1000))
    kvals=set(values)
    for target, witness in WITNESSES_5.items():
        assert len(witness)==5 and sum(witness)==target
        assert all(s in kvals for s in witness)
    assert bitset_no_1001()
    A,B=candidates_fractional()
    assert coefficient_is_zero(A,170)
    assert coefficient_is_zero(B,173)
    num=direct_lucas_partition_check()
    print('VERIFIED: Lucas ambiguity prefix',num,'integer witnesses 997..1006,')
    print('exact sixfold gap 1001 by independent bitset and radical coefficient tests')

if __name__=='__main__':
    main()
