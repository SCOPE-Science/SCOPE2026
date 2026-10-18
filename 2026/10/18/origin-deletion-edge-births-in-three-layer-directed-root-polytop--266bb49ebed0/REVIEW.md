# Scientific review: three-layer directed root-polytope edge graphs

## Correctness — PASS
The statement is quantified over all positive integer part sizes. Each displayed arc is a vertex, and the affine dimension follows from the absence of a nonconstant functional with equal scores on all three cross-layer arc types. The proof gives strict exposing integer potentials for each allowed vertex pair, including a negative-support witness exactly in the singleton-middle case. Every disallowed pair has a second decomposition of the same vector sum, obstructing two-point exposure. The edge count, degrees, diameter, simple-vertex thresholds, and effect of adjoining the origin then follow by exact counting and comparisons. A separate exact-integer checker verifies all pairs in 125 profiles; this is corroboration, not the infinite proof.

## Originality — PASS, qualified
Numata–Takahashi–Tamaki (2022) give general facet and dimension criteria for directed edge polytopes. Setiabrata (2020–2021) characterizes faces of the origin-*adjoined* root polytope for arbitrary acyclic digraphs, a genuinely broader framework that covers every old nonorigin edge that survives in the origin-adjoined model. Neither inspected result states this full non-origin-adjoined three-layer graph, the all-parameter degree census, or the sharp \(b=1\) versus \(b\ge2\) edge-birth transition. The closest identified published one-skeleton classification applies to the full transitive tournament, which has all within-layer arcs as well and exhibits a linear, rather than arbitrary quadratic, number of origin-deletion edge births. This difference prevents direct specialization of that published theorem. The general face-characterization theorems could yield parts of the present computation after nontrivial additional derivations; this is the chief priority risk, along with possible unindexed equivalent formulations.

## Mathematical value — PASS
The class is the simplest complete transitively layered acyclic digraph containing long edges that violate the graded-rank condition: two-layer root polytopes are products of simplices, whereas three layers introduce paths and shortcut arcs. The result gives a complete one-skeleton and local degree census, detects nonsimple vertices, and proves a sharp structural transition in origin deletion. Setting the middle part to one creates \(ac\) new edges, arbitrarily many and quadratic when the outer sizes grow together; with two or more middle vertices no new edge appears. The precise threshold is not a renamed or arbitrary finite slice and is not merely the known general facet classification restated.

## Closest literature and limitations
- Y. Numata, Y. Takahashi, D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521, 2022. Primary paper inspected at its introduction, facet theorems and examples.
- L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191, 2020–2021. Main face characterization and transitively closed applications inspected. This is the strongest broad-coverage comparison; the claim explicitly distinguishes the origin-adjoined and non-origin-adjoined models.
- *Exact 1-skeleton and simple-vertex exhaustion of transitive-tournament root polytopes*, published mathematical research record, identifier `71a9627069b9`. Full statement and proof inspected. Its complete-tournament hypothesis is not the present complete three-layer hypothesis.

The theorem does not address missing cross-layer arcs, arbitrary quivers, or higher face numbers. Neither publication priority nor independent mathematical validation has been externally certified. A finite checker cannot replace universal proof.

Self-review: passed. Independent audit: not yet performed.
