# Review: solid-metric dimension of consistently directed toroidal grids

## Correctness — PASS

The statement quantifies over all integers \(m,n\ge3\) and concerns directed distances *from* landmarks, not ordinary or strong resolving sets. The ordered-pair equivalence is reconstructed directly. The lower bound uses two explicit classes of ordered vertex pairs: every second-coordinate row must contain a landmark, and every first-coordinate column must contain two distinct landmarks. The four-case distance calculation is valid under the normalization \(m\le n\), including the equality case \(m=n\). The sufficient interval-expansion lemma is proved with an exact modular distance-difference identity, and both explicit families satisfy its premises. Symmetry completes the general case. Direct-distance and integer-programming tests supplement but do not replace the proof.

## Originality — PASS (best-knowledge, with priority risk)

The closest work is Hakanen–Pavan (IWOCA 2026, DOI:10.1007/978-3-032-27732-9_23; expanded arXiv:2610.35041v1). Its Section 6 treats certain path/cycle products with source-containing factors; the no-source, consistently directed torus violates its stated hypotheses, as noted explicitly in Remark 6.5. The new exact formula is not an implication of that theorem. Mengesha–Vetrík (2019) treats ordinary directed Cayley metric dimension, which requires unequal distance representations rather than two ordered strict inequalities. Rodríguez-Velázquez et al. (2014) treats strong metric dimension of undirected graphs, using a different shortest-path definition. Targeted mathematical-record searches for source-free cycle products, solid-resolving sets, toroidal grids, and equivalent formulas did not identify a covering statement. Unsearched or differently named literature remains a priority risk; search failure by itself is not novelty proof.

## Mathematical value — PASS

The motivating paper explicitly leaves consistently oriented source-free cycle products outside its available forced-vertex product machinery. The exact two-parameter formula resolves this natural missing Cartesian-product family and reveals a transition at the ratio \(\max(m,n)=2\min(m,n)\). The local lower bound and interval expansion provide structural explanations and optimum constructions, even though these vertex-transitive digraphs have no forced landmarks. This is an infinite-family determination of the invariant, not an arbitrary finite slice or a routine substitution into an established product formula.

## Scope and outstanding risks

The result does not cover other cycle orientations, bidirected arcs, higher-dimensional tori, or enumeration of all minimum landmark sets. The June 2026 conference chapter establishes the earliest verified public source date for the motivating line of research; the expanded version dated October 26 was read for the detailed product-result comparison. Historical priority and the proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
