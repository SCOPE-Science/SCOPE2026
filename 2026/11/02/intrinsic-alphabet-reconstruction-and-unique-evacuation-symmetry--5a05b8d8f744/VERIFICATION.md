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

# Reproducibility and verification

Run `python3 verify_stylic.py`. It constructs the transformations associated with insertion of each letter into every possible column, closes these transformations under composition, and compares their action tables directly. It uses no external modules beyond the Python standard library.

Verified cases: ranks \(1\) through \(5\), respective sizes \(2,5,15,52,203\) and idempotent counts \(2,4,8,16,32\). For ranks \(1\) through \(4\), a complete two-sided Green-ideal calculation identifies precisely the original generator transformations as maximal proper \(\mathcal J\)-elements. For every checked rank, the idempotence orientation test is checked on all ordered generator pairs; all generator permutations are tested; and the source's reverse-letter/reverse-word anti-involution is checked against every pair in the full multiplication table. Program output ends `VERIFY_OK`.

The unlimited-rank classification is proved abstractly in RESULT.md; the finite checks only guard against implementation, order-convention, and small-boundary errors. The source theorems used as premises and global originality are not independently audited here.
