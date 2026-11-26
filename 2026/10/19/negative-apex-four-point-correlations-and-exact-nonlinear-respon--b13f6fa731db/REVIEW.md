# Independent mathematical audit

## correctness

PASS

Summing each apex gives a constant times exp(AB·log cosh(2G/T)/2); at the specified R this cancels the rung exactly. The leg-spin law is the product of two stationary zero-field Ising chains with independent bond increments of mean ρ. The conditional apex mean is u(A+B)/2, with conditional independence across sites. For distinct sites all mixed moments in the cumulant may use these means, and cumulants add over the independent legs. In one leg with ordered gaps a,b,c the fourth moment is ρ^(a+c); the adjacent pairing cancels it and the two crossed pairings both equal ρ^(a+2b+c). Multiplying the one-chain cumulant by 2(u/2)^4 gives exactly the negative crossed factorization. In the density, using S_i²=1 gives repeated-index cumulants −2, −2C_ij, −2C_ij² and −2C_ij C_ik for patterns 4, 3+1, 2+2, and 2+1+1. With their ordered multiplicities and the 24 permutations of four different sites, each summand is absolutely summable after anchoring; translation multiplicities divided by N tend to one for fixed offsets. An independent transfer-matrix check uses a dimensionless apex tilt x=h/T. The leg Markov operator in the symmetric basis 1,(A+B)/√2,AB has eigenvalues 1,ρ,ρ². The site tilt is cosh(x) times 1+(u/2)(A+B)tanh(x). Put t=tanh(x), v=u/√2. The simple eigenvalue λ(t) near 1, excluding cosh(x), satisfies λ−1=v²t²ρ/[λ−ρ−v²t²ρ³/(λ−ρ²)]. Expanding λ=1+a t²+b t⁴+O(t⁶) gives a=v²ρ/(1−ρ) and b=v⁴ρ⁴/[(1−ρ)²(1−ρ²)]−v⁴ρ²/(1−ρ)³. The fourth pressure derivative in x is −2−16a+24b−12a², exactly the displayed density. The positive-temperature spectral gap at zero gives analytic pressure near zero and bounded boundary corrections to the block log generating function and its derivatives, justifying the thermodynamic response. The third h derivative of magnetization is the density divided by T³; the cubic Taylor coefficient has the further factor 1/6. 3+2ρ−3ρ²=3(1−ρ²)+2ρ>0, and 1−ρ∼2e^(−2J/T) yields −3u⁴e^(6J/T)/8 at fixed u. Read VERIFICATION.md and verify.py without executing them; the recorded 38 checks include finite periodic comparisons at lengths 30 and 60, not a proof of the limit.

## originality

PASS

Compensation and the independent-leg reduction are known and not credited. The statement-level comparison separates that mechanism, two-point functions and linear apex susceptibility from the evaluated distinct-site connected four-point and cubic-response formulas. No equivalent evaluated result or dominating assertion was found in the inspected sources.

## value

PASS

The compensated point is motivated by the ladder's established correlation and linear-response behavior. The crossed identity identifies both spatial dependence and strict sign of the first non-Gaussian connected statistic at four distinct sites. The integrated formula handles repeated sites and gives an exact nonlinear susceptibility with a quantitatively different strong-leg divergence, usable for checking transfer calculations and comparing responses. It is not a claim of a phase transition or of a sign theorem outside the specified scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
