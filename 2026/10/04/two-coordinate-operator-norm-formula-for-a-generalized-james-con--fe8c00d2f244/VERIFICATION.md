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

The claim is proved without numerical sampling.

For \(1\le p<\infty\), set \(M=\|A_{\lambda,\mu}\|_{\ell_p^2\to\ell_p^2}\). Applying the defining operator-norm inequality to every coordinate pair \((x_i,y_i)\), then summing, gives
\[
\|\lambda x+\mu y\|_p^p+\|\mu x-\lambda y\|_p^p\le M^p(\|x\|_p^p+\|y\|_p^p).
\]
For \(x,y\) in the unit ball this forces the smaller output norm to be at most \(M\).

A maximizer \((a,b)\) for the finite-dimensional matrix norm exists by compactness. On two distinct coordinates, choose \(x=(a,b)\) and \(y=(b,-a)\). The two transformed vectors have coordinate pairs \((s,-t)\) and \((t,s)\), where \(s=\lambda a+\mu b\) and \(t=\mu a-\lambda b\). Hence both output norms are exactly \(M\), proving the reverse inequality.

At \(p=\infty\), the triangle inequality gives the upper bound \(\lambda+\mu\), and the two-coordinate vectors \((1,1)\) and \((1,-1)\) attain it. Since the matrix is symmetric, standard finite-dimensional duality gives equality of its \(\ell_p^2\) and \(\ell_{p'}^2\) operator norms. Maximum row/column sums give the \(p=1,\infty\) values, and \(A^TA=(\lambda^2+\mu^2)I\) gives the \(p=2\) value.

No finite experiment is used to infer an infinite-dimensional conclusion. The only compactness invoked is the exact attainment of a continuous function on the finite-dimensional scalar unit sphere. The result does not assert a closed elementary expression for the intermediate-\(p\) matrix norm.
