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

Encode Petersen vertices by disjoint 2-subsets of five symbols and Petersen edges by unused symbol plus pairing of the other four. Independent reconstruction of the 15-vertex line graph gives among 105 unordered vertex pairs exactly 30 distance 1, 60 distance 2, and 15 distance 3; distance-three edges form exactly five disjoint 3-vertex fiber cliques. Hence the threshold-two complex is a join of five three-point discrete sets, whose reduced integral homology is Z^32 in degree four (and wedge of 32 S4). The scale-one triangle-star cover has nerve Petersen, H1=Z^6. At threshold three the full simplex occurs. S5 permutes fiber factors with the Koszul sign; the tensor trace on each permutation cycle gives degree-four class values (32,0,8,2,0,0,2), degree-one from signed Petersen cellular chains (6,0,-2,0,0,0,1). The complete package verifier's source enumerates all 120 permutations, signed Lefschetz traces and rational Specht multiplicities; the group-theoretic trace formulas and join proof independently support those results. Integral torsion-free homology does not justify integral splitting into rational irreducibles.

## originality

PASS

The nonequivariant X2 join/wedge follows from standard antipodal partition data and is not new. The complete seven-conjugacy-class S5 character at both persistent stages and the two invariant degree-four lines are the relevant additional invariants.

## value

PASS

The Petersen line graph is a canonical diameter-three antipodal object. Full rational S5 barcode, irreducible identification, and invariant subspace dimensions make the symmetry topology explicit, distinguishing an ordinary wedge-count computation from representation-aware persistent homology. This is a meaningful natural complete classification for the graph, with exact finite scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
