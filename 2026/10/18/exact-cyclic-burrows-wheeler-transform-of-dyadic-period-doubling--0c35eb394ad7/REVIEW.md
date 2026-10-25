# Independent mathematical audit

## correctness

PASS

PASS. For W_m obtained from theta(0)=01, theta(1)=00 and cyclic BWT without sentinel, the exact reverse-complement recurrence T_1=1, T_m=1^{o_(m-1)}0^{o_(m-1)}R(T_(m-1)) yields BWT(W_m)=T_m0^{z_(m-1)} for m>=1, and number of runs 2 for m=1, 2m-2 for m>=2. The substitution forbids cyclic 11. Sorting even and odd rotations gives consecutive classes beginning 0001,0010,01,1; within each class substitution reverses source lexicographic order, and preceding-letter decomposition gives the claimed recursion. Reverse-complement preserves run counts, new boundaries add two, final 0 tail merges. Checked m=1, m=2 boundaries and full lexically sorted rotations against an independently coded recursion for m=1..10. Rank-doubling verification script inspected and its finite domain m<=13 distinguished from the induction.

## originality

PASS

Best-of-knowledge PASS based on reading actual full source claims and comparing implications to materially inspected primary literature and published Resultary records. No identified stronger theorem implies the exact present final claim; named overlaps are credited, not asserted absent merely from search results. Residual risks of unindexed or incompletely inspected sources explicitly remain.

## value

PASS

PASS. The cyclic BWT of a canonical automatic-word family is a natural exact data-compression/string-combinatorics invariant. Known logarithmic BWT-run bounds and morphism sensitivity estimates do not give the actual word. An explicit all-level transform recurrence with exact extremal 2m-2 run count is independently reusable for structural tests, string indexes and comparison with other morphic families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
