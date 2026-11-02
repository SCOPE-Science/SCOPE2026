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

# Verification and limits

The standalone `verify.py` reproduces the distance-polynomial identities by exact rational coefficient arithmetic. It independently evaluates the seven spectral branches using high-precision decimal arithmetic for illustrative orders, including values in the analytically controlled regime, and confirms the two-term formula to the expected order. The expected output is:

```
CHECK_OK exact_polynomial_identities= 512 finite_spectral_checks= 130 uniform_proof_applies_q>=100
```

Run `python3 verify.py` with Python 3.11 or later and no third-party dependencies. The analytic inequalities proving positivity of the bipartition derivative, existence of the unique root, and strict negativity of the competing eigenvalues for every admissible order are written explicitly in RESULT.md. The finite checks are neither exhaustive over all orders nor a substitute for those arguments.

The source relationship and remaining novelty risk are explained in REVIEW.md and AUDIT.json. No independent audit has been undertaken.
