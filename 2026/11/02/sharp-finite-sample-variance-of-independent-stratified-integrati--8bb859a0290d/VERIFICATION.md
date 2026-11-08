---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The independent equal-width stratum samples make Q_n unbiased, with variance the sum of cell variances divided by n². Fix a cell increment Δ and normalized t=Δ/(L H), H=1/n. Every monotone L-Lipschitz path pushes uniform cell sampling to a probability law containing t·Uniform[0,1]; since y²≤y, the remaining law yields Var≤Δ²(1/4−t/6), with equality for a centered slope-L ramp and equal endpoint plateaux. Set t_i=nΔ_i/L∈[0,1], Σt_i≤s=n min(1,L)/L. The exact cubic h(t)=t²(3−2t)/12 and h(x)+h(y)=h(x+y)+(x+y−1)xy/2 imply a global maximizing vector with k equal positive entries s/k and zeros otherwise. Thus the exact maximum is (L²/n4) max_{ceil(s)≤k≤n}[s²/(4k)−s³/(6k²)]. Differentiate continuous k to get nearest feasible integer 4s/3; L≤1, 1≤L≤4/3, fixed L>4/3, and L≥n boundary formulas follow. Independently checked exact cubic identity and exact optimizer fractions n=1,2,5,11,12,15 with L fractions. The proof supplies the infinite-dimensional bound, not numerical optimization.

## originality

PASS

Basak–Bect–Vazquez Theorem 4.1 settles unrestricted bounded monotone one-sample-per-stratum maximum 1/(4n²), attained by a discontinuous midpoint step. It does not quantify a finite global Lipschitz constraint or the k-cell ramp allocation. Existing general Lipschitz-function variance bounds might overlap the local inequality but do not supply this constrained multi-stratum exact finite-n envelope in the inspected sources.

## value

PASS

The mathematical gap is an exact non-asymptotic worst-case risk for a standard unbiased Monte Carlo estimator under natural simultaneous monotonicity, boundedness and finite-slope constraints. It quantifies the finite-L penalty, active-stratum support and the L=4/3 phase transition, which the known unrestricted monotone theorem cannot resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
