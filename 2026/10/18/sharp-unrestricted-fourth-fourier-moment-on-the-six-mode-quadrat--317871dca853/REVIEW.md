# Scientific review: quadratic triangular Fourier aperture

## Correctness — PASS
The proof is entirely finite-dimensional and uses an exactly enumerated convolution quartic, an algebraic sum-of-squares rearrangement, Cauchy–Schwarz and arithmetic–geometric mean, and one-dimensional calculus. The exact identity in RESULT.md controls arbitrary nonnegative magnitudes, including boundary vectors; the phase equality argument then treats arbitrary complex coefficients. The derivative has one positive cubic root, giving a unique nonflat optimal ratio. The embedded checker independently enumerates the convolution coefficient dictionary and checks selected real/complex and finite-grid cases. Finite tests are not the proof of the universal statements.

## Originality — PASS, best knowledge
The exact same six-point frequency set occurs in the closest published triangular-aperture record, but that theorem explicitly assumes every amplitude equals one. Its sharp maximum \(102\) yields normalized \(17/6\); the present unrestricted constant is strictly larger, with unequal necessary magnitudes. Full primary-text comparisons of Ganzburg (2020) and the published finite-array constructions of Gu et al. (2021) and Du–Jiang (2022) found asymptotic metric inequalities or complementary arrays, not the target sharp finite synthesis norm. Related published sharp constants for different supports and moments do not imply this claim. Unindexed prior optimization is a remaining bibliographic risk. These comparisons establish best-knowledge originality, not absolute uniqueness.

## Mathematical value — PASS
The complete total-degree-two triangular spectrum is the first nonrectangular bivariate analytic quadratic aperture with two distinct symmetry orbits. Its unrestricted coefficient norm is a natural operator invariant needed for exact norm comparison and stable finite-grid sampling. The result identifies a definite strict gap between constant and variable amplitudes and classifies all sharp complex extremizers, not just a numerical or phase-only optimum. The proof supplies a reusable positive-square reduction rather than a brute-force optimization.

## Scope and limitations
Only the six frequencies of the degree-two simplex, the fourth moment, and finite tori without two-sum aliasing are treated. No result is claimed for other degrees or general Newton polytopes. Independent mathematical and bibliographic audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
