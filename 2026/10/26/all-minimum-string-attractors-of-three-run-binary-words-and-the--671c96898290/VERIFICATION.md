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

Execute `python3 verify.py` in the same directory. The program generates independent occurrence masks of every contiguous factor and enumerates all two-position hitting sets. Each of the \(14^3=2744\) parameter triples is compared against the structural candidate sets; the program separately rejects all singleton sets. It then verifies that the exact rational function produces the aggregate counts, including the distinct-word uniqueness counts, for each of the 38 lengths from \(3\) through \(40\).

Successful local output: `VERIFY_OK exhaustive_triplets=2744 maximum_single_run=14 enumerator_coefficients=38 unique_counts=38`.

The universal theorem for all positive run lengths is established by the factor-type and forced-boundary proof in `RESULT.md`. Finite computation neither certifies untested lengths nor proves literature originality; no independent audit has been conducted.
