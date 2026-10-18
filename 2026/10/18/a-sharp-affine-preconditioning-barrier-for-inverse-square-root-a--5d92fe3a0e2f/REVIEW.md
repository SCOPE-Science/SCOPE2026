# Scientific review

**Correctness: PASS.** The exact preconditioned matrix is a quadratic polynomial in a nilpotent shift. Symmetry splits its Hermitian part into one scalar block and one two-dimensional block. The latter has determinant proportional to \(2-K^2[2/3+3(t-1/3)^2]\), which proves the sharp uniform boundary and unique optimal slope. An explicit endpoint input produces a singular first compression, and direct multiplication proves the quadratic rescue. The standalone symbolic verifier passed. These are exact-arithmetic results only.

**Originality: PASS, with residual priority uncertainty.** The source work already defines polynomial inverse-square-root Arnoldi and warns of Ritz values near zero; none of those generic facts is claimed as new. The contribution is the sharp uniform affine-slope boundary and dimension/degree separation on the selected minimal Jordan model. Related published work on numerical ranges and polynomial Arnoldi stability was compared, but the exact classification was not located. A related 2012 three-dimensional Jordan Ritz-localization article could not be inspected beyond its abstract; a matching specialized result remains possible. The assessment is not an independent literature-priority certificate.

**Value: PASS.** A polynomial may make all eigenvalues of the preconditioned matrix equal one yet leave a singular one-dimensional inverse-square-root Arnoldi projection. Quantifying the *best achievable* affine slope and showing that degree two is qualitatively different makes this a motivated, reproducible degree-selection and nonnormality benchmark, not a claim of general matrix-function convergence. The concrete obstruction matters precisely because projected matrix functions have singularities or branch cuts; the underlying square root remains well-defined.

The scope is limited to real normalized affine polynomials, this three-dimensional Jordan family, one-dimensional compressions, and exact arithmetic. The full text of one related older paper was inaccessible; this is reported as a specific originality risk.

Self-review: passed. Independent audit: not yet performed.
