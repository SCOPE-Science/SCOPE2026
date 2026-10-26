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

To reproduce finite checks, place `CHECK.py` beside this file and run `python3 CHECK.py`. The script uses the Python standard library only and checks 2,000 conditional second-moment identities by exhaustive enumeration with exact rational arithmetic. It also checks 4,000 randomized parameter configurations for the top Rayleigh eigenvalue and sharp boundary, and 1,000 generic reflection instances. These are genuine checks run against the included code. They are finite and cannot prove the infinite-parameter claims.

The universal proof is given in RESULT.md. Its critical steps are (i) the independent-draw moment identity, (ii) the top eigenvalue and feasible maximizing eigenvector of the interference quotient, (iii) a strictly positive residual coercivity inequality, and (iv) the countable-union-of-lines argument for generic preservation under pure greedy two-worker reflections. In particular, the Euclidean one-step increase witness for relaxation above the boundary is **not** a proof of long-run divergence.

The methods differ from general lock-free asynchronous implementations: all workers use the same snapshot, and no numerical roundoff, inconsistent data, stale snapshot across multiple batches, or malicious thread scheduling is modelled. No independent validation is claimed.
