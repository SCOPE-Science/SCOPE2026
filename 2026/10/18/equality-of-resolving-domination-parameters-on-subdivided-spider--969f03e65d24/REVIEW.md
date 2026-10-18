# Scientific review: equality on subdivided spider trees

## Correctness
**PASS.** The proof first shows that vertex and edge landmark resolution are both equivalent to meeting all but at most one arm. Every vertex-dominating set already meets every arm. For domination, each selected vertex covers at most three consecutive arm vertices; for vertex-edge domination it covers at most four consecutive arm edges. Three exhaustive choices about center selection and depth-one vertices yield the exact minimization formula. The ceiling comparison then proves the iff equality criterion. An independent graph-distance checker validated the resolving-arm lemma on 2,688 vertex subsets and both minima in 51 small cases, and modular calculations checked 42,294 additional arm profiles. Finite checks are corroboration, not the infinite proof.

## Originality
**PASS, with residual bibliographic uncertainty.** Ikhlaq–Hayat–Siddiqui (arXiv:2211.09327v1, 2022) prove a general tree comparison and pose equality characterization as an explicit problem. Their full-text definitions, tree statements and concluding problems were materially inspected. Similar subsequent edge-metric work uses vertex covers instead of vertex-edge domination, while indexed balanced-spider work concerns different domination radii. Mathematical-record searches using exact and equivalent descriptions found no result implying both arbitrary-arm formulas and the equality boundary. Unindexed work and uninspected parts of adjacent publications remain limitations.

## Value
**PASS.** The result solves a motivated classification problem for an infinite, structurally natural subtree family, not only for equal arms: equality occurs precisely when every arm has two or three edges and at least one has two. Its formulas identify a qualitative phase boundary between radius-one vertex coverage and distance-one edge coverage; five-edge uniform spiders produce an unbounded parameter gap.

## Scope and limitations
All arms must have length at least two; unit-length arms and arbitrary nonsubdivided trees are not covered. This statement does not claim a global resolution of the full tree open problem. Computed checks are reproducible with `verify_spider.py`; independent audit, peer review, and exhaustive literature certainty are absent.

Self-review: passed. Independent audit: not yet performed.
