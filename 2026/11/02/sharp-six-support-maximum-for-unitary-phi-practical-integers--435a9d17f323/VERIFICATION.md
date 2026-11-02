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
# Verification and limits

Run \(\texttt{python3 verify.py}\) in a Python 3 standard-library environment. The checker performs exact integer arithmetic and trial division; it computes all necessary prime-power components, the factorization \(2^{32}+1=641\cdot6700417\), the sharp greedy deficit and the extremal product. As an independent small-input check, it tests the prefix criterion against a direct bitset subset-sum computation on \(1252\) configurations, and reconstructs \(15\) initial terms from the defining sequence.

These are finite reproducibility checks, not an exhaustive search of all six-prime-support integers. The infinite maximality and uniqueness are established in RESULT.md using the fully quantified prefix criterion and the monotonic bound. No claim about seven or more prime factors follows, and no independent audit has been performed.
