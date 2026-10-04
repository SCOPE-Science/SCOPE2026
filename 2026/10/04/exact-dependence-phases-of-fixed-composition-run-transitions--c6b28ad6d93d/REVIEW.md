# Review

## Correctness

PASS. The fixed-composition null is uniform over binary words with prescribed counts. One transition uses two distinct positions, two adjacent transitions use three positions and occur jointly only through \(010\) or \(101\), and two disjoint transitions use four positions with four possible orientations containing two symbols of each type. These exact hypergeometric probabilities give the two covariance formulas after subtraction of the common squared marginal.

The sign reductions are exact. The disjoint zero condition would force \(2N-3\) to divide \(N(N-2)\); coprimality with \(N-2\) would then force \(2N-3\mid N\), impossible for \(N\ge4\). Adjacent zero covariance is equivalent to independence for Bernoulli pairs and is feasible exactly at square \(N\). Summing the covariance field reproduces the standard run-count variance.

## Originality

PASS, with a classical-literature residual risk. The complete Smeeton--Cox article was inspected. It works in the same conditional random-arrangement model, explicitly counts a new run by a change from the preceding category, and discusses total-run distributions, clustering, and alternation. It does not state the adjacent/disjoint pairwise covariance phase diagram or the square-size independence classification.

The 1940 foundational papers are obvious potential sources. Scanned copies were located, but the inspected machine-readable route did not expose their mathematical text, so they are not used for a whole-document noncoverage conclusion. Exact and semantic searches did not locate the two thresholds or the “adjacent independent but disjoint dependent” classification. Because a classical proof of the total variance could implicitly compute the same pair probabilities, originality is claimed for the assembled sign/independence classification rather than for the elementary counting identities in isolation.

## Value

PASS. The Wald--Wolfowitz statistic collapses \(N-1\) local change indicators to one count. The theorem exposes the dependence structure hidden by that aggregation: balanced fixed-count samples have negatively associated adjacent changes but positively associated disjoint changes, sufficiently imbalanced samples reverse the distant sign, and special square sample sizes create exact local independence without global pairwise independence. This gives a natural structural explanation of how the classical run variance is assembled from competing local effects.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK words_enumerated=8158 marginal_checks=501 adjacent_checks=438 disjoint_checks=1485 phase_checks=31122 nonzero_far_checks=31122 square_independence_checks=31122 variance_checks=31185`.
