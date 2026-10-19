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

# Verification record

The accompanying `RESULT.md` provides a self-contained algebraic proof. The accompanying standalone Python 3 standard-library program `verify_stale_polar.py` is executed from the artifact directory with `python3 verify_stale_polar.py` and printed:

`PASS 288 mode spectral-root checks, 144 actual nonlinear Jacobian checks, and 100 exact Jordan powers/norm checks`

These tests compute quadratic characteristic roots at 96 combinations of mixture and normalized stepsize for each of three eigengaps, and compare the normalized nonlinear map's finite-difference derivatives with the exact Jacobian. They also compare the first 100 powers of the boundary companion matrix to its closed form and singular-value norm. No external data or special packages are required.

Finite spectral checks do not establish statements for all real mixture fractions or for arbitrary matrix dimensions; the proof derives them from the quadratic Schur inequalities and the symmetric spectral decomposition. The test also does not determine nonlinear asymptotic stability exactly at the step ceiling, global convergence, noisy performance or effectiveness under arbitrary distributed arrival patterns. No independent audit or external certification has been performed.
