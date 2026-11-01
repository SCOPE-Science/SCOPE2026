# Scientific review: squared-cycle packing neighborhoods

## Correctness — PASS

The single claim is a finite integral homotopy classification at \(k=2,3,4\). All graph vertices are enumerated directly as independent \(k\)-subsets of \(W_{3k+2}\), with an independent cyclic-gap test; all neighborhood-complex simplices are enumerated from all open neighborhoods. The complete matching is checked acyclic on the full directed Hasse graph, not merely sampled. Exact signed Morse boundaries compose to zero and have nonzero Smith invariant factors all equal to one. The specific critical dimensions and unit cancellations establish the claimed CW homotopy types. `verify.py` is a self-contained executable certificate, modulo the stated SymPy dependency. Residual correctness risk: the passage from integer Morse data to homotopy uses standard cellular cancellation and simple-connectivity arguments; execution does not constitute independent proof checking.

## Originality — PASS

The closest direct source, Shen et al., *Neighborhood Complexes of induced k-independent graphs*, arXiv:2512.09674 (2025), defines \(H_k\), determines \(\mathcal N(H_k(W_{3k+1}))\) for the adjacent residue, and emphasizes that its cover giving the total-cut nerve need not be good. It does not state the three \(3k+2\) neighborhood types. Shen et al., *Homotopy Type of Total Cut Complexes of Squared Cycle Graphs*, arXiv:2510.22574 (2025), computes \(\Delta_k^t(W_{3k+2})\), a different complex on the original cyclic vertices. Its sphere \(S^5\) for \(k\ge3\) does not imply the neighborhood calculation; the computed neighborhood types have a different degree and demonstrate non-goodness of the cover. Published comparison records concerning ordinary squared-cycle cut complexes and ordinary neighborhood complexes of third-power cycles concern different objects and do not imply this claim. Searches using both the induced-graph and the maximum-packing/disjointness aliases found no covering theorem. An equivalent calculation in unindexed literature remains possible, so the search is evidence rather than proof of global novelty.

## Mathematical value — PASS

This is a natural three-case classification at the first unresolved residue adjacent to a theorem in a recent study. The smallest case exhibits mixed-dimensional integral homotopy, whereas the next two are three-spheres; these behaviors are not predicted by the total-cut sphere formula. The explicit discrepancy proves a nontrivial boundary of the proposed nerve-cover correspondence in the same family. The finite cutoff is mathematically motivated by the three consecutive nontrivial maximum-packing parameters and yields a complete, independently reproducible finite result rather than an arbitrary parameter substitution. It does not give the general \(k\)-formula; that is an explicit limitation, not a claimed extension.

Self-review: passed. Independent audit: not yet performed.
