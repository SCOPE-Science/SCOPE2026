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

# Verification notes

For the self-contained theorem, inspect the domain, generator and boundary regularity in `RESULT.md`. The displayed Green kernel can be differentiated twice to verify the killed backward equation, and the change of variables leading to the scaled exponential-integral representation is exact. The boundary-layer remainder follows by splitting the integral at half of its upper endpoint; the all-moment exponential law follows from positivity, the Green-kernel concentration and moment determinacy. Those proofs—not numerical sampling—justify the universal statements.

Run the supplemental deterministic checker with `python verify.py` in a Python environment with SciPy installed. It evaluates both independent integral representations and checks numerical convergence for multiple field strengths and shrinking-cap parameters. It does not establish uniqueness in the literature, independent audit, or limits outside the stated regime.
