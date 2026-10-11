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

For fixed \(0\le t\le1\), convexity reduces
\[
N(u+tv)^p+N(u-tv)^p
\]
over \(B_X\times B_X\) to vertex pairs. The possible norm pairs are exactly
\[
(1+t,1-t),\quad(1+t,1),\quad(1,1+t),\quad(1-t,1+t),
\]
so the exact fixed-scale maximum is \(1+(1+t)^p\).

Thus
\[
C_{\mathrm{NJ}}^{(p)}(X)
=
\max_{0\le t\le1}
\frac{1+(1+t)^p}{2^{p-1}(1+t^p)}.
\]
For \(p>1\), the derivative has the sign of
\[
H(t)=t^{1-p}-(1+t)^{1-p}-1.
\]
This function is strictly decreasing, tends to \(+\infty\) at \(0+\), and is negative at \(1\), hence has one zero \(\tau_p\). The critical equation gives
\[
C_{\mathrm{NJ}}^{(p)}(X)=
\left(\frac{1+\tau_p}{2\tau_p}\right)^{p-1}.
\]
For \(p=2\), \(\tau_2=(\sqrt5-1)/2\) and the value is \((3+\sqrt5)/4\), matching the known classical endpoint. No numerical sampling or external certificate is used.
