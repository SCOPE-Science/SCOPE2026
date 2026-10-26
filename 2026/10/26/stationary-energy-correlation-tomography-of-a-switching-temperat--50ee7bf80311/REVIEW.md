# Scientific review: stationary energy-correlation tomography

## Correctness — PASS

The stationary stochastic convolution has environment-conditioned variance \(Y_t=(\bar D/\kappa)(1+\delta Z_t)\). The exact filtered-telegraph covariance yields \(K=3\delta^2\kappa/(\kappa+\lambda)\) and \(C=2a+(K/3)(2a+F(\lambda))\). The kernel derivative is strictly negative for every positive known lag, and the constraint \(0<\delta<1\) gives the exact finite open interval for \(\lambda\). These steps prove necessity, sufficiency and uniqueness throughout the theorem's quantified parameter domain. The packaged standalone checker agrees with independent Markov-moment equations in 600 tests; those finite cases are not used as infinite proofs.

## Originality — PASS, subject to priority limitations

Huang et al. (arXiv:1412.7952v1, Sections 3–4) provide general forward Markov-modulated Ornstein–Uhlenbeck moment and transform machinery, not the stated complete three-observable inverse range and bijection. Miyaguchi et al. (arXiv:1605.00106v1) study unconfined fluctuating diffusivity and temporal displacement statistics. Lanoiselée et al. (arXiv:2207.14068v1) consider a harmonically confined *continuous-diffusivity* mechanism; their stationary kurtosis does not establish inverse identification of a telegraph bath from a lagged square covariance. The known unconfined diffusion-inference and switching-stiffness results use different dynamics or measurement sets. The exact inverse theorem is not an identified immediate implication of these inspected full texts, although the forward moment identities follow by specialization of Huang et al. Additional specialized work could contain an equivalent inverse, and one nearby two-state stationary-distribution source was accessible only by abstract.

## Mathematical value — PASS

Unknown switching rate and temperature contrast produce the same positional covariance at all lags, making second-order fitting fundamentally non-identifying. A measurable fourth-order energy autocovariance and stationary excess kurtosis repair that information loss with a constructive global inverse. The exact open feasibility inequalities offer a model-falsification criterion for noiseless statistics and identify two distinct excluded physical boundaries; this is a natural parameter-identification problem, rather than an arbitrary evaluated moment.

## Limitations and priority

The result assumes exact stationary expectations, known trap rate and lag, independent Brownian forcing, symmetric switching, and strictly positive unequal diffusivities. It infers an unordered pair of bath diffusivities. No stability under measurement noise, experimental realization, or general switching model is proved. The exact forward components are covered by established literature. Full-text coverage of every related inverse study cannot be guaranteed.

Self-review: passed. Independent audit: not yet performed.
