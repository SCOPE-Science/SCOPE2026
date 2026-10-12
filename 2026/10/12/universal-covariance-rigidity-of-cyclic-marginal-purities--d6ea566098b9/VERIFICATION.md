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
# Verification

Run `python3 verify.py` with a standard-library Python 3 interpreter. Its local run returned:

`VERIFY_OK incidence_cases=99 four_replica_cases=116 covariance_cases=38`

The incidence computations cover all admissible length parameters up to 20 sites, and check the ranks of the translated Bell-pair cut matrices exactly modulo a large prime. The independent 24-permutation calculation reconstructs exact rational Haar second moments at all checked size/overlap pairs and verifies the claimed balanced/unbalanced covariance ranks, with the small balanced-qubit variance compared to its published numerical value. These bounded computations do not prove the statement for arbitrary sizes or for arbitrary full-support ensembles; the proof in RESULT.md does so via Fourier factors and continuity. Finite modular rank agreement is not a replacement for the analytic rank proof. No external or independent audit was conducted.
