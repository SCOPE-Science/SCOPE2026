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
# Reproducible verification

Use `python3 verify.py` with Python 3.10 or later and no third-party packages. The script builds the graph constraints from two-bit states, constructs the exact transfer matrix, derives the row-swap eigenspace blocks, verifies their two polynomial determinant factorizations via Newton identities, and independently enumerates vertex subsets on each graph of orders \(6,8,10,12,14,16,18\). It compares every coefficient of the 1-limited domination polynomial, not only the optimum.

The enumerations visit \(64+256+1024+4096+16384+65536+262144=349504\) vertex subsets. A further exact transfer recurrence verifies predicted minimum sizes and multiplicities for all \(3\le n\le30\). All these tests completed successfully. In the factorization step, all polynomial division is exact integer division with an assertion checking divisibility; no floating-point root inference is used. The infinite result follows from finite-symbolic identities and coefficient extraction; enumeration of finitely many graph orders alone would not prove it.

The verifier is a separate standalone artifact included with the mathematical result. A source audit by an independent mathematician remains unperformed.
