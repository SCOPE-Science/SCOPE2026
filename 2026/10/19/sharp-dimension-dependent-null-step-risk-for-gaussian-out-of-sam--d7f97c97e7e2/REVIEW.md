# Scientific review

## Correctness

**PASS.** For independent isotropic Gaussian training and evaluation gradients, the normalized hypergradient at zero preconditioner equals a Gaussian projection divided by a chi-square radius, giving the exact Student-ratio law and the one-half zero atom. The second independent noisy objective comparison gives acceptance probability \(\overline\Phi(p\sqrt U/2)\); the size-bias identity \(\mathbb E[U_d q(U_d)]=d\mathbb E[q(U_{d+2})]\) proves the exact accepted risk. The clipped Cauchy boundary-layer integral, the logarithmic \(d=2\) split, and dominated convergence for \(d\ge3\) rigorously establish all three sharp coefficients. The positive cap \(M\), positive learning rate \(\eta\), dimension \(d\ge1\), minibatch \(b\ge1\), and tie convention were explicitly assessed. The standalone `check.py` passed 70 analytical and seeded independent-replay test families. The proof, not finite tests, establishes all universal claims.

## Originality

**PASS, qualified by residual search risk.** Zhang, Gao, Ye, and Udell's stochastic online scaling paper introduces independent-validation hypergradient feedback and null-step acceptance, but its relative-gradient-noise guarantees cannot cover the additive Gaussian model at the optimum. Gao, Chu, Ye, and Udell's original deterministic online scaling work does not entail this noisy acceptance calculation. Classical Cauchy/Student-t ratios and inverse chi-square moments are prior art and are not claimed as new. The closest identified indexed mathematical comparison analyzes scalar *random curvature* and population-scale stability, rather than dimension-dependent accepted risk with *additive Gaussian noise*. No full equivalent was found in the inspected relevant primary sections or searched record indexes. The search is not a uniqueness proof; specialized probabilistic or algorithm-specific prior work remains possible.

## Mathematical value

**PASS.** The result exposes a precise noninterpolation regime in which increasing gradient minibatch size scales the primal risk by \(1/b\) without making the learned scalar step any less heavy-tailed. The sharp \(\eta\), \(\eta^2\log(1/\eta)\), \(\eta^2\) phase distinction and the change from \(d\) to \(d+2\) in the validation-acceptance tail give useful, directly reproducible diagnostic constants for two-update algorithm analysis. The null step is genuinely accounted for rather than omitted.

## Scope and residual limitations

Exact, two-step, isotropic Gaussian, fresh independent training/evaluation expectation oracle initialized at the population minimizer with zero initial scaling. The paper's relative-noise conditions are violated; no global convergence, performance, stationary-tail or finite-dataset claim is made. Earlier specialized Student-ratio treatments remain possible; the relevant primary source sections were read in full, while the general heavy-tail SGD work was examined through its abstract only.

Self-review: passed. Independent audit: not yet performed.
