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

# Reproducible verification

Run `python3 verify.py` with NumPy. The program independently assembles the weighted graph Laplacian for each parameter pair, compares full eigenvalues against the predicted spectral decomposition, checks the cost and normalized target eigenvalue, checks the threshold sign conditions, and samples general nonsymmetric feasible allocations. The observed result was `PASS 1779 finite structural/spectrum/budget/asymmetric comparisons`.

The reproducible checks are finite, use floating-point eigenvalues with explicit tolerances, and do **not** prove all-dimensional optimality. That is established by the Rayleigh-quotient symmetrization, block spectrum, and strictly convex budget argument written in RESULT.md. In particular, failures to find random counterexamples are not treated as evidence of a universal upper bound without the proof.
