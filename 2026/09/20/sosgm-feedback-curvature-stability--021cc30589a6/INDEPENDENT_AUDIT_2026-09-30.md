# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/sosgm-feedback-curvature-stability--021cc30589a6`  
Assigned and audited source tree: `fabca7e5eacaed8c2f0c3d7dd5a71aacc44c403e`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `7592eff5472c82bbc044a3d38b623c1cb7e31a88`  
Disposition: **passed**

## Correctness

**independently_supported**. The scalar random-curvature derivations check directly. Independence gives p_ratio=1/E[A] and p_hyp=E[A^{-1}], while one-step mean-square minimization gives p_ms=E[A]/E[A^2], with the stated ordering by Cauchy-Schwarz/Jensen. The ratio support extremum is the sharp Bhatia-Davis coefficient-of-variation bound, yielding kappa<3+2sqrt(2). For hypergradient feedback, the two endpoint chord inequalities are simultaneously sharp and maximizing in the mean gives ((kappa-sqrt(kappa)+1)^2)/kappa; solving equality to 2 reproduces kappa_hyp=3.546455444684995. The equal-two-point null-step acceptance threshold and restored contraction factor also check. Thus the record properly distinguishes instability of the raw population target from the safeguarded published algorithm.

## Originality

**qualified_source_specific_analysis**. Zhang–Gao–Ye–Udell introduce SOSGM/OSGM-SGD, independent out-of-sample feedback, projection to bounded candidate sets, and the null-step safeguard; hypergradient learning-rate adaptation and instability are much older. Current searches did not locate the exact three-target separation, the two sharp support-only thresholds, or the finite-batch logarithmic obstruction. The contribution is therefore a focused population-level stress test of the 2026 feedback definitions, not a new general stochastic-approximation theory.

## Scientific value

**meaningful_algorithmic_diagnostic**. The result explains precisely what the two feedback losses optimize in a transparent stochastic model, quantifies when raw targets cease to be mean-square stable, and shows mathematically why clipping/null-step safeguards can be essential rather than cosmetic.

## Independent checks

- Derived all three population targets from the displayed feedbacks.
- Verified both support extremizers and the hypergradient threshold numerically/algebraically.
- Checked the equal-two-point null-step acceptance and contraction formula.

## Literature and evidence checked

- https://arxiv.org/abs/2609.11751
- https://proceedings.mlr.press/v267/chu25a.html
- https://arxiv.org/abs/1703.04782
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/sosgm-feedback-curvature-stability--021cc30589a6

## Limitations

- One-dimensional common-minimizer quadratic model only.
- Thresholds concern unconstrained raw population minimizers, not the safeguarded full algorithm.
- Older adaptive-filter terminology may hide related moment calculations.
