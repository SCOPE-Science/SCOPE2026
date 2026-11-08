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

The graph KG(7,3) has 35 vertices indexed by triples of seven points and disjointness edges; Ind(KG(7,3)) simplices are intersecting triple-families. For each of 15 S7 cycle types, an invariant simplex is exactly a union of permutation cycles of triples that are internally and mutually intersecting. Signed oriented simplex traces simplify to -sum_{independent orbit subsets}(-1)^number_orbits; an independently reconstructed exact recursion reproduces all 15 Lefschetz values (22,6,-5,2,4,3,-3,2,0,4,2,-1,1,1,1). The inspected source CHECKS implements Murnaghan–Nakayama for all Specht characters; the virtual representation has +1 each for (7),(4,3),(2,2,2,1), and -1 each for (1^7),(2,1^5), zero otherwise. Feng 2026 supplies independently published rational Betti ranks H6=29, H9=7 and vanishing elsewhere. The -1 terms must be in H9 and dimensions 1+6 exhaust it, forcing H6 to be the positive three Specht summands of dimensions 1+14+14. No unproved integral or higher-parameter claim is inferred.

## originality

PASS

Feng arXiv:2610.17394v1 supplies broad triple-Kneser Betti numbers but no natural S7 character, and Feng–Wang arXiv:2404.10566 full inspected HTML discusses cycles, generators and dimensions rather than graded Specht modules. KG(3,1) in Feng parameterization is this same seven-point KG(7,3), so exact-object normalization is not overlooked. Stable Kneser and Kneser neighborhood-complex symmetry results use distinct graphs or simplicial constructions. No direct dominating equivariant theorem was located; unindexed implicit calculation remains a risk.

## value

PASS

The first mixed-degree seven-point triple-Kneser independence complex is a natural symmetric-group object. Its full graded Specht decomposition, not deducible from the recently computed nonequivariant Betti dimensions, is a complete and potentially reusable representation-theoretic invariant that identifies the invariant line and sign-twisted top degree. It is a motivated exact finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
