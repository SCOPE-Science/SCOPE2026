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

The standalone scripts `biased_crossing_verifier.py` and `crossing_verifier.py` were executed using Python. The biased script reported `PASS biased exact arithmetic assertions: 4644`, while the symmetric script reported `PASS exact assertions: 922`. The former checks four exact probabilities and short complete absolute trajectories, together with independent coefficient generation of the renewal law; the latter checks marginal formulas and conditional return-time-pattern distributions. These finite checks are not substitutes for the four-step analytical proof of the infinite claims. All statements of independence in the limiting theorem are explicitly restricted to the auxiliary Brownian noise versus the return-clock limit.

Reproduction environment: Python 3 and `sympy==1.14.0` (see `requirements.txt`). The symmetric verifier uses only the Python standard library.
