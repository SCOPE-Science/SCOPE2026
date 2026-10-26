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

The supplied `verify.py` is self-contained Python 3 and requires no third-party packages. Execute `python3 verify.py` in the same directory. The successful run prints `HEIGHT_TWO_PREFIX_NORMAL_SEMIGROUP_PASS` and reports 16,383 height-two Dyck paths for semilengths 1 through 14, counts, and stabilized genus values.

The verifier evaluates each original factor-count prefix-normal inequality directly rather than using the proved semigroup shortcut; independently enumerates semigroup subsets and closure; tests mutual agreement, area, genus, conductor, multiplicity and first return; and compares known OEIS A326083 counts. It also evaluates sharp stabilization to genus seven.

The all-length theorem requires, and is supplied by, the mathematical proof in `RESULT.md`. Finite verification does not prove all cases; no external independent audit, formal proof certification, or automated human validation is claimed.
