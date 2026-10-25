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

The identity follows from an area-preserving decomposition of the regular polygon into \(2n\) equal right triangles whose fixed apex is the nearest polygon vertex. Integrating powers of the distance from this vertex in vertex-centered polar coordinates yields the exact moment formula. The derivative of \(\cos t/\sin^{p+1}t\), dominated convergence for \(0<p<1\), the endpoint integral at \(p=1\), and the local approximation \(\sin t\sim t\) for \(p>1\) establish the three limits.

For \(p=1+\lambda/L\), \(L=\log(n/\pi)\), a direct comparison of \(\sin^{-p}t\) with \(t^{-p}\) controls the integral error uniformly for bounded \(\lambda\), proving the critical-window scaling and its continuous value at zero.

Run `python3 check_nearest_polygon.py` with Python 3; no third-party modules are required. The script checks independent geometry sampling, exact low-order reductions, and finite-order numerical approximations to the asymptotic constants and crossover. This is not a formal computer proof: the continuous and all-order parts require the analytic argument. No independent review has been performed.
