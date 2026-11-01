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

# Reproduction of the finite proof

Execute `python verify.py` using Python 3.9 or later. No external packages or downloaded data are used. The script generates the precise three-by-eight graph, enumerates all nonempty matchings twice (recursive edge decisions and a column-transfer dynamic program), and builds a complete greedy-toggle matching on the simplicial face poset.

The test reverses every matched codimension-one incidence and performs a complete directed-acyclic-graph topological sort on all 1,222,549 faces; partial exploration is not accepted. It computes the *signed integral* critical boundary by gradient-path recursion. An explicit unimodular row/column elimination shows that the sole Morse differential has eighteen unit Smith factors, so the homotopy argument in `RESULT.md` cancels the corresponding cells. The printed `VERIFY_OK` lines are assertions backed by recomputation in the script, not substitutes for that recomputation.

The homotopy inference assumes standard discrete-Morse CW realization and the Hurewicz theorem for a wedge of seven-spheres. The proof is only for the finite graph defined in `RESULT.md`, and the external novelty comparison is limited by inaccessibility of the complete 2026 preprint. No independent external audit or certification is represented.
