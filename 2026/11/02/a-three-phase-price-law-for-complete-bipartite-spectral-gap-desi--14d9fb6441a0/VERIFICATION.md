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

# Reproduction

Run `python3 verify.py` with Python 3, NumPy, SciPy and SymPy. The script constructs full Laplacian matrices, checks exact characteristic polynomials, verifies symbolic envelope identities, compares full-matrix eigenvalues to the claimed unit spectral gap, and runs independent numerical constrained minimizations on a parameter grid. The checked execution passed 1,716 deterministic assertions and 26 successful numerical optimizer runs.

The certificate is not a substitute for the all-parameter proof in `RESULT.md`. Numerical optimization can miss counterexamples outside sampled dimensions and ratios, and the script does not certify uniqueness of all asymmetric designs. No independent audit has been performed.
