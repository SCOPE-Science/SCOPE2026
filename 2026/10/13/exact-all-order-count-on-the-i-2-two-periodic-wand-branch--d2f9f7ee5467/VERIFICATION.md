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

The proof was checked from the source reduction
\[
z=h(t),\qquad t=h(z),\qquad h(x)=\frac{\lambda}{2^k}(1+x^{-1})^k.
\]
For a nontrivial solution, setting \(x=z^{1/k}\), \(y=t^{1/k}\), and \(r=x/y>1\) gives, reversibly,
\[
z=\sum_{j=1}^{k-1}r^j,\qquad t=\sum_{j=1}^{k-1}r^{-j},
\]
and
\[
\lambda=2^k\frac{r(r^{k-1}-1)^{k+1}}{(r-1)(r^k-1)^k}.
\]
The substitution \(r=e^{2s}\) gives the hyperbolic formula in the finding.

For fixed \(s>0\), the function \(H_s(u)=u\coth(us)\) has
\[
H_s''(u)=2s\operatorname{csch}^2(us)(us\coth(us)-1)>0.
\]
Thus its integer increments are strictly increasing, which makes the derivative of \(\log\lambda(s)\) strictly negative for every integer \(k\ge2\). This is the all-order uniqueness certificate; no finite enumeration is used to establish it.

The accompanying `verify.py` performs exact rational substitution tests for many finite \(k,r\) pairs, checks the special source thresholds at \(k=2,3\), samples monotonicity, and checks the leading merger coefficient. Those checks are corroborative only.

The scope is \(I_2\) only. The verification does not assert completeness of the source's full four-variable periodic system, and it does not assess extremality of the resulting periodic measures.
