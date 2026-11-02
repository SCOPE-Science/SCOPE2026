# Scientific review: sharp single-edge damage bound

## Correctness — PASS

The claim is quantified over all finite simple graphs and every nonedge. The critical vertex-deletion lemma is proved for each *fixed inherited edge order* by induction, and yields the precise one- and two-vertex expectation bounds. The first-edge identity isolates the newly inserted edge and separates old edges intersecting or avoiding its endpoints. Simultaneous induction proves \(-1/3\le\Delta\le1\), with nonnegative \(\Delta\) whenever an endpoint is isolated. The sharp examples are exactly two disjoint edges plus their connecting middle edge, and an edgeless graph plus one edge. The standalone checker passed 945204 exact-rational/permutation assertions; exhaustive finite tests supplement, not replace, the proof. Remaining correctness risks: none identified for the stated unweighted uniform-edge-order model.

## Originality — PASS (qualified)

Arnosti's 2021 first-online paper defines the RANDOM-EDGE procedure and analyzes comparisons of *algorithms* on random bipartite graphs, not the effect of a single adversarial edge in an arbitrary graph. Miller and Pritikin (1997) analyze expected cardinality and worst-case approximation factors, but the accessible abstract does not assert the sharp insertion-damage inequality. published-finding corpus searches for random greedy matching edge insertion, expected decrement, the one-third bound and vertex-deletion sensitivity found no implication-equivalent result; the nearest stored results concern uniform random greedy **independent sets**, unrelated matching averages, or distinct matching models. These observations cannot prove novelty. Full text of the most plausible older 1997 source remained inaccessible: this is a specific unresolved historical-priority risk, not evidence that the paper is not covering the theorem.

## Value — PASS

The theorem gives a sharp, universal and size-independent stability envelope for a classical randomized greedy algorithm under the natural operation of allowing one extra match. The negative example exposes a performance paradox, the \(1/3\) constant quantifies its worst possible effect, and the isolated-endpoint criterion separates a provably harmless class of insertions. This is a structural graph-probability theorem over all finite input graphs rather than a numerically observed special case. It may inform sensitivity analysis for greedy matching under graph updates; no downstream theorem is claimed.

## Limits

Finite, simple, unweighted graphs; uniform random edge permutation; exactly one new edge; output expected cardinality. No statement about weighted policies, multiple updates, pathwise order or other greedy rules. Older full-text priority remains a risk.

Self-review: passed. Independent audit: not yet performed.
