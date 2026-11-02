# Independent mathematical audit

## correctness

PASS

PASS: Sherman–Morrison gives D(S,I+wvv*)-D(S,I)= -w/(1+w) v*Sv + log(1+w). At positive w the top eigenvector of S minimizes D, while for -1<w<0 the bottom eigenvector does; minimizing over u=1+w selects u=M or u=epsilon, with reduction phi(mu)=mu-log mu-1. The unique score crossing epsilon*(M) lies in (0,1/M) since M-1/M-2log M>0. For any noncommuting positive update, the Rayleigh quotient at e1 is <=epsilon and a vector in span(e2,e3) perpendicular to v has quotient >=1, so kappa>=1/epsilon. For any negative update, e3 has quotient >=M and some vector in span(e1,e2) perpendicular to v has quotient <=1, hence kappa>=M. The explicit diagonal updates attain both bounds, proving unrestricted rank-one infimum min(M,1/epsilon). Exact tie, mismatch interval (epsilon*,1/M), ratio 1/(M epsilon), supremum 1/(M epsilon*)~e^M/M² follow. Independently verified M=6, epsilon=1/20 and 500 noncommuting random Hermitian rank-one Rayleigh cases; samples are not the optimality proof.

## originality

PASS

PASS (qualified): Bock–Andersen (2023 arXiv, 2025 journal) establish directed Bregman log-determinant low-rank eigenvalue selection, which the proof explicitly credits. Their article does not state the signed-indefinite rank-one global spectral-condition regret interval in the read sections; positive-semidefinite-error conditioning results in their 2024 paper cannot directly cover signed S-I. The new comparison is with all noncommuting Hermitian rank-one corrections and has a sharp exponential worst-case gap. General matrix nearness equivalence could still give an implicit corollary.

## value

PASS

PASS: A sharp, unbounded approximation ratio for a practical divergence-optimal rank-one preconditioning objective, with precise parameter range and exact global spectral benchmark, is a motivated numerical linear algebra counterexample. It does not conflate condition number with iteration count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
