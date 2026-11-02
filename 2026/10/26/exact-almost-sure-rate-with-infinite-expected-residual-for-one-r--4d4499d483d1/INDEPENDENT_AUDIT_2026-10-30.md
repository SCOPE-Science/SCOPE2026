# Independent mathematical audit

## correctness

PASS

Diagonalizing symmetric A preserves Gaussian sketches. Direct algebra gives r^+=((b-a)uv/(aXu+bYv))(Y,-X), a.s. nonzero and never aligned with an eigenspace; its direction is perpendicular to a fresh isotropic Gaussian sketch. Hence the postfirst-step orientations are iid uniform modulo pi, log norm multipliers are stationary 1-dependent (separated even/odd subsequences iid), and logarithmic singularities are integrable. The circular integral E log|c cos t+d sin t|=log(sqrt(c^2+d^2)/2) gives the exact average log multiplier. For the moments, the denominator is ||Ar||T with T normal and independent perpendicular W contributes at least a constant |W/T|, whose pth moment diverges p>=1; conditioning at each step proves all positive times. The probability-zero zero-denominator/eigenspace events and definite/indefinite cases are handled. Independent SymPy identity proof and 300000 angle-pair samples for each of (1,3),(-1,-3),(-1,2) gave observed means -0.692714,-0.691933,0.000583 against targets -0.693147,-0.693147,0; numerical tests are corroboration only.

## originality

PASS

Nakatsukasa–Tropp (2021 preprint, 2024 SIAM) introduced sketched GMRES. Burke–Güttel–Soodhalter (2023/2024) established its projector and convergence theory. The latter complete 24-page paper was inspected, especially Sections 3–5: assumption (3.1) requires an epsilon-subspace embedding with m<s and epsilon<1; Sections 4–5 give true/sketched residual bounds conditional on this approximation. The fresh Gaussian 1x2 row in the assessed one-dimensional restart is intentionally not a uniform embedding on R2. No read theorem implies the exact two-eigenvalue pathwise Lyapunov exponent jointly with infinite true-residual moments at every positive time. The deterministic optimal Richardson rate is prior mathematics, not claimed new. The former Nakatsukasa–Tropp full text was unavailable after arXiv and lawful repository PDF failures; authorized institutional access returned vpn_disconnected, leaving a specific priority risk, as does possibly unindexed random-matrix product literature.

## value

PASS

The finding sharply separates pathwise linear convergence and divergent unconditional Euclidean residual moments for a natural minimal stochastic residual-minimization experiment. It gives an exact Lyapunov exponent and a concrete failure mode of inadequate sketch dimension, with a nonconvergent-exponent boundary for opposite-sign eigenvalues. These are meaningful structural facts rather than a tiny arbitrary numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
