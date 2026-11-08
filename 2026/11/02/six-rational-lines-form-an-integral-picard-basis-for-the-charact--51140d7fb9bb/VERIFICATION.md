---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Clebsch model sum X_i=sum X_i^3=0 over F2 is a nondegenerate Hermitian cubic after extension to F4. All 27 geometric lines are F4-rational. Its 15 F2-points give Frobenius trace 5 on rank-7 geometric Picard, hence invariant rank 6. The six specified binary isotropic spans form rational lines with Gram determinant -2. Since an integral full-rank sublattice index d satisfies d^2 dividing abs(det) 2, d=1: they integrally generate the arithmetic Picard group; geometric Frobenius has A1 reflection. Independently recomputed six binary line spans, their intersecting/nonintersecting Gram matrix and exact integer determinant -2 without trusting package log. Also checked trace equation 15=1+4+2*5. The full 27-line count and identification require standard cubic/Hermitian geometry, not the finite determinant alone.

## originality

PASS

Best-of-knowledge qualified PASS: Vikulova arXiv:2312.17032 develops this characteristic-two symmetric cubic and Frobenius conjugacy class A1; trace, 15 lines and reflection type are already covered. McKean arXiv:2101.08217 classifies possible rational-line counts on smooth cubic surfaces rather than explicitly proving these particular six line divisor classes form an integral basis. Kadyrsizova et al. arXiv:2007.12018 includes characteristic-two cubic-surface geometry; no matching selected Gram matrix basis found in sections inspected. Exact claimed additions have not been shown covered by the inspected published results; residual priority risks remain explicit.

## value

PASS

Explicit integral divisor basis, not just rational-point or rational-line count, for a marked arithmetic cubic surface. It supplies a concrete saturated lattice presentation useful for Galois actions and divisor computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
