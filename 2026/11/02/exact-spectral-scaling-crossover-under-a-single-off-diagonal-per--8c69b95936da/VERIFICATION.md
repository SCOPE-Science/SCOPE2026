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

# Reproducible checks

Execute `python3 verify.py` using the Python standard library. In the reviewed environment the program returned:

```
PASS: 255 exact-fraction identities and 4032 independent numerical comparisons
```

The exact checks verify the two-dimensional block's trace and determinant, the proposed minimizing scales, the condition-number values at three rational sample couplings, and equality of both branches at many rational critical parameters. The floating-point comparisons independently evaluate the two roots of the coupled block and compare the proposed optimum to 4,032 alternative scales over several SPD parameter sets. They are diagnostics, not an exhaustive certification of all real parameters.

The proof in `RESULT.md`, not finite enumeration, establishes positivity, monotonicity, the unique global optimizer, and the limiting expansion. The assumptions \(a>b>c>0\) and \(0<t<\sqrt{2ab}\) are essential; the uniqueness claim excludes the unperturbed endpoint. The result concerns spectral condition number only, not finite-iteration convergence or an independent audit.
