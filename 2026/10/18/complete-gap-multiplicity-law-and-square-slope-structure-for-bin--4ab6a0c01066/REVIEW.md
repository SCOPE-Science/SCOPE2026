# Independent mathematical audit

## correctness

PASS

For coprime a,b the rational expression is a polynomial (check zeros of the denominator, including order two at 1). Below ab each representable integer has at most one nonnegative representation, so the coefficients are the first differences of semigroup membership. A maximal missing run of length d gives a (-1,+1) coefficient pair at exponent distance d; reciprocity counts an equal number of (+1,-1) pairs. For b=ha+r the entry block of residue x is T_[ux]_a, with T_j=hj+floor(jr/a) strictly increasing. For 2<=D<a the two endpoints can precede all D-1 interior residues iff their insertion ranks are adjacent on the circle of P_D. Reflection v -> [uD-v]_a pairs the gap just before those first two ordered endpoints with the gap just after them. Thus there are H eligible cuts and each interval from the second endpoint to the first interior insertion has width H, starting at delta+s with 0<=s<H. Summing T_(delta+s+H)-T_(delta+s) and doubling proves the formula. For D=a the sole arc is the one at the initial singleton, giving 2h, also for a=2. For r=1 the thresholds are hj; for r=a-1 the noninitial threshold differences are h+1; both advertised specializations follow. The independent denominator recurrence agrees on all 1,853 coprime pairs with 2<=a<=40 and a<b<=100 (python3 /workspace/branches/independent_replay.py 3); the finite computation is not the proof. The frozen verifier was inspected, not executed.

## originality

PASS

The prior exact maximal-gap and ±1 laws and the prior general gap-support classification are covered and credited. A distinct later Resultary report computes the same entire histogram under semigroup translation and gives affine frequencies; it must not be counted as a different statistic or as evidence of an earlier publication. The specific equal-width insertion law, compact floor sum, and twice-square slope are distinct supported content: the later general formula is a sum of individually variable threshold differences and does not evaluate them as H equal contributions or prove their square sum. This is a statement-level assessment, not an exhaustive priority claim.

## value

PASS

Counting all gap lengths was already motivated in binary cyclotomic work, including exact counts in special residue classes. The theorem supplies the analytic histogram without expanding the polynomial, includes coprime composites, and explains why its affine slope is twice a square by identifying the width and number of contributing insertion intervals. This structural refinement is useful even given the other complete threshold-sum algorithm; no extension to higher-generator semigroups is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
