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

# Verification notes

The isometry is a change of variables \(x=e^s/(1+e^s)\), with Jacobian \(x(1-x)\). The transported kernel is exactly \(e^{-(s-r)/2}\mathbf1_{r<s}\), so the commutator kernel and Hilbert--Schmidt identity have no normalization constants left unaccounted for.

The integrals required for critical constants are exact: \(\int_0^\infty t^2e^{-t}\,dt=2\), \(\int_0^\infty te^{-t/2}\,dt=4\), and \(\int_0^\infty te^{-t}\,dt=1\). The compact approximants integrate rank-one kernels whose factor norms multiply to one; this certifies their trace-class property. For nonzero limiting phase speed, the translated test vectors converge weakly to zero but have a nonvanishing commutator output on unit intervals. For diverging speed, integration by parts bounds the oscillatory component by \(4/v(n)\).

`verify_chirp.py` implements finite quadrature diagnostics at \(\theta=1/4,1/2,3/4,1\). Its output is not an infinite-dimensional certificate, and the proof of the exact threshold and energy asymptotics is independent of sampling. Only the stated operator and phase-velocity hypotheses are verified; other Schatten ideals and irregular velocities are unresolved. Independent audit has not been performed.
