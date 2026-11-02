# Scientific review: positivity thresholds for one-dimensional Chebyshev–Korobov quadrature

## Correctness — PASS

The Fourier diagonalization is valid because all discrete circulant Gram eigenvalues are strictly positive. Nonzero discrete Fourier modes of the unconstrained kernel weights exactly coincide with those of integrated periodic tents. The zero mode is evaluated from the Fourier coefficients of the half-periodic sine density and a classical cotangent partial-fraction identity. The minimum tent mass is rigorously at a density zero, using an explicit folding identity and circular interval-overlap rearrangement. Solving the exact sign inequalities yields the positive-weight and constant-function sign thresholds, and Taylor expansion proves their distinct orders and parity dependence. Direct 65-digit Gram solves independently agree with the formula in 174 supplementary checks. Limitations: floating-point tests do not prove the infinite-dimensional statements, which rest on the explicit analytic argument; they do not establish any other density, kernel, or dimension.

## Originality — PASS with historical-priority limits

The source arXiv:2610.01113v1 discusses higher-order periodized lattice-based integration and explicitly does not resolve positivity for its broader multivariate method; its inspected relevant statements do not give a sharp one-dimensional smoothness-one threshold or the constant-function sign law. Karvonen–Kanagawa–Särkkä (2019) supply general kernel-quadrature positivity conditions and Sobolev magnitude bounds, but their statements require different hypotheses and do not imply these formulas. Novak–Zhang (2016) treat univariate Sobolev optimal quadrature under different norms and exactness, while Kaarnioja et al. (2021) focus on periodic lattice interpolation without this nonsmooth density sign frontier. The exact discrete Fourier/tent decomposition is consistent with classical spline theory, and an older equivalent specialized identity may exist; searches cannot exclude that possibility. The accepted claim is the complete explicit two-threshold classification for this specified natural kernel-density family, not a new general theory of positive kernel quadrature.

## Value — PASS

Unconstrained optimal integration weights need not be positive, so exact sign transitions are useful diagnostics for robustness. Here the density's zeros force tent masses of order \(n^{-2}\), while kernel zero-mode mismatch supplies a common negative offset. Their competition produces an order-\(n\) critical kernel-amplitude scale; a second, order-\(n^4\), parity-dependent transition can make even a positive constant integrand evaluate negatively. Both formulas hold for every grid size rather than only a chosen numerical example and quantify why the source's general positivity question is subtle. They do not establish high-dimensional positivity or an effect for all kernel normalizations.

## Closest literature and residual risk

The most directly related source is Bartel et al., arXiv:2610.01113v1 (2026). The main antecedents are Karvonen–Kanagawa–Särkkä (2019), Novak–Zhang (2016), and Kaarnioja–Kazashi–Kuo–Nobile–Sloan (2021). A historically unnoticed periodic-spline equivalent is possible. The companion exact and high-precision numerical checks substantiate the derivation but do not provide independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
