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

# Verification details

Running the packaged standard-library program with `python3 checker.py` returned:

```
EXACT_RATIONAL_CASES_OK 3 4 8
PARAMETER_GRID_OK 720
BOUNDARIES_OK
FINITE_DIFFERENCE_JACOBIANS_OK 12
VERIFY_OK
```

The exact rational tests use \(\lambda=\varepsilon=1\) and \(\beta=1/25\). The one-step matrices, square-of-conjugated Jacobian identity, and determinant/trace of the two-step derivative are checked in rational arithmetic at gains \(3,4,8\). A deterministic 720-case parameter grid checks the cycle and Floquet data; further checks exercise the finite and unbounded spectral plateau boundaries.

Floating-point calculations at repeated-root endpoints can exhibit a square-root amplification of rounding. The diagnostic therefore uses an appropriate numerical tolerance while the exact rational characteristic polynomial decides the endpoint identities. The analytic proof in RESULT.md, not the finite tests, establishes the universal assertions. No external or independent validation has been performed.
