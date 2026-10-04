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

The proof uses the four-dimensional zonotope identity
\[
|Z(g_1,\ldots,g_m)|=\sum_{|I|=4}|\det(g_i:i\in I)|.
\]
Only one generator is scaled, so for \(s\ge0\) every relevant volume is exactly affine in \(s\). The packaged checker enumerates all maximal minors using integer arithmetic and obtains intercept/slope pairs \((4,10)\), \((12,18)\), \((8,18)\), and \((24,32)\). It then checks coefficientwise that the defect is \(8s-4s^2=4s(2-s)\) and verifies the source point \(s=1\).

The analytic sign classification follows from this exact factorization; no numerical grid or finite sample is used as evidence for all real parameters. The dimensional lift uses only multiplicativity of volume under Cartesian product with the unit cube.

Limit: the verification concerns only the explicitly displayed deformation. It does not classify arbitrary zonotopes or arbitrary simultaneous generator rescalings.
