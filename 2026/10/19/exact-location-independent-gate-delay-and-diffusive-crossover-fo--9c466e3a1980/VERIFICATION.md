---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The killed chain has a unique finite mean: with positive probability bounded uniformly over its finitely many transient states, the walker reaches the open endpoint before any gate flip within a fixed time. The backward equations use total walk rate two only at interior sites, and include κ in the lost rate at the reflecting endpoint when its flip kills. Reflection gives M₀=M_N=C; the interior average solves ΔM=−1 and thus M_i=i(N−i)/2+C, while the half-difference solves ΔH=2κH with H₀=−C and H_N=C. Substituting H₁/C=sinh θ coth(Nθ/2)−cosh θ into the reflecting endpoint equation gives 2C[κ+sinh θ coth(Nθ/2)]=N+1. The same boundary balance gives C₁=1/[2(1+κ)] when there are no interior points. The derivative of the hyperbolic part, multiplied by 2sinh²(Nθ/2), is cosh θ sinh(Nθ)−N sinh θ>0; the κ part increases as well. For fixed N the hyperbolic term tends to 2/N at zero rate and is asymptotic to κ at large rate. At κ=c/N², Nθ→√(2c) and Nκ→0, yielding the stated crossover and its limiting constants. As a separate check, I folded the process into the frame where 0 is open: a flip sends i to N−i and the chain is killed at 0. Fifteen rational rate/order solves (N=1,2,3,7,11; κ=1/7,2,27/13) gave the location differences exactly and matched the hyperbolic delay at 65 decimal places. The backward-equation proof handles all N and κ.

## originality

PASS

The closest inspected exact discrete result uses a directed cycle and a spatially averaged mean. The closest continuum antecedent has alternating boundary gates and supplies the switching-boundary framework; the crossover profile is the explicit interval solution of that framework. Neither covers the closed all-size undirected lattice path profile with reflecting vertices, instantaneous killing on a flip, and uniform initial gate. The distinct supported result is the finite-size endpoint correction and site-independent delay, with controlled convergence to the continuum expression; not a new switched BVP or a novel continuum model.

## value

PASS

An all-site finite-path mean is a natural benchmark for random walks with switching endpoints. It identifies an exact invariant of start positions despite stochastic boundary switching, supplies a simple rational evaluation, and distinguishes fast, quasistatic and diffusion-scale switching effects. The finite correction is meaningful even when the continuum profile is obtained by established methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
