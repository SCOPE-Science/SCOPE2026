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
The theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Critical checks:
- the source vertex formula specializes to coordinate coefficients \(Mi+N(\tau_{i-1}-\tau_i)\);
- the affine centroid is \(M(d+2)\mathbf1/2\);
- the centered \(MN\) cross term telescopes to \(MN\,d(d+1)\);
- the remaining squared-radius fluctuation is exactly \(N^2\mathcal E(\tau)\);
- \(\mathbb E\mathcal E=(d+1)^2(d+2)/6\);
- splitting the square of the adjacent-product sum into identical, one-overlap, and disjoint pairs yields
\[
\operatorname{Var}(\mathcal E)
=
\frac{(d-2)(d+1)^2(d+2)(5d+11)}{180};
\]
- coordinate-permutation symmetry and zero coordinate sum force the covariance to be a scalar multiple of \(I-J/(d+1)\), with scalar fixed by the trace.

`verify.py` exhaustively enumerates all inner permutations for \(2\le d\le9\) and checks the exact rational mean and variance formulas. It also verifies the vertexwise radius identity on representative rational parameter pairs and the dimension-two cosphericity transition. It does not replace the arbitrary-dimensional proof or assess originality.
