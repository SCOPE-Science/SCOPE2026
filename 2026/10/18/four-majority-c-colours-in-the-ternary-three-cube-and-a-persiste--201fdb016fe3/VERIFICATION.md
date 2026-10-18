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

# Reproducible checks and scope

Execute `python3 verify.py` from the directory containing this document and the other supplied files.

The script examines all \(\binom{27}{6}=296010\) labelled six-vertex subsets of \(K_3^{\square3}\), retaining a subset exactly if every member has at least three neighbours within it. It independently generates all three-by-two coordinate rectangles and asserts that the two collections coincide and have size \(54\). It then checks the four-symbol table and its product extension at dimensions \(3,5,7,9\), for all vertices and all neighbours, including the number of nonempty colours.

The proof (rather than these bounded computations) establishes the class-size obstruction, exact value in dimension three, classification of six-vertex sets and the bound in every greater odd dimension. Rechecking mathematical correctness and bibliographic priority by an independent researcher remains outstanding.
