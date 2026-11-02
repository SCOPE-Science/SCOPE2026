"""Exact half-open interval certificate for five cyclic rotated odometers.
Only Python's standard library is required; no numerical sampling is used.
"""
from fractions import Fraction as Q
from collections import defaultdict

ZERO, ONE, QUARTER = Q(0), Q(1), Q(1,4)


def meet(a, b):
    l, u = max(a[0], b[0]), min(a[1], b[1])
    return (l,u) if l < u else None


def canonical(intervals):
    if not intervals: return []
    intervals = sorted(intervals)
    out = [intervals[0]]
    for l, u in intervals[1:]:
        a,b = out[-1]
        if l <= b: out[-1] = (a, max(u,b))
        else: out.append((l,u))
    return out


def first_returns(s):
    # surviving original x-intervals, and their current-image translation.
    survivors = [((ZERO, QUARTER), ZERO)]
    found = []
    for n in range(1, 12):
        fresh = []
        for iv, shift in survivors:
            for j in range(5):
                # x+shift lies in the j-th fifth before the rational rotation
                sub = meet(iv, (Q(j,5)-shift,Q(j+1,5)-shift))
                if sub is None: continue
                rotated = shift + Q((j+s)%5-j,5)
                # Before the first entry to B, the odometer acts by only
                # two translations, +1/2 and -1/4; the third branch returns.
                for a,b,translation,returns in (
                    (ZERO,Q(1,2),Q(1,2),False),
                    (Q(1,2),Q(3,4),-Q(1,4),False),
                    (Q(3,4),ONE,None,True),
                ):
                    part=meet(sub,(a-rotated,b-rotated))
                    if part is None: continue
                    if returns: found.append((part,n))
                    else: fresh.append((part,rotated+translation))
        grouped=defaultdict(list)
        for iv,shift in fresh: grouped[shift].append(iv)
        survivors=[(iv,shift) for shift,ivs in grouped.items() for iv in canonical(ivs)]
        if not survivors:
            merged=defaultdict(list)
            for interval, time in found: merged[time].append(interval)
            return sorted((interval,time) for time,parts in merged.items() for interval in canonical(parts))
    raise AssertionError('Unresolved first-return branch')


def affine_map_on(iv,s):
    """Return either a unique affine formula F_s(x)=x+t on all iv or split."""
    (l,u)=iv
    out=[]
    for j in range(5):
        piece=meet(iv,(Q(j,5),Q(j+1,5)))
        if piece is None: continue
        rot=Q((j+s)%5-j,5)
        for n in range(1,18):
            a=1-Q(1,2**(n-1));b=1-Q(1,2**n)
            pre=meet(piece,(a-rot,b-rot))
            if pre is not None:
                shift=rot-ONE+Q(3,2**n)
                out.append((pre,shift))
        if any(u>1-Q(1,2**17) for l,u in [piece]):
            raise AssertionError('dyadic limit reached; choose smaller intervals')
    grouped=defaultdict(list)
    for piece,delta in out: grouped[delta].append(piece)
    return [(piece,delta) for delta,parts in grouped.items() for piece in canonical(parts)]


def exact_checks():
    expected=[
      [((Q(0),Q(1,4)),4)],
      [((Q(0),Q(1,10)),2),((Q(1,10),Q(3,20)),10),((Q(3,20),Q(1,4)),3)],
      [((Q(0),Q(1,10)),6),((Q(1,10),Q(1,5)),3),((Q(1,5),Q(1,4)),2)],
      [((Q(0),Q(1,20)),2),((Q(1,20),Q(3,20)),8),((Q(3,20),Q(1,4)),1)],
      [((Q(0),Q(1,5)),1),((Q(1,5),Q(1,4)),6)]
    ]
    for s in range(5):
        got=first_returns(s)
        assert got==expected[s],(s,got)
        assert sum((u-l for (l,u),t in got),ZERO)==QUARTER
        mean=4*sum(((u-l)*t for (l,u),t in got),ZERO)
        second=4*sum(((u-l)*t*t for (l,u),t in got),ZERO)
        variance=second-mean*mean
        assert (mean,variance)==[(Q(4),Q(0)),(Q(4),Q(46,5)),(Q(4),Q(14,5)),(Q(4),Q(54,5)),(Q(2),Q(4))][s]
    # The five non-B periodic intervals for s=4 form a complete cycle.
    J=[(Q(1,4),Q(7,20)),(Q(11,20),Q(13,20)),
       (Q(17,20),Q(19,20)),(Q(2,5),Q(1,2)),(Q(7,10),Q(4,5))]
    for k,I in enumerate(J):
        got=affine_map_on(I,4)
        assert len(got)==1,(I,got)
        iv,delta=got[0]
        assert iv==I
        assert (I[0]+delta,I[1]+delta)==J[(k+1)%5]
    # Pointwise no returns in C, and positive-length union of the tower and C is full.
    # s=4 first-return tower consists of B plus its five non-base images.
    tower=[(Q(0),Q(1,5)),(Q(1,5),Q(1,4))]
    live=[((Q(1,5),Q(1,4)),ZERO)]
    for _ in range(5):
        out=[]
        for I,sh in live:
            for part,delta in affine_map_on((I[0]+sh,I[1]+sh),4):
                shifted=(part[0]+delta,part[1]+delta)
                out.append((shifted,ZERO))
                tower.append(shifted)
        live=out
    assert sum((u-l for l,u in J),ZERO)==Q(1,2)
    assert sum((u-l for l,u in tower), ZERO)==Q(1,2)
    assert sum((u-l for l,u in [*tower,*J]), ZERO)==ONE
    whole=sorted([*tower,*J])
    assert whole[0][0]==ZERO and whole[-1][1]==ONE
    assert all(whole[i][1]==whole[i+1][0] for i in range(len(whole)-1))
    assert canonical(whole)==[(ZERO,ONE)]
    print('PASS: five complete first-return partitions, means, variances, 5-cycle, full partition')

if __name__=='__main__': exact_checks()
