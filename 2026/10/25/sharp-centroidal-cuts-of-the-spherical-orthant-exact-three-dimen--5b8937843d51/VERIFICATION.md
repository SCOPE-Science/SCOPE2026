---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

By half-normal Gaussian direction representation the spherical centroid is proportional to (1,...,1). In d=3 all normals perpendicular to centroid reduce by permutations and sign reversal to (a,1-a,-1), a in [0,1], with boundary zero normal giving 1/2. The complementary spherical triangle has rays (0,0,1),(1,0,a),(0,1,1-a), and solid-angle formula yields P=1-(4/pi)atan[(sqrt(1+a²)-a)(sqrt(1+(1-a)²)-(1-a))]. Independently the spherical-coordinate integral is (2/pi)∫q/sqrt(1+q²), whose second derivative is strictly negative; symmetry gives unique maximum at a=1/2 and exact minimum by normal reversal. For all d, H_d≤mean(H1..H_{d-1}) gives E erf(mean/√2), strictly rising by leave-one-out sample means and strict Jensen concavity, converging by SLLN. Independent quadrature agreed at six parameters; exact minimum 0.46455905439754 and canonical limit erf(1/√pi). The d>=4 assertion is confined to specified normals.

## originality

PASS

Materially inspected spherical Grünbaum and spherical Winternitz results give body-uniform inequalities and reductions, not the exact all-right spherical triangle normal profile or strict dimension-family cut asymptotic. Best-knowledge sharp model-case contribution; the solid-angle and Jensen methods themselves are prior art.

## value

PASS

A complete sharp directional classification for the canonical spherical orthant strengthens the broad Grünbaum benchmark in a natural fixed-body case and identifies all normal orbits. The independent strict dimension-monotonic cut law and limiting constant supply a meaningful geometric comparison without overstating higher-dimensional global optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
