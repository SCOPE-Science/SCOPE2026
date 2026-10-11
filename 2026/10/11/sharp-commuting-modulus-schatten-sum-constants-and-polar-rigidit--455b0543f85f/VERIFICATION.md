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

# Verification scope

The analytic proof is self-contained conditional only on standard Schur--Horn/Jensen and complex interpolation of Schatten classes. To reconstruct the first range, diagonalize the commuting moduli, inspect the diagonal of \(T^*T\), and apply concavity of \(t^{p/2}\). For strict \(p<2\), equality forces the Gram matrix to be diagonal and every positive-weight column summand to share an output direction; orthogonality constructs the common partial isometry.

For the second range, explicitly form diagonal weights \(w_{kj}\) and the operator \(V_0=\sum_kU_kW_k\). Directly check \(\|V_0D\|_{S_2}\le\|D\|_{S_2}\) and \(\|V_0D\|_{S_\infty}\le\sqrt m\|D\|_{S_\infty}\), then interpolate with exponent \(1-2/p\). The family \(A_k=e_1e_k^*\) independently gives exact best constants for every \(p\ge2\).

The included `verify_commuting_moduli.py` is an optional deterministic check requiring NumPy. It checks randomly generated jointly diagonal moduli and verifies the explicit extremal family. It is finite numerical stress-testing, not an exhaustive certificate and not a proof of the all-dimensional result. No independent external audit has been performed.
