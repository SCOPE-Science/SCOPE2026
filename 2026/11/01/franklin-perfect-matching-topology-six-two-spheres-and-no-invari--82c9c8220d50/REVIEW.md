# Scientific assessment

## Correctness — PASS
The claim uses an explicitly defined graph and extendibility complex. The standalone `verify_franklin_pmc.py` exhaustively enumerates all 17 perfect matchings, builds all 761 nonempty faces, performs 321 checked elementary collapses and 56 further pairs, and topologically sorts all 761 nodes and 2610 directed incidences of the complete matched Hasse graph. Exactly one critical vertex and six critical triangles remain; Forman's discrete Morse theorem supplies the wedge of six two-spheres. A disjoint exhaustive all-subsets implementation in `verify_franklin_chain.py` reproduces the face count, the 330 nonextendible ordinary matchings and mod-two ranks. Exact signed simplicial Lefschetz traces for all 48 exhaustively enumerated automorphisms yield the trace multiset and zero invariant dimension. No computational inference from finite samples to an infinite family is used.

## Originality — PASS against inspected evidence
The closest located same-graph result concerns the larger ordinary matching complex and its deletion/link profiles; it does not imply the homotopy or symmetry of the proper extendible-matching subcomplex. Bayer et al. (arXiv:2209.02803) treat planar honeycomb patches, Chandrakar and Singh (arXiv:2407.05809) treat polygonal line tilings and two-row grids, and Agarwal and Basak (arXiv:2608.30601) treat a different Möbius-ladder family. Targeted searches included Franklin, crossed-prism, Knödel and toroidal-honeycomb aliases, counts and representation signatures. Residual risk: an unindexed prior computation could exist, and lack of an indexed hit is not itself evidence of uniqueness.

## Value — PASS
Franklin is a canonical vertex-transitive cubic bipartite graph associated with the exceptional Klein-bottle six-color embedding. The perfect-matching complex is the natural extendibility subcomplex of the already studied ordinary matching complex. Its integral homotopy changes from the ordinary complex's twelve three-spheres to six two-spheres, and the entire automorphism group has no fixed rational second-homology vector. The exact homotopy-plus-character distinction is a substantive topological invariant of this symmetric graph, not an arbitrary unlabeled calculation. No general graph-family theorem or equivariant sphere splitting is claimed.

## Scientific limits and closest source
Closest same-graph statement: *Edge-orbit matching-complex splitting for the Franklin graph*, published research record at the exact URL in `RESULT.md`, concerning ordinary matchings. Other sources and verified scope exclusions are listed in `AUDIT.json` and `RESULT.md`. The finite proof is complete for Franklin only; other graph families, nonrational representations and independent external review are not established.

Self-review: passed. Independent audit: not yet performed.
