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

# Reproduction and proof boundaries

Run `python3 verify.py` in a directory containing the embedded verification script. It uses standard-library exact `fractions.Fraction` arithmetic and evaluates Fourier character integrals by integer frequency cancellation; no floating point, external data, or network is required. The expected final stdout line is `VERIFY_OK`.

The tested traces are \(3,4,5,7\), with three integer sensors, coefficients \(c\in\{-2,-1,0,1,2\}\), and lengths \(1\le N\le6\). The script checks exact centering, variance and third moment, pairwise Fourier orthogonality, and the resonant triple \(1/4\). Those finite verifications are not logically exhaustive over all matrices, sensors, coefficients or lengths. The general proof is the two-eigenspace classification of signed triple resonances plus the modular argument for the two-trace-harmonic case, and the Haar factorization/conditional-sign argument. No outside certification has been performed.
