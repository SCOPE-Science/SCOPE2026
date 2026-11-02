# Scientific review

## Correctness — PASS

For stationary iid positive finite-second-moment renewal intervals, the renewal-reward identity gives \(C(s)=D\mathbb E[(L-|s|)_+^2]/\mathbb E L\). Double integration of the harmonic Green kernel gives the exact variance functional. Strict Jensen follows from a directly computed positive second derivative; this is presented as established elementary machinery. A direct exponential integral yields both periodic-uniform-phase and Poisson variances. For \(f(z)=z^2-2z+2(1-e^{-z})\), the derivative of \((1+z)f(z)/z^3\) has an absolutely convergent power series with positive coefficients \((n-3)(n+2)/n!\) for every integer \(n\ge4\), proving strict monotonicity of the variance ratio and the sharp endpoints. Exact algebra and 369 independently implemented numerical checks passed. None of the infinitary inequalities rests solely on numerical sampling.

## Originality — PASS (qualified)

Guéneau–Majumdar–Schehr (arXiv:2306.09453) study this persistent harmonic particle with periodically and Poisson-reset force and supply a Gaussian variance at *reset epochs* for the periodic model; the present theorem evaluates *stationary random-time sampled* variance and supplies a strictly monotone, sharp, dimensionless cross-protocol penalty. The general renewal-reset Brownian covariance is already available from prior renewal theory and Taźbierski–Metzler–Magdziarz (New J. Phys. 27 (2025) 074603), and an earlier stationary finite-window averaging analysis proves deterministic-clock optimality by convexity. Those ingredients are NOT claimed novel; the ratio law for the unreset harmonic filter is the assessed additional mathematical statement. Compared implications rather than just titles: the finite-window boxcar observable and the reset-epoch variance do not state the exponential-filter ratio, although both provide useful inputs. The risk that general pre-existing formulas implicitly encode the ratio and its derivative sign remains and prevents a definitive priority assertion.

## Mathematical value — PASS

A quantitative, sharp protocol-comparison law applies at every physical ratio \(z=\mu m\), giving a clear experimental-design bound: Poisson force resetting inflates steady particle-position variance by strictly between two and six times relative to periodic resetting of the same average frequency. The strict monotonicity, both optimal constants, and correct random-time/epoch distinction are not determined by either protocol's separate variance formula. The clock-functional extension identifies how renewal dispersion affects this persistent harmonic observable. These are complete structural comparisons rather than an arbitrary numerical parameter slice.

## Scientific limits

Independent scientific validation has not occurred. The theorem does not concern finite-time transients, signed filter kernels, dependent reset durations, particle-position resetting, or stochastic ordering of entire distributions. The novelty comparison could be affected by unlocated broad renewal-filter theorems; the 2025 general covariance representation is explicitly acknowledged.

Self-review: passed. Independent audit: not yet performed.
