# Review of the third-coefficient Hardy support transition

## Correctness — PASS

The reduction of a bounded coefficient functional on analytic \(H^{1/2}\) to fourth powers of unit \(H^2\) polynomials uses the published outer-extremal theorem and the fact that only the first four root coefficients enter the functional. The finite-dimensional objective is exactly the cubic-convolution expression in `RESULT.md`. The small-parameter upper bound through \(t=1/5\), the strict transverse Hessian sign for \(t<1/2\), and the rational competitor at \(47/100\) have been checked independently of numerical optimization. Continuity, compactness, and uniform local strictness then establish a separated, non-binomial optimizer at the first departure. Supplementary reproducible checks are in `CHECK.py`; they are not offered as a proof of the infinite statements.

The infimum definition does not identify \(t_*\) numerically. The argument does not classify all maximizers at coexistence or later regimes.

## Originality — PASS relative to inspected evidence

Brevig–Søvik (arXiv:2610.21788v1) proves the outer-extremal structural theorem but not a sharp mixed third-coefficient support function or metastable optimizer transition. Brevig–Saksman (arXiv:1905.09547) obtains individual coefficient extrema, while Brevig–Grepstad–Instanes (arXiv:2011.07790) analyzes fixed-constant-term coefficient problems, solving the first-coefficient regime and leaving higher orders open for \(0<p<1\). Those statements do not imply the coexistence threshold proved here. Previously obtained sharp support formulas involving different coefficient pairs do not determine the cubic-convolution metastability mechanism for \(a_0+t a_3\).

Searching for Hardy \(H^{1/2}\) mixed first/third coefficient support, optimizer coexistence, third-order Taylor coefficient stability and related formulations found no covering statement. These searches are not a proof of universal novelty: a previously unindexed equivalent or more general result remains possible.

## Value — PASS

The problem asks when the sharp linear support functional \(a_0+t a_3\) first ceases to have a two-term fourth-power maximizer. The proof locates the first global departure strictly before the binomial's local-instability point, and proves that a distinct family of optimizers arrives with a positive shape gap. This coexistence provides genuinely qualitative information about the sharp coefficient body's exposed extremals, not just a numerical or normalization improvement. The exact critical parameter and complete support function remain open.

Self-review: passed. Independent audit: not yet performed.
