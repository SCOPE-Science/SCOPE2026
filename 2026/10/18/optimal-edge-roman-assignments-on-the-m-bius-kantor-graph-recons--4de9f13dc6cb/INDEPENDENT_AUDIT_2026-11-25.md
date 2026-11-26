# Independent mathematical audit

## correctness

PASS

For a fixed label-2 support T, edges with neither endpoint touched by T must have label 1, and any other edge outside T can have label 0. An extraneous 1 can be lowered; therefore every global minimum is its unique canonical completion, with cost 2|T|+|U(T)|. Supports of size at least 6 have cost at least 12. Independently generated GP(8,3) edges and enumerated all 55,455 smaller supports by their endpoint sets. By sizes 0 through 5 the minimum costs were 24,21,18,15,12,11, with respective multiplicities 1,24,132,184,54,72. All 72 global optima have exactly five 2s, one 1, and eighteen 0s. Pairwise intersection size four on the optimal supports gives exactly 96 exchanges, none preserving the single edge. The 24 degree-four and 48 degree-two vertices form the two parts; the branch-neighbor pairs of the degree-two vertices are distinct. I suppressed them and found a complete adjacency-preserving bijection to the line graph by independent backtracking, not relying on the certificate's proposed bijection. I separately verified the certificate's states, exchanges, GP-to-LCF and branch-to-line-graph maps. Independent flood distances gave eccentricity 8 for all vertices, confirmed connectedness, and put the endpoints of the certified length-eight path exactly eight apart. Thus the claim is of an abstract subdivision, not of a natural indexing by the single edge.

## originality

PASS

The supported distinct result is the exact optimum-state census and the once-subdivided line-graph structure for this recomputing support-exchange rule. Ordinary Roman domination on the line graph is the known equivalent input optimization, not itself new. The closest ordinary Roman reconfiguration rules and several exact catalogue analogues were checked at the statement level.

## value

PASS

A natural cubic symmetric benchmark supports more than a Roman domination number: the minimum labeling space recovers the original edge-incidence structure after suppressing forced degree-two states. The structure and metric data make it useful for comparing dynamics under different minimum-state exchange rules; here the support-recomputation rule even turns an edgeless local-swap graph on the same functions into a connected graph of diameter eight. The exact census alone would not imply these conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
