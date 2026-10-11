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

# Reproducibility and limits

Run `python3 verify.py` with the Python 3 standard library. This checks every height-rotation-fixed cyclic word for odd lengths \(N\in\{3,5,7,9,11,13\}\), the full crossing-exchange conditions across every basepoint and integer pair, trivial deletions, and both standard symmetries. It also reproduces the \(50\) seven-petal components of the published same-petal-count graph as an external check on the implemented moves. The symbolic all-length proof is in `RESULT.md`; no finite run is presented as a proof for arbitrary lengths. The code does not identify knot types or evaluate nonstandard knot invariants. The review is same-model only; independent audit has not been performed.
