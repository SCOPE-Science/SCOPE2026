---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The irredundant facet normals are u_i=e_i, v_i=-e_i-e_(i+1), w=-sum e_i. At vertex p_S (independent, |S|=k), active u-rays for i not in S and 2k active edge v-rays, plus w iff k=m. The n rays {u_i:i not in S} ∪ {v_s:s in S} are unimodular (triangular minor ±1), so Cl(local) is free of rank k+1_(k=m). The integral character h=(-1 outside S,2 on S) pairs -1 with active u,v, and pairs 1-m with w at k=m, hence K=(m-2)[D_odd] primitive and zero when k<m. For face F_0, the m+1 maximal independent sets avoiding 0 have successive indicator differences e_(2r+1)-e_(2r+2), yielding a unimodular m-simplex and Z_0≅P^m linearly. Its generic normal cone has rays u0, the m alternate v-rays and w=sum(v)-u0, giving free local Cl rank one and K coefficient m-2, non-Q-Cartier. Miyazaki Thm 3.4 supplies known non-Gorenstein support; the generic non-Q-Cartier loci force equality. Face monomial ideals yield scheme-theoretic pair intersection corresponding to F_i∩F_j, a simplex with q or m-q+1 retained vertices. Independently enumerated all 29 independent sets of C7 and face intersections counts [1,3,2,2,3,1], agreeing with formulas. Source finite verification read, not used as proof in unbounded m.

## originality

PASS

Miyazaki 2022 already gives the set-theoretic non-Gorenstein locus of the affine Ehrhart ring, and toric local-divisor sequences are standard; no priority claim is made for either. The added scheme intersections, exact local class groups and primitive non-Q-Gorenstein discrepancy, linear P^m components and fixed-point rank spectrum are not the support theorem and are not stated in the inspected primary text.

## value

PASS

Refines the singular-locus picture from a union of abstract orbit closures to explicit projective geometry, pairwise intersection incidence and local canonical-class obstructions. These local invariants measure precisely why the components fail Q-Gorenstein and can be used in toric birational/singularity calculations; it is a motivated natural complete classification, not an arbitrary fixed small cycle table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
