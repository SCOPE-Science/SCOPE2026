# Independent mathematical audit

## correctness

PASS

Independently recovered both cumulant rates for the stationary fixed-N occupation chain. Write X=k-N/2, C=dN+N²/2, q=C-2X², and let B be the off-diagonal rate operator. The ordered pair density of distinct count events at lag u>0 is π B exp(uL)q. Detailed balance gives π B=π diag(q), so the variance is μt+2∫₀ᵗ(t-u)Covπ(q(K₀),q(Kᵤ))du; this includes the shot-noise term, absent for the integrated rate alone. Direct differences give LX²=C-(4d+2)X² and LX⁴=C+(6C-8d-2)X²-(8d+12)X⁴. Setting both stationary means to zero gives E X²=C/(4d+2) and Var(X²)=Nd(N-1)(N+2d)(N+2d+1)/[4(2d+1)²(2d+3)]. The centered q has relaxation rate 4d+2, so ν=μ+8 Var(X²)/(4d+2), with μ=Nd(N+2d)/(2d+1), as stated. N=1 gives constant intensity; N≥2 gives positive excess. At d=o(N^(2/3)) the denominator of F-1 is o(N²) and the numerator is asymptotic to N²; at the critical scale the ratio is 1/(8c³); above it the bound O(N²/d³+N/d²) tends to zero. The time limit precedes all those scalings. The frozen exact-fraction verifier was inspected, not executed; the finite tests are not needed for this derivation.

## originality

PASS

Credit the established SIP rates, conditional equilibrium, and general activity-variance machinery. The supported distinct claim is the explicit all-successful-jump Fano factor for the closed two-site SIP and its three particle-number scaling limits. No compared source states that claim or eliminates the model-specific centered-rate and amplitude calculation. This is a best-of-knowledge comparison, not proof of publication priority.

## value

PASS

The closed two-site SIP is a natural benchmark with exactly conserved particle number, and its unsigned activity need not be inferred from signed current or static correlations. The formula gives an exact noise benchmark and identifies precisely how coupling must grow with particle number to suppress excess variance. The scale N^(2/3), including its finite crossover amplitude, is informative beyond a small-case check. It does not imply Poisson convergence of the full count law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
