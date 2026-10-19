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

The accompanying `four_run_checker.py` is self-contained and uses only Python 3 standard-library modules. Execute `python3 four_run_checker.py` in the same directory. It checks every \(1\le a,b,c,d\le6\) against an independent factor-occurrence-mask enumerator (1296 tuples; 125496 candidate pairs), and every \(1\le a,b,c,d\le4\) against a second, direct factor-set implementation (256 tuples). It also verifies the symbolic predicted sets, exact counts, threshold classification, and constructed three-position witness on every checked tuple.

Recorded local execution returned:

`ALL_FOUR_RUN_CHECKS_PASSED quadruples 1296 candidate_pairs 125496 direct_quadruples 256`

No finite enumeration certifies the universal quantifier over arbitrarily large runs. That quantifier is discharged by the case proof in `RESULT.md`. The original source's first-public date is recorded from arXiv:1907.04660, version 1, 2019-07-10; no date is asserted for this new theorem.
