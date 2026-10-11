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

# Verification of the angular-return rigidity theorem

The proof is analytic: the radial-power derivative along oriented angle is the linear scalar equation \(dv/ds=2p(\lambda+Fv)/G\). Explicit integrating factors give \(P(v)=\rho v+B_\lambda\) on every positive-radius section; \(\rho\in(0,1)\) and \(B_\lambda>0\). Integration of \(d(\log r)/ds\) on the unique fixed graph yields the physical-time period. Linearization of this exact section map gives \(\rho=e^{-2p\lambda T}\), establishing the universal exponent and the exact relaxation per revolution.

Execute `python3 check.py` using only the Python standard library. It numerically integrates the exact angular equation for noncircular cubic cases with distinct anisotropies and a distinct linear-growth coefficient. It compares the affine return, physical-time period, transverse multiplier and the same-time-and-multiplier anisotropy property, printing `CHECK_OK` if they agree to the stated numerical tolerance. The finite calculations do not establish the general theorem; the proof does.

A complete text of Bendjeddou–Llibre–Salhi (2013) was unavailable. Consequently, the literature comparison cannot rule out an earlier equivalent quantitative argument. No independent review has been carried out.
