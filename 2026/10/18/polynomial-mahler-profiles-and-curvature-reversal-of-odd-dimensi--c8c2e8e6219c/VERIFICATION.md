---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Axial cylinder+caps yield vol(C)=kappa_d+2a kappa_(d-1); support h=||u||+a|u1| gives polar cross sections (1-az)^2-z^2 for z∈[0,(1+a)^-1]. For d-1=2m, integrate the mth power after z=(1-b)s, yielding β_m(1+(β_m-1)b)int_0^1(1-s)^m(1+(1-2b)s)^m ds and beta-polynomial. Differentiate exactly at b=0 and b=1. β_m=(2m+1)binom(2m,m)/4^m, and recurrence β_(m+1)/β_m=(2m+3)/(2m+2) yields β_m²>m+1 and β_m<2m-1 for m>=2, hence endpoint curvature signs and at least one inflection. Sympy rebuilt polynomial independently for m=1..10, confirmed deg m+1, R(0)=1, R'(0)=0, R''(0), R''(1), R(1), and mixed signs. All-m proof is analytic, finite checks corroborate only.

## originality

PASS

Campi–Gronchi 2006 full OA 10-page article states reciprocal polar-volume convexity in shadow systems (Theorem1, Section2), no evaluated axial-capsule polynomial or b-parametric curvature profile in the inspected sections. Meyer–Reisner 2006 extends shadow-system convexity; its abstract is accessible but complete paper not accessible after arXiv, alternative OA and Oxford VPN attempts, a priority risk. Blaschke–Santaló maximum at the ball is not a dimension-dependent second derivative. Resultary Mahler query returned no matching capsule curvature theorem among inspected hits.

## value

PASS

Mahler volume product is a canonical affine-invariant convex-geometric quantity on an elementary, ubiquitous parallel-body family. Odd-dimensional polynomiality and the sharp dimension threshold where the natural relative-length curvature reverses identify a nontrivial boundary between 3D concavity and higher-dimensional inflection; no unmotivated slice or unneeded downstream theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
