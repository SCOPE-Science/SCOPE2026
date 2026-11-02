# Self-review

## Correctness — PASS
The exact survival law is reconstructed by enumerating injective mapping paths with prescribed indegrees and averaging over the independent uniform start. Its \(\{0,d\}\) specialization is a finite binomial product. Taylor expansion of logarithms through cubic order, a Gaussian envelope to discard large paths, and half-line Euler–Maclaurin summation give the stated order-one coefficient with \(O_d(n^{-1/2})\) remainder. The limits \(d\ge2\), \(d\mid n\), and \(n\to\infty\) at fixed \(d\) are explicit. `check.py` uses exact rational exhaustive small-instance enumeration and separate numerical asymptotic comparisons; no finite check substitutes for the infinite proof.

## Originality — PASS (with historical priority risk)
The 2018 Leckey–Wormald paper directly implies the exact finite survival product after averaging, so neither that combinatorial identity nor the Rayleigh leading mean is attributed as new. Its Theorems 2.1–2.2 give leading weak/moment limits, with no explicit order-one offset. Martins et al. (2017 preprint, 2018 conference paper) study global cyclic-period products and orders rather than this correction. The older 2015 Martins–Panario abstract discusses mean rho-length heuristics and is the closest incompletely inspected source; full text was not accessible, so this remains a real priority risk. Semantic research-record searches found related collision/expanding-map results but no comparable formula. Originality is limited specifically to an explicit second-order asymptotic extraction with a degree-dependent sign transition, not the underlying exact distribution.

## Value — PASS
Restricted-indegree mappings are established benchmarks for iteration/first-repeat costs in Pollard-type polynomial heuristics. A leading square-root law cannot identify whether the finite-size bias is positive or negative. The new offset yields a complete rational correction for each fixed degree, a sign change at degree four, and an analytic remainder. The sign distinguishes classes that have similar leading Rayleigh behavior after coalescence scaling. It is not claimed to predict actual polynomials at order one, where exceptional indegrees matter.

## Closest sources and limitations
Leckey–Wormald, arXiv:1803.02667v1 (2018); Martins–Panario–Qureshi–Schmutz, arXiv:1701.09148 (2017); Martins–Panario, arXiv:1505.02983 (2015), abstract only; Hansen–Jaworski, arXiv:math/0603529 (2006). Residual risks include unknown priority in the older rho-length paper and classical asymptotic analysis of functional mappings. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
