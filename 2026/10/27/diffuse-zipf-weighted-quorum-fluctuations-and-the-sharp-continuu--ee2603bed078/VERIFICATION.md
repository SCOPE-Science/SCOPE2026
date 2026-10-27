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

## Verification of the analytical claim

The proof in `RESULT.md` is an infinite-parameter argument; no finite experiment is treated as an asymptotic proof. Its independent-summand representation and inversion are exact for every finite \(N\). For \(u>0\), the exponentially suppressed Riemann sums give the variance and Lyapunov bounds. The singularity-free, undiscovered-mass integral and the generalized harmonic-number expansion give the deterministic correction. These facts justify all limiting transitions at fixed \(s,\theta,\lambda\).

Run `python verify.py` with the packages in `requirements.txt`. It checks exact mean-root identities, derivative and variance integrals, and the approach of scaled finite-population crossing shifts to their predicted constants for four specified parameter pairs. Asymptotic conclusions are based on the proof, not on the numerical outputs.

## Limits

The displayed checks use floating-point quadrature and root finding and are not mathematical certificates for arbitrarily large \(N\). No external or independent scientific audit has been performed. The analysis makes no claim for supercritical continuum centering when the leading shift coefficient vanishes.
