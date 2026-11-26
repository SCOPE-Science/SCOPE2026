# Independent mathematical audit

## correctness

PASS

Checked the entire initial-support and rate quantifiers. The simplex and all coordinate faces are invariant. With s*=1−δ, W=Σr_i x_i and G=Σp_i x_i x_{i+1}, the exact identity S′=(s*−S)W−G yields S′≥s*r_min S−(r_max+Σp_i)S², hence an eventual positive population floor. The ratio y_i=x_i^(1/r_i)/Z with Z=x_a^(1/r_a) at the first occupied index cancels the vacancy term exactly: (log y_i)′=−p_{i−1}x_{i−1}/r_i. Since all y_i are nonincreasing, S≤Σ(y_i(0)Z)^(r_i), so the population floor bounds Z away from zero. The first species of each occupied run has constant y_i; a predecessor bounded away from zero forces exponential decay, while an integrable predecessor yields a strictly positive limiting y_i. This proves alternating support on each run, including singleton runs and initially absent gaps. Every adjacent product decays exponentially, and the forcing equation (S−s*)′=−W(S−s*)−G makes S−s* exponentially small. The survivor quadrature has a unique normalization root with positive derivative, giving exponential coordinate convergence. Time averaging the exact log ratio gives the extinction exponents for initially present eliminated species only. At a fully supported odd equilibrium the even rows form the diagonal invasion block; the odd block has rank one and eigenvalue −Σ_odd r_iℓ_i, leaving precisely the asserted tangent zeros. Read the checker without executing it: there are 420 ratio assertions over 105 rational cases, not 420 distinct cases, plus the population-balance assertions and four finite RK4 examples. This wording issue does not affect the analytic proof.

## originality

PASS

The earlier homogeneous-demography version already covers run-parity selection and exponential convergence and implies its own corresponding extinction exponents. The frozen theorem's substantive extension is to genuinely unequal reproduction and proportional mortality rates with common break-even vacancy. That class, with weighted limit composition and sharp exponents, is not implied by the homogeneous theorem or the general convergence statements inspected.

## value

PASS

The unequal-rate extension separates the effect of turnover from the common ecological threshold: distinct clocks and attack strengths change terminal composition and extinction speed but not the support picked from each initially occupied run. That answers a selection question left open by equilibrium counting and identifies which individual disappearance rates depend on the selected trajectory. The contribution is more than the equilibrium independent-set restriction or a rerun of the homogeneous rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
