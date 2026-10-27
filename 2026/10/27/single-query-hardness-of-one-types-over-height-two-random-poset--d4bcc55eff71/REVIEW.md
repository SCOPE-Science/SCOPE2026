# Scientific review

## Correctness

**PASS.** The downset/upset classification partitions the nonalgebraic types into empty-side and nonempty-side cases. For bipartite height-two posets the latter case is exactly biclique-subset enumeration, equivalently independent-set enumeration in the bipartite complement. The isolated-vertex amplification and remainder bounds are exact; one integer-division query recovers the starting graph's independent-set count. The disjoint-edge factor establishes hardness for height **exactly** two, and ternary certificates establish membership in the counting class. Exhaustive small graph checks and larger samples reproduce the identities.

## Originality

**PASS, qualified.** The previously published random-poset hardness result proves unrestricted and greatest-element hardness using a two-query ordinal-sum identity, but does not imply height-two hardness or the bipartite-complement one-query identity. The finite-poset extension lemma and bipartite independent-set hardness are acknowledged predecessors. Examined studies of minimal-element poset extensions and generalized intervals concern different enumerators. Equivalent formulations and residual publication-priority risk remain documented in the structured review.

## Mathematical value

**PASS.** This locates a sharp low-height tractability frontier: height-one parameter counting is elementary, whereas height-two counting is \(\#\mathrm P\)-complete. The explicit complement identity and isolation extraction explain the boundary structurally and convert a graph counting problem into one exact type-count query. The claim is not merely a restatement of unrestricted hardness.

## Limitations

Hardness is asserted under polynomial-time Turing reductions, using one query for the displayed bipartite-independent-set reduction. The construction does not establish bounded-degree or connected-input hardness, approximation hardness, or independent validation. Specialized earlier work may still cover the same restriction.

Self-review: passed. Independent audit: not yet performed.
