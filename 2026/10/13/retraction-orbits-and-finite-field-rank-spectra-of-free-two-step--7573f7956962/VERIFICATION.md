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

# Verification of the retraction rank polynomial

The accompanying `verify.py` uses only the Python standard library. Run `python verify.py` in the directory containing this file to enumerate all generator maps for \((n,q)=(2,2),(2,3),(3,2)\); each extends uniquely to an endomorphism of \(V\oplus\bigwedge^2V\). The program builds the full Lie endomorphism matrix, tests composition idempotence, verifies every basic Lie bracket, determines the full linear rank, and compares all coefficients with the closed polynomial.

Observed distributions: \((n,q)=(2,2)\): ranks \(0,1,3\) with counts \(1,12,1\); \((2,3)\): counts \(1,36,1\); \((3,2)\): ranks \(0,1,3,6\) with counts \(1,224,896,1\). Standard output ends with `VERIFY_OK`.

The checker exhausts the specified finite cases only. The all-dimension, all-characteristic theorem rests on the complete algebraic proof in `RESULT.md`, not on extrapolation from the checks. Gaussian coefficients are integer product ratios, and the exponent \(r(n-r)(n+2r)/2\) is integral for the stated ranges. No computationally intensive external certification or independent audit has occurred.
