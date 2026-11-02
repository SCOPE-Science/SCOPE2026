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

# Exact verification

Run `python3 verify_windmill.py` with Python 3; no external libraries or downloaded datasets are required. The program independently constructs the weighted nodal matrix \(6G\) from the windmill edge list, inverts it over rational numbers, computes kernel integrals for every vertex, and compares against the closed formula for tested sizes. It additionally checks the two positive-polynomial certificates and the triangular-petal threshold across many integer parameter pairs.

A complete execution of this packaged program returned `SUCCESS {'identities': 7332, 'matrices': 240, 'thresholds': 4888} total 12460`. These checks corroborate the explicit algebraic identities in the proof. They do not assert an exhaustive computer search over infinitely many parameters. No independent human mathematical audit has been conducted.
