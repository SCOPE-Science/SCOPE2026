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

# Verification of Fibonacci entrance law

Execute `python3 verify.py` using a standard Python 3 interpreter. The verifier uses exact rational arithmetic, integer Fibonacci recurrences, polygon half-plane clipping, and the shoelace area formula. It independently confirms for every \(1\le n\le19\) that the survivor and first-hit areas coincide with \((2F_nF_{n+1})^{-1}\) and \((2F_nF_{n+2})^{-1}\), respectively; it checks the first-entrance inequalities at all polygon vertices. It prints `VERIFY_OK` on success.

## Checks and their limits

The exact finite computations were executed on the packaged verifier and yielded `VERIFY_OK`. The infinite tail constants, universal weak conditional law, and exact exponential-moment boundary are proved analytically using the Fibonacci matrix identity, Binet asymptotics, uniform approximation of densities on shrinking triangles, and dominated convergence of normalized first-hit regions. Polygon clipping at finitely many depths does not independently certify those infinite statements.

The only external mathematical input is the stated critical half-memory tent-map definition and the already-established observation that its upper triangle consists of period-three trajectories. The present proof restates and verifies those identities directly.
