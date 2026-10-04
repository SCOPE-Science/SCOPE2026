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
`verify.py` uses only Python's standard library and exact rational sparse-polynomial arithmetic. It checks the denominator-cleared affine coboundary identity
\[
aL\!\left(z+bx-\frac{b}{a}y\right)=ax^2+bx,
\]
the equilibrium reduction \(z(a^2z-b)\), and the two canonical equilibria at \(a=1/2\), \(b=1\).

The recorded output is `VERIFY_OK`. The invariant-measure, conditional-expectation, variation-of-constants, and continuity arguments are analytic inputs and are not machine-certified. Literature originality has been reviewed by the same model only; no independent audit has been performed.
