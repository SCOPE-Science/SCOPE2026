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

The analytic proof was reconstructed from the scalar vector field and the convexity assumptions. The critical checks are: \((1-r)/\epsilon>0\); \(\pi'\le0\); the chord inequality \(\pi(P)\le1-P/p_*\); strict decrease of the comparison function; and the affine majorization obtained from \(\pi'(P)\ge\pi'(0)\).

`verification/verify.py` independently checks the equality case and representative convex polynomial families. It prints `VERIFY_OK` only if all tested inequalities and exact identities hold. These finite checks do not replace the proof and make no claim of exhaustive numerical certification.

The source's existence, stability, and comparative-statics conclusions are outside this verification except where their monotonicity calculation is used to order the unique root. No independent audit has been performed.
