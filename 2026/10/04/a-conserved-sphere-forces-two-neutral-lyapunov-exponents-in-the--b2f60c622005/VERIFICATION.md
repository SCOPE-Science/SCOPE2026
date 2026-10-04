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

The exact checks are replayable with `python3 verify.py`. The script reconstructs the printed vector field, verifies \(\dot H\equiv0\), verifies zero divergence, checks uniqueness of the equilibrium under \(a\ne0\) and \(b\ne0\) by the four stationarity equations, and checks the source example's energy and reported finite numerical Lyapunov arithmetic.

The two-zero-exponent conclusion is an analytic cocycle argument, not a numerical inference. On a nonzero sphere, the vector field is nonvanishing and therefore supplies a bounded flow-direction cocycle with exponent zero. The identity \(dH_{\phi_t(p)}D\phi_t(p)=dH_p\), together with constant \(\lVert dH\rVert=2R\) on the sphere, supplies a second zero exponent on the normal quotient. Since divergence vanishes, Liouville's formula makes the total exponent sum zero, leaving an opposite pair.

Limits: no value or positivity of the remaining exponent is certified; finite-time numerical exponents and discretized integrator dynamics are outside the theorem.
