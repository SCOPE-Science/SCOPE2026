# Independent mathematical audit

## correctness

PASS

The odd central differences isolate delta^2 T[u,u,u]/6. Gaussian spherical pairing identities yield E[T[u,u,u]u]=3t/[n(n+2)] and E[T[u,u,u]^2]=(6||T||_F^2+9||t||^2)/[n(n+2)(n+4)]. The symmetric harmonic decomposition T=H+sym(t⊗I)/(n+2), with orthogonal trace and harmonic pieces, cancels the trace variance to give delta^4||H||_F^2/[6(n+2)(n+4)], nonnegative with equality iff H=0; the zero-variance basiswise identity follows from sum_a (t·u_a)u_a=t. For rank one, sphere sixth moment is 15/[(n+2)(n+4)], while coordinate risk is sum a_i^6; Jensen bounds 1/n^2<=sum a_i^6<=1 prove both sharp orderings. Completing square in s+s^2/2 >=-1/2 proves global strong convexity of the realized quartic. Independent rational exact checks verified crossover for n=2..100 and a rotated pure-trace frame; those samples do not prove arbitrary tensor quantifiers, which follow from complete Gaussian pair partitions.

## originality

PASS

The full-frame estimator and spherical moments are prior (Feng–Wang); the reviewed exact harmonic tensor variance identity, nonzero-cubic zero-variance classification, and sharp coordinate-vs-Haar localization crossover require extra contractions and optimization of sixth powers. This is an exact structural refinement, not invention of Haar frame estimators. Closely relevant Feng–Wang full text could not be read in this audit because arXiv/OA full text failed and authorized institutional retrieval required unavailable VPN. The best-of-knowledge PASS remains priority-limited and must not be read as a complete inspection or a novelty certificate.

## value

PASS

A natural estimator design question at a true stationary/minimizing point has a sharp answer: complete orthogonal frames eliminate projection randomness yet retain anisotropic cubic truncation error; random frames help for localized tensor directions but hurt by up to asymptotic factor fifteen for dense rank-one directions. The exact harmonic nullspace and risk crossover distinguish whether randomization is beneficial at equal query count and under equal independent evaluation noise. These are mathematically motivated sharp structural facts rather than a generic second-moment restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
