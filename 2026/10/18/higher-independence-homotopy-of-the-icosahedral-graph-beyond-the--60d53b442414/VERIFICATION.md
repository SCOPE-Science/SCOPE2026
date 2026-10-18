---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Execute `python3 verify_higher_icosahedral.py` with Python 3.9 or newer; no third-party packages are required. The program constructs the twelve-vertex graph, verifies thirty edges and twenty triangles, and exhaustively enumerates 4,096 induced vertex subsets with two component algorithms and the connected-forbidden-subset characterization. The four intermediate-stage complete acyclic matchings have 351, 531, 673 and 1,035 pairs, respectively, and only the critical zero-cell plus 10 dimension-three, 70 dimension-three, 350 dimension-four, and 450 dimension-five cells. Every oriented Hasse incidence is included in the directed-cycle test.

Independent exact mod-two reductions of the full simplicial boundary matrices yield the rank vectors recorded in RESULT.md. The proof of **integral homotopy** is not an inference from mod-two ranks: it follows from the verified acyclic matchings with no nonzero-dimensional attaching-map targets. The script also checks all induced vertex complements after deletions of at most four vertices and the exact high-threshold skeleton identity for every stage seven through eleven, plus contractibility at twelve. The final success marker is `ICOSAHEDRAL_HIGHER_INDEPENDENCE_STAGES_VERIFIED`.

Limitations: no claim is made about inclusion-induced homology maps, equivariant actions, or infinite graph families. No independent mathematical audit has yet occurred.
