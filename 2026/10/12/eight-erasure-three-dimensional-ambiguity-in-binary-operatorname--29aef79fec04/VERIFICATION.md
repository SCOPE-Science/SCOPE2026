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

# Reproducible verification

From the extracted package root run `python3 artifacts/verify.py` with Python 3 standard library. No external data or packages are required. Expected end marker: `VERIFY_OK`.

The program directly enumerates every eight-erasure graph, verifies that only the stated shapes have cycle-nullity three, and exhausts all seven-erasure graphs for parameters \((m,n)=(2,4),(2,6),(3,3),(3,4),(4,4)\). Separately it constructs a systematic generator matrix and enumerates every three-dimensional coefficient subspace in reduced row-echelon form, verifying their minimum supports and the bijection to the eight-erasure sets. The \((4,4)\) instance checks \(788035\) distinct three-spaces and finds exactly \(156\) minimum-support ones, with shape distribution \(6,144,6\) in the three cases.

These are exact finite calculations; the proof for unbounded \(m,n\) is the graph-theoretic argument in `RESULT.md`. This check is not a proof of literature uniqueness, and an independent audit has not been performed.
