# Independent mathematical audit

## correctness

PASS

Gaussian STFT radial Hermite eigenvalues are λ_n(a,w)=1/n!∫_a^{a+w}e^(−u)u^n du. Telescoping adjacent difference equals [e^(−a)a^(n+1)−e^(−(a+w))(a+w)^(n+1)]/(n+1)!, with sign of H(a,w)−(n+1), H=w/log(1+w/a), and H(0,w)=0. Thus unique maximum at floor H and adjacent tie only when H=m; crossing a_m=w/(e^(w/m)−1). Crossing derivative jump is w e^(−a_m)a_m^(m−1)/((m−1)!(a_m+w))>0, with asymptotic w/(sqrt(2π)m^(3/2)). Center c=a+w/2, Stirling uniformly for bounded maximizer n−c and s∈[−w/2,w/2] yields relative correction −[B2({c})/2+w²/24]/c with uniform O_w(c^(−2)); rare floor(c)−1 maximizing cases near integer c change coefficient only O(1/c). Fractional c dense along chosen sequences gives exact second-term range. Independent high-precision incomplete-gamma top-mode calculations verified crossings for 12 (m,w) cases, and two-term numeric errors ~10^(−9) at a≈1000 for w=1. These finite checks are corroboration only.

## originality

PASS

The nearest primary source Knutsen (2020), open-access Section 3.1, treats the exact same Gaussian ring with w=1, but only bounds the maximizing index by two neighboring integers and gives leading R^(−1) norm with O(R^(−3)) error. The new continuous w>0 crossing radii, strict cusp jumps, Bernoulli-fractional-center coefficient and full subsequential range are not furnished by this general bound or by the underlying radial eigenvalue formula. Possible implicit local Poisson central-limit expansion with lattice corrections is a residual priority risk.

## value

PASS

Determining which Hermite mode actually maximizes an annular time-frequency mask is a natural spectral optimization problem explicitly left at adjacent ambiguity in the primary source. Exact eigenvalue switching and corner amplitudes resolve this ambiguity, and the uniform oscillatory next term sharpens a known O(R^(−3)) uncertainty with the important fact that no constant correction exists. The exact fixed-width classification is mathematical substance beyond a routine asymptotic evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
