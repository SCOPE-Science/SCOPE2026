# Independent mathematical audit

## correctness

PASS

For each fixed opposing sketch, the residual restriction is εI+(1−ε)vvᵀ in dimension d=n−1 with ||v||²=H=ε²R²/(X²+ε²R²). Both basic estimates have conditional mean tr A. Gaussian and uniform-direction moments give conditional variances 2[S²+(d−1)ε²] and 2(d−1)(1−ε)²H²/(d+2), with S=ε+(1−ε)H. The |X|/R density is K(1+a²)^{−n/2}, K=2Γ(n/2)/(√π Γ((n−1)/2)); scaling a=εu gives E H²/ε→Kπ/4=c_n and E H=O(ε). The mixed product is O(ε²) because each direction determines its own S and is independent of its Gaussian radius, independently for the two sketches. Thus averaging halves the leading individual variances. When n=2 the normalized residual uses the exact Rayleigh value on the one-dimensional complement for every defined probe. The repaired tail uses a<ε√((1−t)/(t−ε)), whose scaled probability tends to K√((1−t)/t). For equal means and equal basic variances v, E V̂=(v−c)/2 and Var(T)=(v+c)/2; hence the repaired difference is exactly −c=O(ε²). Those identities independently establish the affected proxy and tail statements.

## originality

PASS

Neither the original estimator, its residual normalization, nor the general expected-proxy identity is claimed new. The surviving claim determines sharp constants for the two original Gaussian estimators on the spiked family, proves that correlation does not affect the leading term, and measures the rare high-residual events. The inspected sources give general bounds or different probing and residual constructions, not these coefficients or an implication for them.

## value

PASS

In a natural numerical-linear-algebra stress family the error is driven by rare failed sketches, not typical residuals. The result quantifies the exact gain of an existing normalization and distinguishes the two-probe dependence from leading single-probe noise. The budget is below dimension for n≥5. This remains useful without a claim of algorithmic optimality or universal normalization benefit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
