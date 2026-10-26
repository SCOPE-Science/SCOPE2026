# Review of sharp affine-detrending inequality

## Correctness — PASS

The rank-two affine projector is reconstructed from the orthogonal basis, giving an exact integration kernel for the Lipschitz derivative. The absolute kernel mass has two explicit rational branches. On the first branch its factored derivative determines one strict local minimum; on the second the mass increases strictly. The only global maximizers are the interval endpoints, each of exact mass \(8/27\), and equality in the integral triangle inequality fixes the two derivative sign patterns. The exact-arithmetic replay checks the algebra; it is not used to infer an infinite or continuum theorem from a grid.

## Originality — PASS within inspected evidence

The closest inspected sources are [1] on \(L^\infty\) stability of unrelated kernel-space projectors, [2] on Hilbert-space Volterra polynomials, and [3] on periodic reverse Bernstein inequalities. None has the same operator, derivative seminorm, endpoint sharp constant, or equality class. An earlier mean-centered fractional-integral result removes only the mean, not the affine trend. Searches for affine detrending, Peano kernels, two vanishing moments and the numeric constant found no exact covering statement. However, specialist Ostrowski or old least-squares inequalities could contain an equivalent result and historical priority is not conclusively settled.

## Value — PASS

Affine least-squares detrending is a natural quantitative operator. Its sharp Lipschitz-to-uniform error has direct interpretation as the worst approximation distortion of a one-slope trend, and the precise localization/equality classification distinguishes it from a routine projector boundedness estimate.

## Checks and limits

The auxiliary `checker.py` replays 12,910 exact-rational assertions; the continuum argument depends on the factorization and sign proof in `RESULT.md`. The claim does not extend to nonuniform weights, quadratic trends, or higher dimensions.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] arXiv:1005.2424. [2] arXiv:2206.09947. [3] arXiv:2302.10122.
