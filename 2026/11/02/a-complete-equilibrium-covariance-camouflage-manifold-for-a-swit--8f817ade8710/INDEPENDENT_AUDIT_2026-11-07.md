# Independent mathematical audit

## correctness

PASS

For positive D, 0<k1<k2 and strictly positive switching rates, stationary second-moment generator gives w=2D(2K-Q^T)^(-1)pi and stationary fourth moments z=12D(4K-Q^T)^(-1)w. Stationary covariance is 1^T exp[(Q^T-K)t]w, C(0)=v, C'(0+)=-D and satisfies a two-root ODE with trace T and determinant Delta. A single exponential requires rho=D/v and the characteristic equation, equivalent, after clearing strictly positive factors, to F=(alpha+beta)^2+2(beta-alpha)(k2-k1)-4k1k2=0. Solving the positive-rate locus gives alpha=(rho-k1)(rho+k2)/(k2-k1), beta=(k2-rho)(rho+k1)/(k2-k1) and k1<rho<k2. ODE uniqueness proves sufficiency. The computed fourth cumulant 9D^2(rho-k1)(k2-rho)/[rho^2(rho^2+rho(k1+k2)+3k1k2)] is strictly positive. My independent SymPy matrix inversion and characteristic identity checked the full symbolic rational identities, not only sample numbers. Excludes coincident stiffnesses, zero switching rates, nonstationary process and finite-data identification.

## originality

PASS

Best-of-knowledge PASS qualified: the stationary Gaussian mixture and forward Markov-modulated OU covariance/moment systems were already known. The distinctive claim is the exhaustive inverse positive-rate two-dimensional covariance-camouflage family for every rho plus its positive fourth-cumulant discriminator. General linear moment machinery is a strong premise, and may permit an algebraic rederivation, but the inspected primary statements do not provide this inverse classification. This is not a claim of novelty of Gaussian mixtures or formulas for generic MMOU moments.

## value

PASS

A complete nonidentifiability result for a natural Markov switching physical trap: even the entire stationary two-time position covariance and power spectrum can be indistinguishable from equilibrium, while a quantified fourth cumulant separates the models. The complete inverse family is a meaningful structural classification, not an arbitrary sample or mere renamed moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
