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
The exact upper-bound calculation is
\[
C_{\rm seg}^2\le 1+\frac19+\frac1{1089}+\frac{4^{-37}}3.
\]
It follows from the source estimate \(|\alpha_i^*(x_s)|\le1/s(\beta_i^*)\), together with the forced size data \(s_2\ge3\), \(h_2\ge5\), \(s_3\ge33\), and \(h_3\ge38\). The remaining squared evaluations are bounded by \(\sum_{r=38}^{\infty}4^{-r}=4^{-37}/3\).

For the lower bound, the segment \(\{1,2,4,8,16,32,64\}\) and restricted generators based on \(\{1\}\), \(\{3,4,5\}\), and \(\{64,\ldots,96\}\) give the exact value
\[
C_0=\left(1+\frac19+\frac1{1089}\right)^{1/2}.
\]
The finite checker at `artifacts/verify_segment_bound.py` confirms the heap-tree incomparability relations, the inequalities \(3>2^1\) and \(33>2^5\), and the decimal evaluations. It does not certify the infinite argument; that argument is the geometric-series proof above.

The proved claim does not assert equality of the two endpoints, and it does not extrapolate from finite computation.
