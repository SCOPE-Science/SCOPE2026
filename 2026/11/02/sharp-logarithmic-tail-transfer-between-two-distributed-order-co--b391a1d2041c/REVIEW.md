# Scientific review

## Correctness — PASS

The coefficient generating functions are well defined by integrating fractional coefficients of \((1-z)^{-\beta}\) and \(((1-z)(3-z)/2)^{-\beta}\). Factoring the BDF2 symbol yields a negative-binomial convolution with exactly computable mean \(\beta/2\). A uniform ratio expansion and geometric-tail control give the precise fixed-order difference with an error integrable over every stated nonnegative order density. Endpoint Laplace integration proves the two sharp logarithmic laws. Absolute summability permits identifying the total difference through the Abel limit, which vanishes by dominated convergence; summation of the positive asymptotic tail yields the universal finite-prefix ratio \(1/2\). The endpoints, strict startup sign, and quantifiers are checked. The standalone numerical checks are supplementary, not proofs.

## Originality — PASS with residual historical uncertainty

Ren–Su (arXiv:2610.23163v2, Sections 4.2 and 5) analyze radial-symbol CQ error and stability for the same uniform-order integral and show BE/BDF2 finite-time convergence comparisons, but not paired weight-difference asymptotics or a sum-zero compensation law. Yin–Liu–Li–Zhang (DOI:10.3934/dcdsb.2020168, Sections 2–5 and Eq. (7)) give general distributed-order CQ constructions and a fixed-order singular expansion. The latter already supplies the ingredients of the fixed-order first correction and is not claimed as new. The present theorem additionally proves the uniform order-endpoint transition for all power-law order densities, the exact cancellation, and the universal half-coefficient cumulative law. Published mathematical-record searches found other BDF2 positivity and weighted-kernel results but no implication covering these coupled claims. Prior generic asymptotic machinery might allow another derivation; historical exhaustiveness and independent priority review are not asserted.

## Value — PASS

Uniform and nonuniform distributed-order kernels exhibit very slowly decaying memory. The theorem gives the sharp quantitative redistribution from startup weight into the tail when switching from first- to second-order CQ, including the residual accumulated mismatch after an arbitrarily long finite convolution. Its order-density independence in normalized units supplies a practical sharp benchmark for truncation and memory-compression error analysis. It does not infer improved PDE accuracy, stability, or coefficientwise positivity for all time levels.

## Closest literature and limitations

The closest direct source is Ren–Su, *Stability and Error Estimates for Convolution Quadrature under Radial Symbol Bounds*, arXiv:2610.23163v1, publicly submitted October 16, 2026, with relevant detailed material in v2. Yin et al., *Approximation methods for the distributed order calculus using the convolution quadrature*, first public May 15, 2020, provides the broader fractional/distributed-order construction and generic fixed-order expansion. Lubich (1986, 1988) establishes CQ foundations. The precise paired long-memory compensation remains subject to specialized historical-priority verification. No claim is made for start-corrected implementations, signed densities, discrete order measures or nonlinear systems.

Self-review: passed. Independent audit: not yet performed.
