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
# Verification record

The universal statement is proved analytically in `RESULT.md`. The included `verify.py` performs finite consistency checks only.

It checks representative admissible pairs \((r,w)\), verifies the width relation
\[
w=r(1+\sqrt3u-c),
\]
recomputes the moved vertex by an independent circle rotation, and confirms the closed formulas for \(a(x)\), \(b(x)\), and \(D(x)\). It checks that the exact area-deficit quotient approaches
\[
L(r,w)=\frac r2\left(2u^2+\frac{\sqrt3u(1-2u^2)}c\right)
\]
for small positive \(x\), and confirms the equivalent sine formula for \(L(r,w)\). It also verifies the endpoint value \(C_{\mathrm{can}}(w,w)=\sqrt3/(2w)\) and numerically approaches the classical limit \(C_{\mathrm{can}}(r,w)\to1/w\) as \(r/w\) grows.

The script does not establish the universal quantifiers, does not certify literature originality, and does not determine the globally optimal Hausdorff stability constant. Those points rest on the analytic proof and the stated literature comparison.
