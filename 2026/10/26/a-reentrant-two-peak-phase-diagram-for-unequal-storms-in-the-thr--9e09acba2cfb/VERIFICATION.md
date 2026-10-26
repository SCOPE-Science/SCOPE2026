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

# Verification instructions and limits

The claim is a theorem about all real \(d,m>0\). The proof in `RESULT.md` gives an explicit derivative reduction, all boundary cases, and strict sign arguments, including the fold equality. These steps—not numerical tests—establish the claim.

Run `python verify.py` in a directory containing the verification script. This uses the Python standard library, generates a fixed-seed sequence of 4,000 randomized parameter choices (one was excluded for closeness to the fold), and checks exact stationary-point counts and derivative signs in 3,999 remaining cases. It also checks the three reentrant example separations and the maximizing delay in a small numerical neighborhood. The script prints `PASS` on success.

Finite testing is neither exhaustive over real parameters nor a proof of novelty, measurement stability, or hydrologic applicability. Independent validation was not performed.
