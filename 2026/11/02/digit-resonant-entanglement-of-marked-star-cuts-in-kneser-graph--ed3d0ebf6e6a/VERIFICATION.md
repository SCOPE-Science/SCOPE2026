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

# Verification details

The finite-field checker is `check.py` (NumPy required; see `requirements.txt`). From the standalone source, reconstruct the actual Kneser disjointness matrix for each marked-star partition, compute its rank by Gaussian elimination over the given prime, then independently compare the closed incidence-block expression. The checker also constructs graph-state amplitude vectors for two ten-qudit examples in dimensions two and three and checks the reduced-state nonzero eigenvalues.

Observed successful execution: `VERIFY_OK exact_cross_matrix_checks=135 direct_spectra=4 sharp_resonance_checks=4284 largest_eigenvalue_error=1.94e-16 universal_odd_graph_checks=52`. The rank and spectrum checks are finite samples, and the congruence checks range over tested parameters only; the infinite theorem is established by the explicit mathematical proof in RESULT.md. The output is not an independent audit.
