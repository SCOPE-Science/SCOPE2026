---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

On the coordinate torus multiply by the invertible monomial and invert x to obtain Q(y)=sum_i c_i y_i y_(i+1). Its Hessian is a weighted symmetric cycle. For odd n the determinant is 2 product c_i; for n=2m the parity-ordered cyclic bidiagonal block B has det B=product_odd c + (-1)^(m-1) product_even c. Positive weights imply det B=0 exactly when 4|n and the alternating products balance. A nonzero (m-1)-minor makes corank H exactly 2. The two parity-supported nullvectors have no zero supported entries, so projectivized kernel intersects the torus as P1 minus its two endpoints, reduced; local linear diagonalization of the quadratic form yields transverse rank n-2 throughout. Independently verified exact Hessian ranks for lengths 5,6,8,10,12 and weighted balanced/unbalanced eight-cycles. This concerns the torus only, not boundary strata.

## originality

PASS

Telen 2026 Theorem 7.11 derives the nonexceptional exclusion criterion and Example 7.12 displays one balanced octagon line; its matrix M argument contains the necessary parity-product obstruction. The reviewed contribution gives the converse for every balanced positive cyclic weight, the exact reduced scheme on the projective torus, and uniform transverse analytic normal form of rank n-2. Those conclusions were not stated as a full classification in the inspected primary article; the stronger source still materially constrains novelty.

## value

PASS

This is a natural all-polygon, scheme-theoretic local singularity classification, with an exact parameter-dependent degeneracy boundary, reducedness, and constant transverse analytic type. Local analytic type and multiplicity matter to singularity theory and are not merely a finite example or a combinatorial restatement of an exclusion theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
