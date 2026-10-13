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

# Verification of the three-exponential moment comparison

The claim is a continuum statement proved analytically. A density convolution and derivative identity give a positive decomposition of the absolute-moment transform. The two positive kernel families have strictly positive logarithmic curvature for every real order \(s\ge2\); the only additional external mathematical premise is the one-order Gaussian moment lower bound in Brazitikos–Tang–Tkocz, Theorem 1.

`verification/check_moments.py` is self-contained, uses only Python's standard library, and ran successfully. To replay, run `python3 verification/check_moments.py` from the directory containing this file. Its 2,647 assertions include independently computed exact rational even moments, mass normalization, variance identities, sampled Gaussian comparisons, exact rational curvature inequalities, and noninteger numerical curvature spot-checks. The finite checks do not prove any interval statement; Steps 1–4 of `RESULT.md` provide the proof.

The convention for coincident positive scales and for one zero coefficient is by continuous limiting of the exact formulas. The scope does not include four or more summands or any independent scientific certification.
