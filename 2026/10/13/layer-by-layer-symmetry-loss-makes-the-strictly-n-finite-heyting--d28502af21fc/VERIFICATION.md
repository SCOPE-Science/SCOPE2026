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

`verify.py` exhausts every top-level permutation for widths from two through seven and, for each truncation depth, constructs the uniquely forced lower-level permutations when possible. It then checks every ordered pair of vertices against the source order relation before accepting the map as an automorphism. The resulting counts are compared with the exact factorial formula, including depths beyond the predicted rigidity threshold.

The program also checks symbolically that the source widths \(q=2^n+1\) hit the rigidity threshold at depth \(q-1\) through \(n=8\). This latter loop is a consistency check only; the proof in `RESULT.md` establishes the all-\(n\) statement.

Expected replay output:

`VERIFY_OK 53567 exact assertions; exhaustive top-layer permutations for q<=7 and all truncation depths`

Scientific limit: finite exhaustive computation does not prove the infinite family. It checks the recurrence and boundary cases in small widths; the general theorem rests on the symbolic adjacent-level argument in `RESULT.md`.
