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

Run `python CHECK.py` with `mpmath` available (see `requirements.txt`). The code implements the exact half-integer formula and independent Bessel-integral quadratures, checks the Langevin-function logarithmic derivative identity, locates stationary points for representative tilts with high-precision bisection, and tests the two endpoint expansions. It prints `CHECK_OK` followed by the count of completed assertions. The numerical root samples and the finite collection of checked tilts are not an exhaustive proof. The accompanying `RESULT.md` gives an analytic proof with explicit quantifiers and critical asymptotic steps. No independent audit has been performed.
