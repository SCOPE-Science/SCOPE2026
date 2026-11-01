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

The group presentation G=V ⋊ C2 with odd p forces every nonzero-on-s endomorphism to be (A,u), while sending s to the identity forces A=0. Composition (A,u)(B,v)=(AB,u+Av), so idempotence is exactly A²=A and Au=0. Counting complements of image and kernel gives N_r=[d choose r]_p p^{(r+1)(d-r)}. Translating affine fixed points reduces a commutant to block-diagonal projections, giving P_{d-r}Q_r with the vertex itself removed and the trivial homomorphism inserted. A finite commuting family has a common fixed point (product of commuting affine idempotents), and its linearized projections simultaneously diagonalize; maximal Boolean cliques and their unique common point/coordinate lines follow. This proves all odd primes p and integers d>=2. Independently enumerated p=3,d=2: 47 graph vertices; rank counts 9,36,1; degrees 14,8,46; 54 maximal cliques of order 5. The finite check is corroboration, not the all-d proof.

## originality

PASS

The rank-one ordinary dihedral endomorphism retractions are known (Arvasi–Odabaş–Wensley), and simultaneous diagonalization is classical. Their treatment of d=1 and small-group cat2 tables does not imply the rank-stratified affine-projection commutation graph for all d>=2, its exact degree census, or all maximal compatible systems. Element-commuting and subgroup-commuting graphs have different vertex sets. The inspected literature did not supply equivalent d>=2 formulas, subject to unindexed affine idempotent semigroup work.

## value

PASS

A uniform full commuting graph for a natural infinite family of nonabelian groups, including all rank multiplicities, local degrees, maximal cliques, clique count and symmetry orbits, is a motivated structural classification beyond routine matrix projection counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
