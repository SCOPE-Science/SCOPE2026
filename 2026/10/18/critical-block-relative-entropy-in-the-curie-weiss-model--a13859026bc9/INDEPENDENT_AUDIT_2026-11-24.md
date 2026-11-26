# Independent mathematical audit

## correctness

PASS

For the zero-field Gibbs weight with exponent S_N^2/(2N), the Hubbard–Stratonovich identity makes the block exactly a latent-field product mixture. With X_N=N^(1/4)H_N the exponent is N F(N^(-1/4)x), F(h)=h^2/2-log cosh(h), with quartic leading term x^4/12. The global bound c min(x^4,sqrt(N)x^2) dominates exp(A x^2) times the rescaled density for each fixed A and large enough N, splitting at |x|=N^(1/4). Hence the block likelihood converges locally uniformly in the normalized spin sum, and the reference-law CLT gives weak convergence of those likelihoods. Independent replicas give the exact second-moment factor (1+tanh(H_N)tanh(H_N'))^k; (k/(2sqrt(N)))(X_N^2+(X_N')^2) bounds its logarithm. The resulting uniform L^2 bound makes L log L uniformly integrable. Thus this is KL convergence, not an inference from TV convergence. For Y=Z+sqrt(alpha)X, the density p_alpha satisfies partial_alpha p_alpha=-(2sqrt(alpha))^(-1) partial_y(p_alpha E[X|Y=y]), and partial_y log(p_alpha/phi)=sqrt(alpha)E[X|Y=y]. Integrating by parts yields the stated derivative, positive since Cov(X,Y)=sqrt(alpha)v. On compact positive alpha intervals Gaussian/quartic tail bounds control the derivatives; conditional Cauchy–Schwarz controls the squared conditional mean times p_alpha by the convolution with x^2 times the quartic density, giving continuity. At zero, Taylor in sqrt(alpha) uses symmetry, Gaussian L^3 control and quartic tails; the first term is alpha v(z^2-1)/2. Applying the quadratic expansion of L log L and normalization gives v^2/4. At infinity, the density of X+delta Z, 0<delta<=1, is bounded by C exp(-c|x|^4)+C Pr(|Z|>|x|/2) by splitting at |delta Z|=|x|/2. Boundedness and this tail dominate the entropy integrand, so h(X+delta Z) tends to h(X), giving the claimed log correction and constants. This is for fixed positive alpha in the finite-volume limit; the endpoint expansions apply afterward.

## originality

PASS

The critical block scale, quartic fluctuation law, positive TV profile and Gaussian-channel derivative identity are not new. The distinct result is the exact finite positive KL profile in that window, with the likelihood-tail estimate needed to take the entropy limit. Known fluctuation and TV statements cannot be used in place of that estimate. The endpoint calculations are properties of this exact profile, not new Gaussian-channel identities.

## value

PASS

Quantifies exactly how fair-product approximation fails on the natural first nontrivial block scale in relative entropy, a strictly more tail-sensitive criterion than TV. The quartic-Gaussian profile, monotonicity and the quadratic-to-linear-with-log-correction crossover are useful benchmarks, not just a numerical sample or restatement of weak convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
