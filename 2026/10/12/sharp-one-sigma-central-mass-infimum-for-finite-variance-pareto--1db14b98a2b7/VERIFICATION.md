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

The proof is analytic on the complete domain \(a>0\), \(\alpha>2\). Exact Pareto moments give the support reduction \(\mu-\sigma<a\), and exact tail evaluation gives the closed form in `RESULT.md`. The strict global inequality uses only \(\log(1+x)>x/(1+x)\) for positive \(x\) and the identity \((\alpha-1)^2=\alpha(\alpha-2)+1\).

The asymptotic check expands
\[
\log A_\alpha=\frac{2}{\alpha}+\frac{1}{\alpha^2}+\frac{7}{6\alpha^3}+O(\alpha^{-4}),
\]
which yields the displayed first and second corrections after exponentiation.

`verify.py` provides a supplementary finite regression check at representative shape parameters. Its output is `VERIFY_OK`; no finite computation is used to establish the all-parameter theorem or the limiting infimum.

The literature comparison inspected the full Pareto sections of arXiv:2305.02114 and arXiv:2401.09998, plus the open Gamma one-sigma result. The residual originality risk is an equivalent elementary calculation under different terminology.
