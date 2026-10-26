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

# Reproducibility and verification

The claim and proof are given in `RESULT.md`. Run `python verify_numeric.py` and `python verify_exact.py` with Python 3, NumPy, SciPy, and SymPy installed; neither script requires network access. The exact-rational script checks the complete characteristic-polynomial factorization, shortcut-cost budget, and eigenvalue contact condition for 30 parameter configurations. The numerical script reconstructs the graph Laplacian from incidence vectors on 90 configurations, compares its second eigenvalue with the explicit solution, tests 9,000 independent asymmetric feasible allocations, and performs 12 local constrained minimizations for comparison. The recorded console output is in `verification_output.txt`.

Finite numerical results, regardless of count or precision, cannot establish global optimality over all graph sizes and all real costs. The universal result follows from the explicit invariant spectrum, Schur-complement inequality, and monotonicity argument in `RESULT.md`. The code does not certify absence of equivalent prior literature; no independent mathematical review has been performed.
