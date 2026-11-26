# Independent mathematical audit

## correctness

PASS

For the stated best-shot response rule, a pure equilibrium is exactly an independent dominating set. Let H=G+uv. A minimum set of H remains independent in G. Removing uv can leave at most one endpoint undominated (the other must be selected). It is then safe to add the undominated endpoint, so i(H)≥i(G)−1. For the other direction, a minimum set S of G with k vertices survives unchanged unless both endpoints are in S. In that case, after discarding t from S for either t=u or t=v, the other endpoint covers t and exactly the private outside neighbors of t lack coverage. A maximal independent set of those neighbors restores domination without touching any retained vertex. The two private-neighbor sets are disjoint and outside S, so choose the smaller to get i(H)−k≤−1+floor((n−k)/2)≤floor((n−4)/2). For the upper witness, the two ends of a four-vertex path with a,b≥1 attached leaves are an independent dominating pair and no vertex is universal. Closing the path into a cycle leaves three cases: retaining one end forces all leaves of the other end and one middle vertex, giving attained costs b+2 or a+2, and retaining neither forces all leaves and one middle vertex, giving a+b+1. Balance a and b for the sharp increase. For the lower witness, a star with one edge subdivided has a dominating pair but no universal vertex; connecting the center to the far leaf makes the center universal. For n=4,5, P_n to C_n gives zero change; at n=3 the sole possible connected insertion is P_3 to C_3 and both have i=1. The supplied finite verifier was inspected as corroboration, not a substitute for the proof. Both endpoints of the interval are attained; the theorem does not require that every intermediate integer is realized.

## originality

PASS

The distinct contribution is the sharp universal signed comparison and its attainment at all orders, including odd-order upper witnesses. A distinct same-day catalogue record has an equivalent upper-bound witness at every even order ≥6 and the six-vertex positive example; these existential claims are not separately credited. It does not state a universal upper bound, the lower bound, or the odd-order tree witnesses. No priority order is inferred from the shared date.

## value

PASS

A local graph edit trades improved domination against broken independence. The exact worst-case asymmetry quantifies both effects and supplies a graph-size limit on the minimum pure-equilibrium contributor count. The universal bound and the all-order sharpness, rather than the independently known even-order counterexamples alone, make the result useful. It does not predict which equilibrium a network will select.

The dated certificate retains the supplied scientific assessment, sources and limitations.
