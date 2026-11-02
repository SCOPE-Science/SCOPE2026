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

The constructive proof in RESULT.md is the mathematical verification of the stated finite-dimensional universal bounds and equalities. In particular, the two-measurement support-rank proof is independent of numerical search; the qubit Bloch-difference construction works for every state pair; the qutrit norm identity and its sharp spinor witness cover all nonnegative error triples and zero budgets.

The bundled `verify_three_obs.py` script is self-contained and uses only Python's standard library. Run `python verify_three_obs.py`. On inspection and execution, it reported **PASS 40012 finite assertions**. These tests include random normalized complex vectors, randomly sampled error budgets, direct threshold witnesses, the qubit Bloch-sphere chord replacement, and deterministic endpoint samples. Sampling alone neither proves the universal result nor excludes equivalent prior work.

Scientific scope: finite-dimensional complex Hilbert spaces and self-adjoint observable expectation differences; all maxima are over nonempty compact sets. The counterexample extends to higher dimensions and larger numbers of measurements by adjoining inactive coordinates and zero measurement operators. No claim is made about experimental statistical uncertainty, general three-observable triples, independent mathematical auditing, or externally certified novelty.
