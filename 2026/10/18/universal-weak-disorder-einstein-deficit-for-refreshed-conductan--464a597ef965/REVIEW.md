# Independent mathematical audit

## correctness

PASS

With edge indices relative to the walker, the independent refresh part has gap mu on the mean-zero product space. The unbiased zero-disorder shift part is self-adjoint and nonpositive. Both disorder and field perturb only bounded operators, analytically near zero by the bounded-mark assumption. A way to verify the variance limit and analyticity without assuming a bounded corrector is to tilt the two shift terms by exp(z) and exp(-z), leaving the diagonal and refresh terms unchanged. At zero parameters the time-one semigroup has an isolated simple eigenvalue 1 and the remainder has norm at most exp(-mu). Small analytic bounded perturbations preserve the isolation and exponential separation, so the product-start moment generating function is the leading exponential times a nonvanishing analytic prefactor, plus an exponentially decaying relative error locally in z. Differentiating its logarithm gives the speed and variance rate, also for noninteger times by the bounded fractional-time semigroup. At zero field, reflection makes the stationary drift zero. Write G=(-L0)^(-1) on the mean-zero space, g=eta_0-eta_{-1}, S=T_--T_+, and f=Gg/2. The stationary-density derivative in disorder is h1=Sf/2, and its field derivative is G^2 S^2 g/8 by differentiating the adjoint Poisson equation. Using d_lambda=1-d^2 and the exact density normalization gives mobility coefficient -E[g^2]/4+<g,h1'>/2. Differentiating the tilted eigenvalue twice gives the variance rate pi[1+2(p T_+-(1-p)T_-)chi], where L chi=-d and chi=epsilon f+O(epsilon^2); its quadratic coefficient is <(T_+-T_-)f,h1>+<g,(T_++T_-)f>/2, the same as the bracket calculation including refreshes. In the coordinate-linear sector the resolvent symbol is 1/(mu+1-cos k). Periodic integration by parts reduces the variance integral to minus rho, where rho=mu+1-sqrt(mu(mu+2)); the additional mobility integral is rho+mu rho'. Thus the deficit coefficient is sigma^2(1-rho+mu rho')/2 = sigma^2 sqrt(mu/(mu+2))/2. Sign reversal of all marks gives even analyticity and hence the fourth-order remainder. The coefficient is positive and increasing at fixed positive mu, with the stated endpoint limits; the perturbation argument does not supply a remainder uniform as mu tends to zero.

## originality

PASS

The exact model, CLT and a qualitative failure of the Einstein relation are already covered. The supported distinct contribution is the evaluated joint second-order expansion, and thereby the strict variance-minus-mobility sign for weak symmetric disorder at every fixed positive refresh rate.

## value

PASS

A qualitative counterexample for some rates does not tell whether weak disorder has a robust signed effect when refresh is slow but strictly positive. The exact coefficient gives that sign for all positive fixed rates and quantifies both refresh endpoint limits at the coefficient level. It is a useful analytic benchmark for dynamic response, not a claim about strong disorder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
