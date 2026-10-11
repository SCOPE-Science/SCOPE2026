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

# Certificate and reproducibility

From a directory containing `certify_nine_vertex.py`, run:

```bash
python3 certify_nine_vertex.py
```

No third-party packages or downloaded files are necessary. Under ordinary Python 3, the checker prints `VERIFY_OK`. It reconstructs all nine algebraic unit vectors, fourteen outward facets, all twenty-one edges, and the constrained \(18\times18\) volume Hessian from the oriented determinant formula. The program encloses \(\sqrt3\) and \(\sqrt{2\sqrt3-3}\) by rigorous scaled integer-square-root bounds with scale \(10^{18}\), computes the rotational projection using its exact diagonal Gram identity, and certifies positivity of

\[
-\mathcal H+P-\frac{39}{100}I_{18}.
\]

It uses outward-rounded interval additions, products, quotients and a rational interval \(LDL^{\mathsf T}\) factorization, verifying each pivot is strictly positive (in fact each pivot exceeds \(0.05575\)). Strict facet half-space margins are certified above \(0.5476\). The exact stationary condition also follows from the cited global-maximality theorem and direct trigonometric-algebraic cancellation; the checker independently displays a high-precision tangent-gradient residual but **does not infer exact zero from that residual**. The exact rotational Gram identity follows by direct symmetry and the unit-sphere relation.

The final quadratic-deficit inequality is an analytic consequence of a negative-definite Hessian transverse to a compact rotation orbit and uniform Taylor expansion. It does not assert an explicit neighborhood radius, global stability, or optimality of the numerical spectral-gap bound. The certificate tests a finite algebraic matrix using exact enclosures; it is not a grid search over deformations.
