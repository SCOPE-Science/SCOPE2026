# Review: an exact upper-tail law for random planar shadows of cross-polytopes

## Correctness

**PASS.** The claim fixes the coordinate normalization of the \(n\)-cross-polytope and Haar measure on \(\operatorname{Gr}(2,n)\). The frame identity \(\sum_iw_iw_i^{\mathsf T}=I\) and Cauchy--Binet identity \(\sum p_{ij}^2=1\) establish the disjointness of large minors. If a minor is at least \(\sqrt{2/3}\), writing the other projected generators in that pair's basis bounds their total squared coordinates by \(1/2\), so every remaining generator lies inside the pair's symmetric diamond and the area is exactly twice that minor. The published equality classification makes the complement of these neighborhoods compact with area strictly below two, proving an actual nonempty interval rather than merely a formal asymptotic. The single-minor distribution is derived from two independent spherical Beta factors and the Gamma duplication formula; it is \(\operatorname{Beta}(1,n-2)\), yielding the precise polynomial. Independence and a tail-integral argument justify both the Weibull limit and mean asymptotic. The staged `check.py` program ran successfully and checked 136,035 finite identities/diagnostics. The checker is supplementary, not an infinite proof.

## Originality

**PASS, with bounded historical-priority risk.** The inspected full-text arXiv manuscripts of Ivanov (2018, 2026) determine planar/global projection maxima, equality cases, and other deterministic extremal geometry; the recent result supplies the maximizing-plane input but no Haar-distributed area tail. The independently located Böröczky--Henk preprint on *Random Projections of Regular Polytopes* studies expected face counts rather than volume distributions; its abstract, theorem, section 3 and discussion were examined, including screenshots of the original PDF. The all-dimensional exact upper-tail identity and consequent Weibull constant are not covered by the compared statements, though the marginal Beta formula itself is classical spherical probability. Searches also checked projected-volume tails, Grassmannian minor aliases, and closest available mathematical records; none showed the final result. Search absence cannot establish global priority. Filliman's 1988 paper remains incompletely inspected.

## Mathematical value

**PASS.** The probability that a random plane nearly attains the *sharp* cross-polytope projected-area maximum is a natural geometric concentration observable not characterized by the maximum theorem alone. Unlike a generic quadratic large-deviation estimate, the finding gives a strictly exact power law on a nonempty interval in **every** ambient dimension, with the full binomial coefficient and exponent. It also determines the exact rate and limiting distribution for the best of many random orientations. These are substantive stochastic consequences of the deterministic 2026 extremal classification, and not an arbitrary numerical example, renaming, or known-table lookup.

## Closest sources and limits

- Grigory Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072 (2026-07-13): maximum \(2\) and uniqueness of coordinate-plane extremizers in projection dimension two are an essential pre-existing input.
- Grigory Ivanov, *On the volume of projections of the cross-polytope*, arXiv:1808.09165 (2018-08-28), published 2021: already proved the planar extremal result and explored regular-hexagon non-global local maxima. It does not furnish the requested Haar area tail.
- Böröczky and Henk, *Random Projections of Regular Polytopes* (May 1997 preprint): studies face-count expectations of random cross-polytope projections, not the distribution of area near its maximum.
- P. Filliman (1988): an older relevant geometric source located bibliographically; historical equivalence remains possible without a complete inspection.

The positive endpoint of the proven interval is implicit and may be nonoptimal. Bulk/lower-tail area laws and projection dimensions beyond two are unproved. Standard Beta and Gamma identities are used without asserting discovery of those facts. Independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
