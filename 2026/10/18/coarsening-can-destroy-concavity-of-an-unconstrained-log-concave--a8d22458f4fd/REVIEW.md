# Scientific review

## Correctness — PASS
The five weights are exact hat-function moments under an explicitly strictly concave log spline, so the fine score vanishes and strict convexity modulo additive constants gives its uniqueness. The tent-envelope argument extends this to the full log-concave MLE. The coarse score is an exact expectation difference; rational Taylor enclosures prove each score coordinate is below one millionth in magnitude at the rational trial point. The centered Gram matrix has rigorously positive principal minors and gives a local Hessian lower bound, forcing the unique global optimizer into a radius-one-hundredth ball. Its upward slope jump is then greater than 0.1952996. All relevant calculations and bounds are checked by the included standalone script. Limitation: this is a weighted, not equal-count, data example; no statement about concavity-constrained coarse maximization is made.

## Originality — PASS on accessible evidence
The open question following the subdivision example in Grosdos et al. (arXiv:2003.04840 / 2023 journal paper, Section 2) predicts exactly the opposite implication for a subdivision coarser than the optimum. The full original source was inspected rather than relying only on its abstract. The earlier paper of Robeva–Sturmfels–Uhler proves realizability of subdivisions after varying sample weights and does not assert shape preservation on *fixed* weights after deleting knots. Searches for coarsening, constrained/unconstrained spline projection, equivalent curvature obstructions and related published claims yielded no encompassing result. The later corrigendum's full text was not obtained; possible unindexed or inaccessible prior work is a residual risk. The negative search is not considered proof of uniqueness.

## Value — PASS
This explicitly answers a research question posed by the motivating paper, showing that a natural knot-simplification heuristic need not retain the shape constraint even when the initial maximum-likelihood log-density is strictly concave at every interior fine knot. The evidence is an exact, reproducible, nonasymptotic certificate, not an arbitrary isolated shape test.

Self-review: passed. Independent audit: not yet performed.
