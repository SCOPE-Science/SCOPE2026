# Independent mathematical audit

## correctness

PASS

For the explicitly labeled 12-vertex cubic Frucht graph, direct iterate the simultaneous zero-forcing operator over all binomial(12,0)+...+binomial(12,4)=794 possible seed sets. No forcing seed of size <=3; exactly 89 size-four seeds force, with times 3:8,4:32,5:43,6:6. Adjacent four-sets differ in two bits (one vertex swap): exhaustively compare 3916 pairs, yielding 366 edges. Induced subgraphs at thresholds 3,4,5,6 have (8,10,components 6+2), (40,100,connected diameter8), (83,322,connected diameter6), (89,366,connected diameter6). The six-vertex fast component is a triangular prism, other fast component K2; distance between fast components in time<=4 graph is four. Inspected both original independent verification programs: direct forcing and distinct fort-hitting LCF labeling with explicit graph isomorphism. An independently coded full enumeration corroborated all forcing time and graph counts. This is complete finite exhaustiveness, not an infinite-family theorem.

## originality

PASS

Hogben et al. (2014) define parallel propagation time and efficient minimum sets; Geneson, Haas, Hogben (2020) formalize single-vertex zero-forcing reconfiguration graphs. Their relevant primary full texts do not state a time-filtered exchange graph for Frucht nor this disconnection-to-connection cutoff. Both definitions predate and are properly credited. Published Resultary zero-forcing records concern different graphs (fans, friendship, multipartite), not this exact cubic Frucht combination.

## value

PASS

The Frucht graph is a canonical smallest asymmetric cubic example; its natural speed-filtered space of efficient zero-forcing configurations is disconnected despite the full exchange graph being connected. The exact one-round connectivity threshold, diameter change and bridge length are natural metrics of the trade-off between fastest propagation and reconfiguration flexibility. Although finite and graph-specific, it is a motivated complete classification, not an arbitrary isolated number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
