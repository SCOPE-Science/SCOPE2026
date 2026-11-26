# Independent mathematical audit

## correctness

PASS

Reconstructed the all-n proof in RESULT.md lines 13–38. Equal-length choices of closed walks would make a useful branching cyclic SCC unbounded; distributing common-length laps excludes comparable cyclic SCCs. For fixed m and a subset of the noncyclic interior states, a fixed cyclic SCC between acyclic endpoints contributes at most one run per entry vertex (the exit is forced by m); the order of the visited SCCs is determined by any fixed topological sort. The bound (1+a)2^(n-a-2) is strict for a>=2; for a=1 the two options for a fixed subset have disjoint length ranges, and for a=0 the count is bounded by one binomial layer. When an endpoint belongs to a cyclic SCC of size c, the known endpoint determines the internal segment in the appropriate time direction and gives the bound 2^(n-c-1) unless both endpoints lie in that SCC, when the count is at most one. Trimness with coinciding endpoints puts every state in their SCC. Equality therefore requires an endpoint loop and every interior subset: empty, singleton and pair subsets force every forward edge in the one total order. Padding at that loop yields exactly 2^(n-2) runs for each m>=n-1 and the distinct labeled graphs number 2(n-2)!. Inspected verify.py and computation.txt without executing the former; the small-graph sweep also includes nontrim graphs and its walk-count cutoff is corroboration, not the proof. The proof wording about choosing vertices between endpoints of an edge is read as choosing just the two interior endpoints, or the corresponding singleton/empty subset.

## originality

PASS

Credit the prior unary lower bound; pass the sharp upper bound under both singleton endpoints and the classification of all equality graphs, not the numerical lower bound alone.

## value

PASS

In a canonical finite-ambiguity model the result identifies the exact largest growth-independent multiplicity and, more usefully, the two structural equality mechanisms and their exact labeled count. The necessity of the endpoint loop is substantive and not just a re-statement of the older lower construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
