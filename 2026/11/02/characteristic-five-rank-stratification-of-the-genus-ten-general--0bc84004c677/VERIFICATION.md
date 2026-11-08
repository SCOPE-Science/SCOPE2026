---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: For lambda not 0,1 the two cubic Jacobian gradients are independent, and adjunction for smooth (3,3) in P3 gives genus 10. Koszul H1(C,O)=H3(P3,O(-6)) has ten positive inverse-monomial classes summing to 6. Direct independent F5[lambda] polynomial expansion of (F1 F2)^4 and coefficient rule [X^(5a-b)] yields exactly six nonzero Hasse–Witt entries arranged into paired 2x2 Frobenius blocks at (1,8),(3,7),(4,6); each block either invertible or wholly zero, at exactly lambda=-1,2,3 respectively. Semilinear stable rank is 6 generic/4 special, and Cartier kernel dimension a=10-rank=4/6. Direct independent exact polynomial arithmetic and F5 rank tests at lambda 2,3,4 reproduced the entries and exceptional ranks; all algebraically closed parameters follow from factored polynomials, not finite tests.

## originality

PASS

PASS at best knowledge: Carvacho–Hidalgo–Quispe identify the genus-ten curve and a characteristic-zero quotient-Jacobian decomposition. Hidalgo computes p=2 Cartier behavior on this model and states a p>=5 special formula requiring exponent k dividing p-1; k=3 does not divide 4 in characteristic 5. These prior statements supply the object and method but not the exceptional lambda=-1,2,3 p=5 rank locus. An unlocated elliptic-factor supersingularity calculation could imply the result and remains a priority risk.

## value

PASS

PASS: Complete 5-rank and a-number stratification for a geometrically natural one-parameter family of genus-ten curves, with precise jump orbit and zero additional loci; intrinsically useful arithmetic geometry even without full Newton polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
