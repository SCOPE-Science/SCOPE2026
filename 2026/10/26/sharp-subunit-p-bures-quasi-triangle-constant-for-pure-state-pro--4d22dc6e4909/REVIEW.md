# Scientific review

## Correctness
**PASS.** The claim is restricted to rank-one positive projections, where the \(p\)-Bures formula reduces exactly to \(\sqrt2\sqrt{1-\cos^p\theta}\). The sharp bound follows from (i) a factored nonnegative second derivative at \(p=2/3\), (ii) convexity inherited for lower exponents via an explicit integral \(L^2\)-norm representation and Minkowski's inequality, (iii) a strictly monotone halving ratio proved by a derivative-ratio average, and (iv) projective-angle triangle geometry. A two-dimensional orthogonal-endpoint midpoint attains equality. The attached deterministic checker passes its finite diagnostics; those diagnostics are not a substitute for the analytic proof.

## Originality
**PASS, provisional pending independent priority verification.** The nearest source (Sra 2026) supplies the \(p\)-Bures formula and proves metricity for \(1\le p\le2\), not the sharp subunit constant. Komálovics–Molnár 2023 (Proposition 8) and Vuong–Osaka 2026 (Theorem 1.3) already prove the qualitative failure of the triangle inequality under the equivalent inverse parameter; neither resolves the exact supremal ratio when \(0<p\le2/3\). Vuong's April 2026 quantitative study concerns nonsharp spectral and local quasi-triangle bounds. Targeted searches for the explicit constant, the exponent \(2/3\), angular convexity, and projective-rank-one equivalences found no controlling stronger result. An unknown older result about power-transformed Fubini–Study distances is a residual priority risk.

## Mathematical value
**PASS.** This is a dimension-independent *sharp* quasi-metric distortion on the natural pure-state boundary of a recently studied operator divergence. The exponent cutoff is not chosen arbitrarily: \(2/3\) is independently proved to be the precise transition for convexity of the angular profile, which explains the stable midpoint extremizer. The result gives all equality geometries and the exact singular scaling as \(p\downarrow0\), rather than a cheap triangle-inequality counterexample.

## Limits and closest coverage
The optimal constant for \(2/3<p<1\) and all mixed states is undetermined. The qualitative nonmetricity claim alone was established earlier and is **not** asserted as the new contribution. Primary sources: Sra arXiv:2610.15889; Komálovics–Molnár JMAA 529 (2024) 127226; Vuong–Osaka arXiv:2610.11021; Vuong, *Quantitative geometry of the symmetric \(\alpha\)-\(z\) Bures–Wasserstein divergence* (2026).

Self-review: passed. Independent audit: not yet performed.
