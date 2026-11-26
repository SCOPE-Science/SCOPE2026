# Independent mathematical audit

## correctness

PASS

Exhaustively and independently checked the supplied JSON as data. The canonical ordering is the lexicographically least sorted sequence of base-3 column codes under row permutations. Explicitly expanded every representative under both row and column permutations, marking all 531441 labeled profiles with no intersection between representative orbits. Checked each positive unique support and exact normalization with cleared integer denominators; checked the six expected envy inequalities, EFX by removal of each comparison bundle's least-valued good for the evaluating agent, and nondomination against the own-utility vectors of all 81 complete allocations. All 5053 witnesses pass, including the illustrative lottery; 392 profiles have all three levels in every row, and the support histogram is (1123,2091,1772,67). Relabeling preserves every condition, so this is exhaustive for the claimed finite domain. Replay: `python3 /workspace/branches/frozen_replay.py 3`.

## originality

PASS

The distinct finding is the joint EF/EFX/integral-PO guarantee, with four support points sufficient, on the fixed smallest consecutive positive three-level alphabet at the four-good, three-agent size. The closest indexed material gives a three-level counterexample on a different numerical alphabet; available positive theorems restrict the valuations in different ways or have extra hypotheses. No inspected prior statement or mechanical implication establishes this fixed-domain theorem.

## value

PASS

The first consecutive positive integer alphabet beyond the known bi-valued guarantee settles a meaningful compatibility boundary in the same small market that already permits impossibility. The comparison with the nearby {1,3,4} counterexample shows that the actual levels, not just their cardinality, matter. The certificate gives an exact finite benchmark for identifying which domains allow ex-ante fairness with complete EFX/PO support, plus a usable uniform support bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
