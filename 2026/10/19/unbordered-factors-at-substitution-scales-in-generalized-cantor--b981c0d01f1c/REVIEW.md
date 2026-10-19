# Scientific assessment

**Correctness — PASS.** Uniform substitution blocks and palindromic iterates reduce every candidate starting with \(1\) to an explicit position within an iterate. The first-copy positions exhibit a border of length \(q^{k-1}\). Every last-copy position yields an unbordered factor: a hypothetical period would force a second occurrence of its final \(1\) past the support. Reversal symmetry supplies all factors starting with \(0\), and their one-counts prove distinctness. The source code confirms 24 finite parameter cases using an independently generated word and full KMP border tests. These computations are corroboration, not the infinite proof.

**Originality — PASS with residual risk.** The closest prior claims are general automatic-word regularity and unbordered-factor enumeration (Charlier–Rampersad–Shallit, arXiv:1102.3698), unbordered complexity of Thue–Morse and period-doubling (Goč–Mousavi–Shallit, arXiv:1211.1301), and factor/permutation complexity for this exact Cantor-like substitution family (Lü–Chen–Guo–Wen, DOI:10.1016/j.tcs.2015.12.022). None inspected states or implies the explicit classification. Search coverage is finite; equivalent earlier work in unindexed literature remains possible.

**Mathematical value — PASS.** The result completely determines a natural border-free factor invariant at every substitution-power length across infinitely many fixed-point families. Explicit factors and the exact scale exponent \(\log_q2\) provide structural information absent from total factor counts. No assertion is made for other lengths or q below three.

Self-review: passed. Independent audit: not yet performed.
