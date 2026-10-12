# Scientific review

## Correctness — PASS
The homogeneous heavy-ball quadratic is Schur-stable throughout \(0<t<2\), \(0\le\beta<1\); the independent autoregressive noise has a stable companion mode for \(0\le r<1\). Stationary moment equations lead to the explicit variance identity and the completely signed rational difference. Every denominator is positive in the stated domain. The quadratic comparison has nonnegative leading coefficient, negative linear coefficient and a strictly negative right-endpoint value, which proves the unique crossover and its exact strict/equality boundaries. The threshold polynomial has one increasing zero, and differentiating it proves the correlation dependence. An independent six-moment exact-rational checker agrees in 270 test cases and two contrasting examples. It is auxiliary and does not replace the general algebraic argument.

## Originality — PASS, narrowly scoped
The exact white-noise stationary variance is covered by Liu, Ziyin and Ueda, arXiv:2012.03636; no novelty is asserted for that slice. Kühn and Rosenow, arXiv:2306.05300, give a broad covariance representation and explicit analyses for the different finite-range **negative** epoch-induced noise covariance. The representation permits specialization but does not itself classify when positive momentum reduces variance under persistent autoregressive noise, the unique crossover, or the moving threshold. Gadat, Panloup and Saadane, arXiv:1609.04228, and Dang, Babanezhad and Vaswani, arXiv:2401.06738, do not give an implication-equivalent stationary comparison. Targeted primary-literature and mathematical finding-index searches did not locate it. General filtering/linear-system results could conceal an algebraically equivalent classification: this remains a substantive residual originality risk, not an independence claim.

## Value — PASS
Colored minibatch noise and momentum each create temporal memory, so whether momentum **helps** stationary risk is a natural hyperparameter choice rather than an arbitrary numerical statistic. The exact frontier \(\tau(r)\) rising from \(1\) to \(\sqrt2\), and the exhaustive strict-improvement interval ending at a unique \(\beta_c\), distinguish conditions under which momentum improves rather than worsens stationary error. A single fixed setting even reverses sign as noise correlation changes, providing a clear consequence not explained by merely rescaling variance.

## Closest sources and limitations
The known white-noise covariance and general temporal-covariance response formulas are explicitly acknowledged; neither finite testing nor absence from a database proves global novelty. This is a one-dimensional fixed-parameter additive-noise classification, not a statement about convergence acceleration, nonlinear learning systems, or minibatch laws in general. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
