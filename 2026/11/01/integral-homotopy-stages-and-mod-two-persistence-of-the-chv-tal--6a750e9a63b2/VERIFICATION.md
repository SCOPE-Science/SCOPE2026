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

# Finite verification of the Chvátal higher-independence filtration

Execute `python3 VERIFY.py` from this directory using Python 3; only its standard library is required. The authoritative actual execution output is embedded as `CHECK_OUTPUT.txt`. A compact record of integer differential hashes, unimodular witnesses and barcode intervals is embedded as `MORSE_CERTIFICATES.json`. The checker rebuilds the complete graph, all 4096 induced-subgraph masks, every simplex of every stage, every toggle matching pair and every directed face-poset incidence. It explicitly proves acyclicity by topological sorting in both the augmented and ordinary settings.

It then computes all signed integral Morse differentials by recursive unit elimination and verifies explicit determinant-\(-1\) minors in exactly five nonzero boundary matrices. At cutoff three, it also verifies the chain identity between the successive degree-three and degree-four boundaries. From these integer matrices and the independently justified attaching-map interpretation of the Morse CW model, the finite homotopy classifications follow.

A second computational route performs direct ordinary simplicial boundary reduction over \(\mathbb F_2\), sorted by exact first-cutoff values, independent of the Morse matrices. The persistent barcode includes every nonzero-dimensional positive-length interval and the single essential ordinary degree-zero class. The exact coloring backtrack verifies the graph has no three-coloring and provides a four-coloring. Separate exhaustive deletion checks show vertex connectivity four (all deletions of up to three vertices preserve connectivity, and one explicit deletion of four disconnects the graph), explaining the classical simplex-skeleton endpoints at cutoffs 8 through 11.

The total across all twelve stages is **30,253 augmented faces, 14,481 matching pairs and 167,180 directed incidences**. The verification is exhaustive over the declared finite domain. It does not establish analogous statements for arbitrary graphs, integral persistence maps, or independently audited scientific priority.
