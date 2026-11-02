---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For two ordered points on an equal-length m>=3 arm star, the simultaneous outward radial scaling (u,v)→c_t(u,v) with denominator (1-t)+t*max(u,v) continuously increases all distances and preserves the clearance a>0; on the max-radius-one locus, shrinking an inner same-arm point to the center is also distance-nondecreasing and equivariant. For 0<a<=1 this is a Γ=S_m×C2 strong deformation onto the connected crown graph K_m,m minus its diagonal edges. Its signed cellular incidence e_ij↦B_j−A_i gives a free integral H1 of rank m(m−1)−2m+1=m²−3m+1; arm permutations relabel and particle swap reverses oriented e_ij to −e_ji. For 1<a<=2 all allowed ordered distinct-arm pairs form contractible radial triangles, deforming to m(m−1) isolated tip pairs; a>2 empty. Inclusions within regimes preserve the retraction models and crossing the threshold maps H0 by augmentation. The C1/C0 exact sequence yields χ(σ,0)=f²−3f+1 and χ(σ,1)=1−2t2; independent exact chain-level counts check 1,740 actions on m=3..6. Standard S_m modules on oriented/unoriented pair sets yield the even exterior-square standard module S^(m−2,1,1) and the odd kernel S^(m−2,2) (vanishes m=3). These arguments are uniform in m and positive real a; the finite group tests are corroboration.

## originality

PASS

Prior 2026 Li–Özaydın gives a weighted bipartite graph deformation for arbitrary star arm lengths and nonequivariant field persistent homology; Wawrykow gives homology/stability of ordered star configurations. The present claim adds an integral boundary lattice preserving both full arm permutation and particle swap, character formulas, rational Specht decomposition with exchange parity, and maps at the exact clearance threshold. General-model constructions could be specialized to recover this action, so claim of priority is qualified.

## value

PASS

When all arms have equal length, a large geometric S_m symmetry arises. Nonequivariant rank/barcode loses which cycles reverse under particle exchange and which irreducible arm modules persist. This complete equivariant integral boundary lattice and one-cutoff persistence for a canonical robotic/graph configuration family gives motivated structural information at all m, not an isolated finite trace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
