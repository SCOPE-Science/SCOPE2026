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

The packaged `verify.py` uses only Python's standard library and exact rational arithmetic. It checks the following finite algebraic certificates: the identity for \(G(\tau(T))\), the projective matrix relation \(M^3=512I\), the two entry-renormalization identities modulo \(G\), the monic integral equation for \(z\), the power-basis discriminant \((128\cdot91)^2\), and the Eisenstein coefficient tests at \(7\) and \(13\).

The script does not numerically certify the general local-number-theory statements used after the Eisenstein tests. Those proof steps use the standard implications “Eisenstein of degree \(3\) gives total ramification” and “for tame total ramification of degree \(3\), the discriminant exponent is \(2\).”

Expected output:

`VERIFY_OK mobius_order=3 root_cycle=exact entry_cycle=a->c->b field_discriminant=8281 eisenstein=7,13`
