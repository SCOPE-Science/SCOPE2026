# Scientific review: exact geodesic-subpath counts for theta graphs

## Correctness

**PASS.** The proof partitions all unordered pairs into the pole pair, pairs belonging to a single arm (excluding the pole pair), and pairs internal to different arms. The universal baseline includes all distinct-vertex pairs and one zero-length path per vertex. For internal pairs on one arm, direct and alternate-arm routes are explicitly compared, including two equal shortest detours. For pairs on different arms, all four possible simple paths are listed and separated into two affine groups. The tie and duplicate-minimum boundary counts lead to the stated closed formula without double counting. This addresses every integer triple of path lengths at least two. Independent graph construction and exact BFS shortest-path counting agree for 364 short triples and 200 wider random triples.

## Originality

**PASS, with historical-priority risk.** Knor, Sedlar, Škrekovski and Zhang (2026) introduced this particular invariant and derived formulas for hypercubes, grids, sequential joins and extremal cacti, but their complete open preprint does not contain a three-path theta formula. Their cactus arguments do not directly apply because the theta cycles share edges. A geodesic-transversal source studies a different counting/optimization object. Accessible published summaries for geodesic subpath numbers on bicliques with a deleted matching and for diameter-two extrema concern different graph families. Searches for synonyms and three-path theta parameters revealed no result implying the present all-length formula. Relevant inaccessible or unindexed literature remains a genuine priority risk; search results cannot certify novelty.

## Mathematical value

**PASS.** A three-path theta graph is a canonical first noncactus series-parallel family. Unlike a cactus, its cycles overlap in edges; the shortest-route choice can therefore involve three equally short paths for some internal vertex pairs. The exact length-parity formula is not implied by the original paper's cactus theorem or its shortest-path counts for grids and hypercubes. It supplies a fixed-size integer-arithmetic expression for all three arm lengths and isolates the separate source of extra geodesics from equal shorter arms and from short third-arm routes. This natural exact family count can be used to test extremal conjectures beyond cacti; no broader theorem or classification is asserted.

## Closest literature and limitations

Primary: M. Knor, J. Sedlar, R. Škrekovski, X.-D. Zhang, *Counting geodesic paths in graphs*, arXiv:2604.04907v1 (first public 2026-04-06), DOI 10.1007/s00009-026-03159-3. Also compared: P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042, whose parameter is not the total geodesic count. The formula concerns simple three-arm theta graphs only; arbitrary numbers of arms, other series-parallel graphs, and fixed-order extremizers remain open here. Independent mathematical audit and comprehensive historical-priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
