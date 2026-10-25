# Independent mathematical audit

## correctness

PASS

For r,D,L>0 and -1<a<0, the exact backward generator D∂²+r(f(ax)-f(x)) yields a Laplace-resolvent characteristic-series with factors s+r+Da^{2j}k². Contractive Laplace perpetuity gives stationary π_L>0. Strong Markov decomposition at a Brownian point hit gives G_s(x,L)=E_x[e^{-sτ_L}]G_s(L,L) (jump crossings do not count); sG_s(L,L)→π_L. Two denominator factors bound the resolvent difference by |a|^n|L-x|∫|k|/[(1+ck²)(1+ca²k²)]dk, equal to |a|^n|L-x|log(a^{-2})/[c(1-a²)], yielding dominated convergence, absolute Fourier-series convergence and explicit tail bound. Independent Fourier cosine quadratures at D=r=L=1,a=-1/2, using 19 terms, found π_L≈0.2028088623482, E_0τ≈1.3472474853 and κ≈1.6786337452; differences from package numbers reflect truncation/quadrature and are bounded. This is an infinite-parameter proof from the resolvent, not a claim of interval-certified quadrature. Minor documentation inconsistency: RESULT.md describes verify.py as standard-library-only but actual inspected script imports NumPy and SciPy; this does not change mathematical content.

## originality

PASS

Biroli et al. derive the same negative-rescaling MFPT boundary-value equation but explicitly supply κ through simulations in Sec. III.B; the reviewed all-real-x Fourier potential kernel and κ evaluation are not in that section. Classical local-time/Green potential identities are acknowledged methods, not new.

## value

PASS

Closes the explicit undetermined negative-reset boundary constant in a precisely posed first-passage problem with an all-starting-point, simulation-free integral-series resolvent and geometric truncation error. The constant was a genuine missing quantitative input in a relevant published analysis; the formula is useful without finite-window simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
