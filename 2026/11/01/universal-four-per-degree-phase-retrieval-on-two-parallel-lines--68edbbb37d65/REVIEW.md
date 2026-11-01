# Review of two-parallel-line polynomial phase retrieval

## Correctness

**PASS.** For every \(d\ge1\), the real intensity polynomial on a line has degree at most \(2d\), and the top two coefficients do not depend on line height. After \(2d+1\) first-line and \(2d-1\) second-line observations, both entire line-intensity polynomials agree. The ratio of two nonzero candidate polynomials is rational and unimodular on both lines; reflection makes it periodic with nonzero imaginary period, forcing a constant ratio. The zero case and lower actual degrees are included. The ambient dimension/linear interpolation statement follows from an explicit Lagrange construction. The exact standalone checker passes 390 trials; these are auxiliary and not a proof of infinite universality.

## Originality

**PASS, with priority risk.** The relevant mathematical statements and proofs in accessible full-text pages of Przybyłek–Siedlecki (arXiv:1907.09371, Section 4), Bodmann–Hammen (arXiv:1302.5487, Section 2), Philipp (arXiv:1403.4769, Theorem 1.1), Liehr (arXiv:2308.05722, Theorem 1.1), and Chalendar–Partington (arXiv:2403.16255, Sections 2.2–2.3) were compared at the level of measurement sets and polynomial scope. The first supplies a quadratic-size radial/angular grid; the next two supply other structured low-redundancy frames and derivative measurements; the last two address infinite line or circle uniqueness for different function classes. None of those inspected statements directly implies the universal arbitrary-node, value-only, two-parallel-line \(4d\) result. The strongest residual risk is an overlooked equivalent theorem within general structured phase-retrieval frames or an earlier parallel-line polynomial interpolation result.

## Mathematical value

**PASS.** A natural measurement-design question is whether one can use a fixed small number of samples on just two parallel measurement lines and still recover every degree-bounded polynomial. The theorem gives a universal, nonadaptive, geometrically explicit \(4d\) construction, improves the quadratic-size general polynomial sampling construction for this setting, and identifies exactly why two high-degree intensity constraints are redundant between the lines. The dimension claim is deliberately confined to the ambient trace-interpolation space rather than overstated as a nonlinear optimality theorem.

## Scope and unresolved issues

The proof is noiseless and exact; no uniform conditioning, numerical stability, bit-complexity, or global minimal measurement count is established. It does not contradict nonuniqueness for unrestricted entire functions on two parallel lines. Independent mathematical validation and exhaustive historical-priority certification are not claimed.

Self-review: passed. Independent audit: not yet performed.
