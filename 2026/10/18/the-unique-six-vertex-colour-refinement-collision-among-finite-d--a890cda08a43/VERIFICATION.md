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

Both computations below were run on the embedded source code; their outputs appear in `verification_output.txt`.

**Standard-library independent enumeration:** `python3 verify_dags.py` builds all \(2^{\binom n2}\) topologically labelled DAGs for \(1\le n\le6\), runs globally synchronized directed refinement until its computed palette stops changing, then identifies distinct colour-preserving directed-isomorphism classes inside each signature bucket by exact backtracking. It asserts the six expected isomorphism counts and logical-class counts, and prints `VERIFIED` after the last assertion.

**Second implementation:** `g++ -O3 -std=c++17 canon_dags.cpp -o canon_dags && ./canon_dags 6 > canonical_dags.txt && python3 analyze_canonical.py`. The C++ implementation computes the minimum directed adjacency integer across all permutations, independently of refinement, and the Python analyzer then computes stable directed colours and groups the canonical types. It produces the same six count pairs, with only the six-vertex group of size two.

The argument that these computations are exhaustive uses the existence of a topological ordering for every finite DAG and explicit (not probabilistic) isomorphism testing. The all-orders mathematical part—the equivalence of directed colour refinement and \(C^2\) on the stated DAG language—is a standard finite-model-theoretic theorem. The explicit exceptional witness is checked structurally in `RESULT.md`. No arbitrary-order DAG count, publication priority guarantee, or external validation is asserted.
