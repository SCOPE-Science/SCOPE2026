# Mathematical self-review

This corrected scientific summary narrows the frozen self-review to the transfer theorem; the independent assessment is separate.

## Correctness — PASS

The proof reduces each zero-cell condition to the exact row-plus-column inequality \(r_i+c_j\ge2\). The exhaustive dichotomy between an empty column (forcing each row weight at least two) and all columns nonempty (forcing total weight at least the number of columns) supplies the sharp lower bound and, crucially, complete equality cases. On the equality line both families occur, with intersection counted by allocations of two labeled columns to every row. The connectivity proof uses constructive nonempty-fibre recoloring moves for onto maps; a third non-singleton fibre mediates swaps between singleton fibres whenever \(n>m\). The complementary row-weight-two family has a factorwise multiset-transfer structure. The proof explicitly checks that the allowed moves in the strict \(n>2m\) regime cannot change row totals. Product-metric and degree formulas follow from complete local adjacency. Two programs independently corroborate the claims by exhaustive directly checked configurations and by separately constructed rowwise states; see their actual source and output files. Finite checks are supporting evidence, not substitutes for the proof.

## Originality — PASS, with stated residual risks

*Minimum Italian domination on rook graphs: exact optimizers and a sharp transition* (reference [6] of the corrected finding) gives the same full minimum-weight classification and counts. These are background, not novelty claims. That source does not give the unit-transfer connectivity theorem or product geometry. The perfect Italian product theorem of Varghese–Lakshmanan concerns the stronger equality condition and uses a different state space; there is no substitution for the unrestricted transfer operation. General domination bounds, threshold-three variants and complete multipartite graph results also do not supply the transfer theorem. The original papers by Chellali et al. and Klostermeyer–MacGillivray were not wholly inspected, so the comparison is limited to checked statements and leaves open unindexed overlap.

## Value — PASS

The known family classification does not tell whether optima can be transformed into each other without leaving minimum weight. A single extra column removes the frozen-square obstruction. For \(n>2m\) transfers factor by row, giving the exact travel cost and degree distribution over all optima. The theorem concerns the specified unrestricted transfers, not the usually different graph obtained by constraining transfers to rook edges.

## Closest literature and scientific limits

Chellali, Haynes, Hedetniemi and McRae (2016), DOI 10.1016/j.dam.2015.11.013, introduce the variant. Klostermeyer and MacGillivray (2019) compare domination variants (public abstract inspected, not entire article). Varghese and Lakshmanan (2023; preprint 2019) give the perfect Italian result (full primary theorem text read). Davila and Krop (2017) give general Cartesian weak-two lower bounds (open-access article inspected). No unrestricted-edge token-slide or other reconfiguration model is asserted equivalent. Originality has not been independently validated and cannot be established by absence of search hits alone.

Self-review: passed. Independent audit: not yet performed.
