# Independent mathematical audit

## correctness

PASS

PASS: Sign recursion P_{j+1}=P_jQ_j, Q_{j+1}=P_j(-Q_j) produces the stated bit-parity word. At rank k, P_k=A B A (-B), where A=P_{k-2} and B=Q_{k-2}. For starts in B or -B the two halves start with opposite signs; for the two A boundary starts their final signs differ. For interior A starts, the two halves have shared A fragments, matching endpoints and exactly one transition at each pair of glued boundaries, so transition totals match. Remaining single-letter imbalance equals the signed sum of B, which is zero exactly for odd k: q_{2h}=2^h, q_{2h+1}=0. Binary 2-Abelian equivalence follows from endpoints, one-symbol count and total transitions. This establishes all k>=2, not only checked ranks. Independently enumerated direct overlapping-binary-11 signs and five-component factor signatures for all positioned cuts, ranks k=2..11: observed 0,2,0,14,0,62,0,254,0,1022 as predicted. k=2 has no interior A cut.

## originality

PASS

PASS best-of-knowledge: exact positioned cyclic 2-Abelian square cuts for complete dyadic Rudin–Shapiro prefixes are not the 1-Abelian infinite-word complexity of Lü–Chen–Wen–Wu or the 2-Abelian factor-complexity studies of Thue–Morse/period-doubling by Parreau et al. Summation parity identity is classical; its combination with boundary transitions yields the distinct exact classification.

## value

PASS

PASS: Two natural order-two word invariants—2-Abelian equivalence of two half-rotations and the cyclic cut-location set—have a complete parity phase transition and an exact fraction of good cuts. This is not a relabeling of abelian complexity; the adjacency and two boundary joints matter. A researcher studying automatic-word rotations or 2-Abelian powers could use the formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
