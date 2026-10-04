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
`verify.py` uses only Python's standard library and exact rational sparse-polynomial arithmetic. It reconstructs the Lie derivatives of \(x\), \(y\), \(z\), \(x^3/3\), \(yz\), and \(xy\), including the identities needed for \(\mathbb E[x^2]=2c^2\) and \(\mathbb E[z^2]=\mathbb E[y^2]\). It also checks that the \(\sin^2 t\) coefficient in the harmonic equality-case residual is nonzero.

The recorded output is `VERIFY_OK`. The standard Wirtinger inequality and its equality characterization are analytic inputs; literature originality and measure invariance are not machine-certified.
