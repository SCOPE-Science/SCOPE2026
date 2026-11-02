# Self-review

## Correctness
PASS. The lower witness is the spectral sign of the explicitly diagonalized weighted symbol, and its norm is evaluated by a two-dimensional characteristic polynomial plus a repeated eigenvalue. For each parameter regime, the upper Gram matrix has constant diagonal equal to the claimed norm and both positive/negative offsets are positive semidefinite; their nontrivial two-by-two compressions are checked algebraically. Gram vectors give an operator-norm bound over complex inputs, and row cloning plus compression handle arbitrary extra coordinates. The theorem includes the endpoint cases \(k=0\), \(n=k\), \(k=1\), \(k=5\), and \(k=6\). Supplementary tests are not used as an infinite proof.

## Originality
PASS, qualified. The circulant fully flipped core is classically covered by Mathias's formula, and several small-size numerical constants appear in Holbrook–Johnston–Schoch. Neither is claimed as a new separate result. The candidate advance is the sharp all-size two-orbit family, including a closed transition at six and explicit optimal Gram and contraction witnesses. Davidson–Donsig and Christensen give more general factorization or symmetry tools but the inspected relevant results do not state the specialized closed phase formula. Residual risk: equivalence may be hidden in older Schur-multiplier, matrix-completion, or norm-optimal factorization treatments; the Mathias paper's complete text could not be exhaustively compared.

## Mathematical value
PASS. A concrete, natural signed diagonal perturbation of the all-ones Schur multiplier exhibits a nontrivial finite cutoff: one extra coordinate changes a complete reflection's norm only for a precisely classified range. The exact value and cutoff govern every matrix size, not just sampled instances, and both worst-case inputs and optimal factorization certificates are explicit. The result supplies sharp benchmarks for operator norm amplification under entrywise signs.

## Limits
No claim of a general Schur sign-matrix classification, independent audit, or exhaustive historic priority resolution is made. Small Schur spectra and the core circulant identity are prior literature.

Self-review: passed. Independent audit: not yet performed.
