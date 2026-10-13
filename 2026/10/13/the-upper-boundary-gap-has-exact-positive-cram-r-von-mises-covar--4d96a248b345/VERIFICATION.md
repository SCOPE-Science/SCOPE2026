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

The proof is analytic. Conditional on \(M_n=m\), the lower order statistics are exactly \(m\) times the order statistics of \(n-1\) iid uniforms, so their first moments and the unordered quadratic sum give the conditional Cramér–von Mises regression directly. The covariance then uses only \(\mathbb E[M_n^k]=n/(n+k)\) for \(k=1,2,3\).

The standalone `verify.py` uses exact rational arithmetic to replay the conditional formula on 1,501 finite \((n,m)\) pairs and the covariance for all \(2\le n\le80\). It separately reconstructs the variance of \(W_n^2\) from the empirical-process kernel
\[
h(x,y)=\frac13+\frac{x^2+y^2}{2}-\max(x,y),
\]
using exact polynomial integration over the unit interval and triangle. It confirms
\[
\operatorname{Var}(h(U,U))=\frac1{180},
\qquad
\mathbb E[h(U,V)^2]=\frac1{90},
\]
and therefore \(\operatorname{Var}(W_n^2)=(4n-3)/(180n)\). It also verifies the exact correlation and \(\mathbb E[W_n^2]=1/6\).

Successful replay prints:

`VERIFY_OK conditional=1501 covariance=79 kernel=79 mean=199`

Finite checks are not used as evidence for an infinite parameter range; the displayed conditioning and kernel arguments prove the quantified statements.
