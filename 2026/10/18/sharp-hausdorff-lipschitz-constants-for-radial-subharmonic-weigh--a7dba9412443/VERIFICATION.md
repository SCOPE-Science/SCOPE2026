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
The entire claim is the sharp radial-subharmonic weighted-perimeter theorem in `RESULT.md`. Its analytical proof checks the normal variation, divergence with the origin-flux condition, monotone curvature quermassintegral bound, convex approximation including dimension collapse, radial inclusion monotonicity, and Minkowski interpolation. For \(\phi(r)=r^p\) and \(p>0\), the radial Laplacian is \(p(n+p-2)r^{p-2}\) and is positive off the origin.

Run `python3 CHECKS.py` with the Python standard library. The checker verifies exact second-moment integrals for rounded rectangles, strict ball parallel-increment domination on tested cases, the concentric-ball sharp coefficient, and degenerating-rectangle convergence to the two-sided line-segment measure. These are finite diagnostics and do not certify the universal theorem or any independent audit.

No independent audit was performed.
