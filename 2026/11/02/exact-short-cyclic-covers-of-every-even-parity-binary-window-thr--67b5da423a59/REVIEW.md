# Scientific review

## Correctness

**PASS.** The mandatory even-parity edge set is a directed permutation of all length-\((n-1)\) words. Removing it from any covering Euler walk leaves a balanced augmentation, which decomposes into simple directed cycles. Connectivity is equivalent to connectivity of the hypergraph of mandatory components touched by those cycles; the reverse implication follows by Euler's theorem. The executable code canonically enumerates all simple cycles within verified feasible augmentation budgets, then uses an exact finite bitmask recurrence whose completeness follows by ordering the hyperedges of a connected family. This proves the minimum additional arc counts \((2,3,8,8,14,18)\) for \(n=2,\ldots,7\). Explicit witness words and an independent exhaustive small-order check corroborate the result. No statement for a larger order is inferred from a finite enumeration.

## Originality

**PASS, with qualified historical priority.** Burstein and Kitaev (2003, arXiv:math/0311399) treat unavoidable abstract word patterns and pattern universal cycles, not shortest cyclic covers of all indexed even-weight binary factors. Sawada, Williams, and Wong (2013, doi:10.1007/978-3-642-45278-9_33) cover consecutive weight intervals with no extra factors; their exact theorem does not imply the parity-selected cover lengths. The comparable previously recorded circular weight-two covering theorem concerns one weight level only, so neither direction of implication yields these parity-union minima. Searches for even-parity universal cycles, minimal parity covers, Euler augmentation, and these exact numbers identified no equivalent published theorem. The abstract of Campbell's 2013 thesis is available, but its full download was blocked and remains a residual priority risk. Absence from searches is not offered as a proof of uniqueness.

## Value

**PASS.** Parity-selective factor coverage is a natural restricted universal sequencing problem, whose required de Bruijn arcs form many disjoint permutation cycles. The result supplies six exact optimal lengths including the renewed shortening at order five after order four requires a complete de Bruijn cycle. The strict improvements at lengths five and seven over the odd-only-cycle construction reveal that merely connecting the odd parity necklace cycles can miss the true shortest cover. The finite classification and complete exact code enable comparisons of future parity-constrained constructions, without asserting an all-order formula.

## Closest work and scope

Sources: Burstein–Kitaev (arXiv:math/0311399, 2003-11-23); Sawada–Williams–Wong (IWOCA 2013 author manuscript, https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf); Campbell (ETSU 2013 thesis abstract, https://dc.etsu.edu/etd/1130/). The first two accessible works were inspected at the level of definitions and the relevant theorems; Campbell's full thesis was not readable. Results apply only to binary cyclic words with exact inclusion of each even-weight factor of lengths two through seven; no uniqueness or all-length extrapolation is claimed.

Self-review: passed. Independent audit: not yet performed.
