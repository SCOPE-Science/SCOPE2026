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

The universal claim is proved analytically in `RESULT.md`. The decisive exact steps are:

1. phase reduction to \(A+Bz+Cw+D e^{i\phi}zw\) with nonnegative moduli;
2. exact maximization over \(w\);
3. evaluation at \(z_\pm=\pm e^{-i\phi/2}\);
4. the triangle inequality \(X_+Y_+ + X_-Y_-\ge2(AC+BD)\);
5. the identity
\[
2(A^2+B^2+C^2+D^2)+4(AC+BD)
=(A+B+C+D)^2+(A-B+C-D)^2;
\]
6. the sharp witness \(1+z+w-zw\), whose norm is \(2\sqrt2\).

`artifacts/verify.py` checks the two-sample inequality on deterministic pseudorandom complex-phase data and verifies the sharp witness. The finite computation is only a consistency check and does not certify the infinite theorem.

Unproved limits: no complete equality-case classification and no extension to arbitrary four-frequency supports is asserted.
