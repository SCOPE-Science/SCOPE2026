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
# Reproducibility and checked limits

Run `python3 verify_simplex_kurtosis.py` from the folder containing the extracted files. Python 3 and its standard library are the only requirements. The checker independently enumerates Dirichlet monomials for the second and fourth interpoint-distance moments for representative integer simplices in dimensions two through four; compares them against the closed formulas; validates the exact sum-of-squares identity; checks the regular-simplex inertia equalities; checks explicit nondegenerate near-collapse cases; and scans a finite grid of zero-sum integer vectors for the sharp scalar bound. It printed: `PASS: 90001 exact rational diagnostics`.

This computer check is finite: it does not independently establish the theorem in arbitrary dimension, does not prove the Lagrange-multiplier lemma, and does not certify historical novelty. Those statements rely on the written analytic proof. Independent mathematical audit has not been performed.
