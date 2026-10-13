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

# Verification notes

The unrestricted proof uses an injectivity statement for the integer difference map, a modular separation of two difference sets, and an exact rank-one Laurent identity. These are proved without numerical approximation in `RESULT.md`. The graph is unweighted and locally finite, and the eigenvector is finitely supported on the prescribed two vertex orbits.

Run `python3 artifacts/verify.py` from the directory containing the extracted files. The script uses only Python's standard library, checks integer sets and coefficients exactly for \(2\le r\le8\), tests the full Laurent determinant identity coefficient by coefficient, and directly evaluates the compact eigenvector residual in both vertex types. Expected final line: `VERIFY_OK exact_Laurent_and_compact_eigenvector r=2..8`.

Finite checks are diagnostics; they do not establish the universal claim. The analytic proof applies to every integer \(r\ge3\). No independent audit has been performed.
