# Independent mathematical audit

## correctness

PASS

Read entire RESULT.md and verify.py. Uniform simplex barycentric coordinates are independent normalized Exponential(1) arrays. Full-log Hilbert variation cancels normalization exactly, so D_ab=log M_ab+log M_ba with M_ab=max_i E_ai/E_bi. For each denominator b, one-column rare event has probability ET_b/N+O(N^-2); intersections for distinct denominators are O(N^-2) as simultaneous small denominators force the maximum among other coordinates, giving joint independent denominator blocks and the precise Galambos exponent inclusion–exclusion formula. Directed log maxima have both tails at most e^-t, yielding moment uniform integrability and joint moment convergence. The bivariate same-denominator exponent -1/x-1/y+1/(x+y) gives log covariance via Hoeffding/Frullani ∫_0^1[-log(1-w+w²)]/[w(1-w)]dw=π²/9; independent high precision quadrature returned 1.0966227112321512 agreeing π²/9, and incident edge variance π²/3 gives corr exactly 1/3. Independence of denominator blocks proves disjoint edges independent in the limit, in fact their finite sample is independent as distinct point arrays. Numerical check confirms the constant, not an infinite N proof.

## originality

PASS

Hilbert metric on a simplex equals variation norm of barycentric log ratios (Foertsch–Karlsson prior). Distribution of single-block normalized ratio maxima is the established Galambos extreme-value copula (Mai prior). The full sample-induced coupling over all ordered pairs and asymptotically independent denominator blocks, with the exact incident/disjoint edge covariance structure, is the assessed final claim. Its ingredients are known but no read source states the joint random simplex distance theorem.

## value

PASS

Random distances in high-dimensional projective simplex geometry have a natural scale 2logN; the complete fluctuation law and universal incident-edge correlation distinguish shared-point effects from independent disjoint edges and provide usable exact joint statistics, not only another univariate extreme-value limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
