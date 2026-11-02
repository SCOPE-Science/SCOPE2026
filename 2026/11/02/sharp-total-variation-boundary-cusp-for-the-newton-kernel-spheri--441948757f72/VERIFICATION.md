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

# Verification and scope

The proof in `RESULT.md` is self-contained apart from elementary harmonicity and latitude integration. A standard-library Python checker `verification/check_newton_boundary.py` independently tests normalization of both measures, the equality of their positive and negative total-variation masses, exact rational three-dimensional antiderivatives for square-gap parameters, and the bounded second-order remainder after subtracting the leading and fractional terms.

To replay after extraction:

```bash
python3 verification/check_newton_boundary.py
```

Recorded output is in `verification/check_output.txt`. It reports 333 successful assertions. Numerical Simpson quadrature has stated finite accuracy and is not a proof of the infinite-dimensional or all-parameter statements. The analytic proof supplies the fixed-dimension asymptotics, exact event, weak derivative and limits of validity. Independent mathematical audit has not been performed.
