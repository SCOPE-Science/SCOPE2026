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

The proof is analytic. The source formula is first rewritten in Bernstein form, after which differentiation yields the exact coefficient differences. Their one-sign-change property is proved from the monotonicity of the binomial row; Descartes' rule then gives the unique positive derivative zero. This handles all integer dimensions \(n\ge2\) and orders \(p\ge1\).

The bundled `verify.py` is an auxiliary replay check, not a substitute for the proof. It checks representative binomial-difference patterns, the exact planar derivative coefficients, the planar critical-point equation, the simplified maximum, and the limiting constants. It was executed from the packaged artifact directory and returned `VERIFY_OK`.

No exhaustive finite computation is used to justify an infinite assertion. The low-dimensional all-body corollary depends only on the pointwise theorem in the cited source; no all-body claim is made in dimensions where that comparison remains open.
