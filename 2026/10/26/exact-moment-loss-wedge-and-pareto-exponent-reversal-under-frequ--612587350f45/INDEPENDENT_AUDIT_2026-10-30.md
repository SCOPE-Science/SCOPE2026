# Independent mathematical audit

## correctness

PASS

The stationary convolution from a two-sided Poisson clock exists because 2 gamma+2(lambda/s)log(1-s)<0. Its conditional variance V=2D integral_0^infty exp(2gamma u)(1-s)^{2N_u}du is positive and satisfies the exact affine perpetuity V=A Vprime+B with A=(1-s)^2 exp(2 gamma T), B=D/gamma(exp(2 gamma T)-1), T~Exp(lambda/s); A and B are dependent but jointly independent of Vprime. Verified negative E log A, nonarithmetic log A, P(A>1)>0, E A^(p_s/2)=1 and a positive moment margin for B, so Goldie implicit renewal applies. Breiman transfers the V survival tail to symmetric X with p_s survival exponent; a stationary Fokker-Planck zero-flux calculation gives q_s for the diffusion. The Taylor third-derivative sign for (1-s)^u changes at exponent u=2, yielding the exact root comparison; the second-order x^2 generator coefficients match 2(gamma-lambda)+lambda s. At fourth order jump generator has extra -4lambda s^2+lambda s^3, giving the strict wedge between b_DA=1-3s/2 and b_true=1-3s/2+s^2-s^3/4; generator moments yield strict fourth-moment ordering when finite. The s->0 positive-root equation b c=1-exp(-c) and implicit expansion gives the nonunit exponent ratio. Independently checked 42 parameter root-order cases and boundaries. Heavy-tail conclusions rely on precisely stated standard theorem, not on simulated tails.

## originality

PASS

Best-of-knowledge originality for the stated final claim after direct comparison of prior implications and source materials; foundational methods, source models and matching components are explicitly credited. Exact moment-loss wedge and Pareto-exponent reversal under frequent partial resetting is not inferred new merely because an exact phrase search fails. Unindexed equivalent publications remain a disclosed risk.

## value

PASS

The stationary second-moment approximation of frequent weak resetting is deceptively exact while its far-tail behavior can have the opposite exponent ordering and even the wrong finite/infinite fourth-moment classification. The explicit open moment-loss wedge and sharp shared-variance reversal are physically motivated limits of diffusion approximations for rare events, not trivial repackagings of a known stationary density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
