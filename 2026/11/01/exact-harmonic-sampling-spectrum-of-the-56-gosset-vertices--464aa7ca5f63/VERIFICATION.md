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

# Reproducible checks

Run `python3 check_gosset.py` with Python 3 and its standard library. The program uses exact `fractions.Fraction` arithmetic to reconstruct the 28 pair labels, certify the Seidel identity \(S^2-6S-27I=0\), calculate normalized Gegenbauer values, verify the beta-moment bound \(965/59049\), and compute rational ranks of the parity blocks through degree 12. The expected output begins `GOSSET_HARMONIC_EXACT_CHECK_OK`.

The central mathematical assertion for **all** degrees \(k\ge5\) is not certified by finite testing: the analytic Gegenbauer integral representation and the explicit strict beta-moment bound are written in RESULT.md. The checker verifies that bound's rational inputs and low-degree exceptions. Literature comparison and provenance limits appear in REVIEW.md and AUDIT.json. Independent mathematical audit and external validation have not been performed.
