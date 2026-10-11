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

The complete dimension-uniform argument is provided in `RESULT.md`: Jensen strictness for balanced signs; nonzero Walsh coefficients from the absolutely convergent integral for the absolute value; Fourier inversion on the antipodal cube; compactness and an explicit sign-class extremizer.

An exact-arithmetic finite diagnostic is supplied in `verify_rectangular_endpoint.py`. It explicitly evaluates all sign inputs, checks the exact sharp ratio, enumerates all nontrivial even Fourier coefficients and their nonvanishing for column dimensions \(2,4,6,8\), confirms strict Jensen loss for a nonflat row, and confirms strict loss if one sign class is omitted. Run with ordinary Python 3: `python verify_rectangular_endpoint.py`.

These four finite cases do not establish any claim for all even dimensions. The analytic proof does. Independent external audit and exhaustive literature verification are not performed.
