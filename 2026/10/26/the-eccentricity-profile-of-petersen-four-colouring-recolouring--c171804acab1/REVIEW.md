# Scientific review

## Correctness — PASS
The precise input graph, named four-colour palette and legal one-coordinate recolouring are fixed. Two standalone exhaustive programs independently enumerate every possible proper colouring and every legal move using different Petersen representations. The first includes all eleven normalized colour/graph-permutation orbits and complete BFS distance histograms, and the second independently repeats each enumeration and uses its own BFS. The state count, degree distribution, orbit sizes, connectedness, radius and diameter agree. The key completeness facts are that the \(4^{10}\) functions exhaust the domain and every graph orbit is covered by a representative. This is exact finite proof, not extrapolation, and no infinite claim is made.

## Originality — PASS subject to literature limits
Eppstein (2010) explicitly gives the 120 three-colourings and their single-recolouring paired structure; the candidate makes no novelty claim for that result. OEIS A296913 lists 12,960 four-colourings. Relevant shortest-path and general colouring connectedness papers do not supply this exact Petersen radius/diameter/eccentricity profile in examined material. Optimal Kneser colourings use three colours, not four. Actual research-record searches for the precise graph, recolouring rule, exact diameter, aliases and covering theorems found no matching claim; that is not a proof of novelty. Inaccessible text and unindexed earlier results remain risks.

## Value — PASS
The Petersen graph's known disconnected optimal-palette (three-colour) dynamics naturally motivates the minimal connected extra-colour case, where optimal transformation distances matter for local recolouring. Determining the complete extremal-distance distribution rather than only counting proper colourings gives a meaningful exact combinatorial benchmark for a natural exchange graph. The result does not promise broader graph-theoretic or mixing-time consequences.

## Closest prior work and limitations
Eppstein's 2010 blog already resolves the three-colour dynamics. The 2008 connectedness study treats general recolouring graphs; the 2014 shortest-path paper motivates metric questions. OEIS already contains the four-colouring count. The result is only for Petersen with four named colours, is computationally exhaustive rather than symbolic, and has possible unlocated prior equivalents. The 2008 full text could not be reviewed.

Self-review: passed. Independent audit: not yet performed.
