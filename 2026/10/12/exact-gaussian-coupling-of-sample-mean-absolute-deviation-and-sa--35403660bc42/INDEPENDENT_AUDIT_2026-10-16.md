# Independent mathematical audit

## correctness

PASS

For Gaussian iid observations, the centered residual vector is isotropic on the d=n-1-dimensional hyperplane. Its spherical radius Q~chi_d is independent of direction. Any integrable positively p-homogeneous statistic T satisfies E[Q^(p+2)]/E[Q^p]=d+p by exact gamma recurrence, so Cov(T(R),S²)=p sigma² ET/(n-1). With T(R)=n^-1 sum |R_i|, p=1 and R_i variance sigma²(n-1)/n, this yields EM=sigma sqrt(2(n-1)/(pi n)) and covariance sigma³ sqrt(2/(pi n(n-1))). Distinct residual coordinates have corr −1/(n−1); exact bivariate folded-Gaussian E|Z1 Z2|=(2/pi)(sqrt(1-rho²)+rho asin rho) yields variance and the stated correlation². n=2 endpoint and n→infinity limit were checked separately; independent chi recurrence/moment and correlation numerical tests corroborate but do not substitute for the analytic derivation.

## originality

PASS

Best-of-knowledge PASS specifically for the exact finite Gaussian MAD–variance covariance and associated finite correlation profile. Segers' same-statistic full-length paper proves general asymptotic MAD theory, but inspected text/searches do not provide this pairwise finite covariance. Bräutigam–Kratz treat sample dispersion statistics together in joint dependence with quantiles; only partial text was accessible and residual uncertainty is recorded. The radial homogeneity/chi-moment identity is classical in mechanism, and that mechanism is explicitly not asserted to be new independently.

## value

PASS

PASS. The finite-n exact covariance and Pearson correlation between two classical robust/nonrobust scale estimators are natural and practically interpretable statistical invariants; they reveal persistent high dependence even though one estimator uses absolute and the other squared residuals. The general homogeneous identity explains the phenomenon compactly, while the nontrivial folded bivariate moment yields the precise finite profile. The novelty/value is not just a textbook gamma recurrence; it is its exact application to this common estimator pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
