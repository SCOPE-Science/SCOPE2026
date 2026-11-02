---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For P_alpha=(1-alpha)I+alpha S with clockwise three-cycle, its nonconstant Fourier eigenvalue is lambda=1-3alpha/2+i sqrt(3)alpha/2. For 0<alpha<1, |lambda|<1, giving rho_k=Re(lambda^k), rho1=1-3alpha/2, rho2=1-3alpha+3alpha²/2, tau=(1-alpha)/alpha. The reversible floor minus tau is (4-6alpha+3alpha²)/(6alpha(2-alpha))>0 because discriminant -12 and denominator positive. Independent exact rational 3x3 autocorrelation matrix checks at alpha=1/4,1/2,3/4,9/10 match formulas. Irreducible, aperiodic, nonreversible. No claim to universal nonreversible classification.

## originality

PASS

Published sharp reversible two-lag variance-floor theorem provides exactly the targeted bound but assumes real reversible spectral measure. It expressly disclaims applicability to nonreversible chains and does not exhibit the all-alpha clockwise three-cycle strict gap. Known asymmetric-cycle nonreversible variance studies were searched and partially inspected; a direct equivalent witness may exist elsewhere. The elementary three-state calculation is not presented as a general variance theorem.

## value

PASS

This is a motivated failure witness for a sharp practically interpretable two-autocorrelation asymptotic-variance floor: reversibility is not a removable technical assumption. It gives a nondegenerate irreducible/aperiodic continuum of strict violations with closed gap rather than a numerical or pathological isolated counterexample, limiting naive nonreversible reuse of spectral-moment estimators. Its calculation is elementary and its usefulness is this explicit boundary, not complexity of proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
