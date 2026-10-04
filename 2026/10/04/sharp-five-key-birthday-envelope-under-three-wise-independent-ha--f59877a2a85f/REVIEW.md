# Review

## Correctness

PASS. The proof symmetrizes without changing the objective or three-wise
marginals, exhausts all seven occupancy partitions of five, and computes the
pair- and triple-collision counts exactly. The two linear occupancy
inequalities are checked on every partition type. Their expectations give the
claimed upper and lower bounds. Three explicit endpoint mixtures satisfy the
normalization and both required collision moments, including the zero
lower-endpoint regime for \(5\le q\le9\).

The exact-rational package replay returned `VERIFY_OK certificate_checks=14 formula_checks=3992 explicit_joint_cases=15 triple_marginal_checks=57750`. The realization argument is complete: coordinate and output-symbol symmetry,
together with the exact pair-collision and triple-all-equal probabilities,
forces every ordered triple to have mass \(1/q^3\). Thus the constructed laws
are genuinely three-wise independent, not merely moment matched.

## Originality

PASS, with a residual design-literature risk. The full simple-tabulation text
was inspected at its definition of independence and its five-key
fourth-moment discussion. It motivates five-key dependence under a
three-independent hashing scheme but does not state the generic five-key
all-distinct interval.

The full limited-independence paper of Benjamini--Gurel-Gurevich--Peled was
inspected at its extremal linear-programming and moment-problem sections. It
provides the general optimization framework but not this \(q\)-ary occupancy
calculation.

Targeted database searches for five-key birthday probabilities,
three-independent collision-free hashing, occupancy moment polytopes, and
equivalent formulations returned a pairwise occupancy envelope as the closest
published result. That result fixes only the pair-collision moment, whereas
the present theorem uses the additional triple-collision moment and has
different sharp endpoints.

The immediately preceding four-key calculation was compared statement by
statement. Its occupancy list and endpoint formulas do not imply the five-key
bounds; the new proof uses occupancy types and supporting inequalities absent
from the four-key case.

## Value

PASS. Five keys are singled out in the classical simple-tabulation analysis as
the first set size where a nontrivial dependence phenomenon is exploited in a
fourth-moment argument. The theorem gives the complete generic answer for the
most basic five-key birthday statistic under exactly three-wise independence:
both sharp endpoints, the exact threshold where zero collision-free
probability ceases to be possible, and realizability of the whole interval.

Same-model review: passed. Independent audit: not yet performed.
