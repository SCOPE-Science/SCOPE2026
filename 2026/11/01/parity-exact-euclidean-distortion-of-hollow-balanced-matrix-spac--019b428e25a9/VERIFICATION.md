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

The standalone program `verification/check.py` was executed from the local package staging directory with exit status zero. It constructed exact balanced signing witnesses and exact orthogonal-projector leverages for \(4\le n\le19\), checked exact projection idempotence for \(4\le n\le9\), and tested 160 random linear-program vertices for \(4\le n\le11\). Output ended `CHECK_OK explicit_witnesses=16 exact_projectors=16 random_linprog_vertices=160`.

The universal extreme-point integrality, Eulerian constructions, symmetry-optimal Hilbert form, and exact extremizer classification are established analytically in RESULT.md. Sampling and randomized LP do not prove the universal assertion. Python 3 with NumPy, SciPy, and NetworkX is used to rerun `python verification/check.py`.
