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

# Verification details

The analytic verification is the explicit factorization of the odd reduced matrix by row phases into two rational \(4\)-by-\(4\) blocks, the exactly computed squared trace, and the algebraic-integer norm obstruction in all odd dimensions. The source's published odd restricted characteristic polynomial provides an independent identity check via Newton's formula.

Run `python3 verify_revivals.py` with the Python standard library. The checker uses exact rational permutation determinants for both dephased blocks for each odd dimension \(3\) through \(201\), constructs both spin signs directly, checks their complex determinants and traces, and checks the small-dimensional norm and general bound. It reports `PASS: 603 deterministic assertions`. Finite tests cannot prove the infinite-dimensional range of \(d\); that part uses the analytic conjugate bound, rational-algebraic-integer principle and field norm.

There is no independent audit, external certification, Lean proof or physical experimental validation. The model excludes arbitrary spin patterns outside the stated central-layer condition only insofar as those patterns are irrelevant to the invariant sector; it does not claim any result for other sectors.
