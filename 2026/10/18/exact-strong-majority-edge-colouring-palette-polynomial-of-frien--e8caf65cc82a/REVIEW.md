# Scientific review

## Correctness — PASS

The statement distinguishes labelled palettes from exact-use or orbit counts. The base-edge degree-two condition forces two different spoke colours in each triangle, which bounds every colour's spoke frequency by the number of triangles. For a spoke, the exact adjacent-colour count is the global spoke count, minus an indicator for the spoke itself, plus the local base indicator. This proves the base exclusion for exactly the colours present in every triangle, in both directions. Inclusion-exclusion over the intersection of two-colour spoke sets yields disjoint cases with zero, one, or two universal colours, and the independent base assignments give the formula. Exhaustive direct graph checks tested 834,518 assignments and agreed in every case. Finite tests do not establish the infinite theorem; the elementary proof does.

## Originality — PASS, with residual risk

The primary May, June, and August 2026 literature on strong-majority edge colourings addresses definitions, existence bounds, and threshold phenomena. The first paper's Proposition 21 **already implies** the index-three consequence on these Eulerian triangle bouquets; this is not claimed new. No full named-palette enumeration for friendship graphs was found in the inspected relevant primary texts or published mathematical-record comparisons. The graph is also described as a triangle windmill, Dutch windmill, or \(K_1\vee(nK_2)\); the strong-majority problem can be expressed on its line graph. The available indexed comparisons are not an exhaustive proof of priority, and unindexed equivalent formulas remain a residual risk.

## Value — PASS

The exact polynomial in named palette size, together with a necessary-and-sufficient classification of every colouring, resolves the complete enumeration for an unbounded natural graph family. The global restriction comes from the interaction of base edges with colours present in every triangle, so the count is not a product of local triangle counts. The count refines an already-known chromatic-index bound and can be specialized to any palette, with all labels retained; these are natural combinatorial coefficients rather than an arbitrary numerical slice.

## Limits and nearest literature

The nearest primary results are Kalinowski–Kamyczura–Pilśniak–Woźniak (arXiv:2605.23828, particularly Proposition 21), Antoniuk–Prorok–Salia (arXiv:2607.00212), and Pękała–Przybyło (arXiv:2608.04122). None of the inspected materials was identified as containing this palette enumeration; definitive bibliographic priority remains unproved. Independent verification of the mathematical proof has not taken place.

Self-review: passed. Independent audit: not yet performed.
