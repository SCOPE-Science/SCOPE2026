---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

On coordinate torus set u=X^m,v=Y^m,w=Z^m; p does not divide m so cover is etale. Differences of partials force u=v=w; common-zero criterion 1+3lambda=0. Side restriction is quadratic lambda(v+w)^2+vw; multiple roots exist only in odd characteristic at 1+4lambda=0. At vertices the equation equals lambda, giving ordinary m-fold points only at lambda=0. Fresh symbolic checks verified Heron four-factor identity at -1/4 and omega-linear two-factor identity at -1/3; distinct factors/smoothness and intersection multiplicities follow from p∤m and etale cover. Cremona birationally normalizes integral lambda0 fiber to a smooth Fermat curve. Plane adjunction gives remaining genera. Fq rational points follow from mth roots of unity and quadratic-sign image in Fq*. Small finite field package checker inspected but universality follows from this stratified algebraic proof, not a sample.

## originality

PASS

Originating Borges–Korchmáros–Speziali 2022 primary preprint introduces this exact pencil and makes a blanket nonsingularity remark; explicit algebraic factorizations reveal singular/reducible special fibers and characteristic-dependent decomposition. The later journal version was not fully accessed; best-of-knowledge original for exact exceptional classification, with material revision-overlap risk.

## value

PASS

The complete exceptional discriminant, branch types, component degrees, geometric genera, and finite-field arithmetic splitting correct a misleading source-level smoothness description and are needed for geometry, singularities, and arithmetic of this natural triangle-invariant pencil.

The dated certificate retains the supplied scientific assessment, sources and limitations.
