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

For m>=2,d>=3 and 1<=r<=m, essential variable count equals rank of first derivative catalecticant: annihilating directional derivatives are precisely the eliminated variable directions. A 1-PS with variable weights B^i (B>d) gives distinct monomial weights by base-B digits. Monomial fixed points of essential rank exactly s are degree-d monomials on exactly s active variables, counted C(m,s)C(d-1,s-1). C-star Euler localization and subtraction yield claimed cumulative and exact χ_c values; when r>d, the fixed point contribution is 0 but Fermat sums x_1^d+...+x_r^d prove nonempty strata. At r=m, Vandermonde identity recovers ambient binomial C(m+d-1,d). Independently counted compositions and supports for 30 degree/dimension pairs with 2<=m<=7, 3<=d<=7; the combinatorial counting proof covers all dimensions.

## originality

PASS

Landsberg–Weyman formalize multilinear tensor subspace varieties and resolutions; Landsberg–Ottaviani discuss symmetric flattenings and catalecticants. Neither primary text inspected states the Euler profile of the *single symmetric factor*, which depends on monomial support size rather than rectangular Tucker rank. A related published SCOPE finding on multilinear Tucker subspace rank has a constant Euler profile and does not imply the nonconstant symmetric support-count profile. The quadratic symmetric rank version is deliberately outside scope and independently treated as a different claim. Relevant independently inspected published SCOPE comparison: Independent-factor multilinear Tucker rank has all coordinate tensors of mode rank (1,...,1), causing constant Euler; symmetric-power monomials have support-dependent catalecticant rank. Hence no immediate specialization or domination.

## value

PASS

Essential-variable and catalecticant-rank filtrations are natural and ubiquitous in the geometry of homogeneous forms. Their complete support-weight Euler law, saturation at r=d and nonempty χ_c=0 high-essential-dimension strata reveal structure not captured by dimension or degree; all-parameter theorem is more meaningful than an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
