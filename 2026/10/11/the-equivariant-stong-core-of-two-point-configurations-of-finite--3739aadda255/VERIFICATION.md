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

Run `python3 verify.py` with Python 3 and no dependencies. Actual execution from the delivered source printed `VERIFY_OK` after complete reconstruction for each parameter from 2 through 12 inclusive. The verifier checks all original points, every nontrivial incidence order, every beat witness, the full pointwise order-preserving retraction, absent core beat points, cardinalities, and equivariance under the rotation, reflection and two-coordinate swap generators. Representative boundary outputs: n=2, total=12, down-beat=8, core=4, height3=0; n=12, total=552, down-beat=48, core=504, height3=1.

The program confirms only these eleven finite parameter instances and does not certify all n. The full quantified conclusion is the symbolic proof in `RESULT.md` using the unique strict predecessor, finite-space order-map homotopy, non-beat-point analysis, and uniqueness of Stong cores. The independent audit status remains not performed.
