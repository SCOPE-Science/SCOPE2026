# Review: A complete leader-property classification for identical product marginals

## Correctness
PASS. For a fixed index and one coordinate, conditioning gives the exact tied-maximum probability \(u_n=\mathbb E[F(X)^{n-1}]\). If the upper endpoint has no atom, cutoffs with tail \(t\downarrow0\) give \(u_n\le(1-t)^{n-1}+t\); choosing \(n\asymp t^{-1}\log(1/t)\) makes \(u_n\le2t\). Coordinate independence gives fixed-index leader probability \(u_n^d\), and the union bound yields \(a_n\le n u_n^d\to0\) along the selected subsequence because \(d\ge2\). If a top atom of mass \(p>0\) exists, a sample point equal to the top vector occurs with probability tending to one. Definitions, ties, finite and infinite essential suprema, and all quantifiers are covered.

## Originality
PASS. The 2022 motivating paper states the broader infinite-value product question and handles continuous products plus several sufficient discrete conditions, but not this complete identical-marginal classification. Candidate-specific published-finding corpus searches under leader-property, common-marginal, maximum-multiplicity, essential-supremum, and top-atom aliases returned no covering statement. The closest own prior structural result gives an exact maximum-tie criterion for arbitrary two-dimensional products but explicitly leaves the infinite-support decision open; the present tail-cutoff theorem is the missing implication and extends to all \(d\ge2\). The 2022 quasi-unidimensional and 2025 graph-based follow-ups concern different dependence classes. Residual risk remains for an elementary equivalent result under older common-maximizer terminology.

## Value
PASS. Equal marginals are the canonical symmetric subfamily of the published product conjecture, not an arbitrary numerical slice. The theorem gives a complete if-and-only-if classification for every dimension and every one-dimensional marginal, including continuous, mixed, discrete, bounded, and unbounded laws. It explains structurally that only a terminal atom can sustain positive leader probability uniformly in sample size.

## Closest literature and limitations
The closest source is Răducan--Rădulescu--Rădulescu--Zbăganu (2022), which asks whether independent components with infinitely many values can have the leader property. The theorem settles the identical-marginal part only. It does not classify heterogeneous products, and in the no-terminal-atom branch it establishes zero liminf rather than convergence of the full sequence.

Self-review: passed. Independent audit: not yet performed.
