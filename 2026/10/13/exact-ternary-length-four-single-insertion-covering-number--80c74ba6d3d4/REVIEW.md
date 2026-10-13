# Scientific assessment

## Correctness

PASS. The finite domain has exactly \(81\) candidate four-symbol words and \(243\) five-symbol targets. Every incidence is independently rebuilt by deleting one position from a target, with duplicates removed. The displayed \(31\)-word family covers every target. The direct zero-gap mixed-integer set-cover computation attains both primal and global lower bound \(31\); the complementary zero-gap maximum-omission computation independently returns \(50\), giving the same sharp lower bound. Both executable formulations and the witness are supplied. Solver-internal branch certificates are not independently checked, and reproducibility requires SciPy/HiGHS.

## Originality

PASS, subject to residual indexing risk. The full 14-page arXiv:2606.15379v1 source was inspected; it establishes general bounds rather than this finite optimum. The publicly accessible full text of arXiv:2409.06425v1 gives \(S(3,4,3)=12\) from earlier data, not \(S(3,5,4)\). The 2021 general covering paper concerns general bounds. Searches for both covering-number notations, subsequence-hitting formulations, and exact tables found no statement implying the present value. A previously unindexed finite table remains a material residual risk.

## Value

PASS. The result settles the next ternary word-length instance beyond the previously documented exact length-three case, for the elementary synchronization-error covering invariant. Its value \(31\) is substantially stronger than the ordinary sphere count's lower bound \(23\), and the sharp witness can benchmark finite insertion-covering constructions. No extrapolation to larger lengths is claimed.

Self-review: passed. Independent audit: not yet performed.
