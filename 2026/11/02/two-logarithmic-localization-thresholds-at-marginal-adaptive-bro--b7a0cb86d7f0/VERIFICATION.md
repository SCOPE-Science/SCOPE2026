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

# Verification record

The main proof is analytic. Direct substitution of \(G(\rho)=\rho^{-d}h(\log\rho)\) gives the **exact** radial conjugation \(\rho^{d+2}\Delta_{\mathrm{rad}}G=h''-(d+2)h'+2dh\). The function \(g(z)=z^{-b/(d+2)}(\log z)^{-c/(d+2)}\) has the intended first-order logarithmic derivative, leaving a residual \(O(z^{-2})\); the exponentially damped Volterra operator then has tail norm \(O(z_0^{-1})\).

The included standalone `verify.py` checks the derivative identity symbolically in representative dimensions and the leading residual decomposition; it cannot certify the infinite-domain contraction argument or the existence/uniqueness of the regenerative stationary law. Both are established in `RESULT.md` under the stated assumptions. The limiting integral test is elementary and requires the exact controlled remainder in the hazard expansion. No independent audit has been performed.
