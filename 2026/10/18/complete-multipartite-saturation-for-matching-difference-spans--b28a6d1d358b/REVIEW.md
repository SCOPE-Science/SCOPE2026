# Scientific review of complete multipartite matching-difference saturation

## Correctness

**PASS.** The saturation proof is a finite induction on within-part edges of an arbitrary matching of the complete graph. Given a forbidden pair in part \(A\), at least \(k\) vertices lie outside \(A\): either one is unused (the three-point difference identity removes the forbidden pair), or at least one other pair lies completely outside \(A\) (the four-point Garnir identity replaces both pairs by cross-part pairs). Every replacement preserves matching size, never overlaps an existing factor, and strictly decreases the induction statistic. The matching-number formula is proved by selection of \(2\nu\) vertices followed by a largest-parts greedy perfect matching. The character-zero complete-graph Specht dimension and graded duality are cited from the motivating paper, not re-proved as novel statements. The packaged program's exact modular rank computations verify 217 homogeneous cases; the argument is infinite and does not rely on that finite test.

## Originality

**PASS under the documented comparison, with remaining bibliographic uncertainty.** The initiating manuscript, arXiv:2609.34260v2, was examined through its definitions, complete-graph Specht result, saturation criteria, and multipartite discussion. Its Corollary 5.13 handles only parts all of size two, its matching-complement theorem does not cover larger within-part cliques, and its linkedness criterion is insufficient for many complete multipartite graphs (e.g., \(K_{k,k}\) is not \(k\)-linked at the top matching degree for \(k\ge2\)). The new theorem covers all positive part sizes and all possible matching degrees. Targeted searches concerning Dunkl matching algebras, Specht saturation, bipartite matchings, matching-difference spans, and equivalent Hilbert series did not identify covering results. A prior unindexed formulation remains possible.

## Value

**PASS.** The initiating paper specifically frames deciding saturation beyond the complete graph as a structural problem. This theorem gives an exact answer for the broad canonical family of complete multipartite graphs, including arbitrarily large complements, and extracts an all-degree Hilbert series. It also supplies a family-wide converse to the known connectivity obstruction while correctly respecting counterexamples outside this family. The conclusion identifies where the algebra truncates and is not merely a recomputation of the ordinary matching polynomial.

## Closest literature and limitations

Grinberg--Kirillov--Shapiro, *Matching algebras and their Dunkl subalgebras*, arXiv:2609.34260 (first public version 2026-09-28; examined v2 dated 2026-10-02), is the primary source for the definitions, complete-graph dimension, graded duality, and previous saturation criteria. Unindexed prior work may exist; the Hilbert dimension formula here is specified only for characteristic zero. The reduction argument independently verifies the proposed new span equality rather than assuming the converse to any cited sufficient condition.

Self-review: passed. Independent audit: not yet performed.
