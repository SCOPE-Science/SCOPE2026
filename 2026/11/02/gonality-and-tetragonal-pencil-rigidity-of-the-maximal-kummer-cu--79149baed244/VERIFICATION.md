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

Kummer valuation 1 at each x=+/-sqrt(-1) proves extension degree m=q+1; tame Riemann-Hurwitz gives genus m-1-gcd(m,4)/2. The rational quadratic conic z^2=x^2+1 with z=y^((q+1)/2)/x is parametrized by t=x+z; independently checked the substitution y^d=(t^4-1)/(4t^2) as exact rational identity. Four deck symmetries over k(y) ensure degree four; three quadratic subfields have genera (m-2)/2 and floor((d-1)/2) twice, at least two for q>=9. Castelnuovo-Severi excludes degree 2/3 maps when g is sufficiently large; at q=7 a unique degree-three pencil would force faithful C2 x C8 in PGL2 characteristic seven, impossible by semisimple order-eight centralizer. For q>=13 genus>9 and the subfield/genus-two uniqueness argument forces every quartic pencil equal k(y). Explicit genus inequalities checked on 12 candidate odd prime powers; the all-prime-power result rests on field-theoretic argument.

## originality

PASS

Best-of-knowledge originality for the narrowly specified final mathematical claim, after separate checks of aliases, broader implication, exact tables and prior theorem implications. Prior source overlap and limitations are credited; this is not a certification of priority.

## value

PASS

Uniform sharp gonality together with the exceptional q=7 double-pencil phenomenon and high-genus uniqueness is a natural global classification of low-degree maps on an arithmetically distinguished Kummer-curve family. This is not a restatement of the classical genus or automorphism calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
