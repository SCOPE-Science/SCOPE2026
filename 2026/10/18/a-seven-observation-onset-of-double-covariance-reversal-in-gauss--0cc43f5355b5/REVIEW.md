# Scientific assessment: Gaussian AR(1) crossings and centered energy

## Correctness — PASS

The probabilistic premise is precisely a centered Gaussian vector with stationary AR(1) covariance \(\rho^{|i-j|}\), \(0\le\rho<1\), and integer \(n\ge2\). The mixed Gaussian sign/quadratic identity follows from twice-iterated Gaussian integration by parts, with derivative coefficients verified directly from \(\arccos(c/\sqrt{st})/\pi\). Substitution of the centering matrix produces the exact finite-polynomial covariance. The geometric-series calculation gives the negative value at \(\rho=1/2\) for all \(n\ge7\); Bernstein representations prove positive values for \(2\le n\le6\); the distance-column expansion proves positivity near \(\rho=1\). The independent verifier reconstructs the matrix, geometric-sum, and symbolic small-window expressions and passed 204 exact assertions. The proof does not infer a universal statement from finite tests. No uniqueness of the two large-window zeros is asserted.

## Originality — PASS, with priority risk

The closest examined full scientific sources are Kratz–León (2006, arXiv:math/0609682) on smooth continuous-time Gaussian crossing-count moments and Nyberg–Lizana–Ambjörnsson (2017, arXiv:1711.02926) on crossing-count cumulants and AR examples. Neither material read supplies the joint covariance between a finite-window crossing count and the sample-mean-centered quadratic energy. Sinn–Keller (2011, DOI:10.1137/S0040585X97984991) studies *crossing–crossing* covariance and therefore is a particularly plausible near neighbor, but the full text was inaccessible. Direct searches also covered the Gaussian quadratic/sign-moment aliases and published mathematical research records. General Gaussian integration by parts and the arcsine crossing law are classical; the asserted distinction is the exact seven-sample threshold with two sign reversals. General methods may imply the result after nontrivial calculation, so residual historical-priority risk remains and independent priority determination has not occurred.

## Mathematical value — PASS

Sign-crossing frequency and centered quadratic energy are two basic summaries of correlated Gaussian measurements, respectively recording oscillation and dispersion. A sign assumption based on independent measurements does not extrapolate monotonically to positively correlated samples: the same covariance is positive for every correlation through sample size six, but for every size at least seven it is positive at zero and near one while negative at one-half. The sharp onset is an interpretable structural finite-window phenomenon, not a choice of an arbitrary isolated sample size. The associated all-window asymptotic quantifies how a fixed positive autoregressive correlation eventually enforces negative covariance.

## Boundaries and closest prior work

The result is restricted to nonnegative AR(1) correlations, joint Gaussianity, and unnormalized centered quadratic energy. No root uniqueness, distributional ordering, non-Gaussian extension, or causal conclusion is claimed. The inaccessible Sinn–Keller full text is an unresolved but not independently decisive priority risk. This is a self-review only, not external historical verification.

Self-review: passed. Independent audit: not yet performed.
