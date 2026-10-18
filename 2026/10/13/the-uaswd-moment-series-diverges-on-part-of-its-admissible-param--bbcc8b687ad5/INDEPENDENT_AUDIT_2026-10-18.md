# Independent mathematical audit

## correctness

PASS

Checked the original integral (bounded Y ensures moments finite) and the outer integrated Taylor block in Eq. (3.8). Its positive inner m-sum is bounded below by the m=0 term A_n=(2/π)(rλ)^n 2^(n/k) Γ(n/k+1)/n!. Gamma-ratio asymptotics give A_(n+1)/A_n∼rλ(2/k)^(1/k)n^(1/k−1): term test fails for every 0<k<1; at k=1 the exact ratio is 2rλ, so failure whenever ≥1. For k=λ=r=1 the integrated m=0 contributions are (2/π)(−2)^n while the original integral equals 1/2. Expanding only the nonnegative reciprocal-square-root factor and invoking Tonelli gives a globally convergent one-sum integral. Eq. (3.12) reuses invalid nested moment rows. Independently checked numerical integral, beta special case and gamma ratios.

## originality

PASS

Alghufily et al. print Eq. (3.8) and Eq. (3.12) without needed convergence conditions; their own fitted Weibull shape 0.9952 exhibits failure. Related unit-arcsine exponential model gives the correct special-case gamma moment, but not the divergence theorem for the source series or its all-shape positive replacement.

## value

PASS

The source presents moments and MGF as core analytic statistics of a new lifetime distribution, and its reported MLE k=0.9952 lies inside the proved divergence region. A rigorously convergent positive integral series recovers valid raw moments. This has direct statistical usability beyond a routine abstract nonuniform-convergence example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
