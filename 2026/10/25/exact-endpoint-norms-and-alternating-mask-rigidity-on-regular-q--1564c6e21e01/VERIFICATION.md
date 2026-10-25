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
# Verification

Run `python check.py` with Python 3.10 or newer. The checker uses only Python's standard library `fractions` and `itertools`; no network access or external papers are needed. It compares two independent exact row-norm formulas for all masks at depths through ten for branching values three through seven, checks every maximizing mask and the finite geometric-sum constants, reconstructs conditional expectation matrices for smaller branching/depth combinations, and tests the Bellman envelope at rational initial states. The displayed PASS assertion total is a reproducible finite computation, not an infinite proof. The all-depth assertions require the algebraic induction in `RESULT.md`. Independent mathematical verification has not been performed.
