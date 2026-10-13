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

Run `python verify.py` after installing the requirements in `requirements.txt`. The exact SymPy checks independently reconstruct the stationary-current parametrization, differentiate the rational current, confirm the quintic numerator and the benchmark factorization, derive both singular scaling polynomials, and evaluate the positive full-occupancy boundary-layer limit. Numerical root checks cover small, moderate, and large positive rate ratios. The observed result is `VERIFY_OK`.

The proof of exactly one positive root for every parameter uses the displayed coefficient sign pattern and Descartes' rule. The asymptotic optimizer location uses analytic two-sided bracketing around simple positive limiting roots. Numerical samples are checks, not proofs for infinitely many parameter values. Neither finite-ring mixing nor the prior published thermodynamic current formula is independently derived here.
