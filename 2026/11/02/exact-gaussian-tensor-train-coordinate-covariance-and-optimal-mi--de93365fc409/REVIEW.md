# Self-review

## Correctness — PASS

Isserlis' fourth-moment formula leaves exactly three pairing states at each tensor mode. A differing physical coordinate pins the local pairing; equal and unequal adjacent Wick states contribute bond factors one and reciprocal bond rank respectively. Spectral diagonalization of the resulting three-state transfer matrix establishes the full mixed fourth-moment formula and covariance. Strict decrease and strict log convexity of the transfer gap factor establish the globally optimal mismatch placements. Diagonal quadratic-form expansion then gives the exact finite-sample variance. The standalone verifier independently expands four bond paths using Gaussian Wick pairing, and checks the transfer and arrangement claims with exact rationals. Finite checks corroborate, rather than prove, the all-parameter assertions.

## Originality — PASS, with historical-priority risk

The 2026 Bujanović–Kressner–Olić paper already implies the single-coordinate fourth moment, and the Meyer–Avron 2023 Kronecker variance formula covers the entire bond-rank-one specialization. Neither is claimed new. The inspected Bujanović–Kressner–Olić full text gives moment upper bounds for trace estimation rather than the rank-greater-than-one cross-coordinate formula. The inspected Rakhshan–Rabusseau tensorized-projection and Cazeaux–Dupuy–Justiniano TTStack analyses give general moment estimates but not the exact spacing-based classification. Comparison of relevant published mathematical claims and prior literature did not identify an equivalent statement or a theorem implying the positive-bond-rank gap-extremal classification. Standard Gaussian replica transfer techniques might have appeared elsewhere; historical priority is not independently confirmed.

## Mathematical value — PASS

The covariance kernel gives an exact replacement for worst-case trace-scale variance bounds for arbitrary diagonal inputs, and the sharp arrangement theorem separates two two-spike positive diagonal matrices with identical eigenvalues and trace solely by the physical mode positions. The exact witness changes variance from \(52\) to \(99/2\) at the same bond rank and sample count. This determines a mathematically natural mode-ordering effect for tensor-structured stochastic trace estimation, not a routine change of normalization.

## Closest literature and limits

Sources: arXiv:2606.15679 (Definition 1 and Theorems 5, 7); arXiv:2309.04952 (Theorems 1, 2, bond rank one); arXiv:2003.05101 (Theorem 1 and proof); arXiv:2603.11009 (Proposition 7.4). The analysis concerns independent real Gaussian cores and diagonal inputs; no optimality claim for nondiagonal matrices or complete TT algorithms is made. Related tensor-network Wick identities may predate the claim.

Self-review: passed. Independent audit: not yet performed.
