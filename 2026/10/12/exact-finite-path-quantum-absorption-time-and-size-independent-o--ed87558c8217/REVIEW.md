# Scientific review: exact finite-path quantum absorption time

## Correctness — PASS

The finite uniform path with a single absorbing endpoint defines a strictly stable conditional generator: a nondecaying eigenvector would vanish at the lossy site and hence at every site by the tridiagonal recurrence. The integrated survival observable is therefore the unique Hermitian solution of the corresponding Lyapunov equation. An explicit full-matrix kernel, with affine real entries on even separations and imaginary entries on odd separations, solves this equation entry by entry. Its diagonal yields the stated exact passage-time law for every path length, starting site, positive hopping, and positive loss rate. Strict convexity then proves the unique finite optimum for every starting site except the lossy endpoint. The standard-library verifier checks 88,560 rational matrix entries; finite verification does not replace the analytic proof.

## Originality — PASS, with residual risk

The closest primary source, Riberi's arXiv:2605.08056, determines absorption probabilities on a semi-infinite boundary-loss chain, whereas the new theorem determines *mean absorption time* on every finite open path and yields an exact length-independent optimal loss rate. Silva's arXiv:2601.09628 evaluates finite-chain exceptional-point conditions, not integrated hitting-time observables. The finite-ring trapping work arXiv:1311.6298 permits permanently surviving sectors absent on this path. The general Poisson-measurement formula in arXiv:0803.3446 and its explicit two- and three-vertex matrices concern a different stochastic measurement protocol; their results do not imply this exact Lindblad rate law. Optimized light-harvesting studies such as arXiv:2403.00058 include additional radiative physics and a different efficiency observable. Dedicated published-record searches found no equivalent or stronger finite-path formula. An unindexed calculation or uninspected supplementary derivation is still possible; published-source search failure alone does not certify priority.

## Value — PASS

The exact expected first-passage time is a motivated resource measure for a lossy quantum wire. The optimized rate's independence from total wire length is a structural, all-size design rule, not an arbitrary small-instance computation. The formula also quantifies both insufficient absorption and quantum-Zeno slowdown, isolates the exception when the walker starts on the sink, and clarifies why the infinite-length limit differs from a finite absorbing chain. It neither asserts uniform optimality for other input superpositions nor extends to multiple sinks, inhomogeneity, dephasing, or branching graphs.

Self-review: passed. Independent audit: not yet performed.
