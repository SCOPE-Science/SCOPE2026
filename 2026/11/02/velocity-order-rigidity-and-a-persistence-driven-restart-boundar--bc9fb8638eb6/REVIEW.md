# Scientific review

## Correctness — PASS

The proof treats the full absorbing–reflecting Markov process and each reset cycle. The sample-path assertion follows from the monotone initial-velocity OU difference and the Lipschitz upper Skorokhod regulator, and does not rely on perturbation. The first-order transform is derived from the killed backward operator and checked against the renewal fraction. The moment recursions, root slope and two sequential persistence limits give the local threshold shift by the implicit function theorem. The closed formulas and independent finite-difference/constant-drift comparisons passed 1,226 standalone checks. Risks: differentiability is used only at nondegenerate translational diffusion; no global finite-activity threshold or uniqueness of crossover persistence is asserted.

## Originality — PASS (best-knowledge with residual risk)

Georgiou, Bressloff and Bertrand, arXiv:2609.21124 (2026), explicitly state that their fixed reset-velocity first-passage phase diagrams rely on simulations, while the analytic expansion uses zero-mean Gaussian reinitialization; the precise first-order fixed-velocity mixed-boundary resolvent, all-activity velocity coupling and opposite persistence limits are not supplied there. Ray, Mondal and Reuveni, arXiv:1811.08239, study constant drift on a half-line, which informs the infinite-persistence limit but does not imply the finite-\(\tau\) phase reversal. Bressloff and Linn, arXiv:2602.02446, treat a run-and-tumble particle with a sticky boundary and thus do not cover the OU mixed-boundary response. Shankari and Sahoo, arXiv:2509.18515, investigate active OU transport under resetting without this absorption geometry. Published research search matches involving OU sensors/autocorrelations or Langevin integration do not state these results. Remaining risk: general first-passage coupling and killed-semigroup perturbation theorems may subsume portions of the proof, and the search is not exhaustive.

## Value — PASS

The sign of an absolute first-passage response is pinned down for every activity and resetting rate, yet the onset-of-beneficial-restart boundary shifts in opposite directions at short and long velocity persistence. This gives a nontrivial distinction between absolute first-passage ordering and relative benefit of restart that cannot be inferred from either a simple monotonicity argument or Gaussian-centered velocity reset results. The explicit transition coefficient supports quantitative prediction of direction-sensitive restarting regimes.

## Scope and limitations

The two persistence laws are sequential limits after the weak-activity derivative. Intermediate-persistence crossover existence, not uniqueness, is proved. The verified model resets velocity and position together, with translational diffusion positive and a fully reflecting right boundary. Correlated velocity resetting, nonlinear propulsion, mixed boundary reactivity and stronger-than-first-order critical-location conclusions remain open.

Self-review: passed. Independent audit: not yet performed.
