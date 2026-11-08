# Scientific review: a critical fourth-cumulant boundary layer

## Correctness — PASS

The claim specifies the original active preferential-resetting process of Boyer and Majumdar [1], including relocation of **both** position and velocity. Their exact Fourier–Kummer characteristic function provides the starting point, not an assumed approximation. The proof retains the time-independent gamma-function amplitude and derives a uniform differentiated asymptotic on a complex Fourier neighborhood for \(r/\gamma\in[3/2,5/2]\). Exact Taylor coefficients produce the positive critical fourth cumulant and the universal \(1/\log(\gamma t)\) threshold displacement. The sign and uniqueness assertions follow from strict negativity of the derivative of \((2-\rho)/\rho^2\) throughout the stated compact interval. The proof deliberately does not assert uniqueness outside that interval. Exact symbolic expansion and independent finite-time generator-moment integration passed 39 checks in the supplied standalone program. Numerical results alone were not used as an infinite-time proof.

## Originality — PASS, with publication-priority uncertainty

Boyer--Majumdar [1] already provide the complete Fourier expression and its leading logarithmic large-deviation exponent. Consequently neither that expression, the Gaussian logarithmic variance, nor the leading fixed-rate fourth-cumulant term is claimed here. The distinction is the finite fourth-cumulant constant at exact cancellation, the uniform moving-parameter excess-kurtosis profile, and the eventual **unique** finite-time sign threshold with its explicit displacement. Equation (70) of [1] drops the needed amplitude; its Appendix B expands only through the variance. Source [2] treats higher moments for a discrete passive preferential relocation walk; its parameters cannot encode a telegraph-switching critical ratio. Source [3] treats Brownian resetting with memory and therefore lacks a persistence-rate cancellation. Targeted scientific literature and indexed-record searches did not find the exact critical-layer theorem. No absence-of-results search proves uniqueness, and a previously unindexed or implicit equivalent analysis of the source's full transform remains a genuine risk.

## Mathematical value — PASS

The finite-time fourth cumulant is a natural and measurable next-order shape statistic when the stationary variance is absent and position spreading is ultraslow. The underlying source predicts Gaussian central behavior with slow logarithmic corrections but does not classify how the sign of the leading non-Gaussian correction depends on the ratio of reset and orientation-switching rates. The new positive constant at cancellation distinguishes an exact zero of the leading logarithmic term from a Gaussian law; the unique shifted zero quantifies where the sign actually reverses for long but finite observations. This is a motivated singular parameter layer, not an arbitrary fixed-parameter calculation or a routine recomputation of the published variance.

## Closest literature and limits

1. D. Boyer and S. N. Majumdar, *Active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439, especially Eqs. (9), (13), (69)–(70), Appendix B. https://arxiv.org/abs/2312.13439 .
2. D. Boyer and C. Solis-Salas, *Random walks with preferential relocations to places visited in the past and their application to biology*, arXiv:1403.6069, higher-moment asymptotics on PDF page 3. https://arxiv.org/abs/1403.6069 .
3. D. Boyer, M. R. Evans and S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743, continuum passive model and Fourier equation. https://arxiv.org/abs/1611.06743 .
4. NIST DLMF §13.7, uniform asymptotic regime for Kummer's function. https://dlmf.nist.gov/13.7 .

No numerical minimum observation time is supplied. No global statement about all positive reset rates, all memory kernels, or inferential accuracy from finitely sampled trajectories is made. Publication priority beyond accessible records remains subject to independent checking.

Self-review: passed. Independent audit: not yet performed.
