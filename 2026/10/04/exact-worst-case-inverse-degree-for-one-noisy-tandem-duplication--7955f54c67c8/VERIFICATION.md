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

The proof is symbolic and all-parameter; computation is used only as an independent check.

`verify.py` constructs the inverse parent set directly from the channel definition: for every possible start it tests whether the two adjacent length-\(k\) blocks differ in exactly one coordinate, deletes the second block when legal, and deduplicates the resulting parents. It separately computes the mismatch profile and checks the exact parent-collision criterion for every legal pair in each exhaustive instance.

Exhaustive tests cover \(27\) binary/ternary parameter cases and \(7{,}829\) received words. The script then constructs the periodic extremal mismatch profile and checks the claimed maximum for \(1\le k\le12\) and \(k\le n\le100\), totaling \(1{,}134\) witness cases. The recorded replay result is:

`VERIFY_OK exhaustive_cases=27 received_words=7829 witness_cases=1134 k<=12_n<=100`

The computation does not certify parameters outside its finite ranges; those are covered by the proof in `RESULT.md`. No claim is made about more than one noisy duplication, variable duplication length, or more than one substituted coordinate in the copied block.
