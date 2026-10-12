# Scientific review: first signed rare circular scan correction

## Correctness — PASS
Gamma-tail Taylor coefficients and the exact beta integral give the local new-cluster intensity. The circular local-dependency graph yields a Poisson total-variation error of order \(O(N^{-1}+N^{-2/(k-1)})\), negligible compared with the signed correction for each fixed \(k\ge4\). The exceptional all-window event is super-polynomially rare. A gamma-concentration sandwich eliminates random-spacing normalization at negligible order. The standalone checker verified 145 exact local algebraic assertions; finite checks are not substituted for the universal proof.

## Originality — PASS, subject to priority risk
The full lead source [1] provides exact formulas for different scan ranges and not this signed large-population coefficient for fixed \(k\ge4\). The older exact-recursion, Bonferroni and Poisson-approximation literature includes relevant general methods, which do not by their identified claims state the coefficient proved here. Full access to some older sources was unavailable; they could contain an equivalent unstated expansion. This is a material residual priority risk, not proof of uniqueness.

## Value — PASS
A quantitative correction to the limiting rare-cluster probability is a natural statistical quantity for assessing finite-population scan significance. Its negative sign and explicit coefficient identify the first bias caused by adjacent overlapping windows, rather than an arbitrary parameter slice or a routine constant improvement. The excluded case \(k=3\) marks a mathematically distinct normalization scale.

## Limits
Fixed \(k\ge4\), fixed \(t>0\); no uniformity or independent validation. See the proof and references in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
