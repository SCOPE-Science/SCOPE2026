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

Read actual KIT full-paper equations (3.16), (4.1), their coefficients Gamma and Lemma 4.1 small-tau conditions; the scalar reduction uses mass 1/6 and stiffness 4, normalized eigenvalue 24, alpha=1/12,beta=1/72. The second iterate factorizes as -(x^3+x-a)(x^2-a*x+1)/((1+x^2)^2+a^2), verified independently with SymPy. This gives global half-line convergence for a<=2 and exactly one attracting primitive 2-cycle for a>2, with p q=1, p+q=a and 4/a^2 derivative product. Not a challenge to a theorem that requires small enough tau.

## originality

PASS

Elementary one-dimensional rational decreasing-map period doubling is known; the evaluated contribution is the concrete actual conforming Kirchhoff Picard solver specialization with an exact forcing boundary and unbounded spurious phase. Source authors prove convergence for sufficiently small tau, not unconditional tau=1 convergence.

## value

PASS

The one-degree-of-freedom conforming FE instance is a motivated minimal counterexample warning that uniqueness of an implicit wave stage does not guarantee undamped Picard convergence. The exact forcing bifurcation and unbounded solver residual are useful numerical-analysis boundaries, not an arbitrary substitution of a rational map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
