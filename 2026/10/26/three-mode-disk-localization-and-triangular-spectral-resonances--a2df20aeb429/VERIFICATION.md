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

# Verification

From the extracted package root run `python verification/check.py` with Python, SymPy and mpmath available. Recorded local output in `verification/results.txt` contains 161 successful assertion groups.

The verifier checks the exact polynomial derivative identity for integer indices 0 through 50; direct exact incomplete-Gamma tail representations and adjacent differences through index 14; the first simultaneous triple-degeneracy at squared radius 2; and high-precision agreement of the three candidate eigenvalues with the largest of the first 100 eigenvalues at 11 test radii.

The proof of claims for all radii and all nonnegative integer indices is the polynomial identity plus exact index-root/sign and number-theory arguments in `RESULT.md`, not finite or floating-point testing. Some literature with different normalization could contain equivalent statements; independent priority verification is absent.
