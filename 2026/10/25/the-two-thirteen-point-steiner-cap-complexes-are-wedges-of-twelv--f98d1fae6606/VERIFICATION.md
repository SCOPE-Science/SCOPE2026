---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. Independently reconstructed the 26 translated blocks and the four-Pasch switch, confirmed both designs have all 78 unordered pairs exactly once and 13 vs 8 Pasch configurations. Exhausted every one of 2^13 subsets under the block-avoidance condition, giving f-vectors (13,78,260,455,312,39) and (13,78,260,455,312,34). With the specified vertex orders, independently rebuilt 568/565 toggle pairs, checked acyclicity of all 4,550/4,520 Hasse arrows, leaving one critical vertex, 4 critical 3-cells and 16 critical 4-cells for C, versus one vertex, 2 critical 3-cells and 19 critical 4-cells for N. Recomputed signed integer Morse differential via gradient substitution, verifying determinants +1 for 4x4 and 2x2 minors; these give split surjections and reduced H4 free rank 12/17. The resulting CW spaces are 3-connected and homological Whitehead/Hurewicz yields the two sphere wedges. Nonidentity translations have no nonempty invariant face, giving reduced Lefschetz -1 and the rational augmentation character. The Pasch relation is expressly only for these two systems, not a general law.

## originality

PASS

PASS best of knowledge. Forbes–Grannell–Griggs counts the same block-avoiding independent sets, and Grannell et al. already classify the two STS13 designs; neither gives their integral homotopy. Nofil studies the exact legal-subset family as a game but nim-values have no implication for Morse attaching maps or H4 characters. Prior design incidence neighborhood results use different vertex and face conditions, and projective-plane cap complexes forbid different triples. Targeted Resultary queries and primary text comparisons found no pre-existing integral 12/17 four-sphere classification or cyclic H4 character; unindexed work remains a residual risk.

## value

PASS

PASS. The two nonisomorphic STS(13)s are the complete first naturally nontrivial two-design classification at this order; their cap complexes are canonical independent-set complexes of the underlying 3-uniform hypergraphs. The exact change from 12 to 17 homotopy spheres under a Pasch trade and explicit cyclic representation are meaningful integral topological invariants, not mechanically implied by counts or game nim-values. A researcher studying cap complexes, trades, or Steiner independence topology can use the exact pairwise classification without a broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
