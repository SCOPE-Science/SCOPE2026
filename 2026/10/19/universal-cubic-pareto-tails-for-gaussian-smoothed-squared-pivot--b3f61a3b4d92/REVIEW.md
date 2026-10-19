# Scientific assessment

## Correctness — PASS
The singular-pivot integral includes the essential squared-pivot sampling weight. Its cubic tail follows by a two-sided triangle squeeze near a zero pivot. Dominated convergence holds because the complementary Gaussian block has rapidly decaying norm and the dominating ratio is bounded by a quadratic polynomial in its energy. This applies to every fixed noncentral Gaussian mean matrix and positive noise variance. Independent chi-square and Dirichlet identities produce the stated centered gamma coefficient. Layer cake proves the exact moment frontier; oriented-minor algebra recovers the established squared-moment identity. The supplied finite checks reproduce key identities but do not stand in for the proof.

## Originality — PASS, with literature uncertainty
The original squared-entry randomized LU construction and its squared-error identity are prior work (Gilles–Wilber, arXiv:2601.22344v1). Divan–Gilles, arXiv:2609.06287v1, analyze randomized approximation and pivot laws. The inspected literature does not state a joint Gaussian-perturbation cubic Pareto tail, its smoothed noncentral coefficient, or the threshold at the third moment. Spielman–Yu, arXiv:2610.08701v1, treat a different, deterministic partial-pivot choice on Gaussian matrices. Published records on complete-pivot cross approximation and adaptive column selection do not imply this distributional claim. Searches of indexed records and accessible earlier findings did not find equivalent coverage. Equivalent results in unindexed or unexamined literature remain possible; novelty has no independent certification.

## Value — PASS
RPLU is motivated by low-rank approximation; its published expected-squared-residual analysis does not control third moments. The theorem identifies a sharp, dimension-independent integrability boundary under any nondegenerate Gaussian smoothing of *arbitrary deterministic data*, even though the squared error remains finite. It quantitatively separates squared-probability randomized pivoting from classical maximum-entry pivoting, and supplies an exact coefficient for all centered rectangular dimensions. This is a meaningful limitation for risk-sensitive use of a recent pivoting method, not a routine restatement of its existing variance bound.

## Scope and risk
One pivot, real independent Gaussian entry perturbations, fixed finite dimensions and exact arithmetic only; no statement about typical input-dependent fixed-matrix pivot tails, repeated pivots, other noise classes, finite-precision errors or full solver stability.

Self-review: passed. Independent audit: not yet performed.
