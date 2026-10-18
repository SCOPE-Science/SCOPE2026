# Scientific review

## Correctness — PASS

The claimed sharp zero-sum Poisson norm is the maximum of centered absolute row sums, not the unrestricted row-sum norm. The proof establishes finite-dimensional median duality, the exact rank-one Green update, the four-residue homogeneous formula, uniform control of the median threshold crossings, and the explicit continuum signed profile. Its maximum is exactly \(1/16\). A separately implemented rational-matrix inversion and balanced-sign extremizer checks agree with the closed formula; `CHECK.py` reports 4269 finite assertions. Infinite asymptotics rest on the analytical argument, not on those tests.

## Originality — PASS within the inspected evidence

The cycle Green kernel, rank-one pseudoinverse perturbation, and eigenpair description of one-edge weighted cycles all precede this result. Beveridge (arXiv:1505.06989v1) gives the classical Green kernel under a different Laplacian normalization; Grudsky, Maximenko and Soto-González (arXiv:2205.12457v1) study the same matrices' eigenpairs. The new assertion is the exact order-\(n\) sharp mean-zero endpoint correction, its positive-part dependence on conductance, and quarter-cycle localization. Related Green-function papers by Carmona and Pozrikidis were only available at abstract level and remain priority risks. A published-record search did not produce a matching claim, which alone is not proof of novelty.

## Value — PASS

The result quantifies the worst spatial response of a ring network under compatible unit-bounded loads when one conductance is modified. It isolates a sharp coefficient and a geometric shift of worst response that a spectral-gap estimate cannot locate, and distinguishes weakening from strengthening. The object is canonical, and the coefficient is an actual leading correction for every fixed positive defective conductance.

## Limitations

The asymptotic remainder is not uniform near zero conductance. The real compatible-forcing constraint and unnormalized Laplacian are essential; the result is not a theorem about all random-walk normalizations, nonlinear sources, or an arbitrary number of defects. An independent proof and bibliographic audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
