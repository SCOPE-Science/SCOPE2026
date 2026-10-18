# Scientific review

**Correctness — PASS.** The row-by-row Gauss–Seidel identity gives a generating-function profile for every fixed number of sweeps; exponentially small tails and a uniform finite-row discrepancy make the dimension limit rigorous. The coefficient residual is computed exactly, the physical Galerkin embedding is genuine, and the energy comparison follows by orthogonal projection. The standalone program verifies finite rational and large-dimension cases, not the infinite theorem itself.

**Originality — PASS, with residual risk.** The motivating 2026 Chebyshev-basis s-step PCG study discusses approximate forward Gauss–Seidel Gram solves and heuristic stopping. The December 2025 inexact Gauss–Seidel study concerns multigrid/coarse-solver effects rather than this explicit all-fixed-sweep rank-one limit. Related established work on Gauss–Seidel and residual-versus-error conditioning is acknowledged; it does not, from inspected material, state the fixed-sweep profile, exact nonzero energy-error constant and realizable Galerkin residual gap together. Older unindexed treatments of rank-one Gauss–Seidel matrices could imply the calculation and remain a bibliographic risk.

**Value — PASS.** The theorem exposes a concrete practical interpretation limit: a coefficient residual can pass a fixed relative tolerance while a genuine physical projection barely captures its achievable reduction. The effect persists for equal-norm Gram columns with fixed pairwise coherence, and the exact values for any fixed sweep count distinguish it from an arbitrary ill-conditioned counterexample.

**Scope:** Exact arithmetic, fixed \(a>0\) and number of sweeps, coherent rank-one Gram family, no claim about realized Krylov workloads or variable sweep budgets. Independent verification is not claimed.

Self-review: passed. Independent audit: not yet performed.
