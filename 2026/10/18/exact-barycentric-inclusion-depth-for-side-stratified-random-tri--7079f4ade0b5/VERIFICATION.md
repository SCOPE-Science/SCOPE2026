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

# Verification record

The result has an explicit analytic proof in `RESULT.md`. A reproducible standalone Python checker (`python3 checker.py`) independently implements the geometric containment inequalities for the three sampled side points rather than reusing the corner decomposition. It also compares the one-corner integral with independent Simpson quadrature, tests the derivative order numerically, integrates the spatial mean, and checks the directional entropy limit.

Actual run results: six corner integrals passed; four reproducible direct Monte Carlo experiments (180,000 trials each) passed with absolute tolerance 0.011; strict Schur derivative comparisons passed on the stated grid; normalized spatial mean 1/4 passed by quadrature; five vertex-direction entropy limits passed; `ALL CHECKS PASSED` printed. Monte Carlo deviations were within 0.0021 of the exact formula. The mathematical proof is not inferred from these finite checks.

Limitations: publication-history searches may miss equivalent work; no independent mathematical audit or external validation has been performed.
