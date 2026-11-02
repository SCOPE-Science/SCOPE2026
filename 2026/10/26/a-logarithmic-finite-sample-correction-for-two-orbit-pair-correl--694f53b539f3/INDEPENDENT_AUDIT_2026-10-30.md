# Independent mathematical audit

## correctness

PASS

For b>=2 integer and two independent Haar circle seeds X,Y, the Fourier expansion of each centered cross-hit H_r(b^i X-b^j Y) imposes two independent frequency cancellation equations. Nonzero covariance requires i'-i=j'-j and equals the Bernoulli kernel C_h(r)=[B2({(b^h-1)r})-B2({(b^h+1)r})]/b^h. Counting signed common shifts gives exact Var(Q_N)=C0(r)+2 sum_{h=1}^{N-1}(1-h/N)^2 C_h(r), r=s/N. For (b^h+1)r<1, C_h=2r b^(-h)-4r²; the global Lipschitz bound |C_h|<=2r b^(-h) controls the remaining shifts. Splitting at H=floor(log_b(N/(2s))) gives N Var(Q_N)=2s(b+1)/(b-1)-8s²(log_b N)/N+O_{b,s}(1/N), with logs and error normalized correctly. Independent exact rational interval-intersection versus Bernoulli tests succeeded in 48 cases. The two-orbit index covariance is structurally different from the previously published one-orbit covariance. No CLT or further periodic O(1/N) constant is claimed.

## originality

PASS

The closest published Resultary record on the same expanding map was read in full at its mathematical RESULT.md: Sharp second-moment inflation for expanding circle-map pair correlations concerns distinct pairs of times within ONE orbit from a single seed, obtains leading 4s(b+1)/(b-1), and bounds its remainder by O(log N/N). That statement does not imply the present two-INDEPENDENT-seed covariance selection or the explicit negative log coefficient. Baker–Todd 2026 Theorem A describes pair-correlation convergence, not this exact critical variance; available abstract and related summaries were examined, but full primary paper remained inaccessible. Rudnick–Zaharescu, Rudnick–Technau and Chaubey–Yesha address lacunary correlations and convergence/variance bounds, not the inspected fixed-seed cross-variance formula. Originality is a best-of-knowledge determination, qualified by inaccessible primary full text and alternate Fourier-covariance presentations.

## value

PASS

Finite-sample noise and dependence in pair correlations of two orbits are motivated by the dynamical-statistics question; the single-shift selection rule explains correlation inflation, and the nonzero logarithmic correction offers a sharp finite-size calibration not present in independent re-sampling. The result is an exact structural second-moment law for a canonical expanding system, not merely a generic variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
