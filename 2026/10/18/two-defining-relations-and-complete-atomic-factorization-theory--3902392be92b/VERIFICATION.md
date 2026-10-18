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

# Reproducible checks and limits
Run `python3 verify.py` with an unmodified Python 3 standard library. The program enumerates every product of the eight proposed monoid atoms below the inclusive integer bound \(10^{20}\), independently computes prime valuations, recovers prime-factorial coordinates, and compares every atomic-factorization fiber against the exact closed count formula, the canonical normal form and the length-set endpoints. It checks both defining identities, the eight singleton atomic generator fibers and the two essential length-two/four collision witnesses.

The extracted, freshly executed program reported:

`VERIFY_OK bound=100000000000000000000 distinct_numbers=9556 factorizations=10008 relation_checks=2 full_count_and_normal_form_checks=9556 atomic_generators=8 length_set_checks=9556`

This finite enumerator is not an infinite certificate. The general congruence, minimal presentation, complete-intersection statement and global invariants rest on the explicit well-founded rewriting and uniqueness arguments in RESULT.md. No independent external audit is claimed or performed.
