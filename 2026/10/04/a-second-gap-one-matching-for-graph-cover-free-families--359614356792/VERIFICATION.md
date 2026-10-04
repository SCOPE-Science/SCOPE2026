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

The claim is finite on the constructive side and theorem-based on the lower-bound side.

`verify.py` reconstructs the fourteen displayed subsets on \([6]\), groups them into seven matching edges, checks endpoint incomparability, and checks for every edge that none of the twelve blocks off that edge is contained in the union of its endpoint blocks. This is exactly the \(E_{14}\)-CFF condition used in the claim. The verifier also recomputes \(t(1,14)=6\) and \(t(1,7)=5\) from the central-binomial form of Sperner's theorem.

A successful replay prints:

`ALL CHECKS PASSED; blocks=14; edges=7; cover_checks=84; t1_14=6; t1_7=5`

No random sampling, floating-point calculation, timeout, or partial enumeration is used. The checker does not attempt a literature search and does not establish originality; that assessment is documented separately in `REVIEW.md` and `AUDIT.json`.
