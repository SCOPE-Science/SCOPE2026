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

The theorem is supported by the complete combinatorial argument in `RESULT.md`. `verify.py` independently constructs the graph from doubleton-disjointness, calculates distances by breadth-first search for each vertex, and derives the two graph-edge distance profiles before checking the full neighborhood histogram and the ground-support intersection identity. It does not assume the theorem's graph-distance lemma.

Execute `python3 verify.py` (Python 3.9+; standard library only). The supplied `verification-output.txt` reports the results for integer orders 5 through 9, including 99,753 tested pairs of graph edges. Verification asserts that every histogram coefficient, support-intersection size calculation and edge count matches the formulas. The proof covers all higher orders by algebraic counting and not by extrapolation. The program does not implement a separate general LP solver because the text presents explicit feasible weights and an exact summation lower-bound certificate.

Scientific limits: the scalar Petersen instance is previously known; the computations do not establish originality or independent validation. This document reports reproducibility only, not any independent audit result.
