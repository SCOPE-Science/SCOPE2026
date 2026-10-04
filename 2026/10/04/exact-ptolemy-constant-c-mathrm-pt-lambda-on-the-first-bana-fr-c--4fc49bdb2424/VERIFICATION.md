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

The proof was replayed directly from the stated norm.

1. \(N_\lambda(v)=\max\{E(v),F(v)\}\), with \(E\) Euclidean and \(F(v)=\lambda|v_1|\).
2. \(E\) obeys the Euclidean Ptolemy inequality.
3. \(F\) obeys the one-dimensional Ptolemy inequality after projection onto the first coordinate.
4. In either mixed numerator case, \(F(v)\le\lambda E(v)\), so the Ptolemy ratio is at most \(\lambda\).
5. For \(x=(1/2,1/2)\), \(y=(1/2,-1/2)\), and \(z=(1,0)\), the numerator equals \(\lambda\), while each of the two denominator products equals \(1/2\) when \(1<\lambda\le\sqrt2\). Hence the ratio is \(\lambda\).

The literature-normalization check was also recomputed. Under \((u,v)=(\lambda x_1,x_2)\), the associated absolute normalized function is
\[
\psi_\lambda(t)=\max\left\{1-t,\sqrt{(1-t)^2/\lambda^2+t^2}\right\}.
\]
At the branch-transition point its squared Euclidean comparison ratio is \(2-\lambda^{-2}\), which exceeds the midpoint value \(2\lambda^2/(\lambda^2+1)\) by
\[
\frac{\lambda^2-1}{\lambda^2(\lambda^2+1)}>0.
\]
Thus the inspected midpoint-based exact criteria do not subsume the result.

No finite experiment is used as evidence for the infinite claim. The only unresolved item is a literature-access residual, not a proof dependency.
