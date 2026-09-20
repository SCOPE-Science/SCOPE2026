# Same-model review

**Verdict:** PASS.

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The normalized autocorrelation sequence of a stationary reversible chain is the moment sequence of the normalized spectral measure associated with the centered observable. Under the stated support condition \([0,\beta]\), the lag-one correlation is the first moment of that probability measure.

The pointwise and convexity arguments were rechecked separately:

- Jensen applied to \(x^k\) gives \(\rho_k\ge\rho^k\).
- The pointwise inequality \(x^k\le\beta^{k-1}x\) gives \(\rho_k\le\rho\beta^{k-1}\).
- The exact stationary sample-mean variance identity has nonnegative weights on all positive lags, so the simultaneous autocorrelation envelope yields the finite-\(n\) variance envelope.
- The reversible asymptotic-variance integrand \(g(x)=(1+x)/(1-x)\) is convex on \([0,\beta]\). Jensen gives the lower endpoint, while the chord through \(0\) and \(\beta\) gives the upper endpoint.
- Letting \(\beta\uparrow1\) in the explicit upper construction keeps the lag-one correlation fixed and sends the asymptotic variance factor to infinity, establishing the no-ceiling impossibility result.

The finite-state sharpness constructions were also checked. The two-state refresh kernel \(K_r(u,v)=(1+ruv)/2\) has eigenvalues \(1,r\). The product \(K_\beta\otimes K_0\) with the stated linear observable has normalized spectral measure

\[
\left(1-\frac{\rho}{\beta}\right)\delta_0
+
\frac{\rho}{\beta}\delta_\beta,
\]

so its lag-\(k\) correlation is exactly \(\rho\beta^{k-1}\). Mixing this measure with \(\delta_\rho\) preserves the lag-one correlation and fills the entire claimed interval.

The verification artifact checks a representative four-state construction at \((\rho,\beta)=(0.3,0.8)\), including lags 1 through 6 and finite sample sizes \(2,3,5,20\), and then checks the inequalities for 1000 randomly generated finite spectral measures with the same first moment.

Boundary cases were inspected. If \(\beta=0\), then \(\rho=0\) and all positive-lag correlations vanish. If \(\rho=\beta\), the mean of a measure supported in \([0,\beta]\) is at its upper endpoint, forcing the measure to be \(\delta_\beta\), so the lower and upper formulas coincide. For \(n=1\), the finite-sample factor equals one.

The positivity assumption is scientifically material. General reversible chains can have negative spectral support, so the lower-envelope statements are not claimed without positivity.

## Originality

The literature check covered reversible-chain spectral measures, asymptotic variance, variance bounding, effective sample size, integrated autocorrelation time, lag-one autocorrelation, positive Markov operators, autocovariance moment sequences, and shape-constrained autocovariance estimation.

Relevant prior art inspected includes:

- Geyer (1992), which uses the reversible spectral representation to prove positivity, monotonicity and convexity properties for paired autocovariances and develops initial-sequence variance estimators.
- Roberts and Rosenthal (2008), which characterizes variance bounding for reversible chains in spectral terms.
- Łatuszyński and Roberts (2013), which gives the spectral asymptotic-variance formula and explicitly treats positive reversible kernels.
- Berg and Song (2023), which formulates reversible autocovariances as a moment sequence and develops shape-constrained estimation of the autocovariance sequence and asymptotic variance.
- Salmon and Rosenthal (2024), which reviews and extends efficiency-comparison theory for reversible MCMC.
- Recent work through 2026 on effective-sample-size diagnostics and spectral convergence was also checked for an equivalent fixed-\(\rho_1\) extremal theorem.

No inspected source stated the combined sharp result: simultaneous bounds
\[
\rho^k\le\rho_k\le\rho\beta^{k-1},
\]
the induced exact finite-sample and asymptotic variance identification intervals conditioned on \((\rho_1,\beta)\), finite-state common extremizers, and the corollary that lag-one correlation alone permits arbitrarily large integrated autocorrelation time within positive finite-state geometrically ergodic reversible chains.

The originality claim is deliberately narrow. Once the spectral moment representation is available, the endpoint inequalities use classical convexity and one-moment extremal arguments. An equivalent result could therefore exist in classical moment-problem, operator-theoretic, or MCMC literature without using the terminology searched here.

### Residual coverage risk

The main residual risk is that a spectral-theory or moment-problem source may have recorded the same one-moment extremizers as an immediate corollary without framing them as an effective-sample-size or MCMC variance theorem. A second risk is older MCMC diagnostic literature using AR(1) comparison language rather than spectral-measure language.

No inaccessible source was treated as evidence of non-coverage.

## Value

The result converts two quantities that are often available or interpretable in MCMC analysis—lag-one correlation and a spectral ceiling—into a complete sharp identification interval for the variance of the sample mean, at both finite and asymptotic sample sizes.

It also clarifies the status of the AR(1) lag-one formula under positivity: it is the best-case lower endpoint for integrated autocorrelation time. Thus a single lag-one correlation cannot by itself certify a useful asymptotic effective sample size; the true inefficiency can be arbitrarily larger even in finite-state geometrically ergodic examples.

The common finite-state extremizers make the bounds directly reusable as worst-case benchmarks rather than only qualitative spectral estimates.

## Search/access limitations

Originality is to the best of our knowledge, not an exhaustive guarantee. Search engines may miss results stated as general extremal properties of Hausdorff moment sequences or positive self-adjoint contractions rather than as Markov-chain variance bounds. The principal spectral and MCMC references above were available in abstract or full-text form sufficient to verify their stated scope; no located theorem matched the complete fixed-lag-one identification result.
