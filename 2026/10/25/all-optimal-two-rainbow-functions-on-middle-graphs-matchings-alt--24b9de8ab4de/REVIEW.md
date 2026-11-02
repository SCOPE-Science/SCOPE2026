# Independent mathematical audit

## correctness

PASS

For every finite simple graph, the charge q(v)=|f(v)|+1/2 sum_{e incident v}|f(e)| sums to total token weight and is >=1 for each original vertex, including isolated vertices; a maximal matching realizes |V|. Equality forces each original vertex to bear either one singleton and no selected incident edges, one incident {1,2} edge, or exactly two opposite singleton incident edges. The latter edges form vertex-disjoint alternating even cycles, the doubles a matching disjoint from cycles; all other original vertices U are singletons and the remaining empty edge-vertices impose a proper two-coloring of G[U]. Converse verification proves the bijection and sum over matching/cycle packs. Path tiling states yield (1+z)/(1-z-z^2-z^3); star formula follows. Direct independent exhaustive checks of all 75 simple labelled graphs on 1..4 vertices, counting all feasible weight-|V| assignments from adjacency rather than from the structural formula, agreed, including N(K4)=21. Finite checks are not the all-orders proof.

## originality

PASS

The minimum rainbow weight |V(G)| is prior (Kim 2024) and the path integer recurrence is prior (OEIS A047081). The full equality-case bijection with arbitrary alternating even cycle packs and residual proper-colorings is not established by the inspected middle-graph scalar optimum or Roman minimum classifications. Best-of-knowledge originality holds for this structural counting theorem only; unindexed overlap remains possible.

## value

PASS

Classifying every minimizer is the canonical structural refinement of a known sharp graph-parameter minimum. Alternating even cycles produce optimal two-rainbow labelings beyond matching-derived Roman configurations; the formula treats all finite graphs and yields natural forest, path and star specializations. This is not a rename of the known optimum or a new claim for the classical recurrence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
