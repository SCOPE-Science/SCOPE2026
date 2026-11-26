# Independent mathematical audit

## correctness

PASS

A factor with at least two changes contains a specified complete run and so has only one occurrence, ruling out right-speciality. Both constant factors are right-special; the one-change factors 0^a1^b and 1^a0^b are right-special exactly for a≤b and a<b respectively. This gives p(n+1)−p(n)=n+1 from p(1)=2. A factor with at least three changes cannot have its reversal: the internal run lengths are nondecreasing and the only equal adjacent complete runs occur in the order 0^k1^k. There are n−1 reversal pairs with one change. For two changes the flank bounds for both orientations are a,b≤k around 1^k and a,b≤k−1 around 0^k. Choosing the nonpalindromic representative a<b yields T(n) and T(n−1), where T(m) counts a+2b≤m. The generating function for all nontrivial pairs is z²/((1−z)²(1−z³)); its forward coefficient difference at n is floor((n+2)/3), giving floor(n(n+1)/6) pairs. Subtracting from p(n) proves the stated r(n), hence the 2/3 limit. Unbounded runs of both symbols rule out eventual periodicity. The frozen script was inspected, not run; an independent finite-prefix check at n=10 gave p=56 and r=38. Exact all-length validity rests on the proof.

## originality

PASS

The supported distinct claim is the exact pair of formulas for the specified increasing-run word, with its 2/3 limit as a consequence. The record does not claim to be the first disproof or the first aperiodic example. The 2/3 limit among binary aperiodic words is itself already covered by another construction in the catalogue; it is not separately credited as new. No inspected statement supplies the all-length formulas for this word.

## value

PASS

W is a canonical binary example defined by paired increasing runs. Exact ordinary and reflection complexities quantify how reversals are lost, with contributions isolated by change count. The simultaneous formulas provide a usable test case for the role of reversal closure and recurrence in conjectured limit dichotomies, even though existence of an aperiodic 2/3 example is not new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
