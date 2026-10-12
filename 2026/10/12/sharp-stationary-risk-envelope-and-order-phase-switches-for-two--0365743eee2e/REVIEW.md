# Self-review

## Correctness — PASS

The two component gradients compose exactly to affine epoch maps with shared multiplier \(g=(1-\eta a)(1-\eta b)\) and sign-dependent displacement. For every strictly stationary, balanced order law, the \(\lvert g\rvert<1\) convolution has an absolutely convergent second moment. Herglotz spectral representation proves the global sharp bounds, and the only spectral equality cases correspond to fixed or alternating fair orders. An exact geometric covariance sum verifies the Markov interpolation. The rational family with \(a=N\), \(b=c=1\), \(\eta=(2N-1)/N^2\) proves an unbounded expected-objective ratio even though both individual gradients are contractive. The package verifier independently checked 728 exact-rational finite-horizon identities. Infinite-horizon conclusions are analytic and not inferred from enumeration.

## Originality — PASS (priority not independently certified)

Ying et al. (arXiv:1803.07964) calculate independent-epoch random-reshuffling performance, while Mohtashami et al. (arXiv:2202.01838) study order-dependent bounds. Domingo-Enrich (arXiv:2206.00632) supplies the important general spectral-transfer technique but treats reshuffling optimization with the mean-Hessian zero-order noise approximation rather than the exact original heterogeneous Hessians; its covered schedules are SO and RR, not all stationary balanced couplings. Hu, Doshi, and Eun (arXiv:2209.07446) mainly address asymptotic CLT ordering with diminishing steps and averaged iterates at constant step. Kühn and Rosenow (arXiv:2306.05300) analyze epoch anticorrelation, and Nguyen et al. (arXiv:2604.00260) study a different operator that averages reversed epochs. None of the inspected exact claims covers the derived all-coupling risk interval, equality classification, double order switch, or unbounded gap. The spectral theorem is a pre-existing proof tool, not asserted as a discovery. Equivalent specialized unindexed results remain a priority risk.

## Value — PASS

The benchmark isolates temporal permutation dependence while keeping data marginals, per-epoch gradient evaluations and component losses fixed. The sharp minimax scheduling classification and sign-switch boundaries identify a genuine limitation of ranking shuffle-once versus alternating or independently reshuffled policies only by their small-step behaviors. Unbounded policy separation with individually contractive component updates provides a substantive mathematical counterexample; no general-dimensional or runtime superiority is claimed.

## Scope and limitations

Only scalar two-component strongly convex quadratics, nonfeedback stationary balanced order laws, constant steps and exact epoch-boundary risks under \(\lvert g\rvert<1\) are treated. The sharp extremes can be nonmixing or nonergodic. General nonlinear updates, adaptive schedules, finite-precision termination and within-epoch risk are not classified. Independent priority review and independent audit have not been conducted.

Self-review: passed. Independent audit: not yet performed.
