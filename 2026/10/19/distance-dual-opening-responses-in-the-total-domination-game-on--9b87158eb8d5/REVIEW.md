# Scientific review

## Correctness — PASS
The mathematical state is the set of vertices totally dominated via **open** neighborhoods and the identity of the next player. Every admissible move enlarges this set, so the minimax recurrence is a well-founded exact proof by induction on its complement. The full twenty-bit state calculation and a separately implemented recursive game solver agree for both graphs. Dodecahedron adjacency and five-set containment constructions are related to the generalized Petersen presentations by explicitly checked isomorphisms. All twenty first choices and all 380 ordered distinct second choices have been checked in both starting conventions. These arguments and replayable programs establish the finite claim, without extrapolation to additional graphs.

## Originality — PASS, with residual risk
Henning–Klavžar–Rall's foundational full text proves the general continuation principle and starting-player bound; it does not give these named-graph game values or a five-shell forced-response table. Dorbec–Henning's complete available text concerns cycles and paths. Zhao and coauthors analyze static total domination on generalized Petersen graphs, not the alternating minimax game. Published mathematical-record comparisons of aliases, stronger general bounds and recent summaries did not uncover a logically covering result. Previous accessible claims in the same mathematical collection about the dodecahedron or Desargues graph concern different invariants, so they do not imply the present two-player game classification. An unindexed or inaccessible equivalent specialized game computation remains possible; negative search results alone are not a novelty proof.

## Value — PASS
Two canonical twenty-vertex cubic graphs even have the **same** distance shell sizes, but exhibit qualitatively different optimal game-opening behavior. The dodecahedron has a unique antipodal minimizing reply versus an entire distance-two class of maximizing replies, while the Desargues graph has total second-move neutrality. This complete natural benchmark for adversarial total domination exposes a strategic invariant not determined by degree, order or distance-shell counts, and can be used to test proposed structural principles for highly symmetric graphs. The finite computation is motivated by a nontrivial classification of all opening options, rather than a chosen numerical increment.

## Prior work and limitations
Foundational total-domination-game sources: Henning, Klavžar and Rall (2014 online; DOI 10.1007/s00373-014-1470-9), Dorbec and Henning (2016; DOI 10.1016/j.dam.2016.03.014). Static generalized-Petersen total domination: Zhao et al. (2020; DOI 10.1155/2020/5473675). Scope is limited to two named graphs. Computation and self-review do not amount to external independent validation; some literature may not be indexed.

Self-review: passed. Independent audit: not yet performed.
