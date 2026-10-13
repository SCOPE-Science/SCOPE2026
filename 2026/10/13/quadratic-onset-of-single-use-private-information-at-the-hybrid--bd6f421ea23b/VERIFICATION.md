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

The proof is analytic. The following checks were performed against the displayed formulas:

1. The function \(F(a)=(1-a^2)\operatorname{atanh}(a)-a^3\) has a unique positive zero because \(F''(a)<0\) on \((0,1)\), \(F'(0)=1\), and \(F(a)\to-1\) as \(a\to1^-\).
2. At \(z=0\), direct substitution into the source curvature formula gives \(\Delta_p''(0)=F(a)/a\).
3. Differentiating that curvature formula with respect to \(t=z^2\) and using the threshold relation gives
\[
\Delta_{p_*}^{(4)}(0)=
\frac{3-6a_*^2+3a_*^4-2a_*^6}{a_*^2}.
\]
4. The local stationary equation gives \(z_p^2=6c_*(p_*-p)/B_*+o(p_*-p)\), and substitution into the fourth-order Taylor expansion gives \(C^{(1)}(p)=3c_*^2(p_*-p)^2/(2B_*)+o((p_*-p)^2)\).
5. The embedded checker uses only the Python standard library. It bisects the threshold root, evaluates the two exact coefficients, and directly evaluates the entropy difference at several small positive deficits. Those finite evaluations corroborate, but do not prove, the asymptotic statement.

The numerical root and coefficient values are reported only as decimal evaluations of exact formulas. No exhaustive search, timeout, or finite sample is treated as a proof of the asymptotic claim.
