# Independent mathematical audit

## correctness

PASS

The printed Itô SDE dx=[mS/(a+S)-D]x dt+sigma*x dB gives dlog x=[mS/(a+S)-D-sigma^2/2]dt+sigma dB; Eq.(3.1) omits the -sigma^2/2 drift. For Y=log(S/S*), Z=log(x/x*), the inverse density change has determinant 1/(Sx), absent from source Thm3.1. Under the paper local affine OU approximation, stationary mean solves A mu+(0,-sigma^2/2)=0 and covariance solves A Sigma+Sigma A^T+diag(0,sigma^2)=0. At (S0,D,m,a)=(4,2,3,1), exact mu=(3sigma^2/4,-sigma^2) and Sigma=sigma^2[[9/16,-3/4],[-3/4,19/16]], both independently algebraically verified. Consequently Z~N(-sigma^2,19sigma^2/16), x is lognormal with E[x]=2exp(-13sigma^2/32) and mode=2exp(-35sigma^2/16). This concerns the linear approximation, never an exact nonlinear stationary law.

## originality

PASS

Itô logarithm drift and change-of-variables Jacobians are classical and receive no novelty credit. The contribution identifies BOTH omitted terms in the specific Yang–Zhao–Song Theorem3.1, reconstructs the resulting stationary OU approximation, and supplies explicit corrected distribution statistics for the published parameter set. General Fokker–Planck analyses such as Liu–Chen 2021 treat different SEIS models and do not imply this particular published mismatch. No publication-specific correction located in available search.

## value

PASS

The two transformations determine the actual normalized density, its stationary mean, mode and higher moments; their omission is not a harmless normalization convention. This model-specific correction affects the interpretation of the article’s stationary microbial abundance estimates and is mathematically motivated despite using classical calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
