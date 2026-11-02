# Scientific review

## Correctness — PASS

The 36-pair exact-cover recursion branches over every compatible triple through a currently uncovered pair and produces each order-nine Steiner triple system exactly once. It returns 840 distinct systems; the independent group enumeration produces exactly 840 cosets of the 432-element affine stabilizer. Transposing two points exchanges six blocks, and the 36 resulting neighbors are distinct. A complete 352,380-pair incidence comparison finds no additional six-block-trade neighbors. The first checker performs BFS from each of the 840 systems and confirms the complete intersection/distance table. The second checker independently applies the transposition-length/coset formula over every affine automorphism. The proof distinguishes an actual minimum trade from its path length, and all asserted outcomes are finite exhaustive facts rather than sampling. The group-theoretic deductions of the Schreier description and connectivity are proved separately from the exhaustive table.

## Originality — PASS, with residual priority risk

Existing STS(9) literature already establishes the 840 labelled systems and their possible intersection sizes, as quoted in Chee–Ling–Shen (2008), and older work classifies small trades. Cameron (2002) proves connectivity for a *different* chain with improper intermediate systems; his order-nine point transposition requires two of those steps rather than one proper six-block trade. Forbes–Grannell–Griggs (2006) study single-trade volume between **isomorphism classes**, chiefly of order 15, not a path metric among labelled order-nine designs. The present point-transposition realization, complete labelled trade graph, and particularly the seven-row intersection-to-shortest-path law were not obtained from any accessible inspected source or published semantic search result. A book chapter on uniformly intersecting STS(9) sets by Griggs–Rosa (2003) was identifiable only at abstract level, so an equivalent classification somewhere within it remains possible. Absence of a hit is not a uniqueness proof.

## Mathematical value — PASS

This resolves the smallest nontrivial proper-trade mobility problem for a canonical Steiner design where the smaller Pasch trade cannot be used. It distinguishes one-step overlap from multi-step reachability and produces an explicit optimal upper bound of three simultaneous volume-six trades for *any* two labelled realizations. The association between all possible common-block counts and exact shortest distances is a structural constraint on design reconfiguration, useful when assessing legal local searches or comparing trade-based chains that do and do not admit improper states. This is not merely a recomputation of the known enumeration or of its intersection spectrum.

## Literature and limitations

Closest primary materials examined: Lindner–Rosa intersection theorem as stated in Chee–Ling–Shen (arXiv:0807.2500); Cameron's 2002 complete relevant note sections; Forbes–Grannell–Griggs' 2006 preprint; Forbes' 2006 dissertation chapters 5–6. The Griggs–Rosa STS(9) 2003 chapter had a relevant abstract but inaccessible full text, a material but nondecisive priority uncertainty. No infinite-order claim or independent scholarly audit is made.

Self-review: passed. Independent audit: not yet performed.
