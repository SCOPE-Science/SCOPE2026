# Independent mathematical audit

## correctness

PASS

SVD/orthogonal invariance reduce Z to G^T diag(a,c) H with independent 2xk standard Gaussian factors. The ordered real 2xk singular-value density has factor (s1s2)^(k-2)(s1²-s2²) and gamma(k-1) normalization; the radial-angular check verifies it. Conditional ||Z||_F²=s1² V1+s2² V2 with independent chi-square_k variables. Scaling s2=eps*t produces eps^(2k-1); the chi-square CDF power bound and integrable E[V2^(-(k-1)/2)] justify dominated convergence for k>=2. Separate s1 and t beta integrals yield C_k and the Haar average J(a,c), and J reduces to elliptic K. Direct independent gamma evaluation verifies C2=pi/6,C3=1/15,C4=pi/840, but these finite values do not prove the limit. A fixed finite-threshold simulation in the source checker is smoke testing only.

## originality

PASS

Shao-Nakatsukasa explicitly give a general rank-one-style upper anti-concentration bound and show numerical rank-two slope 2k-1; their theorem does not give an exact asymptotic or elliptic anisotropy constant. The assessed novelty is the leading constant and rigorous rank-two asymptotic, not SVD distributions or Gaussian anti-concentration itself.

## value

PASS

Two-sided Gaussian probing is directly used in randomized resolvent eigensolvers. Determining exact rank-two rare-event decay, including spectral-shape dependence and no logarithm, resolves a specific numerically conjectured regime and provides precise probabilistic calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
