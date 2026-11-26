---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With the stated normalization V_h1=(1/√π)∂_x V_h0. Differentiating the Gaussian-window transform of each Hermite function gives radial densities te^(−t) for h0 and e^(−t)t^(m−1)(m−t)²/m! for m≥1, times the radial measure dt, where t=π|z|². The angular indices m−1 are distinct, so completeness makes the centered disk form exactly diagonal; STFT covariance translates the norm to every center. Integrating via the incomplete gamma recurrence gives adjacent differences e^(−T)T^m(m−T)(m+1−T)/(m!(m+1)), including m=0 by direct integration. At T=1 there are exactly three tied highest levels and a strictly decreasing tail. In the annulus, the fixed h0 input yields the integral of te^(−t) on [a,a+1]; its derivative is e^(−a)((a+1)/e−a), with a unique sign reversal from positive to negative. The strict advantage follows from moving off a=0 (or the logarithm inequality in the proof). A separate high-precision integral gives 0.353224356803948823939 versus 0.264241117657115356809, and rational bounds on the two exponential factors certify a relative gain greater than 33%. Replay: python /workspace/calculations/reproduce_frozen.py (check hermite_annulus). The result gives a lower bound on the annular operator norm, not that norm or its global optimality.

## originality

PASS

Best of current knowledge: the general radial eigenvalue integral and fixed-input superlevel-set principle are established. The supported contribution is the exact strict equal-area annulus-versus-all-disks comparison for the first excited Hermite analysis window. The disk benchmark alone is a specialization of known spectral machinery, and the fixed-input annulus is a standard superlevel-set construction.

## value

PASS

The same physical area, covariance over disk centers, and comparison to the full disk operator norm make this a useful counterexample to transferring Gaussian-window disk optimality. Unit area is a natural normalized spectral degeneracy where three maximizing input modes tie; the simple annular witness gives a certified substantial gap. The constrained fixed-input optimum does not purport to solve free-input shape optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
