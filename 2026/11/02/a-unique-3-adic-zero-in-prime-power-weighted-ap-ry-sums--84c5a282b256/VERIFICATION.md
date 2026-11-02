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

Run `python3 verify.py` in an ordinary Python 3 environment. The verifier uses only the standard library. It constructs every checked polynomial independently from the defining Apéry sum and from the closed-form coefficient identity, tests the residue-polynomial congruence, enumerates modular roots for small powers, checks valuation strata by modular computations, and checks coefficientwise divisibility for six powers of two.

The proof of the universal assertions is in `RESULT.md`: (1) is telescoped, the single denominator of maximum \(p\)-valuation is isolated, and the integral Hensel lift is shown to be unique. The finite tests do not constitute an exhaustive proof for all primes or powers. There is no independent mathematical audit.
