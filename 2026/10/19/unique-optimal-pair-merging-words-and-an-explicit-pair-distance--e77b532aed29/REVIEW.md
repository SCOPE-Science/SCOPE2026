# Review of the unique pair-merging word theorem

## Correctness
PASS. The formula labels the entire unordered-pair set by consecutive integers. In the stated Černý transition system, one input letter decreases the label by exactly one at every pair; the other cannot decrease it by one or more. Thus no word shorter than the label can merge the pair, and the forced descending path provides a word of the claimed length. The cyclic-gap and diametrical boundary cases, including \(n=2\), are treated separately. The unique-descending-edge argument proves both uniqueness of shortest words and the suffix property. A separate reverse breadth-first computation and shortest-path multiplicity count verify every pair for \(2\le n\le80\).

## Originality
PASS under the inspected evidence. Behague–Johnson [1] already identify the worst pair-merging time \(\binom n2\) for the Černý family and a witnessing pair. In an automaton with precisely \(\binom n2\) pair states, that maximal time already implies the abstract multiplicity-one spectrum, by the no-repeated-vertex argument; no originality is claimed for this consequence. Their maximum does not by itself identify **which pair** has each weight or imply the unique shortest word from every pair. Eppstein [2] gives generic shortest-pair-path algorithms, not the present closed pair-by-pair formulas. Gonze–Jungers [3] study triple rendezvous and a different probability invariant. Relevant published related results on global rank deficiency and target avoidance are not equivalent to pair-specific optimal merging lengths. The possibility of a previously recorded equivalent full pair-path analysis remains the main originality risk.

## Mathematical value
PASS. Pair synchronization is the basic primitive in general reset-word algorithms. The Černý family is the canonical worst-case example for synchronization, and it is natural to resolve not only its hardest pair but the *entire* distribution of pair-merging latencies. Proving that all possible values are attained exactly once, and that all optimal pair-merging words are unique suffixes of one maximal witness, reveals a rigid single-chain structure in a standard extremal object. The previously known unlabeled spectrum is not counted as a separate contribution: the value resides in the explicit pointwise pairing, uniqueness of all optimal words, and exact master-suffix structure. The result is an infinite-family structural classification rather than a narrow numerical sample.

## Limitations and closest sources
The finding is restricted to the two canonical Černý transitions and to two-state input subsets. It does not change known worst-case bounds for arbitrary automata; the unlabeled distance spectrum is also already implied by the known extremal maximal pair distance. The closely related 2020/2022 paper [1] supplies the original vocabulary and known extremal maximum, which are explicitly excluded from the novelty claim. Historical equivalent formulations cannot be excluded conclusively by indexing or keyword search.

Self-review: passed. Independent audit: not yet performed.

## References
[1] N. C. Behague and R. Johnson, *Electronic Journal of Combinatorics* 29(3), P3.41 (2022), arXiv:2008.12166.
[2] D. Eppstein, *SIAM Journal on Computing* 19(3) (1990), DOI:10.1137/0219033.
[3] F. Gonze and R. M. Jungers, *SIAM Journal on Discrete Mathematics* 30(2) (2016), arXiv:1410.4034.
