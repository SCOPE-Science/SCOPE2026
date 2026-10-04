# Correctness
The proof reduces every legal sequence to the behavior forced by its first multipartite part. After the first selected vertex, all vertices outside that part are dominated; selecting further vertices inside the part can only footprint themselves, while the first selection outside the part dominates every still-undominated vertex of the initial part and therefore terminates the sequence. This proves the upper bound, the exact value \(\gamma_{\mathrm{gr}}(G)=m\), and the two-form classification. The counting formulas then follow by disjoint case counting, with the \(m=2\) set-count treated separately to remove double counting.

# Originality
Targeted searches for “complete multipartite graphs Grundy domination number maximum Grundy dominating sequences count”, “exact number of Grundy dominating sets complete multipartite graphs”, and close variants found related Grundy-domination and complete-multipartite results but no source stating the ordered-sequence classification or these enumeration formulas. The 2016 source develops Grundy domination and exact values in other graph families and products; the 2026 uniqueness paper gives qualitative uniqueness and iso-uniqueness results but does not enumerate complete multipartite maximum sets or sequences. Residual risk remains that a differently indexed source contains the same formulas.

# Value
The result gives a complete witness-level description, not only the invariant value, for a canonical graph class. It turns the qualitative non-uniqueness question into exact enumerators and separates the exceptional \(m=2\) set-count caused by two possible largest-part orientations. The formulas are immediately usable as closed benchmarks for algorithms that enumerate or sample extremal legal domination sequences.

Same-model review: passed. Independent audit: not yet performed.
