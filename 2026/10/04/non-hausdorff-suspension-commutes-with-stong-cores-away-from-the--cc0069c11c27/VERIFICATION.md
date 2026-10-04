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

The symbolic proof in `RESULT.md` is the proof of the unrestricted theorem. The executable check is deliberately finite and independent of that proof structure.

Running `python3 verify.py` enumerates every labeled poset on \(1\) through \(5\) points, totaling \(4473\) posets. For the deterministic beat-point reduction of each poset it verifies that every chosen beat deletion remains valid after one non-Hausdorff suspension. It then verifies the exact minimality criterion and direct core sizes after \(k=1,2,3\) suspension iterates.

The replay reports \(14864\) lifted beat deletions and \(17892\) theorem instances and ends with `VERIFY_OK`. The finite enumeration is not an exhaustive proof for arbitrary cardinality; untested sizes are covered only by the symbolic argument.
