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

The all-integer-frequency theorem follows from the exact digit product and the finite set of analytic inequalities in the proof; the finite numerical checks are supplementary, not a replacement for an infinite proof.

The standalone `checker.py` file was executed with Python 3 and the standard library. Its successful output was `VICSEK_CROSS_FOURIER_CHECK_OK 58349 finite assertions A= 0.3581726074759163 B= 0.2550051230961403`. The 58,349 checks include the rational separator inequality, all relevant ternary residue cases, off-path lifts across sample levels and the finite box of frequencies \((m,n)\in[-120,120]^2\setminus\{(0,0)\}\). The finite box is not an exhaustive test of all integer frequencies.

Independent computation with high-precision infinite products gave \(A=0.3581726074759164252012471368665\ldots\) and \(B=0.2550051230961402498555820567491\ldots\). Their numerical values are informational; every strict global comparison uses the elementary analytic inequalities proved in `RESULT.md`.

No independent mathematical audit or validation has been performed. The exact fifth-order digit set, equal weights, integer-lattice domain and third-level limitation are essential.
