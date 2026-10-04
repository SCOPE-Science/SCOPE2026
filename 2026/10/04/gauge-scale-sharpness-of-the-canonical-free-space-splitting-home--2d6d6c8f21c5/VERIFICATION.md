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

The proof is exact and symbolic. For a unit vector \(u\), the forward pair \((0,tu)\) and \((0,0)\) has domain distance \(t\) and image distance exactly \(\omega(t)\). For the inverse, \(\eta_t=t\delta_\omega(u)\) has norm \(t\), barycenter \(tu\), and
\[
\|\varphi^{-1}(\eta_t)\|=\|t\delta_\omega(u)-\delta_\omega(tu)\|+t\ge\omega(t).
\]
The published upper estimates are \(\omega_\varphi(t)\le2\omega(t)\) and \(\omega_{\varphi^{-1}}(t)\le3\omega(t)\). Hence the two moduli are comparable to \(\omega\) on every positive scale.

For \(0<t<e^{-1}\), dividing the lower bound by \(t|\log t|^\gamma\) yields \(|\log t|^{\alpha-\gamma}+|\log t|^{-\gamma}\), which diverges when \(0<\gamma<\alpha\). This verifies sharpness of the exponent for the canonical map in both directions.

No computation, exhaustive search, or external certificate is needed. The result does not determine the optimal exponent among all homeomorphisms of the two Banach spaces.
