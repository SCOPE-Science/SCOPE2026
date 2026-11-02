# Self-review

## Correctness — PASS

The exact Zak multiplier follows from integer-modulation orthogonality and support of the hat window, without an unproved spectral diagonalization. The positive multiplier has a bounded inverse with an explicit absolutely convergent Fourier expansion. Extracting the canonical dual's coefficients gives a positive-cell integral with precisely \(q\) nondegenerate maxima of the exponential base. Laplace's method, with the strict complementary spectral gap off small neighborhoods of those maxima, yields the claimed \(n^{-1/2}\) factor and explicit strictly positive coefficient. Evenness plus geometric-tail comparison gives the truncation constant. Exact normalization, boundary behavior, and the fixed-\(q\) quantifiers are checked. The supplemental numerical checker passed 528 assertions; none is substituted for an infinite proof.

## Originality — PASS (provisional historical priority)

The exact tail exponent, complete \(q\)-dependent leading constant, and symmetric truncation-error coefficient are not directly stated in the inspected relevant 2023 B-spline frame-region/obstruction papers, the inspected 2018 frame-set/compact-dual construction, or the 2000 qualitative dual-decay framework. The closest earlier explicitly relevant paper by Janssen (1996) treats minimal duals at integer redundancy, but only its abstract could be checked: full-text comparison is an unresolved bibliographic risk. General Zak inversion by itself supplies neither the explicit asymptotic coefficient nor its validation. Existing exact frame bounds and Zak-fiber spectral laws are prior context, not credited here as new.

## Mathematical value — PASS

The canonical dual is the distinguished minimum-energy reconstruction window even when alternative compact duals exist. Its sharp spatial truncation error controls how reconstruction changes when the infinitely supported canonical dual is physically truncated. The nonvanishing limiting exponential rate under arbitrarily dense integer translation oversampling, and the universal Gaussian saddle-point factor \(n^{-1/2}\) in cell energy, are structural rather than arbitrary finite computations.

## Limits and closest literature

All conclusions are for \(g=(1-|x|)_+\), step sizes \((1/q,1)\), and each fixed \(q\ge2\). They do not assert uniqueness in the literature or independence from a broader unpublished theorem. Relevant literature: Ghosh–Selvan arXiv:2304.11322; Ghosh–Selvan arXiv:2310.01141; Atindehou et al. arXiv:1806.05614; Bölcskei–Janssen, *Gabor Frames, Unimodularity, and Window Decay* (2000); Janssen, *Some Weyl-Heisenberg frame bound calculations* (1996, abstract only). Independent mathematical validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
