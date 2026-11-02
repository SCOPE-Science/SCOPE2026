# Scientific assessment

## Correctness — PASS
The proof begins from the exact Gaussian iteration and obtains the covariance functional calculus. An explicit one-variable derivative sign computation proves the unique interior threshold and its sharp universal spectral ceiling, without finite enumeration. The same spectral calculation gives the asymptotic threshold and explicit stable even-step rank-one counterexamples. Complete four-outcome Rademacher enumeration proves the exact residual-diagonal probe variance ratio. The standalone standard-library verifier passed 4,997 supplementary checks; it is corroboration rather than proof of infinitely many parameters.

## Originality — PASS, with historical-priority limitations
Abhishek and Holman (arXiv:2610.00882v1) already derive the noise-propagation covariance and use randomized normal-operator truncation, which are credited. Celisse and Wahl (JMLR 22(76), 2021) already give the Landweber spectral filter for discrepancy analysis. In the inspected primary mathematical content, neither states the sharp covariance versus normal-rank ceiling, its large-iteration law, or the exact unbounded Rademacher residual-probe variance ratio. Searches for equivalent noise-filter and covariance-eigenvalue formulations and published mathematical records found no covering statement. The full 2019 Ito–Jin randomized-SVD manuscript concerns regularized inverse solutions instead of this finite-step Landweber covariance-rank boundary. An older equivalent specialized result remains possible.

## Mathematical value — PASS
The boundary resolves when a natural dominant-normal-eigenvector approximation also selects dominant propagated uncertainty. The rank inversion occurs even with a nonovershooting two-step, while the stable near-upper-step counterexample shows arbitrarily unfavorable residual-probe cost. The theorem provides a rigorous benchmark for rank selection and sampling-effort allocation, not a guarantee about the complete confidence-interval procedure.

## Scope and limits
The proof concerns full-column-rank finite-dimensional white-noise Landweber iteration, exact eigen-subspace truncation, and standard independent Rademacher probes. The divergent effect requires even iteration counts; the uniform safe-ranking threshold does not. The result does not certify bias, statistical coverage, random eigensolver error or nonlinear reconstruction. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
