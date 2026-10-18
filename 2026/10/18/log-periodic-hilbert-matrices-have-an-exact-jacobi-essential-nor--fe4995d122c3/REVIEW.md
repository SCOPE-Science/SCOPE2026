# Review of the log-periodic Hilbert-matrix essential-norm theorem

## Correctness (C) — PASS

The exact operator and its domain are fixed in the theorem, with a real positive log-periodic multiplier. The proof contains explicit compact-error estimates connecting the discrete Hilbert matrix to the continuous Carleman kernel; the potentially nontrivial step of compactness of the cell-averaging defect is supplied using cellwise Poincaré and a square-integrable derivative kernel, rather than treating a step projection as a small-norm perturbation. Mellin coordinates give the stated convolution kernel and its Fourier transform. Translating compactly supported approximate maximizers proves the half-line essential-norm/full-line norm equality. The positive-kernel argument places the maximal Floquet norm at zero quasi-momentum. Fourier coefficients produce exactly the advertised bilateral Jacobi matrix. The two finite-section tail terms and the nondegenerate top-eigenvalue expansion were checked algebraically. The standalone finite checker passes its declared tests. No finite computation is presented as a substitute for the infinite proof.

## Originality (O) — PASS, with explicitly limited priority assurance

The nearest source is David Norrbo, arXiv:2609.13403v1. Its Theorem 2 gives an exact scalar essential-norm formula only with convergent fine-block magnitude averages, which nonconstant periodic functions of the logarithm fail. Its Theorem 3 supplies a general variational characterization but not this Jacobi norm or its frequency-dependent curvature. The later mathematical note titled *Exact essential norm for slowly oscillating generalized Hilbert matrices on \(\ell^p\)* addresses weights asymptotically invariant under each fixed multiplicative scale. Here a fixed dilation by \(e^{\pi/\omega}\) reverses the cosine phase, so the slowly oscillating theorem does not apply; only its public summary was accessible, not its full text.

Pushnitski--Sobolev, arXiv:2307.09242 (especially Sections 1, 2, and 8, with Appendix A checked for scope), studies self-adjoint Hankel kernels \(p(\log(x+y))/(x+y)\). These are not the output-row-modulated kernels \(p(\log x)/(x+y)\), and their Gamma-function fiber representations do not directly imply the claimed norm identity. Jin, arXiv:2504.19743, treats positive-measure-induced generalized Hilbert operators, not this oscillating row factor. The comparison is mathematical, not an inference of originality merely from unmatched keywords. A broader historic Floquet/Wiener--Hopf theorem might imply some steps. Wong's 1980 paper was available only as an abstract and was not used as proof of noncoverage. Publication priority is not independently certified.

## Mathematical value (V) — PASS

Norrbo's results explicitly distinguish convergent fine-scale magnitude means from oscillatory block behavior and leave exact values difficult outside the limiting-average regime. A fixed log-frequency row oscillation is a natural test case because it is not slowly oscillating under multiplicative shifts. The result identifies its exact essential norm, converts it to a compact numerical problem with an exponentially controlled truncation error, and derives a sharp analytic coefficient that varies with frequency. The strict norm increase \(\pi\sqrt{1+\varepsilon^2/2}\) and the curvature term make a meaningful scale-interaction statement, not a routine substitution or isolated finite calculation.

## Scope and residual risk

Only \(\ell^2\), real \(|\varepsilon|<1\), and fixed \(\omega>0\) are covered. The full essential spectrum and the joint small-frequency/small-amplitude limit remain open here. General abstract periodic Mellin-operator results could carry overlapping norm-reduction consequences. The proof is internally reviewed; no independent audit has been undertaken.

Self-review: passed. Independent audit: not yet performed.
