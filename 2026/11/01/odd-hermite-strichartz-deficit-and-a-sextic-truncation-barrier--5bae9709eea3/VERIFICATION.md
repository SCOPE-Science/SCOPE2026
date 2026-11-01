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

The standalone `CHECK.py` recomputes the Gaussian moments and uses an exact phase-Fourier convolution to verify the two-mode polynomial, the sharp quartic normal form, and the sextic and eighth-order coefficients on the unique cancelling curve. It requires Python 3 and SymPy. The proof extends beyond finite numerical checks by the exact lens transform and finite polynomial identities.

The three-mode series is a local fixed-parameter expansion, not a statement of global optimality for all three-mode or odd initial data. No independent audit or external certification has been conducted.
