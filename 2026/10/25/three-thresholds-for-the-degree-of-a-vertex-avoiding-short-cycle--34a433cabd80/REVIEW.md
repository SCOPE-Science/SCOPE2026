# Independent mathematical audit

## correctness

PASS

Given root degree d and its neighborhood, triangle avoidance forces binom(d,2) absent internal edges and square avoidance forces each outside vertex to choose at most one of d neighbor edges. Independence gives w(d)=binom(n-1,d)p^d q^(n-1-d+binom(d,2)) (q^d+d p q^(d-1))^(n-1-d), with separate d=0 case. Re-derived positive adjacent-weight ratio and Lambert saddle log(lambda/x)=beta*x, x=W(n²p³)/(np²). Scrutinized proof uniform ratio windows, Chernoff degree tails, the alpha=2/3 Stirling rate I_c(a), and alpha=3/4 Poisson-scale avoidance. Independently enumerated ALL labeled graphs on 2..6 vertices with different root cycle detector; degree-by-allowed-graphs counts match binom(m,d)(1+d)^(m-d)2^binom(m-d,2) exactly. These finite checks corroborate the probability law, not all asymptotic rates.

## originality

PASS

Janson–Ruciński 2009 gives *upper tail* bounds for rooted subgraph counts, not the joint zero event or degree conditioned on it. Stark–Wormald 2016/2018 analyzes absence of a fixed subgraph throughout the entire random graph, not simultaneous local triangle/square exclusion at a chosen root. Exact conditional independence is elementary, but the full three-boundary degree/rarity picture is not a corollary without new saddle and LDP analysis. Existing root cycle-exclusion probability literature could still encode an equivalent phase diagram.

## value

PASS

The local tree-like neighborhood condition is natural for branching approximations in sparse random graphs. Exact conditional degree and three asymptotic rarity transitions identify mechanisms between local avoidance and vertex degree, including a critical LDP; not merely a negative occurrence test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
