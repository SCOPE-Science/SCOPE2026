# Review: exact 1-skeleton of positive type-A root polytopes

## Correctness — PASS
Every claimed adjacency is witnessed by an explicit all-parameter integer supporting functional; nonadjacencies follow from a parallelogram identity or the strict sign contradiction for a chain. Vertex extremality, dimension, all local degrees, the exact edge count, the simple-vertex cutoff, and the diameter are derived in the proof. A standalone integer checker confirmed the formulas for all \(3\le n\le12\) and a separate linear program independently classified every pair of vertices for \(3\le n\le8\). Neither finite computation is misrepresented as an infinite proof. The all-dimensional proof does not use the computations.

## Originality — PASS, with specified literature risk
The 2022 quiver-polytope work of Numata, Takahashi and Tamaki supplies general face tools but not this transitive-tournament graph evaluation. Setiabrata's 2020 origin-added root-polytope theorem describes the edges of \(\widetilde P_n\): the new \(n-2\) consecutive-unit-root edges of \(P_n\) cannot occur there. Their absence follows from their necessarily negative supporting height, not a title or keyword comparison. The closest unresolved source is Cho's older root-polytope work, whose full text was not recovered; an equivalent alternative specialization remains possible. Detailed source comparisons, actual queries, and limitations are in `AUDIT.json`.

## Value — PASS
The full 1-skeleton criterion gives all edge incidences, an explicit edge polynomial and degree formula, a path of exactly \(n-2\) new edges under origin deletion, and the sharp disappearance of simple vertices in dimension five and above. This is a structural calculation for a canonical family, not an arbitrary finite example. It does not claim a classification of higher faces.

Same-model review: passed. Independent audit: not yet performed.
