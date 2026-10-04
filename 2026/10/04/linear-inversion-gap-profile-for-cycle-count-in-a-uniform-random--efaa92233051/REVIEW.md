# Review

## Correctness

PASS. Swapping the two images at positions \(i<j\) flips the inversion indicator and changes cycle count by exactly one, with sign determined by whether the positions lie in the same cycle. Conditioning on the two images gives an exact three-case same-cycle probability: zero for a forced fixed point, one for a forced direct connection, and one half for two disjoint prescribed arrows. The resulting signed count is \(2(j-i)-1\), giving the local covariance. Summing over gaps gives the total covariance. Classical independent representations of cycle count and inversion number give the exact variances and correlation.

## Originality

PASS, with a residual mixed-moment risk. The full Gladkich--Peled Mallows paper was inspected at its model definition, uniform point, and expected-cycle theorem. It studies the expected number and lengths of cycles across Mallows regimes, but does not state the exact derivative at \(q=1\), covariance with inversion number, or a positional gap profile.

The full He--Müller--Verstraaten article was searched for covariance and uniform-point derivatives; it develops cycle counts under Mallows weighting but does not state the present mixed first moment.

Parviainen's full paper was inspected because its abstract advertises cycles and inversions. Its Section 2 explicitly defines the relevant inversion statistic after standard cycle-form encoding, not the ordinary one-line inversion number. Its generating function therefore does not cover the statistic in this finding.

## Value

PASS. The Mallows parameter is conjugate to inversion number, so covariance with inversion count is the exact statistical response of any observable at the uniform point. Cycle count is a central random-permutation observable, and Gladkich--Peled specifically study how it changes across Mallows regimes. The theorem supplies the exact finite-\(n\) uniform-point slope and resolves that response into a simple positional profile, showing that long-gap inversions contribute more strongly than short-gap inversions.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutations_checked=46232 local_cov_checks=84 completion_rule_checks=3192 total_cov_checks=7 variance_checks=14 correlation_checks=7`.
