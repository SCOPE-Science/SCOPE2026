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

# Reproducibility

The included `verify_klein_cut.py` uses Python 3 and SymPy. Execute `python3 verify_klein_cut.py` from the extracted package. The expected terminal marker is `KLEIN_ORDINARY_THREE_CUT_INTEGRAL_DUAL_CHECKS_OK`.

It reconstructs the reflected seam for three parameter pairs: \((5,5)\), \((5,6)\), and \((6,6)\). For each, it enumerates every dual three-face and every four-vertex candidate, verifies the explicit \(4mn\) free-face collapse pairs against the entire live face set, and checks equality of the surviving simplicial complex with a chosen Klein triangulation plus all long edges. A spanning tree of the square graph is independently determined before computing the exact integer Smith normal form of its square-cell boundary matrix.

Results: the Smith invariant lists are \(1^{24},2\), \(1^{29},2\), and \(1^{35},2\); the corresponding long-edge counts are \(150\), \(255\), and \(414\). Therefore the sample ordinary three-cut groups in the two nonzero reduced degrees are respectively \((\mathbb Z/2,\mathbb Z^{151})\), \((\mathbb Z/2,\mathbb Z^{256})\), and \((\mathbb Z/2,\mathbb Z^{415})\).

**Proof boundary:** The finite checks do not prove the theorem for arbitrary sizes. The all-parameter classification of graph faces, universal free-face argument, and the Klein surface identification in `RESULT.md` supply the actual infinite-family proof. No independent audit or external formal certificate is asserted.
