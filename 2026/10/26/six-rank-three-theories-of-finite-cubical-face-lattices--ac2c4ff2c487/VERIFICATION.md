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

Run `python3 verify.py` in this directory. No external dependencies are required.

The exhaustive orbit-type engine `logical_types.py` enumerates all two-face coordinate orbits and all possible third-face order-relation patterns. `verify.py` independently checks the same complete rank-three types using explicit elementwise relations for dimensions \(0\) through \(5\), and evaluates the orbit engine for every dimension through \(27\). The program confirms the six class signatures, equality of the signatures at dimensions \(5\) through \(27\), an explicit rank-three distinguishing sentence, and the representative size \(244\). The complete stdout is `output.txt`.

The infinite tail is proved by a three-round coordinate-color Ehrenfeucht–Fraïssé strategy with initial threshold \(27\), as given in `RESULT.md`. Program output does not purport to verify that infinite lemma; no finite sample can do so. Complete text overlap with some historical works is unverified, and independent external scientific audit has not occurred.
