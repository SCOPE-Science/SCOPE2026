---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For r,c in F_(3^n)^×, the transformed sextic has branch equation (t³−t)²=−1/r. The additive map t↦t³−t has image trace-zero, so rational β gives two split cubics (trace zero) or two irreducible cubics (trace nonzero). Nonsquare β gives Frobenius conjugation ±β and trace zero over the quadratic extension, hence 2³ cycles. Frobenius-fixed unordered Weierstrass pairs give rational 2-torsion orders 16,4,1. Pairs ±β parametrize (q−3)/6, nonsquares (q−1)/2, and remainder q/3. Sextic derivative vanishes only at 0,±1, where sextic is nonzero, establishing smooth genus two. Boundary q=3 has empty fully split class. Finite-field source checker uses polynomial gcd of f with T^(q^d)−T in q=3,9,27,81; uniform proof is algebraic, not 116 tests.

## originality

PASS

The primary 2024 D6 study supplies the characteristic-three model and complete-splitting criterion, and standard Artin–Schreier and genus-two 2-torsion facts supply the method. The exact complete three-way Frobenius frequency plus rational 2-torsion parameter census is a meaningful non-identical strengthening; no dominating published statement identified in the actual targeted search. Best-of-knowledge PASS only; historical classification in specialized literature could contain the same corollary.

## value

PASS

A complete arithmetic trichotomy for literal parameters is a natural invariant of the prominent wild D6 genus-two family: precise field-of-definition of all six branch points and fixed rational 2-torsion rank affect arithmetic of the Jacobian. The exact parameter frequencies and exclusion of six-cycles close the classification, not a gratuitous finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
