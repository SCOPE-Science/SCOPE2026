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

The fixed-dimension source equations were rewritten as the single level relation
\[
H_p(r)=\frac{M_1}{M_2},\qquad
H_p(x)=\frac{\int_{R_1}^{x}s^{-p-1}\,ds}{\int_{x+R}^{R_2}s^{-p-1}\,ds},\qquad p=n-2\ge0.
\]
For \(p=0\), direct integration reproduces the logarithmic two-dimensional equation. For \(p>0\), direct integration reproduces the power-law equation in dimensions \(n\ge3\).

For fixed \(p\), \(H_p\) is strictly increasing in \(x\). For fixed \(x\), differentiating the logarithm gives the upper weighted mean of \(\log s\) minus the lower weighted mean of \(\log s\). Because the two integration intervals are separated by the positive gap \(R\), the derivative is strictly positive. These two strict monotonicities prove the dimension ordering without numerical sampling.

For the asymptotic, setting \(\delta_p=r_{p+2}-R_1\) yields an exact identity whose right side is bounded by \((M_1/M_2)(R_1/(R_1+R))^p\). This first forces \(p\delta_p\to0\). Substitution back into the same identity makes both remaining multiplicative correction factors converge to one and gives the claimed equivalent. The strict condition \(R_1+R<R_2\) is used precisely to make the outer-endpoint factor vanish exponentially.

No conclusion is drawn for the endpoint \(R_1+R=R_2\), for nonradial domains, or before taking the segregation limit.
