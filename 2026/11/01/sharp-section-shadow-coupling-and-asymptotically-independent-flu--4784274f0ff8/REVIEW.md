# Review: Sharp section–shadow coupling and asymptotically independent fluctuations of regular simplices

## Correctness — PASS

For every integer \(N\ge3\), all variables refer to the same Haar-unit normal in the zero-sum space. The standard simplex facet has area \(F_N=\sqrt{N-1}/(N-2)!\). Cauchy's projection formula gives the normalized perpendicular brightness \(Y_N=\sqrt{N/(N-1)}\sum|U_i|\). Crossed-simplex-edge combinatorics gives the simultaneous section vertex count \(C_N=p(N-p)\). With each sign class summing to an opposite mass, Cauchy–Schwarz proves the sharp upper bound and positivity proves the strict lower bound; the sign-chamber sphere is connected, making the range complete. Exact first and second moments follow from spherical absolute products with pairwise facet-normal inner product \(-1/(N-1)\). A Gaussian-sample representation and two carefully linearized influence functions establish a joint bivariate normal law, with asymptotic independence from odd/even parity; squaring the sign-count fluctuation supplies the chi-square section deficit. The critical Gaussian remainder is \(o_p(1)\) by a grid-based empirical-cdf argument and norm-expansion estimates. A standalone program independently reconstructs projected simplex hulls, checks finite signed edge crossings, extremizers, spherical-moment integrals and Monte Carlo fluctuations; it prints `ALL_SIMPLEX_SECTION_SHADOW_CHECKS_PASSED`. The experiments are finite checks, not infinite proofs.

## Originality — PASS (historical priority provisional)

The full published text of *Joint chi-square face-vector fluctuations of random central regular-simplex sections* (2026, public research note, identifier `aa90c887fe90`) and *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts* (2026, identifier `d3f9b0447a8e`) already establishes the section-only Gaussian-sign reduction and chi-square law. Those ingredients are credited. The new mathematical statement is the **joint sharp feasibility interval** between section vertices and perpendicular shadow volume, including its complete equality class, and the **same-normal asymptotically independent joint fluctuations** with exact brightness moments. Horváth–Lángi (arXiv:2012.08955, first posted 2020-12-16) gives a general brightness identity, and Kabluchko–Litvak–Zaporozhets (arXiv:1511.08479) analyzes another width statistic and cube projection fluctuation constant. The inspected results do not imply the claimed two-observable feasible domain or same-direction joint probability law. Direct searches under dualities, aliases, inequalities, and section–projection coupling found no dominating statement; database absence alone is not a novelty certificate. The 1992 random-simplex projection paper and a 2020 section-volume paper had no sufficiently accessible complete text; hidden equivalent formulations remain a priority risk.

## Mathematical value — PASS

The relationship is geometrically motivated: observing a regular simplex from one direction produces both a central section with a discrete complexity and a perpendicular shadow with a continuous size. The sharp deterministic envelope gives the complete joint feasible set, with an explicit characterization of its maximizers; it is more than two unrelated marginal formulas. The limit theorem establishes that a genuine finite-dimensional geometric restriction becomes asymptotically negligible at the natural fluctuation scales and describes the remaining Gaussian/chi-square effects. The claim is not a reparameterization of the known simplex vertex-count law: it involves the additional projection body, its first two exact moments, and an independent even influence function.

## Closest sources and limitations

1. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, arXiv:2012.08955 (2020-12-16): brightness identity, not a joint regular-simplex law.
2. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (2015-11-26): different width observable, but closely related Gaussian fluctuation constant.
3. Published note `aa90c887fe90` (2026): all central regular-simplex section face counts, without joint projection brightness.
4. Published note `d3f9b0447a8e` (2026): central section vertex count and chi-square law, without joint projection brightness.
5. F. Affentranger and R. Schneider, *Random projections of regular simplices*, DOI:10.1007/BF02187839 (1992): only abstract available, residual priority uncertainty.

The result is restricted to regular simplices, genuinely central sections and codimension-one orthogonal projections. Generic lower envelope is an infimum; joint independence is only a weak limit. An independent mathematical audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
