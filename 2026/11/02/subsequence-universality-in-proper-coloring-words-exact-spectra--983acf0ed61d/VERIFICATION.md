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

# Verification and reproducibility

Run `python3 verify.py` using the Python 3 standard library. It verifies the analytic stage-product coefficients against a distinct actual-letter mask recurrence, enumerates every proper host within the reported finite parameters, and checks literal scattered-pattern membership for a smaller exhaustive range. It also checks the ternary cubic rational recurrence, binomial survival tails, and sharp shortest-host counts.

Successful extracted-package output:

`VERIFY_OK proper_hosts=1130960 literal_pattern_checks=112420 parameter_coefficients=228 alphabets=2..6 nmax={2: 12, 3: 18, 4: 10, 5: 8, 6: 7} ternary_binomial_tails=TRUE`

Only those finite instances have been machine-enumerated. The all-parameter formal identity follows from the arch decomposition, and the Gaussian law from the i.i.d. renewal representation plus a standard renewal limit theorem. There is no independently executed scientific audit or external certification.
