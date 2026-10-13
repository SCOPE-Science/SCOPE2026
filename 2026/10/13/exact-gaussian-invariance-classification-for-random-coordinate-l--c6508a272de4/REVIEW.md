# Scientific review: exact Gaussian-invariance classification for coordinate Langevin Euler

## Correctness — PASS

The theorem concerns the precise coordinate-only-noise Euler transition of Ding–Li–Lu–Wright [1]. Every hypothesis is explicit: real SPD precision, strictly positive iid coordinate probabilities, base timestep \(h>0\), independent Gaussian noise, and graph components formed by nonzero precision off-diagonals. The necessary direction follows from invariance of the first moment, rigidity of a centered Gaussian mixture under fourth moments, the coordinate off-diagonal covariance equations, and symmetry of \(H^{-1}D\). The resulting graph-component temperatures and **strict** stability boundary then follow by exact diagonal covariance balancing. Sufficiency checks preservation of the full Gaussian conditional distributions by **each** selected-coordinate kernel. The synchronous coupling energy decrement supplies uniqueness under strict coordinatewise stability, including the non-Gaussian alternatives. The KL and Wasserstein identities are standard commuting-Gaussian formulas. An exact-arithmetic executable independently checks finite rational instances, but the all-dimension assertion relies on the stated proof, not those tests.

Risk/limit: no statement is made for nonpositive-definite precision, arbitrary switching, altered noise, or a nonquadratic target. The threshold is strict. The separate stronger stability assumption is applied only when asserting existence and uniqueness of a non-Gaussian invariant.

## Originality — PASS, with remaining priority risk

The motivating source [1, arXiv:2010.01405v1, §§2–4, Appendix] specifies the same transition, recommends directional-Lipschitz probabilities, proves quantitative convergence/error bounds, and examines Gaussian examples. It does **not**, in the inspected full text, state the componentwise necessary-and-sufficient characterization of a stationary **Gaussian law**, the exact connected-graph temperature, or the non-Gaussian stationary-law complement. In particular, a finite-time Wasserstein error bound does not imply that an invariant law is Gaussian; the fact that the diagonal-proportional weights were recommended for numerical complexity does not imply the present invariance classification.

Ding–Li [2, arXiv:2007.14209, §§2–3] updates a randomly estimated gradient but adds **full-dimensional** noise, so no implication follows for the coordinate-only-noise transition. Ding et al. [3, arXiv:2010.11366] treat an underdamped model. The materially read full texts of the closest published numerical results listed below concern (a) one-dimensional underdamped randomized intermediate times and covariance expansions and (b) deterministic coordinate-minimization sampling optimization; neither has this transition kernel or law classification. Equivalent formulations involving random-scan Gaussian autoregressions, Gaussian-mixture rigidity, matrix covariance Lyapunov equations, and exact conditional Gibbs samplers were searched and compared. Gaussian-mixture moment rigidity and single-coordinate autoregression identities themselves are not claimed as new.

Residual risk: broader discrete random-scan linear stochastic process and conditional-MCMC literature may contain an equivalent classification under another name. A negative search is not proof of worldwide novelty, and priority has not been independently certified.

## Value — PASS

The Gaussian target is a standard calibration case for unadjusted coordinate Langevin Monte Carlo. The original method proposes diagonal-Lipschitz sampling to manage computational complexity; this theorem establishes a different, exact structural reason for that choice: it is **precisely** the unique Gaussian-preserving choice on connected precision graphs, and the resulting invariant is a known temperature-scaled target. Alternate stable probabilities do not merely change variance but change the form of the invariant law. The componentwise classification is a motivated complete invariant-law criterion; exact KL and transport biases make the benchmark operational. This is not offered as a general-purpose optimal sampling theorem or a claim about nonlinear targets.

All three axes were reassessed for this one final claim, including the connected-case specialization and the full disconnected-component theorem. No external validation was carried out.

## Inspected source comparisons

[1] Z. Ding, Q. Li, J. Lu, S. J. Wright, *Random Coordinate Langevin Monte Carlo*, arXiv:2010.01405v1, first public 2020-10-03, https://arxiv.org/html/2010.01405v1 . Full HTML read, specifically algorithm, convergence theorems, Gaussian example, and appendices.

[2] Z. Ding, Q. Li, *Langevin Monte Carlo: random coordinate descent and variance reduction*, arXiv:2007.14209, https://arxiv.org/abs/2007.14209 . Full open-access text inspected for distinct whole-vector noise update.

[3] Z. Ding, Q. Li, J. Lu, S. J. Wright, *Random Coordinate Underdamped Langevin Monte Carlo*, arXiv:2010.11366, https://arxiv.org/abs/2010.11366 . Model/abstract compared; underdamped dynamics rather than the present overdamped Euler kernel.

[4] *Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-harmonic-equilibrium-bias-low-cost-randomized-ulmc--160d754f339b . Complete RESULT.md inspected: a one-dimensional underdamped random-intermediate-time family, not random-coordinate overdamped Euler.

[5] *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995 . Complete RESULT.md inspected: deterministic coordinate minimization and rate-optimal probabilities, not invariant laws of noisy Euler coordinate samplers.

Self-review: passed. Independent audit: not yet performed.
