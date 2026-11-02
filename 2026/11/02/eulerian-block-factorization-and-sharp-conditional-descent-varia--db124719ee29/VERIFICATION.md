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

Run `python3 verify.py` in a directory containing the standalone file. The script uses only the Python standard library and exact rational/integer arithmetic.

The tested full permutation lengths are 1 through 9. For each, it independently groups every permutation by its full left-to-right record-position pattern, compares its entire conditional descent polynomial with the prescribed product of Eulerian polynomials, and compares exact conditional means and variances. Every feasible record pattern is encountered. It separately enumerates all position patterns for every length 1 through 15 and every record count, verifying both sharp variance endpoints. The execution completed with `ALL CHECKS PASSED: 1151`.

The all-size conclusions rely on the independent-block symmetry and sharp composition inequalities given in RESULT.md; neither finite enumeration nor a test log proves them. No external independent audit has been performed.
