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

# Reproduction and limits

Compile `verify_half16.cpp` with C++17 and execute the binary. Independently execute `verify_half16_independent.py` with Python 3 standard libraries. Both complete and print counts for every admissible residual ordered row/column degree pair: 906, 6720, 6720, 43440. The sum is 57786, and no adjacency matrix lacking an 8-edge induced subgraph occurs. Exact output from both programs is in `verification_output.txt`. The Python checker additionally reconstructs the two admissible degree partitions of 16. Tests are finite and exhaustive only after the graph-theoretic reduction in RESULT.md; they are not a proof by sampling and do not assert a theorem at 32 edges.
