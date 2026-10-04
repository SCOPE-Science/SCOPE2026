# Same-model review

## Correctness
PASS. The finite domain contains exactly \(120\) permutations. The verifier reconstructs Ulam distance from longest common subsequences, builds the entire compatibility graph, enumerates every maximal clique, and independently checks each accepted structural assertion. The maximal-clique histogram is exactly \(60\) of size \(2\), \(120\) of size \(3\), and \(4020\) of size \(4\), proving both the maximum and the complete labeled census. All \(4020\) maxima have six pairwise distances equal to \(3\). The declared \(240\)-element transformation set is directly checked to preserve all pairwise distances before orbit enumeration.

## Originality
PASS. The closest exact-parameter source, arXiv:1504.05100v1, explicitly gives the prior optimum \(A(5,3)=4\) but does not state a count of maximum codes, universal equidistance, or an orbit classification. The foundational arXiv:1202.0932v1 defines the same Ulam/translocation metric and proves the relevant invariance, but studies bounds and constructions rather than this finite extremizer census. Targeted published-record and web searches for exact-parameter aliases, the count \(4020\), equidistance, maximum-clique enumeration, and symmetry classification found no implication-equivalent result. Residual risk is an obscure or unindexed finite enumeration.

## Value
PASS. This parameter cell is explicitly singled out in the prior finite-search literature as a non-Singleton-optimal small case, with the optimum known but its extremizers undescribed. A complete census plus the universal equidistance constraint and symmetry decomposition supplies a reusable calibration datum for Ulam-code search, classification, and finite-bound methods, rather than merely recomputing the already known value \(4\).

Same-model review: passed. Independent audit: not yet performed.
