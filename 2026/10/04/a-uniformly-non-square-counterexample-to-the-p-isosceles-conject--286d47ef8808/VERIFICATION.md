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

The proof is analytic and self-contained. The supplied `verify.py` rechecks the exact polynomial identity defining the maximizer, the closed form \(U_4^4=(71+17\sqrt{17})/64\), all scalar inequalities used to keep the third strip inactive at the extremizing pair, and the numerical value of the extremizing ratio.

The verifier does not establish the literature claim or replace the supporting-line proof of uniform non-squareness. It is intended to catch transcription and algebra mistakes in the explicit constants only.
