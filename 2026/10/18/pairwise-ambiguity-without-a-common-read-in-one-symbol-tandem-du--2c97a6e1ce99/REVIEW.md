# Scientific review

## Correctness: PASS
A direct run-root and run-excess bijection yields one-coordinate increments for every exact one-symbol duplication. Solving the adjacency-to-two-vertices constraints yields two disjoint clique orientations for \(s\ge3\), and coordinate extrema make the parametrizations unique. Stars-and-bars enumeration proves the two sums; binomial differentiation gives the closed triple count. The shared-read characterization and sharp clique/parent bounds follow directly. The standalone direct-word checker enumerates \(28{,}232\) triangles and higher cliques in the documented finite ranges; this is corroborative evidence, not a proof by extrapolation.

## Originality: PASS, with residual uncertainty
Lenz–Wachter-Zeh–Yaakobi (2017) supply duplication sphere and run-signature theory; Kovačević–Tan (2018) give duplication-correcting bounds and constructions; Yehezkeally–Schwartz (2018) address reconstruction and descendant cones. Chee et al. (2019) treat unbounded cones and use an opposite graph convention. The nearest published exact-one fixed-length result counts **pairs** and notes their unique common descendant, but does not state or imply the higher-order split: pairwise uniqueness does not force a single shared three-way descendant. Search terms and actual sources are documented in `AUDIT.json`. A general graph-theoretic or unindexed equivalent theorem remains possible; no independent literature audit has occurred.

## Mathematical value: PASS
The exact one-read reconstruction hypergraph differs from its pairwise confusability graph. The structural classification gives its entire clique spectrum and the precise frequency of three-source false positives, not simply a small numerical improvement or variant count. The sharp comparison \(n-1\) versus \(\lfloor(n+1)/2floor\) quantifies worst-case pairwise/joint list-size separation; the result applies uniformly to all \(q\ge2\) and all lengths.

## Limitations
Only exact single-symbol tandem duplication is covered, not longer blocks, multiple duplications, substitutions, or optimal independent sets. Program output is finite evidence; the infinite statements depend on the provided combinatorial proof. Equivalence under other terminology cannot be entirely ruled out.

Self-review: passed. Independent audit: not yet performed.
