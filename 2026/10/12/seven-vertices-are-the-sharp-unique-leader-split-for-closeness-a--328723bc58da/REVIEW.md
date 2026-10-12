# Self-review

## Correctness
**PASS.** The claim is finite and exhaustive on a documented complete graph domain. Every connected Atlas graph through seven vertices is checked. Two independent all-pairs shortest-path reconstructions agree exactly. Farness is integer-exact, harmonic centrality uses rational arithmetic, and full permutation checks verify the two seven-vertex orbit sizes and the three six-vertex tie-level orbit sizes. The two seven-vertex leaders have the stated distance multisets and exact scores.

Risk: completeness of the finite input relies on the externally documented Graph Atlas rather than an internally generated isomorphism-complete graph list.

## Originality
**PASS.** Prior work explicitly relates harmonic centrality to closeness and the 2026 harmonic-center paper studies harmonic centers directly, so neither the measures nor their possible qualitative distinction is claimed as new. The accepted claim is the sharp singleton-maximizer boundary and complete first layer. Published-record and web searches using center/maximizer aliases, exact order, exact count, and distance-profile formulations did not locate a covering theorem or table. The 2026 full text was inspected because it is the strongest plausible source; it discusses closeness centers but does not state this comparison boundary.

Risk: the 2026 paper is exceptionally close in topic, and an unindexed small-graph census may exist.

## Value
**PASS.** Closeness and harmonic centrality are two canonical distance-based ways to identify a central actor. Their distinction is mathematically meaningful: one minimizes total distance, while the other rewards many very short distances. The smallest network where those two unambiguous choices conflict is therefore a natural structural invariant. The common pair of distance profiles in both first-conflict classes gives a concrete explanation of the onset rather than only a census.

Self-review: passed. Independent audit: not yet performed.
