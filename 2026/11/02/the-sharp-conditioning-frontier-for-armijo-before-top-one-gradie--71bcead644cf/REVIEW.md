# Review of the sharp Armijo-before-top-one conditioning frontier

## Correctness — PASS
An exact quadratic identity determines the ideal largest accepted full-gradient Armijo step. A second identity reduces the sign of the sparsified first-step objective change to a diagonal-to-Rayleigh ratio. Maximization over the full two-dimensional spectral orientation circle and over the top-one selection cone yields the necessary-and-sufficient bound. The proof treats strict/non-strict inequalities, both tie selections, the isotropic case, all positive scaling parameters, and a strict unique-coordinate counterexample. Standalone deterministic checks compare the closed form with an independent angular search and direct objective computation. Computations do not substitute for the global analytic optimization.

## Originality — PASS, qualified
The direct prior source is Subramaniam, Magesh and Veeravalli (arxiv:2207.10046v1), which proposes scaled Armijo search in error-feedback top-\(k\) compression. Its Sections II and III and main theorem formulas were inspected: they yield sufficient convergence results for the operational backtracking algorithm, not this exact, idealized, two-dimensional first-step spectrum-and-orientation criterion. Searches for equivalent top-one, sparsified Armijo, and rotated Hessian criteria did not identify a covering result. Related published exact Polyak, LARS, and BB results analyze different step maps. A previously derived general matrix-ratio lemma or a specialized unlocated study could subsume the formula; independent priority review has not been performed.

## Value — PASS
The full-to-compressed line-search mismatch is a concrete design question, not a substitution into an existing uncompressed bound. The theorem computes the **sharp** scale required to retain descent for all two-dimensional spectra up to prescribed conditioning, including an oblique worst orientation and a golden-ratio-square boundary for the common half-Armijo choice. This precision can distinguish aggressive but safe scaling from provably unsafe first updates. The result is intentionally limited to the ideal maximal step and zero-feedback first update; practical capped/backtracked choices and later feedback may behave differently.

Self-review: passed. Independent audit: not yet performed.
