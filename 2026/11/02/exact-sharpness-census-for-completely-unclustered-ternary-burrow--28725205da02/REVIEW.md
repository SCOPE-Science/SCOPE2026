# Independent mathematical audit

## correctness

PASS

For the fixed ordered alphabet 0<1<2 and n=13..30 only, the sharp BWT output words L are exactly those with adjacent unequal symbols, Hamming distance ceil(n/2) to sorted(L), and an n-cycle stable sorting permutation. Independently implemented two separate COMPLETE C++ enumerations of all 3*2^(n-1) such words for EACH n=13..30; one used parity pruning and one deliberately used NO pruning. Both give c_13..c_30=(28,4,88,22,120,30,256,61,540,94,1084,180,2148,330,3956,595,8322,1072); n=30 exhaustive generator visits 1,610,612,736 distinct candidates. Verified displayed witnesses with direct inverse and forward BWT and cyclic input runs; cited known factor-two lower bound gives U_q(n)=ceil(n/2) for all q>=3, limited to these n.

## originality

PASS

Best-of-knowledge exact claim-vs-prior comparison after this run’s independent Resultary search and primary-source checks. The known factor-two bound plus constructed ternary witnesses yields finite-range numeric sharpness; the main additional theorem is the complete exact c_n count, which requires a genuine exhaustive one-cycle and Hamming predicate census, not a corollary of mere existence. Priority qualified: Decisive historical-priority uncertainty: full Kumallagov 2026 appendix was inaccessible due vpn_disconnected, so it may contain an equivalent 13..30 table; retain for human full-text comparison, no fabricated NOT_COVERING claim.

## value

PASS

A complete, nontrivial finite classification of sharp unclustered BWT images of primitive necklaces across 18 consecutive natural lengths, including unique four-image n14 shape and all image multiplicities. It resolves a substantial finite range of a published extremal question without falsely claiming all-length conjecture; multiple billions of candidates and independent algorithms establish finite exhaustiveness, not infinite extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
