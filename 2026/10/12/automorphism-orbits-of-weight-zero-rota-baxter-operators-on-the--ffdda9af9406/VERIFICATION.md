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

The bundled `verify.py` uses exact symbolic arithmetic from the multiplication table of the real Grassmann algebra. It checks:

- all ordered basis-pair Rota–Baxter identities for the six rank-one representatives;
- all ordered basis-pair identities symbolically for the three rank-two normal-form strata;
- the full six-parameter algebra-automorphism formula and its determinant;
- the residual stabilizer conjugation formulas on the rank-two slice;
- the transformation laws for \(d/a\), \(bc\), and \(\det(M)/a^2\) that separate the three rank-two strata.

The checker terminates with `CHECK_OK`. These computations verify the formulas used in the proof but do not replace its completeness argument over the infinite real field.
