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

# Verification and limits

The standalone `verify.py` uses SymPy to reconstruct both updates independently, verify the Gaussian covariance rational identities, identify the resonance and the exact asymptotic-variance ratio, and compare exact rational finite-stage calculations. Run `python3 verify.py` with SymPy installed. The completed verification returned `PASS: 483 exact symbolic and rational comparisons`. These checks agree with the self-contained mathematical proof in `RESULT.md`.

In particular, the proof determines stationary existence by checking \(r(z)=1-z+z^2/2\) and strict noise nondegeneracy; the exact Gaussian stationary law by the scalar Lyapunov identity; the sign and unique nonzero root by an explicit rational function; and the long-run average variance by an absolutely summable geometric covariance series. No finite enumeration substitutes for any universal quantifier.

The result does not cover general nonlinear drift, non-SPD curvature, approximate simulation of Brownian-integral pairs, Metropolis acceptance, or other stochastic integrators. The bibliographic originality search cannot exclude unindexed prior equivalent derivations. No independent audit has been performed.
