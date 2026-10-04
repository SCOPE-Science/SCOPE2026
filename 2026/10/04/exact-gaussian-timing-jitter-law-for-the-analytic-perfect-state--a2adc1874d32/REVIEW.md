# Same-model review

## Correctness

**PASS.** The source-chain endpoint amplitude is known exactly. Substituting a Gaussian timing offset reduces the mean occupation probability to the expectation of \(\cos^{2m}(X/2)\). The finite Fourier expansion and Gaussian characteristic function give the displayed exact sum. Strict monotonicity follows term by term. The \(s=c/\sqrt m\) limit follows from dominated convergence on the Gaussian integral, while the fixed-\(s\) law follows from central-binomial asymptotics plus dominated convergence of the exponentially weighted coefficient ratios. The target-jitter law follows by monotone inversion of the continuous limiting profile. A standalone checker independently reconstructs small-chain Hamiltonian evolution and replays all asymptotic regimes.

## Originality

**PASS, narrowly scoped.** The direct anchor discusses deterministic timing windows and the analytic chain's timing robustness. The original chain paper gives the exact endpoint amplitude but explicitly does not analyze other error sources. The 2006 timing-error paper and the 2015–2016 sensitivity literature treat deterministic readout offsets, derivatives, or lower bounds. Targeted literature searches did not locate a Gaussian timing-distribution average, the finite binomial-exponential law, the \(s=c/\sqrt m\) stochastic profile, or the fixed-\(s\) theta-series asymptotic for this chain.

The \(1/\sqrt N\) scale by itself is not claimed as new; deterministic timing-window work already points to that scale.

## Value

**PASS.** Readout timing precision is an explicit engineering constraint in the source literature. A stochastic clock specification is naturally stated by a standard deviation rather than a worst-case window. The exact law converts that specification into a mean transfer probability for every finite chain, while the two asymptotic regimes distinguish shrinking high-fidelity jitter from fixed timing noise. The target formula gives a directly usable calibration rule, and the theta-series law explains the contribution of periodic revivals under broad timing uncertainty.

Same-model review: passed. Independent audit: not yet performed.
