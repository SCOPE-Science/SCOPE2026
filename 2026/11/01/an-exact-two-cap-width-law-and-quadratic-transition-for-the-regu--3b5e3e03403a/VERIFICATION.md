---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Exact 24 vertices V=±e_i and 16 half-sign vectors are unit and antipodal. Pair Gram multiset from independent exact-rational enumeration: inner products -1:12, -1/2:96, 0:72, +1/2:96. For s>=sqrt(2/3), two caps can intersect only if v.z=1/2 (since 2s<=sqrt(2+2 v.z)); three such caps cannot overlap in positive surface measure since 3s<=sqrt(6), equality only lower endpoint. Hence measure inclusion-exclusion exactly 24 single caps minus 96 adjacent double caps. Haar marginal density on S^3 is 2 sqrt(1-t^2)/pi and an orthonormal coordinate pair is uniform on the unit disk, giving P and elementary disk-segment Q. Independent exact Gram enumeration and numerical value at s=sqrt(2/3) 0.9363568184518474 confirm normalization. Expanding y(s)=2 delta+O(delta²) and Q(s0-delta)=4 delta²/(pi sqrt3)+O(delta³) at s0=sqrt3/2 yields the claimed coefficient. The simulation code was inspected but not used to prove the continuum identity.

## originality

PASS

Best-of-knowledge original as a *specific 24-cell Haar one-dimensional width upper CDF and 96-pair transition coefficient*. Distinguish the classical one/two spherical-cap integration method from the new incidence-specific result. Novaga–Song identifies the same 24-cell but its Theorem 1.1 and Lemma 2.3 concern parallelohedral isoperimetry and vertex geometry, not width probabilities. A full published 24-cell Resultary result concerns 3D brightness extrema, not 1D random-width law; cube-width Resultary result has different vertex-incidence matrix. Abas abstract refers to 3D polyhedra and unavailable full text is retained as residual priority risk.

## value

PASS

The regular 24-cell is a canonical four-dimensional regular parallelohedron; its Haar directional width is a natural integral-geometric invariant. The formula resolves the law on ~93.6% of all directions and identifies the first non-smooth overlap phase boundary with coefficient encoding the polytope’s 96 edges. This is a mathematically motivated exact partial distribution, not just a numeric check or recycled facet volume.

The dated certificate retains the supplied scientific assessment, sources and limitations.
