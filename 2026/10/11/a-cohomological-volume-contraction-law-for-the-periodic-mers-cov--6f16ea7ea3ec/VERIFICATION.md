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

The proof uses only the published vector field, a direct Jacobian trace calculation, two logarithmic identities valid on positive trajectories, and Liouville's determinant formula for the variational equation.

`verify.py` implements an exact linear-symbol checker for
\[
\operatorname{tr}J
=-\left(d_1+c+rac{\lambda}{T}+rac{\lambda_1}{D}ight)
+rac{d}{dt}\log(TD),
\]
with the two logarithmic derivatives substituted from the model. It also verifies the source-example baseline contraction factor
\[
\exp\!\left[-\int_0^{\pi/5}(d_1(t)+c(t))\,dtight]
=\exp(-0.16\pi/5)
=0.904357108638\ldots.
\]

A separate high-accuracy numerical replay of the source's displayed periodic coefficients was used only as a consistency check. Starting from the source's displayed initial state and integrating to the attracting forcing-locked response, direct integration of the variational equation gave monodromy determinant \(0.665268082639\ldots\). Quadrature of the exact determinant formula gave the same value to about \(7	imes10^{-13}\). The proof does not depend on this finite numerical experiment.

The determinant restriction does not prove that all Floquet multipliers lie inside the unit circle. It guarantees only that their product has modulus below one, hence at least one multiplier is contracting.
