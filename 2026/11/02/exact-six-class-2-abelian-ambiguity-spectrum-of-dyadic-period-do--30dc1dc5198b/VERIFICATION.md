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

Run `python3 checker.py` in the directory containing the result files with Python 3; no third-party libraries are needed. The checker independently generates a substantial finite substitution prefix, enumerates its distinct contiguous factors at powers-of-two lengths through 1024, and directly computes all contiguous one- and two-symbol occurrence counts. It also computes all factors recursively by the proved even/odd desubstitution, compares the factor sets exactly, and checks endpoint-stratum class multiplicities.

The completed verification printed `ALL_DIRECT_AND_RECURSIVE_CHECKS_PASSED`, including length 8 spectrum (1,1,2,2,3,3), length 16 spectrum (2,3,3,5,5,6), and length 1024 spectrum (170,171,171,341,341,342). These tests are finite, while the arbitrary-length result depends on the exact recurrence and induction in RESULT.md. The original full-text comparison is described in AUDIT.json. No external or independent mathematical audit was performed.
