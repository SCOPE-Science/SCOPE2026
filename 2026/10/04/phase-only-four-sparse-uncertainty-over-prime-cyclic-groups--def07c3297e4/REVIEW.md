# Review

## Correctness
The proof is analytic for every prime \(p\ge5\). At each Fourier zero, the four normalized Fourier summands are unit complex numbers with zero sum. Their monic root polynomial has vanishing first and third elementary symmetric sums and is therefore even, forcing an antipodal pairing. A fixed pairing cannot recur at two distinct frequencies in a prime cyclic group. Three zeros would require all three perfect matchings and then force \(-1\) to be a \(p\)-th root of unity. Two zeros force the support identity \(x_1+x_4=x_2+x_3\), and explicit unimodular coefficients realize two zeros whenever that identity holds. Separate explicit constructions realize zero and one zero.

The standalone checker is finite corroboration only. It replays all four-element supports for every prime from \(5\) through \(31\), including the constructed two-zero witness on every centrally symmetric support.

## Originality
Tao's prime-cyclic uncertainty theorem is the closest broad result. For a four-sparse signal it allows as many as three Fourier zeros and, conversely, guarantees unrestricted coefficient vectors with prescribed support pairs at the sharp cardinality threshold. It does not impose equal coefficient magnitudes, and therefore does not imply the phase-only two-zero ceiling or the central-symmetry criterion.

Krahmer, Pfander, and Rashkov survey finite-Abelian support uncertainty and develop short-time Fourier analogues. Their finite-Fourier discussion uses arbitrary coefficient vectors; searches of the inspected full text found no constant-modulus or unimodular-coefficient restriction matching the present claim.

Targeted database and web searches covered phase-only, constant-modulus, unimodular-null-vector, four-sparse, roots-of-unity, and additive-parallelogram formulations. No inspected source supplied this fixed-support classification. A residual risk remains for older sequence-design or phase-code literature indexed under different terminology.

## Value
The theorem isolates the first sharp difference between unrestricted and phase-only four-sparse uncertainty on prime cyclic groups: Tao's three-zero extremal becomes impossible, while the survival of two zeros is governed exactly by additive geometry of the support. This is a complete all-prime classification for a natural constrained uncertainty problem, not a finite table or a numerical increment.

Same-model review: passed. Independent audit: not yet performed.
