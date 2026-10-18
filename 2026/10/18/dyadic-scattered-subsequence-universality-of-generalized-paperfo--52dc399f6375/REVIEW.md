# Mathematical review

## Correctness — PASS
The two paperfolding definitions are equivalent by the standard folding recursion. For every eight-symbol block, the explicit three-state arch transition identities can be checked for all bits and reachable states. In the case \(d_0\ne d_1\), each block creates exactly three complete arches. In the case \(d_0=d_1\), successive contributions telescope to \(3\cdot2^{k-3}-\mathbf1_{\{d_k\ne d_0\}}\). The greedy-arch principle identifies this count with the largest universally present scattered-subsequence length. A separate counting argument gives the \(1/4\) exceptional fraction. The all-length claim follows from this finite-state proof, not numerical extrapolation.

The bundled `verify.py` executes independent valuation and recursion generators, all instruction choices for \(3\le k\le10\), selected larger samples, all local input-state transitions, and direct subsequence-set checks for small lengths. It returned `VERIFY_OK` in the reported execution. The tests cannot certify infinitely many inputs on their own.

## Originality — PASS, qualified
Holub (arXiv:1207.3585) treats contiguous abelian powers in generalized paperfolding words, not this invariant. Barker et al. (arXiv:2003.04629) and Schnoebelen–Veron (arXiv:2304.11932) develop generic arch/universality methods and were examined in full accessible text; the new instruction-specific all-scale identity is not stated there. Shallit's run-classification manuscript (arXiv:2412.17930) was also inspected in full; its run results do not directly imply the asserted formula. The closest published-finding corpus records concern all-word universality distributions, absent-subsequence extrema, and different paperfolding invariants; the accessible own ledger contained no equivalent claim.

The 2015 paper *A New Approach to the Paperfolding Sequences* could be read only at abstract level, not as complete text. An equivalent result there, in inaccessible sources, or in unindexed work remains a residual risk; database absence is not a novelty proof. 

## Mathematical value — PASS
The new theorem supplies a precise natural combinatorial invariant for an entire uncountable classical automatic-word family, with a sharp instruction-dependent endpoint defect and a shared asymptotic density. The telescoping block transducer is explanatory, not simply a routine finite table or a general-purpose algorithm's output. The result is limited to binary dyadic prefixes, not arbitrary cutoffs or full shortest-absent-subsequence distributions.

Self-review: passed. Independent audit: not yet performed.
