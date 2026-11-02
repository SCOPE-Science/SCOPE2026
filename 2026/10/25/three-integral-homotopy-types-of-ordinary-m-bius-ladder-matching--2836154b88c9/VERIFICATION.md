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

PASS. Precisely for the ordinary matching complexes of M12,M14,M16 (not perfect-matchings or all n), independently reconstructed each edge set (18,21,24 edges), every matching face, complete finite face-count vectors and mod2 homology using a separately written face enumerator. A second independent signed discrete-Morse implementation built the deterministic staged face matching and full Hasse orientation; verified 3990/15036/55256 covering relations and acyclicity, respectively, with 540/1756/5672 nonempty pairs and critical counts n6 {0:1,2:2,3:15,4:3}, n7 {0:1,3:8,4:24}, n8 {0:1,3:2,4:23,5:23}. Its signed gradient-path differential was recomputed and Smith-normal-formed over Z: n6 ∂3=1^2,∂4=1^3; n7 ∂4=1^8; n8 ∂4=1^2,∂5=1^19, no nonunit factors. One 0-cell, no 1-cells and consecutive dimensional attaching degrees permit cellular cancellations and wedge homotopy, resulting in 10 S3, 16 S4, and 2 S4∨4 S5. Independent complete simplicial mod2 betti vectors agree. No infinite-family claim or unsupported extrapolation.

## originality

PASS

PASS best-of-knowledge: These are broad in n but concern distinct graph complexes or open planar families. They do not determine ordinary matching complexes at these exact three closed nonplanar cases. Searched ordinary matching under line-graph independence, twisted ladder, and Möbius ladder terminology. The distinct perfect-matching and independence results are not synonyms for the target.

## value

PASS

PASS. Ordinary matching complexes of Möbius ladders are a canonical, difficult symmetric-family topology problem distinct from the studied perfect-matching complexes. Three consecutive exact small orders include the first mixed-dimension feature at M16, and full integral homotopy types with certified attaching degrees are stronger than Betti counts. The finite size choices are a natural initial segment, not an arbitrary slice or mere recomputation of a known table. No periodicity or statement at larger n is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
