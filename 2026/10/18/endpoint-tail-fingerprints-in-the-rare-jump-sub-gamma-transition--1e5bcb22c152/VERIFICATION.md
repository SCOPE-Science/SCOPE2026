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

# Reproducibility and verification

Run `python3 check.py` in this directory. The program requires the Python standard library only and reports 90 deterministic checks for three integer-parameter beta jump laws and three rare intensities each. Its computations use closed-form finite beta moment generating functions, differentiated independently of the main cumulant expansion, and solve the interior stationarity equation by bisection.

The tests examine finite parameter values and grid-local optimality; they **do not prove** the large-deviation asymptotics, complete parameter-space optimality, publication priority, or historical novelty. The analytical endpoint Laplace lemma, global maximizer localization, and stationary-equation comparison in `RESULT.md` supply the proof. The scientific review is same-model only; independent audit and validation have not been performed.
