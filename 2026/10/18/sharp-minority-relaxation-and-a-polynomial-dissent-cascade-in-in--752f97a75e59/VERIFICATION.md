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

# Reproduction and scope

The included `verify_incremental_voter.py` checks, by exact symbolic arithmetic, the coordinate Jacobian, its spectrum, the left eigenvector recurrence, quadratic order of the nonlinear remainder, and conservation of mass for \(k=1,2,3,4,5\). It additionally integrates sample initial data for \(k=1,2,3\), displaying diagnostic rescalings at finite observation times. Dependencies: Python 3 with `numpy`, `scipy`, and `sympy`. Execute `python verify_incremental_voter.py` in the extracted file directory.

The infinite-time claims use analytical estimates for arbitrary integer \(k\), rather than an extrapolation of those checks. The positive slow projection, integrable quadratic remainder, opposite-edge integrating factor, and special \(k=1\) resonance are the critical proof steps. The theorem assumes attraction to a consensus and is not a classification of all initial conditions. The scientific assessment is limited to self-review; no independent audit has taken place.
