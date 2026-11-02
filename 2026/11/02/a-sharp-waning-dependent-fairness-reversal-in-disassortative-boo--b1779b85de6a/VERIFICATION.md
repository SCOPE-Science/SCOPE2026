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

# Reproducibility and checks

From a directory containing `verify.py`, run `python verify.py` after installing `sympy` and `mpmath`. The script verifies the differentiated stationary susceptibility and the auxiliary positivity-polynomial derivative with exact computer algebra through order 32; it also checks centered finite-difference curvatures in 40 cases, the two endpoint allocations for \(\alpha=2\), and \(u_c(2)\) to at least 14 decimal places. The run passed.

The infinite positivity and uniqueness claim is proved in `RESULT.md` using a general coefficient identity; finite checks cannot establish it. The interpretation is limited to the stationary disease-free invasion matrix. No independent audit, independent validation, or full epidemic convergence verification has been performed.
