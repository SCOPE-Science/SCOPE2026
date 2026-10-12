# Scientific review

## Correctness — PASS

The stated domain is all real \(0<r<s\) and \(0<u<v<1\); no finite-sample-only or numerical-only qualification is used. Direct differentiation of \(Q_a(u)\) gives \(Q_a'(u)=1/(a u B(-\log u/a))\). The function \(B(w)=(e^w-1)[-\log(1-e^{-w})]\) has \(B'>0\), \(B''<0\), and \(B(0+)=0\); hence \((r/s)B(w)<B((r/s)w)<B(w)\), which proves the strict derivative sandwich. Integration proves every interval inequality. Both endpoint limits are established analytically and prove optimality. All logarithmic moments exist, and integrated quantiles justify the centered convex-order corollary. The finite verifier is an arithmetic stress test only and is not the proof; no numerical approximation is used in the universal argument.

## Originality — PASS, with explicitly bounded claims

The closest source is Arab et al. (2021), Proposition 12 and Remark 14, which already supply the corresponding **qualitative one-sided star/dispersive order**. That portion of the result is not original. Datta and Gupta (2020 preprint; 2024 journal), Theorem 4, supplies reversed-hazard comparisons of PRHR maxima but no two-sided optimal quantitative logarithmic quantile slope bound. Doumas' 2026 paper studies the variance of the logarithm of exponential maxima. Giam's 2026 abstract explicitly reports monotonicity of that variance; neither variance monotonicity nor the qualitative star-order implication is asserted as original. The reviewed surviving claim is instead the strictly positive, exact, all-quantile **lower contraction factor \(r/s\)** jointly with its sharp companion upper factor \(1\), which the inspected sources do not state or imply through their qualitative results alone. An unlocated equivalent quantitative formulation remains a bibliographic risk; no unpublished-data uniqueness claim is made.

## Value — PASS

The result determines both optimal uniform distortion constants of the canonical common-quantile coupling of two PRHR extreme-lifetime models, at every real pair of shape parameters. It is not an arbitrary discretization: it characterizes the complete quantile-width scale of the natural exponentiated-exponential family, including rare-event and high-reliability tails. The positive lower factor is nontrivial and provides a two-sided bound on confidence-interval widths and a centered convex-order sandwich stronger than the familiar unscaled monotonicity. Exact optimality and a continuum of real parameters supply mathematical motivation beyond a routine example of a known order.

## Closest literature, verification limits, residual risks

Datta–Gupta arXiv:2002.12436v1 is first public on 2020-02-27, with primary MSC 62N05 stated on its first page; pertinent definitions, Section 3 Theorem 4 and Section 4 Theorem 5 in the accessible complete PDF were inspected. Arab–Hadjikyriakou–Oliveira–Santos (2021), full-text Proposition 12 and Remark 14 were checked; their one-sided implication is credited. Doumas (2026), full 4-page article, was read; Giam's 2026 abstract, not the full paper, was available. Literature and published-database searches using shape, quantile Lipschitz, scaled dispersive, convex-order, star-order and PRHR aliases did not identify a covering **quantitative** theorem. Search absence is not proof of novelty; older equivalent quantile-transform coverage remains the main risk. The analytic proof is self-contained; the accompanying checker tests finite cases and does not independently certify generality.

Self-review: passed. Independent audit: not yet performed.
