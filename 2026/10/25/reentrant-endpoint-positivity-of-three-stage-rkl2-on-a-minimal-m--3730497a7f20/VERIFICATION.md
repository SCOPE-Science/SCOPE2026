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

The exact-rational program `verify.py` (Python 3 standard library) checks 54,712 assertions and emits `verification_output.txt`; execute `python verify.py` from this directory. The tests cover the polynomial and matrix identities, row sums, positive and negative rational step lengths, generic two-stage finite-generator identities, two-state reductions, and perturbations of the pure-birth rates.

The proofs in `RESULT.md`, rather than these finite checks, establish the sharp intervals and universal lower bounds for all finite Markov generators. The classification is limited to endpoint nonnegativity. Independent audit and independent numerical validation have not been performed. Historical-priority verification remains incomplete, especially for the inaccessible 2021 paper of Dawes.
