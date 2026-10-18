# Independent mathematical audit

## correctness

PASS

Independently reconstructed 64 candidate-center to 128 target incidence matrix via all seven insertion positions and both symbols. The 20-center witness consists of multiples of three 0..63 except 21 and 42; direct target counts are 98 covered once, 28 twice, and 2 thrice. To certify the lower bound, independently implemented a complete depth-first covering recursion with 19-center budget: at each uncovered target it branches over all unchosen centers capable of covering that target, rejects only when top-b residual center gains cannot cover remaining targets, and memo-free recursion terminates infeasible after 81,352 calls. Inspected source C++17 verify.cpp algorithm, which performs the same logically exhaustive branching with additional safe pruning (reported 81,671 calls). Thus 19 impossible on complete finite input; no timeout or black-box optimizer inference. Larger than 20 irrelevant and any smaller cover extends to 19.

## originality

PASS

The exact binary S(2,7,6) value was searched in both notations and against classical/recent insertion-covering code literature and exact small Grozea examples. Lenz et al. give asymptotic/general bounds, Pikhurko et al. give density estimates and a different exact q=3 center-length-3 example, and Xie et al. focus improved general bounds. No actual source implies 19 infeasible at the exact binary case; historical unindexed exact tables remain a risk.

## value

PASS

The minimum six-bit one-insertion covering number is a natural fixed-length synchronization-error invariant. A 20-element code is tight while elementary ball-volume bound only gives 16; exact sharp redundancy requires a genuine finite covering obstruction, furnishing a useful benchmark that could be independently reused in code constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
