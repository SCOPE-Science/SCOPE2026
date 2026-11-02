# Scientific review

## Correctness — PASS

The distance rank \(D_n\) is an exact permutation of the unordered-pair set, as proved by cyclic chord-separation blocks. The six parity cases and the special wraparound pair exhaust all alphabet transitions and establish a unique rank-decreasing action, the minimal nontrivial jump \(\lfloor(n-1)/2\rfloor\), and exactly one transition attaining that jump. Word enumeration in the safe slack window follows by a bijection with weak compositions of idle letters plus unrestricted post-merge suffixes; sharpness follows by using the unique minimal upward jump. A separate standard-library checker confirms all pair states and low-slack counts for \(3\le n\le22\), with literal word enumeration for \(n\le5\). No infinite statement relies on sampling.

## Originality — PASS, qualified

The exact extreme pair-merging **distance** and a Hamiltonian traversal of the pair graph are closely anticipated by Montoya and Nolasco, §2.1 (2017). Those are expressly excluded from the priority claim. The new content is the exact counting law for *all words* in the growing slack interval, a state-specific exponent, and a sharp first correction, requiring a global analysis of all nondescending pair transitions. The 2013 shortest-reset algorithm paper addresses full-state words and computational complexity rather than pairwise near-optimal multiplicities. No decisive equivalent or stronger result emerged from the performed specific searches. Unindexed historical papers and uninspected source sections are residual risks, not ruled out by failed retrieval.

## Value — PASS

A controlled system may have two possible initial states instead of total uncertainty. The natural invariant is the number of short commands guaranteed to merge the two states. Here unique optimality coexists with a polynomially growing number of near-optimal commands, and the clean formula persists for a *linearly expanding* number of extra letters. The sharp first excursion proves a genuine stability threshold, not an arbitrary finite computation or a restatement of the known extreme pair distance.

## Limitations and closest prior results

The theorem applies only to the canonical binary Černý family and pair synchronization, and to the low-slack range specified in the result. Montoya–Nolasco (2017, §2.1) is closest on the pair-graph geometry; Kisielewicz–Kowalski–Szykuła (2013 online, §5.2) is closest on shortest-reset algorithms. Independent historical-priority inspection has not been performed.

Self-review: passed. Independent audit: not yet performed.
