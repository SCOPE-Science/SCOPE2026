# Independent mathematical audit

## correctness

PASS

A one-coalition state has no destination, and a singleton with zero cost cannot leave by strict improvement. Thus the cycle test uses exactly unordered nontrivial bipartitions. I independently enumerated all labeled simple graphs and used unordered pairs of actual vertex sets, Fraction costs, and Kahn topological elimination rather than the frozen checker’s masks, cross-products and DFS. Every state was eliminated for every graph. The (graphs, graph-partition states, profitable moves) counts by n=2,3,4,5 were (2,2,0), (8,24,12), (64,448,576), (1024,15360,27520), totaling (1098,15834,28108). Each symmetric enemy relation is one of these graphs; n=1 is trivial. The same independent replay generated the six-agent enemy relation from the displayed coordinates with the strict cutoff; starting from {2,3,4,5}|{1,6}, the movers (1,3,2,4) twice give costs 1>3/4, 1/4>0, 2/3>1/2, 1/2>1/3 twice and restore the partition. The distance-10 pair is correctly treated as friends. The later singleton states do not involve singleton departures.

## originality

PASS

The literature supplies nonconvergence by example, but not the smallest population. The verified improvements are a six-agent line-cutoff witness and an all-symmetric-graphs exclusion through five; the prior twelve-agent result supplies neither.

## value

PASS

The result turns an established failure of convergence into an exact boundary in a natural game model: every smaller individual-enemy graph is acyclic, and a real-line example already realizes the first possible cycle. The stronger graph lower bound separates the effect of small population from constraints of the line embedding, and the explicit witness makes the boundary reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
