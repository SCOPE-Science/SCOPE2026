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
The cyclic Fourier diagonalization establishes the spectrum of the unnormalized difference energy on mean-zero vectors. The scalar optimization is exact for all \(N\ge3\) because every maximizing resolvent profile realizes equality and no unlisted function can improve the Cauchy–Schwarz bound. Periodization of the infinite-line Green kernel and subtraction of the zero Fourier mode prove the hyperbolic resolvent formula. The analysis uses compact-uniform power series only after showing that all global maximizers lie in a positive compact spectral scaling interval; thus the asymptotic expansion is not an unsupported local candidate.

Running `python verify_cycle_sobolev.py` with Python 3 standard library produced `all checks passed`. It compared Fourier and closed resolvents, directly reconstructed Green columns and norm quotients for sizes \(3,4,5,6,7,9,12,20,30,50,80\), and tested asymptotic residual sizes up to \(100000\). These checks are finite numerical evidence only; the infinite statements are justified in the proof. No Lean certification, independent audit, or external formal validation was performed.
