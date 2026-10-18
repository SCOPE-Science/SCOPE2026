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

The standalone `verify_sbc.py` uses the same normalized logistic-confidence flow specified in the theorem. Run `python verify_sbc.py` in an environment with NumPy, SciPy and mpmath.

It enumerates binary sign assignments on one- through four-vertex persuadable graphs in several empty, complete, path and mixed topologies, and checks root residuals, attraction by Jacobian spectral abscissa and agreement with the analytic inverse-Laplacian leading coefficient at three pairs of positive steepness and cutoff values. It checks \(324\) independent sign/center graph attractor instances. It separately brackets scalar roots and checks derivative types in \(15\) finite-precision parameter cases. Some scalar roots are indistinguishable from the interval boundary at ordinary double precision because their displacement is exponentially small; this does **not** constitute an exact endpoint root. An additional \(12\) independent cases use \(75\)-digit mpmath arithmetic and explicit bisection to resolve the outer exponential displacement, the inner reciprocal-steepness expansion, and the finite residuals. The program reports a complete PASS when these numerical tests succeed.

The scientific all-graph and infinite-steepness claims instead follow from the explicit strict-gap \(C^1\) convergence, hyperbolic persistence, matrix positivity, and scalar sign/uniqueness proof in RESULT.md. Numerical tests do not prove completeness outside the one-persuadable case, identify a uniform steepness cutoff, or independently validate originality.
