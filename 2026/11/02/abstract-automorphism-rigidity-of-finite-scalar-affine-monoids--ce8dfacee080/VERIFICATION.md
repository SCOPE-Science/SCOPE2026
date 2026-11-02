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

# Verification of finite scalar-affine monoid automorphisms
The standalone scripts `check_modular_monoid.py` and `check_direct.py` require only Python 3's standard library. Run them independently from the same directory. The first enumerates normalizer permutations fixing the origin and compares the resulting counts with the full affine semilinear group order; it also validates the multiplication law, left-zero set, and rank-zero cases. The second independently checks every candidate monoid permutation directly against the full multiplication table in three small instances. Both report `VERIFY_OK` and their expected full transcripts are embedded as `check_output.txt` and `direct_output.txt`.

Verified normalizer orders include \(2,24,1344,6,432,24\) for \((q,d)=(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)\). Direct monoid automorphism enumerations independently give \(2,24,6\) for \((2,1),(2,2),(3,1)\). Rank-zero checks cover \(q=2,3,4,5,7\).

These are finite checks only; the proof establishes the result for all prime powers and all dimensions by the characteristic left-zero ideal, the translation Sylow subgroup, and scalar semilinearity. No independent external audit has been performed.
