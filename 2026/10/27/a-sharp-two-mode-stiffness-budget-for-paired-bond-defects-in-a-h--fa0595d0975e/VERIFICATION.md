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
# Verification of the paired stiff-spring theorem

The mathematical verification is the self-contained proof in `RESULT.md`. The free-chain resolvent kernel is evaluated explicitly, the two defect gradients yield the exact Birman--Schwinger matrix, and the monotone eigenvalue crossings give an infinite-chain proof of the sharp mode count. The fixed-budget extremizer follows by monotonicity in the product of two positive excess stiffnesses, and the band-edge coefficient follows by an analytic expansion of a finite polynomial.

Running `python3 checker.py` requires only Python 3's standard library and prints `PASS: 56 numerical comparisons (finite Jacobi/Sturm, edge law, allocation).` The checker constructs finite spring-matrix eigenvalues using a Sturm-pivot bisection independently of the infinite-chain resolvent and compares representative parameter choices. It separately checks small-detuning ratios and unique allocation inequalities. These finite checks do not establish infinite-dimensional completeness, originality, or experimental applicability.

The proof excludes the borderline case from the square-summable count. The result assumes exact positive spring strengths and no damping. Historical material that was not available as full text remains a scientific-priority uncertainty.
