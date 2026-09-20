# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The exact kinetic Ornstein--Uhlenbeck transition follows by variation of constants. Itô isometry gives the displayed \(2\times2\) covariance block. Its determinant factors as
\[
\frac{(e^x-1)(xe^x+x-2e^x+2)e^{-2x}}{2\gamma^4},
\qquad x=\gamma h,
\]
and the second factor is positive for \(x>0\) because it and its first derivative vanish at zero while its second derivative is \(xe^x>0\). Thus the one-coordinate covariance has rank two for every \(h>0\), and the \(d\)-coordinate covariance has rank \(2d\).

An affine innovation driven by one \(d\)-dimensional standard normal has covariance rank at most \(d\), whereas two independent \(d\)-normal draws suffice by Cholesky factorization. The quantitative \(W_2\) lower bound follows from the Bures--Wasserstein factor formula and Eckart--Young: among covariance matrices of rank at most \(d\), the spectral rank-\(d\) truncation of \(\Sigma_h\) is optimal, and the squared defect is the sum of the discarded eigenvalues. Since the exact spectrum consists of \(d\) copies each of \(\lambda_+\) and \(\lambda_-\), the optimum is exactly \(d\lambda_-\). The small-step expansion follows from the covariance entries and determinant. The deterministic verification artifact reproduces these identities numerically.

The proof was stress-tested against two possible overclaims. First, a nonlinear measurable map from a lower-dimensional continuous random source need not obey a covariance-rank representation barrier; the theorem therefore explicitly restricts to affine-Gaussian innovations. Second, local transition accuracy does not automatically lower-bound invariant-measure or long-time sampling bias; no such implication is claimed.

## Originality

**PASS, to the best of our knowledge.** Lyu--Wang--Yang (arXiv:2609.20713) explicitly advertise new low-cost underdamped Langevin integrators using one gradient evaluation and two Gaussian draws per iteration. Searches combining the paper title and LC-UBU terminology with exact kinetic-OU covariance, Gaussian-rank, one-/two-Gaussian simulation, Bures--Wasserstein rank approximation, and Wasserstein lower bounds did not locate the theorem stated here.

The ingredients are deliberately excluded from the originality claim. Exact linear Langevin transitions and integrated OU covariance are classical. Gaussian \(W_2\) equals Bures--Wasserstein covariance distance, and rank-constrained Bures--Wasserstein covariance approximation is prior art; Bréchet et al. (ICML 2023) explicitly characterize rank-bounded minimizers. Burrage--Lythe (2009) construct second-order-in-time stochastic methods using one Gaussian random variable per timestep for stationary-density objectives, and Burrage--Lenane--Lythe (2007) analyze related one-Gaussian schemes. These sources prevent any broad claim that two Gaussians are necessary for high-order or accurate Langevin simulation in general.

The originality claim is restricted to applying these facts to the resource question exposed by the new two-Gaussian ULMC constructions: the exact \(2d\)-rank obstruction for the force-free kinetic OU conditional innovation, the necessary-and-sufficient two-\(d\)-Gaussian affine representation count, and the sharp best-one-draw local \(W_2\) defect \(\sqrt{d\lambda_-(h)}\) with leading constant \(\sqrt{d\gamma\alpha/6}\).

The principal residual originality risk is an older or contemporaneous Langevin-integrator source that records the same rank-minimality or Bures lower bound without terminology captured by the searches. The full Burrage--Lythe 2009 and Burrage--Lenane--Lythe 2007 articles were not inspected beyond accessible abstracts/reference metadata; their abstracts focus on stationary distributions rather than exact one-step conditional transition rank, but they are the most relevant uninspected sources. The recent ULMC preprint is also new enough that simultaneous follow-up work may not yet be indexed.

## Value

**PASS.** The motivating ULMC work makes Gaussian count an explicit computational resource and reduces several new schemes to two draws per iteration. The result shows a sharp boundary beneath that resource count for the most basic force-free subsystem: one affine \(d\)-Gaussian draw cannot reproduce the exact joint position--velocity innovation, while two are sufficient. The exact best-one-draw \(W_2\) defect quantifies what is lost rather than only giving a rank impossibility.

The limitation to a local conditional kernel is scientifically useful rather than cosmetic: it cleanly separates exact-transition random-number requirements from stationary-density methods known to succeed with one Gaussian. This avoids turning a local linear-algebra obstruction into an unsupported global sampling lower bound.

## Limitations

The theorem concerns affine-Gaussian innovations and standard Euclidean phase-space \(W_2\). It does not exclude nonlinear random transformations, algorithms with additional non-Gaussian continuous randomness, one-Gaussian methods optimized for weak or invariant-measure accuracy, or cancellations in long-time sampling error. It treats scalar friction and isotropic noise. The local \(h^{3/2}\) defect is not by itself a lower bound on stationary or global Markov-chain bias.

## Sources inspected

- Lyu, Wang, and Yang, arXiv:2609.20713, including the accessible arXiv material describing the universal ULMC framework, its low-cost two-Gaussian schemes, and their stated Wasserstein rates.
- Bréchet, Papagiannouli, An, and Montúfar, ICML 2023 / PMLR 202, for prior rank-bounded Bures--Wasserstein covariance minimization.
- Ning, Jiang, and Georgiou, IEEE Signal Processing Letters 2013, for the Gaussian Wasserstein/Bures covariance connection.
- Burrage and Lythe, SIAM Journal on Numerical Analysis 2009, accessible abstract and reference metadata, for one-Gaussian stationary-density methods.
- Burrage, Lenane, and Lythe, SIAM Journal on Scientific Computing 2007, accessible abstract and reference metadata, for one-Gaussian second-order stochastic integrators.
- Additional exact/integrated Ornstein--Uhlenbeck references located by synonymous searches; none inspected stated the combined Gaussian-count and sharp rank-constrained \(W_2\) theorem above.
