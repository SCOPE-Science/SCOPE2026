# Same-model review

## Correctness
PASS. The proof reduces common support divisors exactly, then treats the only possible least-divisor regimes. The \(q_N=3\) branch is the classical product inequality. The \(q_N=4\) branch uses the parity pairing \(z\leftrightarrow-z\), where three monomials force one parity block to be a nonvanishing singleton. For odd least divisor \(p\ge5\), Meshulam's interpolation bound is exact at support size three; for \(N=2m\), the Chinese-remainder split converts each parity-frequency fiber into the transform of a nonzero at-most-three-point function on odd \(m\), giving the same bound. The sharpness construction has exactly two zero fibers among the \(q_N\)-th roots. The integer checker independently exhausts all \(3\le N\le36\).

## Originality
PASS with residual risk. Searches compared the exact statement, not merely titles: all-order exact support-three cyclic uncertainty; trinomial zeros on the \(N\)-th roots; rank-deficient three-column Fourier submatrices; and the relation to Meshulam's monotone function. Meshulam provides a general lower bound but not this exact even-order result. Bonami--Ghobber analyze exact-support equality cases only for selected group families and explicitly describe arbitrary prime-factor generalization as difficult. Delvaux--Van Barel give prime-power/Kronecker rank-deficiency constructions rather than this all-order exact-support-three formula. No equivalent theorem was found in published-finding corpus or the inspected primary sources.

## Value
PASS. Exact support size three is the first genuinely nontrivial sparse stratum after the elementary two-point case. The formula is uniform in \(N\), exposes a previously hidden distinction between the divisors \(3\), \(4\), and the least odd prime divisor, and converts a natural uncertainty question into a sharp root-of-unity zero bound. It is a reusable structural statement rather than a finite table or isolated computation.

Closest literature and limitations are described in `RESULT.md`. The main residual risk is a differently phrased or poorly indexed prior statement; the theorem does not classify all extremizers or treat support size four and above.

Same-model review: passed. Independent audit: not yet performed.
