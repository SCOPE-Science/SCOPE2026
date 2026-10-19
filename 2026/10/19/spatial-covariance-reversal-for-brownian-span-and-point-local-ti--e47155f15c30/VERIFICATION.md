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
# Independent reproducibility checks

Run `python verify.py` with Python 3 and the standard library. It verifies 60 numerical assertions covering (i) direct heat-kernel and first-passage quadrature against the explicit formulas for \(f_t\) and \(h_t\), (ii) independent numerical time-Laplace integration against the mixed-moment transform, (iii) the exact covariance at the origin, strictly positive far-field signs, (iv) Brownian scaling, and (v) occupation-density covariance conservation. All 60 assertions passed during preparation. These numerical tests corroborate but do not prove unrestricted stochastic identities; the proof is in `RESULT.md`. Independent scientific audit has not been performed.
