# Mathematical review

## Correctness

**PASS.** Hypersimplex adjacency is the Johnson graph \(J(n,2)\), so a generic section contributes exactly two vertices per sign-mixed index triple. For an additive pair-weight sign graph, the established threshold-graph construction representation turns every triple into the bit pattern \((b_j,b_k,b_k)\). Reindexing by the earliest member expresses the mixed-triple count as a sum of products of zero and one suffix counts; the optimal product is the balanced value \(\lfloor k^2/4\rfloor\) for each suffix. Every suffix can be balanced simultaneously. The explicit centered arithmetic normal and a generic small perturbation attain the upper bound: strict mixed triples and complementary tie pairs account for every case and recover the same sum. Degenerate cuts are controlled by a vertex-avoiding perturbation, as independently formulated in the 2024 general-polytope paper. The checker exhausts all construction words through \(n=15\) and tests exact-integer generic central and general cuts, but infinite validity rests on the proof.

## Originality

**PASS, subject to bibliographic risk.** Comparisons were made to the full relevant portions of Diaconis–Holmes–Janson, *Threshold graph limits and random threshold graphs* (2009), Kaibel–Walter, *Simple Extensions of Polytopes* (2013), and De Loera–Lopez-Campos–Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope* (2024), as well as related geometric results. Their weight-graph equivalence, Johnson adjacency description, general polytope bound, and perturbation lemma are all acknowledged as existing ingredients. The present extremal value, balanced-suffix classification, and centered attainment are not statements or direct instances of those published results. In particular the general upper bound with \(\binom n2\) polytope vertices is of order \(n^4\), rather than the sharp order \(n^3\) here. The main residual priority risk is an older equivalent theorem on threshold-graph mixed triangles under graph-theoretic terminology; no failed search is treated as uniqueness proof.

## Value

**PASS.** This closes a natural all-dimensional extremal problem for the hyperplane sections of a prominent family of polytopes. It supplies a sharp bound valid for all affine cuts, an exact combinatorial equality criterion for generic cuts, and the stronger geometric fact that the maximum is already achieved by central hyperplanes. The result is nontrivial relative to the general upper-bound theorem and is not an arbitrary small numerical refinement.

## Scope and validation

The result does not classify degenerate equality cases, higher hypersimplices, or higher face numbers. Bibliographic priority remains provisional. The executable finite checks supplement a complete combinatorial argument but are not independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
