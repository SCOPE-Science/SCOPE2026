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

The supplied verifier uses exact symbolic arithmetic. It reconstructs the five camera matrices, the line-multiview matrix \(M\), and the four-collinear correction \(F\). It then verifies the two displayed polynomial identities for \(x_5F\) and \(z_5F\) by full expansion.

For the witness \(\ell_i=[0:1:v_i^2]\) for \(i\le4\) and \(\ell_5=[0:1:0]\), it checks that \(M\) has rank \(2\), all forty \(3\times3\) minors vanish, and \(F=-12\). This is an exact radical-nonmembership witness.

The verifier does not prove a complete defining ideal for the mixed arrangement and does not make a saturation claim beyond the immediate localizations on \(D(x_5)\) and \(D(z_5)\).
