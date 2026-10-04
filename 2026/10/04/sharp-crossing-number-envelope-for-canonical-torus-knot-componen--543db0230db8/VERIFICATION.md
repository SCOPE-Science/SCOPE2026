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

The proof was checked algebraically against the determinant-one component-tree parametrization. The standalone exact-integer replay is `artifacts/verify_crossing_envelope.py`.

Running the script produced:

`VERIFY_OK pairwise u<=12,v<=14 and global n<=24`

The script verifies the canonical split and component lengths for every generated test knot, checks both sharp extrema and uniqueness on the tested component-size range, and checks the fixed-total-size maximizer through \(n=24\). These finite computations are supporting checks only; the infinite statement is established by the proof in `RESULT.md`.

Scientific limitation: canonical layered size is not asserted to equal minimal triangulation complexity in general.
