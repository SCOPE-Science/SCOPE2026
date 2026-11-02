# Scientific review: a universal three-peak spectral ceiling

## Correctness — PASS

For every finite nonempty set of positive force-covariance weights and relaxation rates, positive damping, and positive stiffness, the stationary transfer calculation yields \(S_X(\omega)=B(\omega^2)/P(\omega^2)\). The proof uses the exact derivative \(G=PB'-P'B\) and the cancellation \(G'=PB''-2B\). The reweighted mean \(H=G'/(2Z)\) is strictly decreasing when the oscillator denominator coefficient \(c<0\); when \(c\ge0\) direct differentiation already proves unimodality. The resulting one-turn structure of \(G\), together with \(G(\infty)<0\), proves the absolute bound on critical frequencies and spectral maxima without approximations or unverified continuation. Boundary cases with coincident critical points are classified as shoulders. A direct matrix-resolvent numerical checker and an exact sharp example provide independent finite checks, not infinite proof.

## Originality — PASS on available literature, historical priority provisional

Masoliver and Porrà (1993), particularly its Section V on the power spectrum, already treat the single-exponential covariance and exhibit the three-maximum spectral regime. The only assessed contribution is universal preservation of that ceiling for *arbitrarily many positive relaxation channels*, with an exact derivative-sign criterion. The previously established single-rate result does not imply the assertion for sums of spectra, since generic positive sums need not preserve modal counts. Milotti (1995) considers continuous relaxation spectra and noise color; Grahovac et al. (2016) considers superpositions of OU processes; neither examined material establishes the stated filtered-oscillator mode theorem. Searches for multiexponential harmonic spectra, Stieltjes-transform extrema, and generalized mixed-color resonance found no dominating statement; search silence alone is not novelty evidence. The first-page original PDF and the relevant spectral sections were accessible, but some scanned equations were imperfectly transcribed, and comprehensive historical priority remains uncertain.

## Mathematical value — PASS

The result is an invariant of the number of effective mechanical degrees of freedom: however many strictly positive exponential noise time scales drive a *single* stable scalar oscillator, only one positive-frequency resonance can occur. It provides a falsifiable experimental constraint and prevents multi-timescale forcing from being mistaken for multiple distinct mechanical resonances. The arbitrary-number, sharp global conclusion is not an arbitrary parameter slice or merely a re-evaluation of a known one-rate peak formula.

## Closest literature and limits

The baseline single-rate spectra and three-peak examples belong to Masoliver and Porrà (1993), DOI 10.1103/PhysRevE.48.4309. Milotti (1995), DOI 10.1103/PhysRevE.51.3087, concerns relaxation-mode noise coloration; Grahovac et al. (2016), DOI 10.1007/s10955-016-1616-7, studies superpositions of OU-type processes. The result excludes oscillatory force covariances, arbitrary signed cross-spectral mixtures, multiple oscillators, extra additive detector spectra, and nonlinear interactions. The analytical proof applies to all finite positive mixtures; numerical experiments alone do not establish this.

Self-review: passed. Independent audit: not yet performed.
