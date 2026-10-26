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

## Verified scope

The general result is established by algebraic two-step update identities and exact cyclic run enumeration in `RESULT.md`. The complement symmetry, boundary cases \(n=3\) and \(n=4\), and multiplicity convention for the two-vertex step-two cycle are explicitly accounted for.

## Computational cross-check

Running `python verify.py` from a directory containing the standalone file checks every one of the \(2^{n+1}\) states for each \(3\le n\le14\). For each size it independently compares the direct recurrent-state census with the weighted run polynomial. The included `check_output.txt` records the successful execution. Exhaustive checks at bounded \(n\) do not establish arbitrary-size correctness; that rests on the proof.

## Limitations

No external independent audit has been performed. The closed formula does not address transient basin statistics, stabilization times, or quotienting by graph symmetries. The literature comparison is bounded by the sources inspected and remaining indexing/access limits.
