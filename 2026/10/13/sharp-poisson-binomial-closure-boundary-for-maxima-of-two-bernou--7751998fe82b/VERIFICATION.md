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

Extract `verify.py` from the same record into a file in the same directory and run `python3 verify.py`. The standard-library verifier uses exact rational arithmetic for its tests and confirms the explicit two-trial discriminant factorization, three-trial PGF coefficients and cubic discriminant factorization on independent finite rational parameter sets. It also brackets the unique interior threshold between \(0.150732\) and \(0.150733\). A deterministic small-parameter check corroborates the coefficientwise scaling in degrees three through seven.

The universal claims rely on the displayed algebraic expansions, real-root criterion for probability-generating polynomials, and the standard continuity theorem for roots of fixed-degree polynomials. The finite test grid does not independently prove an algebraic identity or a statement over infinitely many parameters. There is no claimed external, formal, or independent certification.
