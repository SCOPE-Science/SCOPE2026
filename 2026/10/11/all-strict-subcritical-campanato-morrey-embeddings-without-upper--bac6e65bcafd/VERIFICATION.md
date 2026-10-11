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
# Mathematical verification and reproducibility

The proof derives the volume formula from \(F(t)=2t-t\log t\), with \(F(0)=0\). The identity
\[
\int_a^b\log(b/t)\,dt=(b-a)+a\log(a/b)\in[0,b-a]
\]
proves the ball bounds in the theorem. The comparison of right endpoints \(b_R/b_r\le R/r\) gives the all-centered reverse-growth inequality. The geometric-logarithmic sum for the nested-ball averages converges for each \(0\le\lambda<1\) since its exponential factor has base strictly smaller than \(1\). The endpoint \(\lambda=1\) fails from the explicit formula \(\mu(B(0,r))/r=2-\log r\to\infty\); no experiment is needed for this conclusion.

A reproducible supplementary check is provided as `checks/weight_sanity.py`. With a standard Python 3 installation, `python3 checks/weight_sanity.py` returned `FINITE_SAMPLE_CHECK_OK`; its observed minimal reverse-bound slack exceeded \(3.5\), and its observed doubling ratios were below \(2.8\). These are **finite samples only**; they establish neither global bounds nor exhaustive optimal constants. The mathematical result relies on the displayed analytic inequalities and on Hölder/Minkowski, not on the script.

The bound proved here depends on \(p\) and \(\lambda\). The sharp asymptotic behavior of the optimal embedding constant as \(\lambda\uparrow1\) is not determined. No independent mathematical audit is represented as having occurred.
