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

The analytic verification is the reduction
\[
c_p(u)=\frac{1}{
\left(u^{1/(p-1)}+(1-u)^{1/(p-1)}\right)^{(p-1)/p}
\left(u^{p-1}+(1-u)^{p-1}\right)^{1/p}},
\]
followed, for \(p\in\{3,3/2\}\), by
\[
c_p(u)^{-3}=F(w)=(1+2w)(1-2w^2),\qquad w=\sqrt{u(1-u)}\in[0,1/2].
\]
Since \(F'(w)=2-4w-12w^2\), the only interior critical point is \(w_*=(\sqrt7-1)/6\), the derivative changes from positive to negative there, and the endpoints both give \(F=1\). Thus the global maximum is exact and equals \((17+7\sqrt7)/27\).

The standalone script `verify_dragomir_constant.py` uses high-precision decimal arithmetic to check the critical equation, the closed form for \(F(w_*)\), and the final constant. It also performs a dense finite grid comparison as a stress test. The grid does not prove the infinite maximization; that proof is the derivative argument above.

Limits: real two-dimensional \(\ell_p\) only, with exact closed form asserted only for \(p=3\) and \(p=3/2\). No claim is made for complex scalars, higher dimensions, or a general exponent formula. The full texts of two plausible terminology-overlap sources were unavailable in the inspected lawful sources; this is an originality risk, not a correctness limitation.
