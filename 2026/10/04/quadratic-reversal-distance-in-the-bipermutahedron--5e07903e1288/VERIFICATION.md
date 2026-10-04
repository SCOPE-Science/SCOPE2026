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
The standalone script `verify_bipermutahedron_reversal.py` implements the two published local edge moves on bipermutations. Breadth-first search gives distances \(2,8,15,24\) for \(n=2,3,4,5\), respectively. The script also checks the elementary lower-bound inequality over a range of \(n\) and singleton-set sizes.

The finite search is corroborative only. The proof for all \(n\ge3\) is the copy-inversion argument in `RESULT.md`, together with the explicit block-selection path. No claim is made that the full graph diameter equals \(n^2-1\).
