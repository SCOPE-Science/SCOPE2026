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

The proof uses the exact transition generator, a strictly positive exponential eigenfunction, and a Doob transform whose gap is an M/M/1 process. The decisive uniform-integrability step requires both \(\beta_\theta<\delta\) and \(B_\theta<\delta\). The tilted ergodic theorem and a martingale strong law justify the local large-deviation lower bound; an exponential Markov bound gives the matching upper exponent.

Execute `python verify.py` with the requirements listed in `requirements.txt`. In the checked environment the program returned `PASS: 72 independent finite-dimensional tilt-consistency comparisons; plus 1265 exact rational tilted-generator identities`. Its finite-state matrix truncation concerns a consistency identity and cannot establish the infinite-state or infinite-time theorem. All claimed limiting results have a separate analytical argument. Independent audit and external validation have not been performed.
