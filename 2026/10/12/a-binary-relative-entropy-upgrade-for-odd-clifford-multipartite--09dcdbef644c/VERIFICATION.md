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

The universal proof is analytic and is given in `RESULT.md`.

Local anticommutation gives
\[
\left(\sum_i x_i\Gamma_i\right)^2=\|x\|_2^2I,
\]
hence \(\|x\|_2\le1\). For odd party number, the tensor terms anticommute and therefore
\[
B^2=mI.
\]
These facts establish the exact product threshold and the binary spectral measurement.

For
\[
p=\frac{1+b/\sqrt m}{2},
\qquad
q_0=\frac{1+1/\sqrt m}{2},
\]
data processing yields a binary relative entropy. The derivative
\[
\partial_q d_{\mathrm{bin}}(p\|q)=\frac{q-p}{q(1-q)}
\]
justifies replacing the unknown product-marginal measurement probability by \(q_0\).

The bundled checker confirms the displayed endpoint values, strict improvement over the quadratic expression on a deterministic grid, and \(B^2=3I\) for the three-qubit Pauli instance. Those finite checks are corroborative only.

No claim is made for even party number or for exact fixed-expectation optimality.
