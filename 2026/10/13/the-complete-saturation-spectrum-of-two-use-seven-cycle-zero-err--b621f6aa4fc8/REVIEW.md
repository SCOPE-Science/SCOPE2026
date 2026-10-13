# Scientific review

## Correctness: PASS

On the exact vertex set \((\mathbb Z/7\mathbb Z)^2\), two channel inputs are confusable iff both circular coordinate differences belong to \(\{0,\pm1\}\). In the complement compatibility graph, a maximal clique is exactly a nonextendable zero-error codebook. Standard exhaustive pivoted maximal-clique recursion explores all such cliques with no duplicates; two separately implemented programs generated identical sorted mask catalogues (SHA-256 `362d213751756f339a3319847ce2bc6b580fd2ddc34d124b265e0a1dd417de13`). Each returned mask passed an independent direct membership/nonextendability check, and the generators' orbits partitioned all 83,181 masks. The result covers exactly two uses and all labeled 49-input subsets; no inference from samples is involved.

## Originality: PASS, with residual literature risk

The 2012 odd-cycle product paper and classical formula already determine the maximum cardinality ten. A prior maximum-code catalogue contains 980 such codes and three natural orbits. The 2018 Yang–Zhang theorem already implies minimum inclusion-maximal cardinality seven. The 2026 Hildebrant full text determines the *ordinary* independence polynomial of this same graph, which does not identify which submaximum independent sets are inclusion-maximal or their symmetry orbits. The new claim is instead the full terminal histogram (28, 9016, 73157, 980) and the 229-orbit classification, including 82,201 nonmaximum terminal codes. Primary same-graph literature was compared by the logical scope of its theorems, not just wording. The full 2005 Klobučar paper was inaccessible despite the journal portal listing its PDF, so its exact coverage remains a residual risk; none of the accessible primary statements supplies the terminal census. See `AUDIT.json` for detailed comparisons.

## Value: PASS

Inclusion maximality is the operational stopping condition for iterative zero-error codebook design. A stopping set may have only seven codewords even though ten are possible; moreover 82,201 suboptimal endpoints and their 226 symmetry classes are structurally distinct from the already known optimum census. Enumerating all terminal sizes, their frequency, and symmetry provides a natural complete finite answer for the first seven-cycle channel whose strong-product behavior is more subtle than the pentagon case. The result is not a renaming of a known extremal size or a numerical extrapolation.

## Limitations and sources

Two-use seven-cycle channel only; asymptotic Shannon capacity and higher products are not studied. The exact 2005 PDF was not readable; an unindexed complete enumeration cannot be categorically excluded. Main published comparisons: Klobučar (2005), Korže–Vesel (2012), Yang–Zhang (2018), Hildebrant (2026). All computational code and the exact finite catalogue are included.

Self-review: passed. Independent audit: not yet performed.
