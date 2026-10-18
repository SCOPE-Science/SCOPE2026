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

The theorem follows from an exact Walsh linearization of the full finite-dimensional quadratic mean-field ODE, an algebraic identity for quadratic Walsh moments, the analytic implicit-function theorem, and finite counting. None of these infinite-family conclusions is inferred solely from a finite computation.

`checker.py` constructs transition rates directly from ordered interacting opinion pairs, differentiates exactly in rational arithmetic, verifies the resulting matrices on every nonconstant Walsh character for each tested parameter choice, and checks conservation at nonuniform probability vectors. It checks threshold pairs both equal and unequal and verifies the high-similarity closed spectrum for issue counts two through five.

Command: `python3 checker.py`
Observed result: `PASS: 453 exact rational eigenmode/parity assertions; n=2,3,4,5`.

The executable verifies finite instances and identities, not the arbitrary-dimensional proof or scholarly uniqueness. The local-convergence result is proved analytically and makes no global or stochastic claim.
