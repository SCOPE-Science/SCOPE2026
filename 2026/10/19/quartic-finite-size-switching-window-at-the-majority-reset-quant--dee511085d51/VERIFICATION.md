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

# Verification record

The accompanying standalone `verify.py` was executed with installed Python 3, NumPy and SciPy. It reported `23 assertions passed: exact finite-N integrals, three limits and critical window.`

The verification independently integrates the weighted binomial majority probability through regularized incomplete beta functions for odd populations \(N=51,101,201,401,801,1601\), compares those values to the exact entropy prefactor, critical Gamma prefactor, and supercritical phase interval, separately evaluates the Gamma/CDF area, and tests the critical-window profile at \(\xi=-0.7,0,0.7\). These are finite numerical checks; the proof of the limiting formulas and uniformity is contained in `RESULT.md`.

The original Protocol II formula and its supplement were inspected in arXiv:2202.12655. A related reset-renewal generalization, arXiv:2106.13761, was considered for implication comparison. The self-review does not constitute independent proof validation or publication-priority certification.
