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

Execute `python check.py` from the directory containing this file. The checker uses only the Python standard library and iterates over every four-coordinate composition for lengths \(5\) through \(9\). It verifies explicit lower-bound codes and searches all compatible sets using an exact bitset-based clique solver with mathematically valid greedy-color bounds. Recorded output is included as `check_output.txt`.

The proof of the bound for all larger lengths is algebraic and does not depend on extrapolating a computation. Code replay checks the finite boundary cases but does not constitute independent external review. No independent audit or validation has been performed.
