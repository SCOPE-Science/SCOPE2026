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

Use the included `verify_clebsch_2ind.py` with Python 3 and the standard library. Its complete expected stdout is `verification_output.txt`. It reconstructs all 16 vertices and 40 graph edges from the displayed XOR increments, compares two independent definitions of every two-independence face over all 65,536 possible subsets, and reconstructs all 2,142 nonempty faces. Every one of the 9,280 face-poset cover relations is checked in a complete topological sort after reversing the 1,069 matched covers, establishing the acyclicity needed for discrete Morse theory.

The script projects oriented simplicial boundary operators through every matched unit-incidence pair to find the complete integral Morse differential between critical cells, namely the row matrix `(1, 1)`. This primitive matrix, plus the absence of lower positive-dimensional critical cells, proves the four-sphere homotopy type. The independent F2 boundary-rank computation is corroboration, not a substitute for integral attaching-degree calculation. Signed fixed-face sums compute rational Lefschetz traces `+1,-1,-1` for a translation and two specified transpositions. Generation of the full group action follows from the five-direction relation and the `(16,5,0,2)` neighbor-pair argument.

The code checks this *finite* graph completely, not a conjecture about general folded cubes. The conclusion about all group elements follows from the proved generation and conjugacy argument, not an exhaustive loop over 1920 automorphisms. No independent scientific validation has been conducted.
