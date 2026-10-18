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

For r>=4 the only nonfull resolving neighborhoods are the four-vertex sets from comparing a_i,a_j or b_i,b_j and the x,b_i / y,a_i cross-families; distances confirm kappa=4. Each pair of page sums p_i+p_j>=k; adding all yields total page weight>=rk/2. Uniform internal weight k/4 and zero on spine is feasible. At optimality every pair inequality is tight and g(x)=g(y)=0, forcing p_i=k/2; the only remaining nonautomatic constraints are the two cross inequalities in the claim. For r=4 they collapse to equality forcing alpha_i=beta_i=k/4. For k=4 the page sum=2 forces all internals weight one, and for r>=6, k<=2 two page classes of size at least three give explicit asymmetric optima.

## originality

PASS

Kang–Yero–Yi establishes the general fractional k resolving definitions, lower bound and proportionality criteria; Feng–Lv–Wang supplies Cartesian-product bounds, which with uniform witnesses account for the scalar r*k/2. The claimed new contribution is the COMPLETE optimizer polytope and uniqueness/nonuniqueness classifications for square-page book graphs B_r=K_{1,r} square K_2. The closest full primary paper covers bouquets of cycles sharing one vertex, not books sharing an edge; no equivalent all-minimizer theorem was found.

## value

PASS

A linear program optimum alone does not describe all equality cases. The explicit necessary-and-sufficient page-weight inequalities classify the geometry of every minimum resolving function at every real k in [1,4], identify a unique four-page exception and exhibit genuinely asymmetric optimizers in large books. These are natural data for robust sensor-placement designs and a complete family classification, not arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
