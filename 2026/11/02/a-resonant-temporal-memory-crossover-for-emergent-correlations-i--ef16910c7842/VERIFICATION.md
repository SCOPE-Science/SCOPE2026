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

The independently constructed four-component moment semigroup and the scalar forced covariance equation were compared for nine parameter sets at nine lag values, and the stationary variance was separately compared with the published equal-time formula. Symbolic exact identities check the forcing, the stationary derivatives, and the harmonic-mean crossing. A standalone checker performs 162 numerical and symbolic checks, including sampled strict monotonicity. Its successful run does not independently verify publication priority or replace the complete analytical arguments in RESULT.md.

Reproduce with `python verify_covariance.py` using NumPy, SciPy and SymPy. The theorem applies to stationary data and two distinct particles. Nonstationary starts and interacting particles are excluded.
