# Scientific review

## Correctness — PASS

The graph has the exact 24 edges displayed in `RESULT.md`. Independent finite assertions are reproduced by `verify.py`: 2835 nonempty simplices; 1397 complete disjoint Morse pairs; 10816 Hasse incidences; 2835 vertices removed by the full acyclicity topological sort. The resulting one-vertex Morse CW complex has exactly 34 three-cells and 6 four-cells. Signed gradient projection yields an integral 34-by-6 boundary; exact minors of sizes five and six have determinants -1 and 3, and its rank over the field of three elements is 5. Consequently the Smith invariants are 1,1,1,1,1,3. Hurewicz in the two-connected three-skeleton and elementary changes of attaching-map bases give the claimed Moore summand and 28 three-spheres. Separately, ranks of the original simplicial boundaries are checked over fields of two, three and five elements. The computation is complete rather than an unbounded experiment; no infinite-family claim is made.

## Originality — PASS (best available knowledge)

The closest indexed comparison is the icosahedral matching complex, which likewise contains a Moore summand of order three but comes from the different 30-edge icosahedral graph and has 64 rather than 28 free three-spheres. The 11-vertex Grötzsch graph has a torsion-free matching complex, not this graph. Indexed findings about the *independence* and *neighborhood* complexes of the Chvátal graph have different simplicial objects, and do not determine its matching complex (the independence complex of its line graph). Jonsson's inspected primary text addresses complete-graph matching complexes; the inspected outerplanar theorem cannot apply to the 4-regular Chvátal graph. No equivalent or stronger covering theorem was identified in the checked index or literature searches. The inaccessible 1970 original and possible unindexed sources remain acknowledged risks; bibliographic excerpts alone were not used to certify their noncoverage.

## Value — PASS

The Chvátal graph is the classical smallest triangle-free 4-regular 4-chromatic example. Its matching complex is a canonical topological invariant, and the exact degree-three order-three torsion is invisible to rational homology. This natural comparison isolates torsion that is absent in the 11-vertex Grötzsch graph's matching complex. The complete *homotopy type* goes beyond a homology-rank computation and is neither a generic formula substitution nor an arbitrary parameter slice.

## Scope, limitations and literature

The proof applies to the explicitly labeled 12-vertex graph and its isomorphic copies, not all triangle-free four-chromatic graphs. The verified source date identifies the graph's original 1970 publication rather than a later revision. The original 1970 article was not fully accessible; its bibliography supports identification, not a full-text noncoverage conclusion. Closest full-text inspected sources: Jonsson, *More Torsion in the Homology of the Matching Complex*, arXiv:1203.5658 (complete-graph matching complex); Bayer–Jelić Milutinović–Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (outerplanarity hypothesis). Indexed comparison records are cited in `RESULT.md`. The executable finite proof does not establish independent validation.

Self-review: passed. Independent audit: not yet performed.
