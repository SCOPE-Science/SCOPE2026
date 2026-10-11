# Independent mathematical audit

## correctness

PASS

The morphic induction is sound. The blocks \(P_k=\mu^k(1)\) and \(Q_k=\mu^k(0)\) have length \(2^k\) and differ only in their final bit. If \(L=2^k\), every prefix from length \(L\) through \(2L-1\) is \(P_k\) followed by a prefix of a second copy of \(P_k\), so the current dyadic endpoint set remains an attractor: factors are either already represented in the first block, cross the selected boundary position, or can be shifted into the first block. At length \(2L\), the suffix \(Q_k\) occurs uniquely. Every interior length-\(L\) window is a cyclic rotation of \(P_k\), hence has the same one-count as \(P_k\), whereas \(Q_k\) differs by one bit; therefore the suffix is the only occurrence and avoids the old attractor. This forces the next greedy endpoint \(2L-1\). Independent finite replay through 128 characters and 13 dyadic levels agrees but is not used as the infinite proof.

## originality

PASS

Schaeffer--Shallit define the greedy attractor process and prove a general logarithmic bound, while their period-doubling result concerns minimum attractors of size two. The 2026 Banbara et al. paper completely classifies minimum-cardinality attractors for the same period-doubling words, but that per-word optimum is a different invariant and does not determine the cumulative greedy trajectory. Fresh Resultary and exact-position searches did not locate the powers-of-two-minus-one greedy set. The submitted morphic obstruction is therefore not implied by the closest prior theorems.

## value

PASS

This gives a canonical sharp separation between the online greedy invariant and the true optimum on a standard automatic word: greedy size is exactly \(\lfloor\log_2 n\rfloor+1\) while optimum is constantly two. The all-length structural formula is a meaningful benchmark for greedy string-attractor theory, not a finite table extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
