# Self-review

## Correctness — PASS

The row-score spectral-projector formula is exact on the range of the Gram matrix, including singular Gram matrices for positive ridge parameters. A difference of two scores has only \(q\) distinct negative poles, so its nonzero numerator has degree at most \(q-1\). For sharpness, signed partial-fraction residues alternate, their positive/negative parts give two disjoint-support rows, and the residual Gram square root gives a real orthonormal-column completion. All singular values, crossover parameters and positivity boundaries are reconstructed in the proof. The embedded verifier passed 540 checks, including direct normal-equation scores for actual matrices. Numerical checks are evidence for implementation, not a substitute for the universal proof.

## Originality — PASS (provisional scientific comparison)

The closest full-text papers are McCurdy's deterministic ridge-leverage sorting algorithm (arXiv:1803.06010), Meier–Nakatsukasa's reusable Tikhonov preconditioners for multiple parameter values (arXiv:2203.07329), and Cohen–Musco–Musco's ridge-score sampling/monotonicity work (arXiv:1511.07263). Their stated results concern ranking at a fixed parameter, approximating the data matrix, sketch accuracy or adapting matrix sampling; none inspected establishes the claimed upper bound *and* arbitrary root-location realization along the ridge path. Published mathematical-record searches did not identify a dominating equivalent. A classical Cauchy-transform or interpolation restatement remains a genuine priority risk: independent literature certification is absent.

## Value — PASS

The question is intrinsically numerical-linear-algebraic: reuse of score-based rankings while tuning ridge penalties, which are used both in interpretable deterministic column selection and multi-parameter least-squares computations. The exact maximal number of pairwise reversals and their arbitrarily prescribed locations provide a complete, dimension-sensitive boundary and a structural obstruction to assuming monotone relative feature importance. This is not a claim about the best overall sorting algorithm or statistical sample complexity.

## Scientific limitations

Two-row comparisons, exact scores for one fixed real matrix, positive ridge parameter, and distinct-positive-spectrum count. The construction uses \(q+2\) rows and does not prove that this row count is minimal. Complete-list sorting changes and downstream algorithmic effects remain unproved. Historical priority may overlap with matrix-valued Stieltjes/Cauchy systems under different terminology.

Self-review: passed. Independent audit: not yet performed.
