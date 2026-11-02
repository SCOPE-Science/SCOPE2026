# Self-review

## Correctness — PASS

The stochastic reduction, state-resolved beta law and Gaussian-noise convolution are derived with the rates and physical normalization stated. The proof verifies the posterior sign by a strict positive integral for arbitrary symmetric strictly decreasing coordinate-noise kernels, then shows the four-state MAP decision factorizes into two independent signs. It derives the exact Gaussian Bayes accuracy and the gamma-value at zero noise, proves strict monotonicity by stochastic ordering, and proves the two fast-switching limits through exact beta moments and a uniform-integrability CLT. Boundary decisions occur on null sets. The standalone checker provides independent symbolic, quadrature, angular, asymptotic and Monte Carlo diagnostics; it is not substituted for the proof.

## Originality — PASS, with priority risks

The strongest overlap is Smith et al. (arXiv:2207.10445), whose full text has the same planar four-heading system, rotated independence, and noise-extended position solution, including an appendix on state-resolved equations. The one-dimensional athermal conditional law is independently explicit in Sun et al. (arXiv:2610.24961); Frydel (arXiv:2207.08695) supplies beta–Gaussian position convolution, and Garcia-Millan/Pruessner (arXiv:2012.02900) give thermal state observables. The assessed contribution excludes these known inputs. It is the exact four-way MAP classifier robust to a whole family of observation kernels, a score-only reconstruction formula, and a sharp noise/tumbling crossover with global ordering. Accessible prior research summaries concern radial densities and unrelated orientation processes, not these inference theorems. Related published formulas may imply parts of the classification and publication-priority verification remains incomplete; no broad independence is claimed.

## Mathematical value — PASS

The hidden-heading inference question is natural in single-frame imaging of active particles. The sector invariance shows that multimodal and strongly temperature-dependent position distributions do not alter the optimal directional partition, while the exact success probability quantifies the cost of noise and tumbling. The singular crossover gives a precise design criterion for when thermal blurring changes the scaling of inferable propulsion information. The result is a structural exact classification plus a nontrivial limiting law, not a new parametrization of a known positional density.

## Limitations and closest literature

The theorem is restricted to an isotropic harmonic trap with four orthogonal headings undergoing unbiased quarter-turns, stationary sampling and independent coordinate noise. The accuracy formula requires Gaussian noise and assumes one frame rather than a path. The 2022 source gives exact propagators from which state inference may be derivable; the 2026 state-conditioned 1D result also limits originality claims. Independent external audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
