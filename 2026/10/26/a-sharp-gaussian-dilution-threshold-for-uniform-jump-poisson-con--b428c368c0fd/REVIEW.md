# Scientific review: uniform-jump Gaussian-dilution threshold

## Correctness — PASS

The statement fixes the Poisson rate, uniform mark distribution, variance normalization, one-sided optimal scale, and every boundary case. A direct Lévy exponent calculation yields \(K_X(t)=Vt^2[1+wtH(t)]/2\). The envelope optimization follows by exact algebra including the restricted admissible frequency domain. The key nonstandard lemma is proved in full: log-concavity of the tilted integrated-tail density gives increasing hazard, a strict second-to-first moment ratio, and strictly decreasing \(H'/H^2\). This establishes uniqueness globally; no finite numerical search substitutes for it. Piecewise polynomial log-concavity for uniform marks, rational moment formulas, and the quadratic critical expansion are independently recalculated. The embedded verifier passed 1,488 exact-rational and finite numerical checks. Critical limits and the fact that the optimizer is at zero only as a limiting supremum are explicit.

## Originality — PASS, with residual risks

Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws* (arXiv:2610.00032v1), supplies the canonical transform, general variational formula, M-class criterion and Gaussian convolution monotonicity. These are credited and not asserted as new. That source's worked examples are Gamma and bounded two-point jump laws; it does not specify a uniform jump mark, an exact \(257/372\) Gaussian-to-rate transition, a strict IFR/log-concavity unique optimizer theorem, or the critical Taylor law. Chen and Wang (arXiv:2609.02590v1) study signed Skellam jumps and do not assert optimizer uniqueness even in that example; their threshold therefore does not imply the uniform positive-jump result. Leskelä and Välimaa (arXiv:2508.12103) optimize a Poisson-comparison variance proxy rather than the variance-exact sub-gamma pole. Search comparisons also examined known exact deterministic-unit-jump Gaussian smoothing cases and did not use them as novelty of the present claim; uniform continuously distributed marks and the log-concave-tail structural implication are genuinely different. A prior implicit variational formula could make numerical evaluation accessible; historical equivalent IFR terminology remains possible. Searches do not prove priority.

## Mathematical value — PASS

The fixed-true-variance sub-gamma envelope is a natural concentration tool for noisy marked Poisson counts. Choosing uniform jumps is a continuous-amplitude benchmark and creates a nontrivial critical variance fraction distinct from the deterministic-jump value \(3/4\). The exact and sharp \(\sigma^2/\lambda=257/372\) threshold identifies whether a low-frequency cumulant obstruction is sufficient or whether a finite exponential tilt gives a strictly stronger obstruction. The global unique-optimizer result is not a tautological re-expression of the variational characterization: its proof uses a hazard-ordering principle for an entire class of log-concave integrated jump tails. The quadratic onset quantifies the transition. No larger theorem is required to justify this structural and natural exact computation.

## Sources and limitations

Inspected primary preprints: Y. Chen, arXiv:2610.00032v1 (abstract; Sections 2–8, notably Theorem 3.1, Theorem 4.2, Proposition 5.1, Section 7); Y. Chen and X. Wang, arXiv:2609.02590v1 (Sections 2–7, notably Skellam Section 6 and its lack of unique-optimizer assertion); L. Leskelä and I. Välimaa, arXiv:2508.12103v3 (Sections 2–5 and examples in the accessible HTML). The result does not cover non-log-concave tails, signed jumps, or free variance proxies. Independent mathematical audit was not performed.

Self-review: passed. Independent audit: not yet performed.
