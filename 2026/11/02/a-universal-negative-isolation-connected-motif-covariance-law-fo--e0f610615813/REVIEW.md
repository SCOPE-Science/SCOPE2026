# Mathematical assessment

## Correctness — PASS

The proof uses exactly specified uniform matchings and induced connected subgraphs. Fixing one isolated chord partitions the remaining endpoints into two independent uniform matching arcs. Connected induced motifs cannot straddle these arcs. Counting endpoint pairs by arc size yields the exact covariance. Vandermonde's identity forces each bracket strictly negative. For fixed motif size, adjacent chords supply the leading term and a geometrically bounded tail of nonadjacent isolated chords is lower order. The executable finite checker verifies 684 exact assertions from explicit matchings (including all 10,395 size-six diagrams), without being used as a substitute for the infinite proof.

## Originality — PASS, with historical-priority risk

Acan (2015) and Flajolet–Noy (2000) establish the foundational random diagram model, component behavior, and marginal crossing moments. Neither inspected relevant material states this connected induced-motif covariance kernel, size-only normalization, or universal negative sign. Existing simple-chord/crossing formulas do not dominate isolation of arbitrary (not necessarily adjacent) chords, nor larger connected motifs. The related random graph isolation–motif covariance does not transfer to a non-independent circle graph. Stoimenow (2000) was available at abstract level only; no claim is made about all its contents. A stronger historical generating-function treatment could imply the identity, so priority remains qualified.

## Mathematical value — PASS

The theorem gives a structural all-connected-motif sign law in a natural probability model, a complete finite-size normalized covariance kernel independent of motif shape, and a quantitative leading asymptotic. The explicit disconnected-motif reversal explains why connectivity is mathematically essential. It resolves dependence across an infinite hierarchy of local crossing patterns and global isolated-component statistics, not merely one convenient low-order count.

## Literature and limits

Relevant primary material: Acan, arXiv:1501.01489v1, sections on degree and monolithic diagrams; Flajolet and Noy, RR-3914, component and crossing sections; Paguyo, arXiv:2104.01134, marginal simple-chord and crossing results. The full text of Stoimenow's *On the number of chord diagrams* (2000) could not be inspected and is a residual historical-priority risk. The proof does not cover disconnected patterns in general, nonuniform chord models, or growing motif sizes. Independent expert validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
