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

# Verification evidence and limits

The included `verify.py` is standalone Python 3 standard-library script. Run `python verify.py` in the directory containing this file. It performs exact rational checks of the three-vertex coexistence equilibrium and both boundary Perron radii; five rational examples of a two-vertex reciprocal-bias bipartite continuum; strict Jensen inequalities for 135 sampled rational pairs; exact rational odds-barrier checks; and numerical convergence checks for synchronous and diminishing-step expected updates from three asymmetric initial states.

The general uniqueness, Perron necessity/sufficiency, and attraction results are proved analytically in `RESULT.md`; finite tests cannot establish those universal claims. The almost-sure stochastic statement depends on Theorems 3 and 4 of arXiv:2308.09275. No independent scientific audit has been performed.
