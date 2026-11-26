# Independent mathematical audit

## correctness

PASS

An undominated set U and the player to move determine the game: possible successors are precisely U minus N[v] for v with N[v] intersecting U. Every successor is smaller, so induction from U empty proves the min/max recurrences. The opener moves again after two fixed moves. An independently written exact replay using frozensets and paired turn values checked all 182 Heawood and 306 Pappus ordered legal opening pairs. For distances in increasing order it obtained (reply count, Dominator-open total, Staller-open total) = [(3,7,6),(6,5,6),(4,5,6)] and [(3,8,8),(6,7,8),(6,7,8),(2,7,7)] respectively, at every opening vertex. The resulting starting values are (7,6) and (8,7). Vertex transitivity alone would not prove constancy within a distance sphere, but all-pair verification does; alternatively Fano point stabilizers are transitive on their spheres, and a Pappus point stabilizer at the origin acts by (x,y) -> (A x,B y+C x), A B nonzero, transitively on each of the four spheres.

## originality

PASS

The conditional two-ply minimax tables, and the exact scores in the inspected antecedents, were not found in earlier coverage. One later indexed record gives identical results on both graphs and extends them to other graphs; this is exact overlap, not evidence of earlier priority. The originality judgment is bounded by the sources inspected.

## value

PASS

The two classical cubic incidence graphs test the minus phenomenon on natural bipartite objects. The exact response table gives more than two start scores: it distinguishes why Staller must answer locally against a Dominator opening, while the minimizing reply to a Staller opening is unrestricted on Heawood and forced to maximum distance on Pappus. This is reusable exact data for contrasting optimal play in structured graphs, not just a recomputation of ordinary domination or a win/loss label.

The dated certificate retains the supplied scientific assessment, sources and limitations.
