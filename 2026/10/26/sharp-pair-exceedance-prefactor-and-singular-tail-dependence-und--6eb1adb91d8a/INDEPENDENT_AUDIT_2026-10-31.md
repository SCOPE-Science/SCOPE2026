# Independent mathematical audit

## correctness

PASS

Poisson marking splits pair-affecting resets into independent rates alpha,alpha,c; their union rate is delta. Conditioning on the last such reset gives exactly the integral of c Q_t(x)^2 plus 2alpha Q_t(x) E Q_t(x-Y) against exp(-delta t) dt, with Y Laplace rate k1=sqrt(lambda/D) and independent of subsequent Brownian noise. Mills ratios locate the unique saddle t*=x/sqrt(2Ddelta); Bessel K2 asymptotics give J(x)~exp(-k2 x)/(delta sqrt(2pi k2 x)). In the same saddle window Q_t(x-Y)/Q_t(x)->exp(k2Y/2); the Laplace moment equals 2lambda/c because k2/2<k1 for c>0. Strict exponential integrability plus saddle localization justify the tilt, yielding coefficient c+4alpha lambda/c. Independent integral quadrature at N,m=(5,2),(6,4),(3,2) confirmed positive ratios increasing toward 1 (convergence is especially slow when c small); it is not proof of an asymptotic. The c=0 boundary is exactly independent via Poisson thinning.

## originality

PASS

The de Mauro-Majumdar-Schehr 2026 source already supplies the exact same mathematical model stationary pair density, so there is no novelty in the pair law or any finite-position probability. The new asserted result is evaluation of the positive-quadrant far-tail integral to the full x^-1/2 factor and coefficient and the singular independent-reset comparison. This nontrivial saddle/exponential-tilt extraction is not tabulated in inspected supplement; originality qualified because density logically encodes the tail and an equivalent asymptotic may exist.

## value

PASS

The exponential rate alone is inadequate for calibrating extremely rare pair excursions: the nontrivial x^-1/2 prefactor and exact parameter coefficient distinguish shared reset marks from independent thinning and reveal a singular tail mechanism. This is a mathematically motivated sharp asymptotic, not a recomputation of stationary moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
