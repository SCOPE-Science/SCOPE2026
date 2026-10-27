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

# Reproducibility and boundaries

`verify.py` directly enumerates all disjoint domain-image pairs for orders 2 through 12, constructs the unique increasing partial injection for each pair, and tests both forward and inverse up-fence preservation and individual parity. This direct test is logically independent of the gap-criterion calculation in the proof. It compares every rank coefficient with fixed expected histograms, tests the attained rank range, and verifies the complete words for orders 4, 8, and 12. A separate exhaustive complement-domain check tests all order-16 top-rank candidates. It does not enumerate all of the monoid for large orders or prove the general theorem, which follows from the written proof.

Run `python3 verify.py` from the directory containing both files. Python standard library is sufficient. See `verification_output.txt` for recorded output. No independent mathematical audit or validation has been performed.
