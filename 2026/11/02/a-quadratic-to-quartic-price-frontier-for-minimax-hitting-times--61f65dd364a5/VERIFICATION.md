---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification and analytic scope

The delivered `verify.py` was run from the final package directory with Python, NumPy and SciPy. Its exact output was:

```
PASS: 19538 deterministic finite assertions (not a proof of the universal theorem)
```

The checks include absorbing-generator linear-system solutions for random positive mass and conductance vectors, equality of the full pairwise worst first-hitting time and the two endpoint formulas, comparison with unconstrained edge-by-edge epigraph optimizations, heterogeneous-price duality identities, equality at balanced optima, strict active-direction inequalities beyond the one-price threshold, independent feasible competitor samples, exact three-state formulas, and numerical checks of both asymptotic scales.

The numerical optimization solver may return non-success on particular samples; the script counts only inequalities and equalities actually checked, and never treats solver failure as a mathematical certificate. Machine checks at finite sizes do not prove a theorem for all \(n\), all positive prices, or all stationary masses. The universal argument in `RESULT.md` supplies separate exact steps: backward hitting-time recurrences, sharp weighted Cauchy–Schwarz with explicit equality, strict scalar concavity, derivative-sign boundary classification and a controlled singular Riemann sum. The result is not an independently validated theorem.
