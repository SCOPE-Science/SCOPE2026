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

# Reproducible verification

The file `verify.py` uses only the Python standard library. Execute `python verify.py` alongside this file to test exact rational identities, not floating-point approximations.

The checker independently enumerates uniform subsets and internal gap compositions for all integers \(2\le N\le11\) and \(2\le k\le N\). It checks conditional uniformity, total and conditional expectations, the two exact covariance identities, stochastic threshold means, the one-step urn transport equation, strict finite covariance signs, and quadratic-concentration monotonicity. In the recorded run it exited with status zero and printed `exact_checks_passed: 6527`.

Finite enumeration does not certify the infinite family. The uniformity induction, vector martingale identity, exact moment formulas, and covariance arguments in `RESULT.md` provide proofs for arbitrary finite admissible parameters. No external or independent audit has been performed.
