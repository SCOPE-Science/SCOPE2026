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

The proof was checked from the definitions of the snowflaked metric and Hausdorff dimension.

1. Point separation: for every distinct pair in the connected set, a continuous scalar functional separates the pair; in the complex case a rotated real part gives a real scalar functional.
2. Hölder exponent: continuity gives \(|f(x)-f(y)|\le C\|x-y\|_X=C d_p(x,y)^{1/p}\).
3. Dimension transfer: a direct cover calculation gives \(\dim_H f(E)\le p\dim_H E\) for this exponent.
4. Connected image: the scalar image contains a nondegenerate interval, hence has Hausdorff dimension at least \(1\).
5. Sharpness: an affine line segment has metric equal, up to a constant factor, to \(|s-t|^p\), whose Hausdorff dimension is exactly \(1/p\).
6. Boundary case: in \(L_p[0,1]\), \(t\mapsto\mathbf 1_{[0,t]}\) satisfies \(d_p(F(s),F(t))=|s-t|\), giving an exact dimension-one connected subset.

No numerical computation, finite enumeration, or external certificate is needed. No claim is made about all equality cases or other fractal dimensions.
