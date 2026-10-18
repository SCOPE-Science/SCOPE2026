# Scientific review: sharp transverse damping of resonant coexistence

## Correctness — PASS

The stated assumptions make every equilibrium coordinate and the three environmental variances strictly interior, so all sign arguments are legitimate. The environmental equations determine the exact equilibrium segment; the five-dimensional Jacobian has one simple tangent zero and a quartic whose Hurwitz determinants factor explicitly. The decisive determinant is proportional to the strictly positive factors times \((x_*-y_*)^2\). At equality, direct quadratic factorization proves one imaginary pair and two decaying directions. The log-odds integral selects the exponentially approached point through normal hyperbolicity. The analytic proof establishes all parameter quantifiers; the exact symbolic/finite computational checks in `verification.py` corroborate, but cannot replace, it.

## Originality — PASS, subject to publication-priority risk

The closest direct source is Betz, Fu, and Masuda (2024), arXiv:2404.17082, whose five-dimensional and appendix discussion treats the source dynamics but does not state the sharp resonant full-interior transverse spectral test. A prior result on resonant conservation and equilibrium continua is acknowledged as background rather than counted as new. Wang, Zheng, and Fu (2019), arXiv:1906.07161, develop manifold attraction in a distinct low-dimensional public-goods feedback model, and Tilman et al. (2020) treat broader two-variable feedback behavior; neither provides the five-variable determinant-square criterion for the present model. Published related claims with equilibrium segments, two-community phenomena, and oscillations were compared by mathematical implication rather than by matching titles. No direct covering result was identified. Broader unpublished or overlooked spectral theory could still subsume the classification.

## Value — PASS

The result turns a numerical/general five-dimensional coexistence problem into an all-parameter classification of four transverse eigenvalues, with a sharp symmetry boundary: environmental response *heterogeneity* supplies strict damping while perfect equality leaves an undamped oscillatory mode. It identifies when balanced encounter mixing supports local convergence to a coexistence family and specifies the destination using an invariant. This is a structural, parameter-uniform ecological-game statement, not a recomputed stability sample or relabeling.

## Limits and closest literature

Only a resonant, frequency-dependent affine-payoff and balanced-mixing slice is covered; no global basin, boundary-equilibrium classification, or nonlinear conclusion in the undamped case follows. The relevant first public source date is April 25, 2024. Closest literature: Betz, Fu and Masuda, arXiv:2404.17082; Wang, Zheng and Fu, arXiv:1906.07161; Tilman et al., Nature Communications 2020. Independent scientific and priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
