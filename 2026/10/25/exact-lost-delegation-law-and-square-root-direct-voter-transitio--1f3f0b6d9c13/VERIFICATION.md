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


# Verification and scope

Run `python3 verify.py` with Python 3.9 or later. The program uses only the Python standard library. It independently enumerates all independent local decisions for eight networks of part sizes between one and four (including the theorem's \(m,n\ge2\) domain) for \(q=1/2\) and \(q=1/3\). Rational weights are exact. For each outcome, it traces both side populations to a direct ballot or to a repeated vertex, and confirms the stated finite path-exposure formula and normalization. Explicit \(m=n=3\) rational values are also checked. These are reproducible finite tests; the all-size identity and asymptotic limits are supplied by the written proof, not inferred from computation. The checker does not verify novelty, asymptotic proofs, or publication priority.

The fixed-density limit is derived by first-collision decomposition and dominated convergence; the critical window is derived by a uniform Gaussian tail and local falling-factorial asymptotics. These analytic steps should be checked separately by readers. Independent audit and validation were not performed.
