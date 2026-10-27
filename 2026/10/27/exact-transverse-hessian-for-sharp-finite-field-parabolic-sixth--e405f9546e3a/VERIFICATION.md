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

The mathematical proof derives every asserted coefficient from finite-field character sums and the two-transitive affine action, requiring \(p>3\). The executable checker `verify_parabolic_hessian.py` uses only standard Python and verifies the triple-fiber identity and both perturbation identities over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13},\mathbb F_{25}\). The analytic proof, not the finite tests, supplies the theorem for all prime powers of characteristic greater than three.

Direct complex Fourier evaluation at \(q=5,7\) corroborated the second variation separately in real and imaginary mean-zero directions. The sharp constant \(1+q^{-1}-q^{-2}\) is sourced from the cited 2024 paper; the exact Hessian is calculated here. No uniform-in-\(q\) remainder, independent audit, or external validation is claimed.
