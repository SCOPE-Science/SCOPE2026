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

# Finite verification and mathematical limits

Execute `python3 verify.py`. The program exhaustively constructs all functions on \([n]\) for \(2\le n\le7\) and computes the number of cyclic vertices and the number of indegree-zero vertices directly from the maps. Using exact rational arithmetic, it compares the observed tails with the factorial formula, the conditional origin factorial moments with occupancy counts, the complete origin-fugacity mixture at tested weights, the strict stochastic inequalities, and the uniform covariance identity.

Executed output includes `PASS exact assertions: 486`; at \(n=7\) all \(823543\) mappings were enumerated. Supplementary floating-point calculations at \(n=2000,10000,50000\) approximate the coefficient \(\sqrt{\pi/8}\). These are diagnostic only. The all-size and asymptotic results rely on the independent proof in `RESULT.md`, particularly the positive mixture, likelihood-ratio order, and tail-difference Riemann sum. No independent audit has been performed.
