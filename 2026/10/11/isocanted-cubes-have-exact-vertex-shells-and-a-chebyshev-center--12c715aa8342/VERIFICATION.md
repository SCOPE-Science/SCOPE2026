---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For d≥2, ℓ>0, 0<a<ℓ the precise Euclidean body is |x_i|≤ℓ/2, |x_i−x_j|≤ℓ−a. Every nonempty W⊆[d] contributes an extreme vertex with coordinates ℓ/2 on W and a−ℓ/2 outside, plus its antipode, as confirmed from the original 2020 vertex classification and 2024 centered inequalities. Squared norms depend only on k=|W|, and consecutive differences equal a(ℓ−a)>0; hence d shells and 2 binomial multiplicities, with only ±ℓ/2 * 1 at outermost radius ℓ√d/2. Opposite poles give the sharp and unique Euclidean minimal enclosing sphere. Every center z of an inscribed Euclidean ball of radius ρ satisfies |z_i|+ρ≤ℓ/2, |z_i−z_j|+√2ρ≤ℓ−a. These constraints are necessary and sufficient for all facets. At z=0 the minimum clearance gives exact radius; at the coordinate-controlled regime all z_i=0, while in difference-controlled regime all z_i are equal and coordinate facets bound a diagonal segment. This proves the sharp transition including equality case. Independently enumerated exact rational vertex-shell counts in d=2..6 and checked symbolic formulas; source checker inspects d≤8. The proof, not the finite enumerations, covers all d.

## originality

PASS

The 2020 full primary text supplies the complete labeled vertex combinatorics, and 2024 full primary text gives the halfspace/zonotope description and volumes. A later published related Resultary finding DOES explicitly give the unique Euclidean minimum enclosing sphere and its pole contacts, so that particular subclaim is already covered and not new. However it treats John and Löwner ellipsoids, not the complete Euclidean incenter phase diagram or d strict vertex shell multiplicities. The surviving complete Euclidean inball center classification is neither a volume identity nor an ellipsoid contact theorem.

## value

PASS

The complete incenter locus and its sharp one-point-to-segment phase transition are intrinsic Euclidean geometric data of a natural all-dimensional class of zonotopes. They explain when metric optimality loses uniqueness; exact strict vertex shell multiplicities also record radial stratification useful for studying contact and non-isotropic approximations. The outer sphere subclaim is known, but does not remove mathematical value of the distinct complete center classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
