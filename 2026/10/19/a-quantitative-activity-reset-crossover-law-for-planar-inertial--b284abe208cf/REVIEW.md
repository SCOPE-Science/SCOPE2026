# Self-review

## Correctness — PASS

The full-state regeneration age is exactly exponential and independent of the between-reset Brownian noises. The stochastic convolution (2) follows from the linear velocity equation with zero velocity at reset. Brownian scaling produces the exact coupled law (3). The pointwise kernel and angular inequalities (4), conditional \(L^2\) triangle inequality, and planar Itô isometry reproduce all four coefficients in bound (1); the active-orientation coefficient uses the integral \(\int_0^s(s-z)\sqrt z\,dz=4s^{5/2}/15\), and the exponential fifth and sixth moments. Conditional Gaussianity gives both the characteristic function and density; factorial moments give anisotropic second/third moments. Uniform polynomial-moment control yields convergence beyond \(W_2\). Above the crossover, division by \(\alpha_r\) gives a nonzero one-dimensional limit. The packaged finite checker corroborates published finite moments and the asymptotic formulas, but finite tests alone do not establish the theorem.

## Originality — PASS, with residual risks

The primary 2026 paper is inspected in full (model, complete-reset setting, stationary second/fourth moments, transient results and appendices) and credited for those results. It does not state the joint \(\mathrm{Pe}_r\sim\sqrt r\) limit with a complete anisotropic planar distribution and an explicit Wasserstein error. The passive underdamped, random-acceleration and overdamped active-reset studies share modeling ideas but do not provide the same inertial active joint-scaling conclusion in accessible material. Search of indexed published research and related published statements did not yield an equivalent statement; this is **not** proof of global uniqueness. A broader general stochastic-convolution/renewal theorem might imply the result. Full text of two older preprints could not be accessed; their abstracts and available citations were compared. No independent originality audit has occurred.

## Value — PASS

The source identifies inertial high-reset localization by finite moments, yet fixed activity hides when self-propulsion survives on the fluctuation scale. The new joint scaling resolves the physically natural strength threshold and describes an entire non-Gaussian anisotropic distribution rather than one further moment or a routine finite-parameter special case. The explicit \(W_2\) rate permits quantitative use of that limit and separates three experimentally interpretable regimes. The transverse/longitudinal variance and mixed third moment show precisely why a variance-matched Gaussian fails.

## Scope and closest literature

Patel and Shee (2026), arXiv:2602.21134, supply the dynamics and finite moment formulas, but not the stated joint law/error; Franke and Sokolov (2026) treat passive underdamped resetting; Singh (2020) concerns passive random acceleration, Kumar–Sadekar–Basu (2020) the overdamped active case. The literature comparison leaves open implicit derivability from general renewal-limit results. The theorem requires complete fixed-orientation resets and fixed inertia, not partial or random-angle resetting.

Self-review: passed. Independent audit: not yet performed.
