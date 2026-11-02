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

# Reproducible verification

Run `python3 checker.py` using Python 3 and its standard library; a successful run ends with `ALL_CHECKS_OK`. The direct enumerator checks the condition that every positive coordinate of a row points to a state having that same complete row. The formula enumerator independently builds all set partitions. The orbit tester applies every simultaneous permutation to rows and columns rather than relying on the claimed orbit product. All listed direct tests and the idempotent boundary succeeded. This is a finite cross-check; the proof for all sizes and denominators is the set-partition and simplex argument in RESULT.md.

Independent audit was not performed.
