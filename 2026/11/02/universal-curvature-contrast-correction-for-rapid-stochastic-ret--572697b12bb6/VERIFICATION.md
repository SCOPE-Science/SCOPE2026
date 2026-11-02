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

The analytical certificate is the exact all-rate renewal/Dynkin identity and the small-time expansions in RESULT.md. The leading coefficient follows from the stopped search cycle's success probability and drift-discrepancy expectation; no numerical result is used to infer an infinite-dimensional or all-parameter statement.

Run `python verify.py` with Python 3, NumPy, SciPy. The script independently assembles sparse finite-difference resolvents for cycle success and discrepancy, checks two genuinely nonlinear confining potential pairs and the identical-drift control at several reset rates. Mesh and finite computational domain are approximations, not certified interval enclosures. The test therefore checks consistency rather than constituting a proof or independent audit. The supplied assumptions imply positive recurrence of the return drift, finiteness of the mean, and exponentially small killed-versus-unrestricted small-time corrections.
