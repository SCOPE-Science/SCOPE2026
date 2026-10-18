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

Reproduce by extracting `verify.py` and executing `python verify.py` with Python 3, NumPy and SymPy installed. The program prints `VERIFY_OK` after testing three exact symbolic radical identities, full dense eigenvalue spectra at all 58 integers \(3\le m\le60\), and 400 additional feasible nonsymmetric-weight examples. Checks use actual transition matrices and not only the reduced two-by-two formulas.

The symbolic checks confirm the explicit radical expressions satisfy the tangent quadratic. Full eigenvalue matrix tests and random feasible trials are finite supporting evidence, not a substitute for the all-integer spectral inequalities or the common-kernel uniqueness proof given in RESULT.md. No external independent audit has been conducted.
