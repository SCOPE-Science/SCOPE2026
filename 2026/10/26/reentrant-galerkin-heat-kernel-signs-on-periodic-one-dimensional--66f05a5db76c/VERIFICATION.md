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

The matrix identities and infinite-family estimate are given in `RESULT.md`. The self-contained Python standard-library script `verify_semigroup.py` performs 45 exact rational evaluations of a Taylor-polynomial matrix entry, verifies its residual bound from the real spectral interval, and proves an exact coefficient-alias bound sufficient to extend these inequalities from sizes at most 50 to every larger periodic mesh. It also checks the polynomial root brackets and transformed Descartes coefficient list.

Executed command: `python3 verify_semigroup.py`.
Observed outcome: 45 rational inequalities passed, the largest tested value occurred at size eight, and all rational tail-bound checks passed. This is computational verification of specified finite algebraic certificates, not a claim that finite testing alone establishes the infinite statement.

The analytic proof covers all integers \(n\ge6\), all \(\ell>0\), and unit diffusion; the proof of minimality explicitly covers sizes three through five. The exact threshold statement is restricted to the six-cell case. Independent audit has not been performed.
