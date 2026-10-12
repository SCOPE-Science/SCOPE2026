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
The checker implements the source Gompertz–Lindley survival and density formulas and a positive progressive Type-II competing-risks sample.

It evaluates the likelihood directly from
\[
\prod_i\prod_j\{f_j(t_i)\overline F_{3-j}(t_i)\}^{I(\delta_i=j)}
\{\overline F_1(t_i)\overline F_2(t_i)\}^{R_i},
\]
then evaluates the printed Eq. (3.1) factorization and the expanded Eq. (3.2) kernel separately.

It verifies
\[
\frac{L_{3.1}}{L_{\mathrm{model}}}
=\alpha^{-4R}(1+\alpha)^{-2m}
\]
and verifies that Eq. (3.2) agrees with the direct model likelihood up to a parameter-free constant.

For \(n=30\), \(m=20\), \(R=10\), and \(\alpha=1.1\), it also verifies the missing posterior log-score term and the change in the correction factor between \(\alpha=1.1\) and \(\alpha=2\).
