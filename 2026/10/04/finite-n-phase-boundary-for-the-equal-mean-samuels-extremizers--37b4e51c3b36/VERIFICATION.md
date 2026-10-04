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

The proof was checked symbolically at the level needed by the claim.

For
\[
F_n(\delta)=\log\frac{\delta}{1+\delta}-n\log\frac{n+\delta-1}{n+\delta},
\]
direct differentiation gives
\[
F_n'(\delta)=\frac1{\delta(1+\delta)}-\frac n{(n+\delta-1)(n+\delta)}.
\]
Clearing positive denominators yields exactly
\[
(n-1)(n+\delta-\delta^2).
\]
This confirms the single-hump derivative structure used for uniqueness. The signs \(F_n(0+)=-\infty\), \(F_n(1)>0\), and \(F_n(\delta)\to0^+\) as \(\delta\to\infty\) then establish one and only one positive crossing.

The expansion
\[
n\log\left(1-\frac1{n+\delta}\right)
=-1+\frac{\delta-1/2}{n}+\frac{-\delta^2+\delta-1/3}{n^2}+O(n^{-3})
\]
was independently re-expanded from the power series of \(\log(1-u)\). Substitution into the root equation and Taylor expansion of \(\log(\delta/(1+\delta))+1\) at \(\delta=1/(e-1)\) gives
\[
\frac{e(3-e)}{2(e-1)^3}
\]
as the \(1/n\) coefficient.

Numerical roots for several \(n\) were used only as consistency checks. No finite computation is used to infer uniqueness, asymptotic validity, or novelty.
