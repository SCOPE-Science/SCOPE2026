---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The fine nodal slopes 3, 0, −1/4, −1/2 are strictly decreasing at the knots. The fine score vanishes by construction and the log-normalizer's hat covariance is positive definite modulo constants. For the full log-concave class, restriction to the data interval and replacement by the secant interpolant through the log values at the sites cannot increase the normalizing integral; positive mass outside or a positive gap from the interpolant on a set of positive measure makes the likelihood comparison strict. This proves uniqueness of the normalized density (up to null sets). Coarse hat moments are exactly the corresponding fine-density moments, since every coarse hat is its own fine-grid interpolant. An independent rational integration using the Bernstein expansion of each affine power enclosed the three coarse score coordinates at the trial point (approximately 5.096e−9, −4.360e−9 and −2.799e−9); each interval lies inside (−10⁻⁶,10⁻⁶). Direct integration of the centered Gram matrix reproduced leading minors 27/80, 457/7200, 257/108000 after subtracting I/10. The density lower bound 1/40 on the radius-1/100 ball multiplies the Lebesgue variance lower bound (minimize the squared deviation over constants), yielding Hessian >I/400. The objective increases by more than 21/200000000 on the sphere, giving an interior critical point, unique globally by strict convexity. The slope jump is strictly greater than 488249/2500000 after bounding the trial-point displacement, and normalization does not change the jump. Replay: python /workspace/branches/independent_replay.py 2.

## originality

PASS

On the inspected evidence this is a distinct counterexample on the fixed-weight implication explicitly left open by Grosdos et al. Their old nonconcave fit is on an incompatible, not coarser, subdivision. Realizability of another subdivision by changing the weights cannot refute or settle the fixed-weight claim. The inaccessible corrigendum leaves a concrete priority risk, not evidence of coverage.

## value

PASS

The witness answers a precise published question about a natural knot-deletion heuristic. It shows that even starting with strictly decreasing slopes at every fine interior knot does not ensure a concave unrestricted reduced fit, and the failure can occur at a retained knot away from the removed one. The exact certificate resolves that substantive issue without a numerical concavity tolerance or a change of weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
