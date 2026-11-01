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

# Verification

Use Python 3.9 or later with the standard library, and execute `python3 verify_petersen_cuts.py` alongside the file. Its output must exactly reproduce `verify_petersen_cuts_output.json`.

The script reconstructs the Petersen graph as \(\operatorname{KG}(5,2)\), checks all ten degrees and adjacency symmetries, and independently constructs every ordinary cut complex for \(2\le k\le10\) through (i) complements of disconnected induced sets and (ii) testing every candidate face for a witness in its complement. For each nonvoid complex it verifies all matched/unmatched Hasse incidences by a complete acyclicity topological sort in both forward and reverse vertex orders.

For \(k=5\), the forward reduction gives one critical vertex, eight critical three-cells, twelve critical four-cells and an integer boundary with seven unit Smith factors; the reverse reduction gives ten critical three-cells, fourteen critical four-cells and nine unit factors. The full ranks agree and give \(\widetilde H_3\cong\mathbb Z\), \(\widetilde H_4\cong\mathbb Z^5\) with no torsion. The zero/low-degree-cell and integral attaching-map proof in `RESULT.md` establishes the homotopy type. All other cases are exhausted by the displayed complete critical-cell lists and boundary matrices. Reproducibility does not establish publication priority or independent validation.
