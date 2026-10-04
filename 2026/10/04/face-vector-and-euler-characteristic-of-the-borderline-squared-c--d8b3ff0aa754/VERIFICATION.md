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

`verify.py` constructs the square of each cycle \(C_{k+5}\) for \(3\le k\le14\). For every five-subset it compares direct induced-graph connectivity with the proof's cyclic-run criterion. It then generates every nonempty face from the resulting facets and checks the full face vector, the reduced Euler characteristic, and the conditional \(\beta(k)\) identity.

The replay prints one summary row per tested \(k\) and ends with `SQUARED_CYCLE_FACE_VERIFY_OK`. The enumeration is finite and is used only as a regression and boundary check. The claim for every \(k\ge3\) rests on the all-parameter run-classification proof in `RESULT.md`.

No independent audit has been performed.
