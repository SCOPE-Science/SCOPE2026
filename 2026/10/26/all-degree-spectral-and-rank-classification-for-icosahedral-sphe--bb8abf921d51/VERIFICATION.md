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

# Reproducibility and limits
Run `python verify.py` with the documented `requirements.txt` packages installed. The program independently constructs all twelve Euclidean icosahedron vertices, checks their pairwise angles and tight-frame identity, evaluates complex spherical harmonics via SciPy, and computes the full Gram eigenvalues at degrees \(0\) through \(25\). It compares each against the stated analytic spectrum with absolute tolerance \(10^{-10}\). SymPy independently prints the exact Legendre recurrence values used to classify exceptional degrees. The recorded stdout is included as `verify_output.txt` and reproduced from the embedded script.

The finite test cannot prove absence of rank loss at arbitrarily large degrees: that conclusion follows analytically from Bernstein's inequality. The test is not independent mathematical audit.
