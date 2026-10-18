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
The mathematical proof in RESULT.md is self-contained given the published reflection-center classification. In particular, the proof of the off-coordinate-line bound does not rely on sample data.

Run `python3 check.py` from this package: six exact prime-field tests for \((r,d,p)=(3,4,17),(4,4,17),(5,4,17),(3,5,11),(4,5,11),(4,6,13)\) exhaustively construct the center set, enumerate all lines spanned by distinct centers by Plücker minors, and check that exactly \(\binom r2\) lines are rich with \(d\) centers and all others have no more than three.

These are finite computational checks only. They do not establish the uniform complex proof, uniqueness of invariant smooth hypersurfaces, or literature originality. No independent audit has been performed.
