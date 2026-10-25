# Independent mathematical audit

## correctness

PASS

Trim accepting runs have exactly three disjoint depth layers since different accepting-prefix lengths would generate wrongly sized accepted words. For each letter a_i an accepting path passes through a private distinct depth-one p_i; sharing would accept a_i a_j. In a cactus a final state cannot be adjacent to three distinct selected p_i because K2,3 yields two simple cycles sharing an edge; hence >=ceil(n/2) final states. Tree case forbids any pair sharing final, so >=n finals; planar K2,n and matching-cactus/tree constructions attain all lower bounds. At odd n an extra middle-to-final edge in any equality case makes two four-cycles share the edge from s to that middle vertex, forcing unique singleton and perfect pair matching. Independent NetworkX block-cycle enumeration for n=1..4 checked normalized NFA minima and exact numbers of labeled optimal end-state assignments (1,1,6,6).

## originality

PASS

Grobler-Koziel-Siebertz establish existence of a bipartite cactus representation for every regular language and give D3/K2,3 graphical examples; this general existence theorem does not provide the exact all-n state minima and rigidity as stated. Other planar NFA and undirected symmetric-transition automata use different topology/model. Most directly relevant Grobler et al complete paper could not be retrieved through open sources or authorized institutional access (VPN disconnected); full-document noncoverage is not asserted.

## value

PASS

The natural language family D_n, already used as the motivating noncactus example in cactus automata, gives a sharp quantitative trichotomy for unrestricted/planar/cactus/tree state costs, plus a complete classification of minimal cactus automata. This advances the explicit state-blowup issue beyond general existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
