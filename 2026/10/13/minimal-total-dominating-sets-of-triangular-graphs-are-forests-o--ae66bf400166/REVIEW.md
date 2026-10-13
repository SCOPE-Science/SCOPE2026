# Review of minimal total dominating sets of triangular graphs

## Correctness — PASS
The edge-domination criterion (at most one isolated vertex and no selected isolated edge) is necessary and sufficient even for selected vertices of the line graph. Deleting a cycle edge never harms it, so minimal selected graphs are forests. In the isolate-free case the leaf-edge test forces components to be exactly three-vertex paths. With one isolate, nonpendant-edge deletion forces a two-vertex split-off component, which is equivalent to stars with some once-subdivided arms. The hub-rooted exponential count corrects its unique double-counted four-vertex path. The proof covers every \(n\ge3\), and the exact checker agrees on all \(2{,}131{,}016\) examined subsets for orders three to seven.

## Originality — PASS with residual risk
The mathematical closest comparisons are the general claw-free upper-total-domination bounds of Favaron–Henning (2003), Henning–Yeo (2006), the output-sensitive minimal-total-domination enumeration reductions of Kanté–Limouzy–Mary–Nourine (2014), and the ordinary edge-domination algorithm of Kanté and collaborators (2014). The latter uses closed adjacency and does not imply the open-adjacency total domination enumeration. The general total-domination polynomial of Chaluvaraju–Chaitra counts all, not just inclusion-minimal, sets. No inspected primary statement or relevant searched published record implied the complete \(L(K_n)\) classification and EGF; search noncoverage is not a uniqueness proof. Full text of a relevant 2003 bound paper and a general 2014 polynomial paper was inaccessible; alternate terminology and unpublished or unindexed equivalent results remain genuine priority risks.

## Value — PASS
The exact inclusion-minimal-set polynomial supplies each cardinality count, gives the lower and upper total domination numbers as consequences, and identifies the precise selected-forest geometry. A complete classification on a natural family is more informative than the known general inequalities and than computing one small parameter. The four-vertex-path correction is necessary for reproducible exact enumeration.

## Scientific limits
Finite enumeration is independent corroboration only. The result makes no statement about full total-domination polynomials, arbitrary line graphs or independently certified priority. Access limits are recorded without claiming inaccessible full text was inspected.

Self-review: passed. Independent audit: not yet performed.
