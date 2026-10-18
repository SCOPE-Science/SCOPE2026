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

# Reproducibility checks
Execute `python3 verify.py` in a Python 3 environment; it requires only the standard library. `verification_output.txt` records the actual output from that command. The program independently generates the adjacency relations of \(S(K_n)\), uses breadth-first search to test edge-deletion distance changes, and evaluates each probe subset directly. All \(2^{n+\binom n2}\) subsets for each \(3\le n\le6\) are checked, totaling \(2,131,008\). It independently computes both complete polynomials and the minimum monitoring multiplicities, then compares all coefficients. The proof for unbounded \(n\) is the mathematical structural argument in `RESULT.md`, not the finite computation. A separate bibliographic priority limitation arises from unavailable full text of the 2025 subdivision-graph study.
