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

# Reproducible verification and boundaries

Run `python verify_cycles.py` with Python 3 and the standard library. The executed copy produced `PASS 142 finite tests; analytic asymptotics proved separately`. It evaluates the explicit correction function in numerically stable form, brackets sufficiently distant period-two points, performs bisection, tests their positive and negative iteration residuals, checks sample Newton contractions, and compares large-index roots against their asymptotic displacement coefficient.

The code verifies finite floating-point examples, not the asserted existence of infinitely many orbits. That existence and the eventual unique-root claim follow from the sign comparison and uniform derivative asymptotic in `RESULT.md`. The location law follows from the written uniform asymptotic expansions. The Newton comparison follows from the global derivative bounds and mean-value theorem. No verification of general attraction/repulsion, finite precision root certification, or convergence for additional nonlinear equations is claimed.

Scientific literature evidence: arXiv:2609.08110v1 was inspected through the introduction, method construction and early theoretical section before later material became inaccessible; arXiv:2312.12305v1 was read in full. Published mathematical research records and open literature were queried for stronger coverage and related corrected-Newton periodic orbits, with residual historical-priority uncertainty. Independent auditing has not been performed.
