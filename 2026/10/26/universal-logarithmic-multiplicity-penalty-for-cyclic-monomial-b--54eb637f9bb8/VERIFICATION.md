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

# Verification of the critical multiplicity theorem

The theorem is proved analytically in `RESULT.md`, Steps 1–4. Independent validation has not been performed. The supplied pure-Python checker `verify_critical_multiplicity.py` checks the rational finite Hilbert-matrix identity exactly for \(2\le r\le9\), and compares numerical reciprocal error differences to the predicted limit for three distinct monomial exponent patterns at degree \(K=20{,}000\) and \(r=2,3,4\).

Executed command: `python3 verify_critical_multiplicity.py`.

Actual output: `CHECK_OK: exact Cauchy identities r=2..9 and 9 independent 20000-degree asymptotic tests`.

The checker is included with its dependencies (Python standard library only), can be run from the directory containing the embedded files, and does not depend on earlier calculations or other records. The finite numerical tests do not certify the infinite asymptotic statement; the rigorous reduction, Stirling estimates, Schur-complement limit, and Cauchy determinant identity supply that conclusion. The main reproducibility choices are the coefficient norm of `RESULT.md` and a total-degree multiplier cutoff of \(dK\), with \(d\) fixed.
