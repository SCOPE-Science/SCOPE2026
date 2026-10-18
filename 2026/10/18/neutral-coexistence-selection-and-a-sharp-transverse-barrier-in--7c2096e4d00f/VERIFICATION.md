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

The argument is analytic. The identities checked directly in `VERIFY.py` are the exact mass-deviation factorization, fixed-segment spectrum, and the multiplicative composition increment; sample trajectories provide finite checks only.

For arbitrary positive parameters and initial conditions, the proof in `RESULT.md` derives a compact interval for total mass, monotonicity of a composition coordinate, dichotomy of finite/infinite limiting composition ratio, and a contradiction against convergence to a normally repelling equilibrium without finite-time landing. A local contraction/selection-drift estimate proves optimality of the threshold; elementary unimodality gives the complete one-step preimage line.

`python VERIFY.py` is the reproducibility command. It needs Python 3 and SymPy. It is not an independent audit or a proof by finite enumeration. No claim is made about the uninspected full text of the related preimage article.
