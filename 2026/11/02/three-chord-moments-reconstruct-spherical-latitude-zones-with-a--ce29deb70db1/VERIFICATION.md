---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Uniform area on a spherical latitude zone gives height Z uniform on [a,b], mean m and second height moment q=m²+h²/3. For independent points X,Y, contraction of first, second and third coordinate moment tensors yields μ1=m², μ2=1/2−q+3q²/2, μ3=m²(20m⁴−60m²q+12m²+45q²−18q+3)/2. Since L²=2(1−X·Y), these equal the first three even chord moments by an invertible triangular map. μ2 determines q up to reflection q↔2/3−q; both distinct roots feasible iff 1/2<m<1/√3, and μ3 difference −4m²(5m²−1)(3q−1) is nonzero for two distinct feasible roots. Thus first three identify (m,h), with reflected axis the only isometry ambiguity. An exact pair m=11/20, h=√17/20 versus √57/20 has equal E[L²]=279/200 and E[L⁴]=583/200 but differing E[L⁶]=5523679/800000 and 5722119/800000. Independently recomputed these fractions and fold difference in SymPy.

## originality

PASS

Moseeva–Tarasov–Zaporozhets random sections/spherical cap distance distributions concern geodesically convex regions and full distance distributions, not the exact first-three-moment reconstruction of generally nonconvex two-boundary latitude zones. Mémoli–Needham provide general metric-measure distance distribution inverse context, not the sharp two-moment fold of this two-parameter family. Basic tensor contractions are acknowledged prior tools; exact threshold is assessed new on read evidence.

## value

PASS

Sharp finite-moment identifiability and a constructive two-moment failure for canonical spherical zones is a motivated inverse-geometric statistic; the exact boundary 1/2<m<1/√3 and third-moment obstruction distinguish geometry not captured by lower moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
