# Independent mathematical audit

## correctness

PASS

In the one-based word 11010001…, a factor with a unique occurrence forces a hit in that occurrence. The factor 11 forces [1,2], and the factors 1 followed by 2^j-1 zeros followed by 1 force [2^j,2^{j+1}] at the selected even j≥2, because the consecutive powers have distinct gaps. These intervals are disjoint. The final factor 0^{2^{m-2}}1 ends uniquely at 2^m: every earlier one has a shorter preceding zero run. Its interval starts at 3·2^{m-2}, beyond all selected two-one intervals. For odd m≥3 the additional 0^{2^{m-3}}10 can only have its one at 2^{m-1}, as earlier zero runs are too short and the final one has no successor. The interval starts at 3·2^{m-3}, after the prior packing, and ends at 2^{m-1}+1<3·2^{m-2}. The counts give k+1 for m=2k and k+2 for m=2k+1. Independently checking the cited upper bound, Schaeffer–Shallit Theorem 8 uses i=k-1 in both cases: the lengths are 4·4^i and 8·4^i in the respective intervals, and adding one to their zero-based positions gives the two frozen sets of exactly those cardinalities. The case 11 alone needs one position.

## originality

PASS

The supported distinct contribution is the matching all-dyadic lower bound and hence exact minimum, not the published attractor construction. Two later indexed dyadic theorems are exactly equivalent and a later all-prefix theorem strictly subsumes it; those are coverage, not evidence of earlier priority over this frozen result.

## value

PASS

The powers-of-two characteristic word is the cited canonical automatic example with unbounded prefix attractor size. The result closes the stated optimality gap at all natural dyadic scales and gives elementary parity-sensitive packing witnesses, allowing later work to distinguish actual compression optima from greedy behavior. This is more than a few sample sizes and does not claim arbitrary prefix lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
