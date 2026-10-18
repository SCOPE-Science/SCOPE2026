# Independent mathematical audit

## correctness

PASS

For scalar kernels k_n(t)=b^n exp(-b^n t), Minkowski/Tonelli and near-Dirac positive-time inputs prove exact operator norm sup_{norm(v)_r=1} integral norm_r((k_n(u)v_n)) du, not just a bound on a test vector. For finite r set a_n=|v_n|^r on simplex; r=infinity maximizing coordinates have absolute value one. Logarithmic intervals (b^-j,b^{1-j}] turn the norm into shifted sums v_{n-j}(w)=b^{n-j} exp(-b^{n-j}w); truncated |k|<=K tails integrate to eta<=b^-K+exp(-b^{K+1}), via telescoping e^-b^k. Uniform a_n=1/N on N-2K center scales gives lower bound; Hölder across at most N+2K populated scales and the sum a_n=1 give matching upper; dividing by N^{1-1/r} gives claimed explicit error. For b↓1, shifted Riemann sums of G_r(x)=exp(rx-r exp x) yield Gamma(r)/r^r and coefficient Gamma(r)^{1/r}/r*(log b)^{1-1/r}; for r=infinity sampled sup exp(x-exp x) has max 1/e, and b→infinity selecting adjacent kernels yields kappa→1. Independently computed kappa_2(2)=0.416277305367437044167102342 with 70 summands and mpmath quadrature, matching claimed 18 digits; numerical integration alone does not prove norm asymptotics.

## originality

PASS

The directly matching 2026 primary Lorist–van Neerven–Veraar–Weis arXiv:2608.20266v2 was read in its relevant full PDF Sections 3 and Proposition 3.4 (incl. pages 7-8). Its diagonal geometric kernels serve qualitative non-maximal-regularity of the larger mixed ell_1(ell_r) space, with coarse lower divergence; it does not provide the exact finite-block Bochner L1 norm, log-periodic coefficient kappa_r(b), explicit finite cutoff error or both spacing limits. Blunck 2001 principally concerns discrete/continuous maximal regularity at time p>1 under different hypotheses. Related Resultary spectrum/semigroup entries use different operators or exponents. Potential general vector convolution optimization theorem furnishing the same coefficient under other terminology is a recorded risk.

## value

PASS

This determines quantitative finite-rank severity of a natural endpoint maximal-regularity obstruction, not merely restating qualitative failure. A complete invariant kappa_r(b) distinguishes dense logarithmic eigenvalue levels (vanishing coefficient for r>1) from sparse levels (coefficient 1), with explicit approximation error and all r endpoint cases; these natural spectral-spacing facts are useful independently, with no claim about arbitrary generators or a joint b,N uniform limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
