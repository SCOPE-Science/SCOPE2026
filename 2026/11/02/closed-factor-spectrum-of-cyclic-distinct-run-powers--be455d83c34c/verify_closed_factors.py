"""Literal finite verification of a closed-factor classification for cyclic distinct-run powers.
Only standard Python; no external packages."""
from collections import Counter
from itertools import product


def is_closed(w):
    """Literal definition: a nonempty proper border appearing at its two ends only."""
    if len(w) == 1:
        return True
    for l in range(len(w) - 1, 0, -1):
        b = w[:l]
        if w[-l:] == b:
            return sum(w.startswith(b, j) for j in range(len(w) - l + 1)) == 2
    return False


def predicted_factors(run_lengths, repeats):
    q = len(run_lengths)
    p = sum(run_lengths)
    P = ''.join(chr(65 + i) * r for i, r in enumerate(run_lengths))
    W = P * repeats
    A = {chr(65+i) * s for i,r in enumerate(run_lengths) for s in range(1,r+1)}
    B = set()
    for i,r in enumerate(run_lengths):
        middle = ''.join(chr(65+((i+j)%q)) * run_lengths[(i+j)%q]
                         for j in range(1,q))
        for s in range(1,r+1):
            x = chr(65+i)*s
            B.add(x + middle + x)
    C = set()
    for m in range(1, (repeats-1)*p + 1):
        h = min(p, (repeats-1)*p-m+1)
        for phase in range(h):
            if len(set(W[phase:phase+m])) > 1:
                C.add(W[phase:phase+p+m])
    assert not A&B and not A&C and not B&C
    return A|B|C, (len(A),len(B),len(C))


def predicted_profile(run_lengths,repeats):
    p = sum(run_lengths)
    hist=Counter()
    for r in run_lengths:
        for s in range(1,r+1):
            hist[s] += 1
    for r in run_lengths:
        for s in range(1,r+1):
            hist[p-r+2*s] += 1
    for m in range(1, (repeats-1)*p+1):
        h=min(p, (repeats-1)*p-m+1)
        excluded=sum(max(0,r-m+1) for r in run_lengths)
        assert h >= excluded
        hist[p+m] += h-excluded
    return +hist


def check(rr,k):
    W=''.join(chr(65+i)*r for i,r in enumerate(rr))*k
    seen={W[i:j] for i in range(len(W)) for j in range(i+1,len(W)+1)}
    literal={x for x in seen if is_closed(x)}
    expected, parts=predicted_factors(rr,k)
    assert literal==expected, (rr,k,len(literal),len(expected),literal^expected)
    hist=Counter(map(len,literal))
    assert +hist==predicted_profile(rr,k), (rr,k,hist,predicted_profile(rr,k))
    p=sum(rr)
    total=(k-2)*p*p+(p*p-sum(r*r for r in rr))//2+2*p
    assert len(literal)==total, (rr,k,len(literal),total)
    return len(literal),len(seen),parts


def main():
    families=0; distinct_factors=0; closed_factors=0; counts=[0,0,0]
    for q in (3,4,5):
        for rr in product(range(1,5),repeat=q):
            for k in (2,3,4):
                got, allf, parts=check(rr,k)
                families += 1; closed_factors += got; distinct_factors += allf
                counts=[x+y for x,y in zip(counts,parts)]
    print(f'VERIFY_OK families={families} distinct_factor_instances={distinct_factors} '
          f'closed_factor_instances={closed_factors} disjoint_type_counts={counts} '
          'literal_sets_profiles_and_formula=TRUE')

if __name__ == '__main__':
    main()
