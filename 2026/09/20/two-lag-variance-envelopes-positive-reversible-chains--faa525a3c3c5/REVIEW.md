# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument reduces the normalized autocorrelation sequence of a positive reversible chain to a probability moment sequence on \([0,1]\). The two extremal measures have been checked algebraically to reproduce exactly the prescribed first two moments. The lower and upper inequalities follow from quadratic Hermite interpolation with remainder signs \(x(x-b)^2\ge0\) and \((x-a)^2(x-1)\le0\), respectively.

For later lags, \(x^k\) has strictly positive third derivative for \(k\ge3\). For finite-horizon sample means, the kernel \(H_N\) is quadratic for \(N\le3\) and has strictly positive third derivative for \(N\ge4\). For long-run variance, the transform \((1+x)/(1-x)\) has positive third derivative, and the lower extremizer gives the claimed closed form. The no-finite-upper-bound statement is supported by an explicit two-point family with exactly fixed first two moments and an upper support point tending to one.

Finite-state realizability was checked directly using products of symmetric two-state reversible kernels. This also verifies that the extremal and approximating spectral measures are realizable by Markov chains rather than only by abstract measures. Exact-rational verification reproduces the stated worked example and several additional parameter cases.

Boundary cases were examined separately: \(r_1=0\) forces the spectral measure to \(\delta_0\); \(r_2=r_1^2\) forces a single spectral atom and hence a geometric autocorrelation sequence; and \(r_2=r_1>0\) requires spectral mass at one and yields infinite long-run variance for that centered component.

## Originality

**PASS, to the best of our knowledge.** The spectral moment representation is classical and is not claimed as new. The general truncated Hausdorff/Markov--Krein extremal mechanism is also not claimed as new.

The closest modern source inspected was Berg--Song (2023), which explicitly represents reversible-chain autocovariances as a moment sequence, develops the associated complete-monotonicity structure, and uses it for shape-constrained sequence and asymptotic-variance estimation. Geyer (1992) supplies the classical positive/monotone/convex initial-sequence perspective; Kipnis--Varadhan (1986) supplies the reversible spectral framework; Roberts--Rosenthal (2008) connects the upper spectral edge with variance bounding.

Literature checks included exact and synonymous searches involving the first two autocorrelations, lag-two information, asymptotic variance, effective sample size, truncated Hausdorff moment bounds, moment representations of reversible autocorrelations, and Markov--Krein extremality. No source located an explicit sharp envelope for all later autocorrelations or finite-horizon mean variance from exactly \((r_1,r_2)\), nor the fixed-two-lag finite-state construction showing unbounded asymptotic variance when \(r_2>r_1^2\).

The principal residual originality risk is that these formulas may occur as an unadvertised specialization of classical truncated moment theory or in older MCMC spectral-diagnostic work under different terminology. This is a meaningful risk because the mathematical extremal mechanism is classical; the novelty claim is therefore restricted to the explicit reversible-chain consequences and their realizability/impossibility interpretation.

## Value

**PASS.** Short-lag autocorrelations are routinely used as diagnostics for Monte Carlo dependence, while uncertainty of sample means depends on the full correlation tail. The result states exactly what two population lags can certify in the positive reversible setting: all finite-horizon variances admit computable sharp intervals, but asymptotic efficiency can remain arbitrarily poor unless the first two lags lie on the geometric boundary \(r_2=r_1^2\). The finite-state construction makes this limitation concrete rather than merely formal.

## Scientific limitations

The Markov operator must be positive semidefinite; general reversible chains with negative spectrum require a different moment problem. The bounds are for a fixed observable and exact population autocorrelations, not for estimated lags with sampling uncertainty. The upper finite-horizon endpoint with positive spectral variance uses an atom at eigenvalue one and is therefore nonergodic, although finite-state irreducible chains approach it arbitrarily closely while keeping both prescribed moments exact. No claim is made that the generic two-moment extremal lemma is new.
