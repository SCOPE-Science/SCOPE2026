# Scientific review: bounded VaR surrogate for the LAPFr model

## Correctness — PASS

The source PDF (DOI:10.3934/math.20251187, Eqs. (1)–(3) and (13), pp. 27017–27018 and 27022–27023) provides both the exact CDF and the Lambert-W surrogate, including the domain \(\alpha,\theta,\beta>0\). The proof substitutes the surrogate equation into the true CDF, giving the *exact* achieved coverage \(q\log(1+z)/z\). Its strict deficit follows from \(\log(1+z)<z\). The finite surrogate endpoint, sharp generator-parameter coverage range, and true upper-tail divergence follow from monotone inversion and the explicitly calculated derivative \(h_\beta'(1)\). The final lower-tail statement uses expansions at zero. Independently replayed `verify.py` checks scalar inversion, numerical claims and the coverage identity. No finite numerical test is used as the proof of an infinite limit.

## Originality — PASS, with residual priority risk

The main paper already calls Eq. (13) an approximation; its novelty is not challenged on that point. It also states that the approximation is suitable for high confidence levels, without providing the exact coverage identity, the universal sharp under-76% limiting coverage ceiling, or the finite-versus-diverging quantile theorem. The related GLEP model in AboAlkhair et al. (2025, DOI:10.3390/math13193097) recommends numerical inversion for a different logarithmic generator. That related general principle is not this exact model-specific high-tail calibration failure. Searches for the source title, Lambert-W inversion, VaR calibration, asymptotic quantile error and equivalent generators revealed no indexed covering result. An unindexed correction or a more recent follow-up remains possible; no uniqueness or independent validation is claimed.

## Value — PASS

VaR is the central quantity the source uses for extreme financial and insurance losses. Unlike a small truncation or rounding error, using the printed surrogate at nominal 99% confidence can yield only about 72.28% actual model coverage for an admissible parameter set. More fundamentally, the surrogate never diverges while the true quantile does. The proof identifies the entire offending parameter regime and supplies a robust exact inversion procedure, restoring the intended risk threshold without changing the probability model. This is substantively consequential even though the underlying inequality and scalar root-finding technique are standard.

## Closest literature and limits

Aljadani (2025), DOI:10.3934/math.20251187, Section 3.1, is the precise source of the disputed high-confidence approximation. AboAlkhair et al. (2025), DOI:10.3390/math13193097, Section 2.2, documents numerical inversion of a related log-exponential family. There is no claim that published datasets, fitted estimates, or numerical software actually used the displayed approximation rather than an exact inverse. The analysis is a mathematical conditional statement about Eq. (13), not an independent audit of any third-party empirical work. The related publisher page returned an access restriction on a later direct fetch; accessible indexed section text supported only a limited comparison.

Self-review: passed. Independent audit: not yet performed.
