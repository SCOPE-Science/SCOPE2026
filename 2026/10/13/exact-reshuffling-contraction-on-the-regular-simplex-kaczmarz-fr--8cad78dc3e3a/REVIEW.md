# Self-review

## Correctness
PASS. Simplex permutation symmetry forces the permutation-averaged Gram operator to be scalar on the error space. A fixed-order Hilbert--Schmidt recurrence computes that scalar exactly, and the displayed arithmetic-geometric identity yields the closed form. The with-replacement comparison follows exactly from the unit-norm tight-frame identity. The embedded exact verifier enumerates all row orders through \(n=5\) as corroboration only.

## Originality
PASS. Strohmer--Vershynin provide the with-replacement expected-contraction baseline. Han--Xie provide the closest general RRK convergence framework and the same epoch-product representation, but their spectral-norm theorem does not imply an exact permutation-averaged scalar MSE channel. A highly relevant 2026 regular-simplex reshuffling manuscript was inspected: its contraction factors are different non-projective matrices, and its low-length/all-length statements do not cover the Kaczmarz projector family. Exact-MSE randomized-Kaczmarz literature remains a residual alias risk where full text was unavailable.

## Value
PASS. The theorem is a natural exact benchmark for random reshuffling on the canonical \((n+1)\)-vector equiangular tight frame. At equal row-action cost it exposes an asymptotic separation, \(c_n=\Theta(1/n)\) versus a with-replacement factor tending to \(e^{-1}\), that is invisible in generic norm bounds.

## Closest literature and limitations
The closest direct RRK source is Han--Xie, while Strohmer--Vershynin supplies the archive anchor and with-replacement baseline. The result is limited to consistent unit-relaxation Kaczmarz on the regular-simplex frame with independently refreshed permutations. It does not classify generic tight frames, noisy systems, or single-shuffle reuse.

Self-review: passed. Independent audit: not yet performed.
