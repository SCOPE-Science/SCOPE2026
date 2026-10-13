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

# Reproducibility
Execute `python3 check_claim.py` using Python 3 and the standard library. The program expands exact four-variable integer-coefficient polynomials and confirms the complete mixed-derivative factorization, verifies the original three-state backward equations in 54 rational parameter cases, and checks that concrete one-tenth-rate-reduction cross increments have opposite signs at catastrophe intensities zero and one when \(x=y=c=1\).

Successful output:

```
VERIFY_OK formal_coefficients= 22 formal_derivative=1 first_step_cases= 54 protection_signs= 2 certificate=exact
```

The all-parameter sign conclusion follows from the exact identity and the strictly positive nonconstant polynomial coefficients, not from finite sampling. The verification does not independently establish whether related literature already contains an equivalent theorem. No external or independent audit was performed.
