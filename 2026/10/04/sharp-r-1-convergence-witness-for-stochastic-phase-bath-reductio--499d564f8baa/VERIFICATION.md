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

The analytic verification uses the source Hamiltonians specialized to two sites, zero hopping, one oscillator per site, and a thermal product bath. The displaced-oscillator propagator and thermal displacement characteristic function give the exact coherence factors. The uniform phase integral is evaluated as a modified Bessel function, and the Taylor series of that function gives the asymptotic coefficient.

`verify.py` performs three consistency checks: deterministic quadrature of the one-copy phase integral against the Bessel closed form, strict finite-temperature under-dephasing for several values of \(R\), and convergence of \(R\|\rho_s^{(R)}-\rho_s\|_{\mathrm{tr}}\) to the analytic coefficient. These numerical checks do not prove the infinite-dimensional oscillator identity; the proof is the closed-form displacement calculation in `RESULT.md`.
