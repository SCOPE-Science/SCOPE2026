# Self-review

## Correctness
**PASS.** At a common total \(N\), Shannon entropy is exactly \(\log N-N^{-1}\log Q\) with \(Q=\prod_i n_i^{n_i}\), and Simpson concentration is exactly \(N^{-2}\sum_i n_i^2\). Thus equality of the two ecological indices reduces to equality of two integers, avoiding floating-point ambiguity. The verifier exhaustively generates every partition through \(N=30\), cross-checks partition counts by an independent dynamic program, and reproduces exactly two first pair-collisions at \(N=24\) and one first richness-augmented collision at \(N=30\). It returns `VERIFY_OK`.

Risk: the theorem is specific to positive integer census profiles and exact equality, not noisy estimated diversities.

## Originality
**PASS.** Hill's classical framework owns the identification of richness, Shannon diversity, and inverse Simpson as diversity orders \(0\), \(1\), and \(2\), and later diversity-profile literature owns the use of the full order continuum to characterize abundance structure. The checked literature and exact-profile searches did not state the finite inverse thresholds \(23/24\) or \(29/30\), nor the complete first collision layers.

Risk: a small exact collision could exist in unindexed pedagogical or software material.

## Value
**PASS.** Shannon and Simpson are among the most widely used abundance-sensitive biodiversity summaries, and richness is their canonical order-\(0\) companion in the Hill framework. The result quantifies, for the first time located here, exactly how far these familiar summaries remain jointly lossless on integer census profiles and gives the first compositions they cannot distinguish. This supplies a natural identifiability benchmark for diversity summaries rather than an arbitrary numerical comparison.

Self-review: passed. Independent audit: not yet performed.
