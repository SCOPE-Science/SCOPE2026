# Review of the shared-path sensitivity finding

## Correctness — PASS

The claim is an explicit finite-dimensional theorem rather than an extrapolation from numerical samples. The terminal Gaussian model yields the population sensitivity matrix \(K=(2\pi\sqrt3)^{-1}e_de_d^\top\). Fixed Brownian endpoints constrain every estimated score to their column span, and full column rank makes the nonzero eigenvector assertion rigorous. Orthogonal invariance gives the exact Beta projection law. Gaussian regression, the bivariate normal orthant identity, and convexity yield the exact best conditional-expectation risk and the stated lower bound. The one-path outer-product collapse is an algebraic identity. The independent standalone checker completed 10,944 supplementary checks; those are not substituted for the general proof.

Limitations: the fixed-span argument requires a constant drift and a parameter-independent score vector for each reused Brownian path. It is not claimed for arbitrary spatially varying drift perturbations.

## Originality — PASS, with historical-priority uncertainty

The direct motivating source is Zou, Lie and Marzouk (2026), arXiv:2610.33210v1, especially its score estimator in Section 3.2, martingale control variate and sensitivity matrix in Section 3.3, and explicit cross-parameter Brownian-path reuse in Section 4.1. The present statement is not its general derivative-informed basis theorem: its new content is the parameter-independent score-span mechanism for the constant-drift specialization, exact Beta geometry, a nonzero conditional prediction-risk floor even as outer sampling grows, and the exact single-path collapse. The motivating paper's state-dependent score integrals need not share this restriction.

Holodnak, Ipsen and Smith (2018), arXiv:1801.00682, analyze independent unbiased outer-product samples and principal-angle bounds; that independence/unbiasedness comparison does not cover common-path nested score samples. Luo, O'Leary-Roseberry, Chen and Ghattas (2026), JMLR 27(182), address derivative-informed approximation and Monte Carlo covariance sampling but do not directly provide the fixed-path span and risk result in their inspected theoretical sections. The Beta projection law and Gaussian orthant identity are classical ingredients and are not independently claimed as discoveries. Actual current research-record searches found related Gaussian subspace and sample-reuse phenomena, but none implying this model-specific statement. Historical priority remains provisional because an unidentified older general random-features or nested-Monte-Carlo theorem could imply it.

## Mathematical value — PASS

The motivating numerical method has two independent sample budgets: paths inside each score estimate and outer drift samples used to approximate the sensitivity operator. The theorem proves that increasing only the outer budget cannot defeat a finite shared-path geometry barrier in this natural Gaussian model, despite the population sensitivity operator having exact rank one. The exact Beta law turns the obstruction into a parameter-dependent prediction, and the arcsine expression quantifies an unavoidable, strictly positive generalization risk even for the *optimal* one-dimensional ridge predictor allowed by the sampled span. The single-path result exposes complete loss of outer-sample information under the centered score. This is a structural numerical-design benchmark, not a textbook scalar convergence exercise.

The theorem does not establish an effect for all implementations, nor does it negate the numerical performance reported by the motivating source. Independent expert verification and historical priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
