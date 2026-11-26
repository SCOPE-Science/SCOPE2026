# Independent mathematical audit

## correctness

PASS

For fixed a=r−1 and c, the probability of a degree-j line is asymptotic to e^{−c}(log N)^{j−a}/(N j!). Thus smaller degrees disappear and, by independent lines on each separate side, degree r appears on each side with high probability. For the mixed factorial moments, conditioning on the crossings of s fixed rows and t fixed columns leaves disjoint sites. A crossing pattern with h>0 occupied cells costs O(p^h) relative to an empty pattern; losing v entries from any line's residual degree target costs O((log N)^{−v}) or makes that event impossible. The total loss exponent over the lines is 2h. This proves the stated independent Poisson limit, including a=0 where nonempty crossing patterns are impossible. Conditional on a specific cell being occupied, its two residual counts are independent and each has probability O(log N/N) of being at most r; the expected number of such doubly low occupied cells is O((log N)^3/N). On their absence, if the respective minimum degrees are at least r and r−1, all unoccupied cells meet the odd bound, and any occupied violation would force both endpoint degrees at most r+1. If both minima are at least r, the analogous calculation yields the even bound. Conversely the two degree-(r−1) lines intersect to disprove odd domination, and any degree-(r−1) line intersects a degree-r line on the other side to disprove even domination. Therefore the limit has the stated OR/AND and joint mass vector, with gap 2z(1−z), z=e^{−lambda}, maximized at z=1/2. Uniform-permutation coupling at c±epsilon sandwiches monotone success, and continuity gives the fixed-budget and hitting-time limits. If the fixed-budget assertion is read to include the Poisson counts and high-probability reduction as well, the same estimates apply directly: on M=O(N) prescribed sites in finitely many lines with h=O(1) prescribed hits, the fixed-budget probability of the pattern is (m)_h/(N²)_h times the product over i=0,…,M−h−1 of [1−(m−h)/(N²−h−i)], uniformly asymptotic to p^h(1−p)^{M−h} at p=m/N². This gives the same mixed moments, rarity bounds and first/second moments for degree r. The proof requires fixed r. Separately the bitboard replay /workspace/evidence/2.py exhausts all subsets of orders 2,3,4 and checks the open-neighbor identity and both deterministic implications wherever the high-probability hypotheses hold. /workspace/evidence/2.out gives counts; these finite checks do not establish the limiting laws.

## originality

PASS

The deterministic rook occupancy identity and the r=1 joint empty-line Poisson ingredient are covered and not credited as distinct. The scoped contribution is the joint odd/even total-domination reduction and accompanying fixed-r shared-window law for this Bernoulli and fixed-budget problem. The closest published degree-sequence approximation inspected does not apply at this density. The closest indexed Poisson result concerns power domination and has a differently defined event.

## value

PASS

A single critical window conceals two different reliability mechanisms despite the consecutive requirements: one needs a clean side, the other two. Resolving those events jointly, with a nonvanishing worst gap of one half, answers a natural random-placement question missed by deterministic minimum-cardinality theory. The occupied-edge estimate says precisely when it is valid to replace open-neighbor constraints by low-line statistics, and fixed-budget and hitting-time forms are mathematically useful. The result is not credited for the routine transfer alone and does not purport to be uniform in r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
