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

# Verification and reproducibility

Execute `python3 check.py` in the directory holding the six accompanying documents and the checker. It runs without third-party dependencies and reports 256 exact polynomial Gaussian-integral identities and the degree-one Laguerre root at one. The source of the checker is provided in full.

The analytic proof in `RESULT.md`, not this finite computation, establishes Weyl covariance, the Gaussian generating identity in all orders, the contractive disk-averaging functional, the limiting annihilation for every bounded measurable mask, and the resulting sharp operator-norm distance. The Hermite STFT/Fock unitary identification follows from Abreu--Speckbacher (2018), Section 6.3.

No independent mathematical audit, proof certification, or external experimental validation has been performed.
