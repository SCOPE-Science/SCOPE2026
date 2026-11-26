# Independent mathematical audit

## correctness

PASS

An independent generator calculation gives V=bar D/kappa, M=E[S X²]=bar D delta/(kappa+lambda), and E[X^4]=3(V²+bar D delta M/kappa), by applying stationarity to X², SX² and X^4. For g(h)=Cov(X_0²,X_h²)/V², conditioning on the current bath state gives g'(h)=-2 kappa g(h)+2 bar D delta M exp(-2 lambda h)/V² with g(0)=2+K. Solving gives exactly C=2a+(K/3)(2a+F(lambda)). Differentiation of the integral for F gives a strictly negative derivative for every h>0, including at lambda=kappa. At fixed 0<K<3 the physical contrast constraint is exactly 0<lambda<kappa(3/K-1); the endpoints yield F=1 and F=F(kappa(3/K-1)) with contrast reaching 1 at the latter. The intermediate-value theorem and strict monotonicity give necessity, sufficiency and uniqueness of the unordered diffusivity pair and rate. Ordinary two-point positional covariance only uses V and kappa. The bound VERIFICATION.md and check_claim.py were inspected, not executed; the reported 600 finite tests are not the basis for the universal result.

## originality

PASS

Pass is limited to the exact three-scalar inverse and its strict physical realizability region at a known positive lag, not the forward Markov-modulated OU moment framework or the general idea of diffusivity tomography. The inspected primary and indexed statements do not cover this inverse from these observables.

## value

PASS

Every positional covariance at every lag is blind to contrast and rate. The exact inverse shows that excess kurtosis plus one lagged energy measurement restores identifiability and gives a sharp compatibility test separating the no-switching and zero-diffusivity boundaries. This is useful for deciding whether ideal stationary data can come from the model; it is not a claim of noise robustness, practical estimability or identification for asymmetric switching.

The dated certificate retains the supplied scientific assessment, sources and limitations.
