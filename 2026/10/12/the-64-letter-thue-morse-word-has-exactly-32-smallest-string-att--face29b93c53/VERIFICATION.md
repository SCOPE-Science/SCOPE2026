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

Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs \(t_6\) from the Thue--Morse morphism. It computes the exact position-cover set of every distinct factor twice: once by grouping every substring interval and once by independently enumerating factors and locating all overlapping occurrences.

After removing only cover sets made redundant by inclusion, it checks every three-position subset of the 64 positions and every four-position subset. There are no size-three attractors and exactly 32 size-four attractors.

A separate recursive hitting-set enumerator runs on the unreduced factor-cover collection and must return exactly the same 32 sets. Finally, the result is compared byte-for-byte as integer tuples with the two closed-form 16-element families and checked for reflection closure.

Independent audit has not been performed.
