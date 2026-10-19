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

The proof is a finite EPPF calculation plus a quadratic sign analysis, valid for every parameter satisfying \(0\le\alpha<1\) and \(\theta>-\alpha\), and every integer \(n\ge2\). The standalone checker `check.py` uses `fractions.Fraction` and complete enumeration of all set partitions through eight labels for five rational parameter pairs and four deterministic graph families. It checks exact normalization, expectations, and mixed covariances; 1,015 comparisons passed.

The checker is a finite consistency test, not proof for untested values of \(n\), irrational parameters, or arbitrary graphs. Generality follows from exchangeability, the marked-block EPPF factorization, and the exact quadratic calculation documented in `RESULT.md`. Historical priority has not been independently verified.
