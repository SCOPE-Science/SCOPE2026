# Scientific review

## Correctness
PASS. Exhausting the six permutation matrices reduces their coefficients to one parameter; nonnegativity gives exactly the stated closed interval. The nonconstant affine coordinates can vanish only at endpoints, so all real minimum supports are endpoints. Endpoint expressions are integer linear combinations of input entries, proving the finite-precision equality. The \(13\)-denominator example attains five terms. The bundled standard-library verifier checked 13,558 denominator/matrix pairs over denominators \(1\) through \(12\), with 67,790 exact assertions. This is supplementary to the full analytic proof.

## Originality
PASS, with historical-priority qualification. The motivating 2026 minimum-decomposition paper treats finite precision and general optimizers, while the 2018 Birkhoff-heuristic paper states a general extreme-point fact. Neither checked accessible text gives the explicit \(3\times3\) two-endpoint formula, all-optima characterization, or equality of real and finite-precision minima. The parity relation itself is classical and explicitly credited. Older polytope literature could contain an equivalent small-dimensional formula, and this remains a residual bibliographic risk.

## Value
PASS. Dimension three is the first Birkhoff polytope with nonunique coefficient representations, making it the smallest natural case where minimum-term and exact-grid questions differ from a fixed unique decomposition. The result completely classifies the optimum, gives a constant-size exact algorithm, proves precision has no cost, and pinpoints the sharp five-term worst case. This supplies a small exact benchmark for permutation-based scheduling without claiming results for larger dimensions.

## Scope and limits
Exact real or rational \(3\times3\) doubly stochastic matrices only; no floating-point robustness or higher-dimensional conclusions. Comparisons are best knowledge, not a formal priority guarantee.

Self-review: passed. Independent audit: not yet performed.
