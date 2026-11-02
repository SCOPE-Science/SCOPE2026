---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For one season, column substochasticity bounds spectral radius by max diagonal reproduction at d=0. In two seasons, the positive diagonal symmetrizer Q commutes with D_t and replaces C by symmetric B; A(d)=D2^{1/2}((1-d)I+dB)D1^{1/2} yields sqrt(rho(M(d)D2M(d)D1))=||A(d)||_2, and convexity gives endpoint dominance for all dimension and all positive D_t. For two patches with opposite environments, endpoint radii ab and c²a² switch at c=sqrt(b/a); strict inequality for interior d follows from unequal endpoint norms or the noncollinear singular-vector image at the tied endpoints. At three seasons, the exact swap example yields endpoint rho 4, interior rho 25/4. Independent exact symbolic monodromy calculations and symmetric stochastic 3x3 norm-convexity checks passed. This is asymptotic linear growth, not an ESS theorem.

## originality

PASS

The linear algebra norm convexity is elementary prior mathematics and the unconditional dispersal literature already investigates periodic environments, but the cited primary ecological study concerns evolutionarily stable migration strategies in a different, density-dependent model. The assessed finding is the precise arbitrary-patch two-season linear spectral-radius inequality plus shortest three-season interior counterexample. The original Schreiber–Li text was unavailable beyond its abstract in this run, so exact overlap cannot be excluded; this qualifies best-of-knowledge originality.

## value

PASS

The two-versus-three seasonal boundary is a natural structural answer to when an intermediate constant dispersal fraction can outperform both extremes. It holds for arbitrary habitat number and reversible mortality-bearing movement and supplies both a strict example and an exact cost threshold, not merely numerical parameter tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
