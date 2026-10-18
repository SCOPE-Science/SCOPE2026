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

# Reproducibility and checks

Execute `python3 checker.py` using a standard Python 3 interpreter. The checker constructs field addition and multiplication, including a polynomial-model extension field for cardinality four, and exhaustively enumerates all ordered vertex-coordinate pairs in each of seven cases. Every attainable and unattainable prescribed target is compared with the theorem's closed formula, with no sampling, randomized data, or external package dependencies. Exact cases are \((q,m)=(2,1),(3,1),(2,2),(3,2),(4,2),(2,3),(5,1)\).

The program asserts (i) every single-target fiber, (ii) total pair mass, (iii) the exact commutator-image size, (iv) the all-target decomposition into at most two commutators, and (v) agreement of the zero fiber with an independently computed centralizer/class-number aggregate. Successful execution prints `ALL_EXACT_CHECKS_PASSED`. Finite checks do not constitute an exhaustive proof for arbitrary \(q,m\); the general argument is the bijective calculation in RESULT.md. No claim of independent validation is made.
