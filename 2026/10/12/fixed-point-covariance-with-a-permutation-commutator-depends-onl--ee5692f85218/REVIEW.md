# Scientific review

## Correctness — PASS

With deterministic \(\eta\in S_n\), uniform \(\Pi\in S_n\), \(n\ge3\), and \(f=\#\mathrm{Fix}(\eta)\), the theorem proves
\[
\operatorname{Cov}(\#\mathrm{Fix}(\Pi),\#\mathrm{Fix}(\eta^{-1}\Pi^{-1}\eta\Pi))
=\frac{f(n-f)}{(n-1)(n-2)}.
\]
The source-to-claim proof explicitly computes contributions from each fixed and moved point of \(\eta\), including exact remaining-position expectations and the critical count \(\sum_b|\{i,\eta(i)\}\cap\{b,\eta(b)\}|=4\). There is no asymptotic or computational premise in the all-size identity. The exact checker covers 876 reference-permutation cases and 669492 uniformly weighted ordered permutation pairs, plus the upper-bound and nonindependence witnesses. The nonindependence argument uses the trivial center of \(S_n\) for \(n\ge3\). The claim excludes \(n\le2\) and non-uniform \(\Pi\).

## Originality — PASS (with residual risk)

Diaconis–Evans–Graham's Section 6 introduced the same statistic and its marginal expectation and Poisson approximation; this is prior, not newly claimed. Fulman's Theorem 3.5 provides all marginal moments of the commutator statistic for fixed \(\eta\); the second moment can depend on 2-cycles but is not a joint moment with fixed points of \(\Pi\). Moreno–Rivera provides counts indexed by Hamming noncommutation distance, but no fixed-point weighting of the original \(\Pi\). Primary full-text analysis and published-record searches did not identify the all-cycle-type exact mixed covariance or its derangement-dependence boundary. A hidden representation-theoretic mixed-moment identity or older near-commutation enumeration could still imply it; this is a real historical risk rather than a certification of global priority. The currently indexed published search cannot exclude unpublished work.

## Value — PASS

The two statistics are central in random permutations: ordinary fixed points and local commuting agreements with an arbitrary deterministic reference. A general classification showing that the covariance depends **only on fixed support**, is never negative, is strictly positive for mixed support, and vanishes for every derangement while the statistics remain dependent gives a structural dependence fact across all cycle types and finite sizes. The sharp maximum and macroscopic limiting profile strengthen the classification. This is not offered as a new derivation of an already established marginal mean.

## Scope and limitations

All conclusions concern one mixed second-order moment for uniform \(\Pi\); they give no independence assertion, full joint law, higher mixed cumulant, or nonuniform model result. Primary MSC 60C05 and earliest verified public source date 2013-08-01 refer to the motivating archival technical report, not to an invented publication date for this finding. Independent priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
