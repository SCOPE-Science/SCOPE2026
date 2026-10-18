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

# Verification and boundaries

The source `verify_pathdigraph.py` uses Python 3's standard library. Execute `python3 verify_pathdigraph.py` from the extracted package directory. It reconstructs every arc from the strict face-deletion definition for all integers \(3\le n\le11\), checks that each oriented three-clique has the claimed common-pair form, that no four-cliques occur, and that the edge set agrees with an independent complete-tripartite-block reconstruction. It tests graph connectedness, the three face counts, the exact mod-two two-boundary rank, both Betti numbers and the weighted all-block two-sphere sum.

The finite computation is a cross-check only; its output does not certify the universal theorem. Integral torsion-freeness, homotopy type and all \(n\ge3\) follow from the explicit mathematical proof in RESULT.md, specifically the decomposition into joins of discrete sets and the point-gluing lemma. No chain-level enumeration is claimed beyond \(n=11\). This verification does not assess arbitrary digraphs, path order above two, or the relaxed incidence condition.
