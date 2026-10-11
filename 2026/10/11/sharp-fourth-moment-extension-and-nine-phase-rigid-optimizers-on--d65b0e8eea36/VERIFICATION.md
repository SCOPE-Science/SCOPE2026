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

Run `python3 artifacts/verify.py` using only the Python standard library. The script directly reconstructs the five support points, all convolution entries on \(\mathbb F_3^2\), and the nine normalized Fourier values. It independently checks convolution–Fourier fourth-moment equality on 2,000 deterministic complex-valued test inputs, verifies the claimed fourth-moment bound on those inputs, evaluates all nine optimizer phase classes, and confirms the radical coefficient by direct substitution. The recorded run prints `VERIFY_OK`.

Proof-level checks independent of the finite test include character orthogonality with the precise factor \(1/9\), the nonnegative pair-sum table, the signs of the pair-balancing derivatives, the at-most-endpoint nature of two-axis mass optimization, the order-three Young bound, the exact factor \(-16(r+1)(2r^2+r-4)/(r^2+4)^3\), and the cubic-root phase relations. The text proof covers all complex functions on the specified five-point surface. Random tests are not a substitute for it. No statement concerning larger finite fields, independent validation, or unindexed prior literature has been verified here.
