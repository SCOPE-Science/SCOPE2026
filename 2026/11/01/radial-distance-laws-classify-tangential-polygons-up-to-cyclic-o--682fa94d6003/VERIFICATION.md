---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed all seven steps of the pinned RESULT.md. For outward-normal angular gaps 2g_i (0<g_i<π/2, Σg_i=π), a side has tangent-coordinate interval [-r tan(g_{i-1}),r tan(g_i)] and perimeter 2rΣtan(g_i). This yields exact boundary hinge survival S(z)=Σ(tan g_i−z)_+/T, including repeated knots; slope jumps m_j/T and Σm_j g_j=π recover T, each integer multiplicity, and n. The uniform-area Jacobian on each O-to-side triangle is r s ds dℓ, giving radial factor √U and F(t)=area(P∩B_t)/area(P), F′(t)=2t/(r²T)Σ(g_i−acos(r/t))_+ for t>r. Recovering area from F(t)≈πt²/A, and r as the last exact-disk radius, makes interior-law inversion independent. All admissible cyclic gap lists are geometrically realized and Euclidean congruences act by dihedral permutations, giving (n−1)!/2 distinct generic realizations. Checked rational four-gap angles tan g=(1/2,1/3,2,3), Σg=π and T=35/6; there are three four-gap dihedral orbits. Source rational geometry verifier read and normalization/critical endpoints checked analytically; its finite logged tests are not used as proof of the universal statement.

## originality

PASS

Best-of-knowledge PASS for exact inverse distance-to-incenter distributions of all tangential convex polygons. The published Resultary width-classification theorem uses uniform-direction projection width only for centrally symmetric polygons; although it also recovers an unordered tangent-angle multiset and has dihedral fibers, it does not imply either distance distribution nor the general nonsymmetric four-side ambiguity. The Rabinowitz paper gives a cone-measure transfer used as background, not the hinge inversion; PDE and general tomography sources do not give the claimed two exact inverse laws.

## value

PASS

An exact two-way geometric-probability inverse classification for a natural nontrivial family; the distance observable loses cyclic adjacency while preserving every half-exterior angle and scale. The explicit hinge spline, inversion with unknown n and repeated parameters, and first generic nonuniqueness in n=4 are useful as a sharp tomography identifiability boundary, not just a routine area/perimeter identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
