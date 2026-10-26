# Scientific review: the Desargues color-switch graph

## Correctness: PASS

The finite enumeration is exhaustive, not an extrapolation from samples. An edge-perfect-matching recursion generates all 60 matchings. Their complementary two-factor types (36 with two ten-cycles, 24 with one twenty-cycle) give 32 unordered three-matchings by an independent counting identity. The complete certificate lists these 32 colorings and all 36 legal one-cycle Kempe switches. A stored 20-vertex bijection preserves and reflects all 30 edges of the original Desargues graph, proving the large component's isomorphism; the other 12 states pair as six edges. A separate direct edge-color backtracker, with color names fixed around one vertex, reconstructs the whole quotient without using the matching enumeration. Both programs were executed against the packaged certificate; outputs agree. Risk: the proof uses a finite executable certificate rather than a closed-form conceptual classification, but both algorithms exhaust all possibilities by construction and do not assume their conclusion.

## Originality: PASS, with explicit priority risk

Relevant primary work includes Belcastro–Haas (arXiv:1209.1730; 2014 publication), Belcastro–Haas (Australasian J. Combin. 2017), and Goedgebeur–Östergård (arXiv:2105.01363; 2022 publication). The 2017 article treats edge-Kempe reconfiguration graph structures and is particularly close, but its explicit examples are other cubic graphs such as crossed prisms; a twenty-vertex crossed prism has four-cycles and is not the girth-six Desargues graph. The 2022 study's exhaustive census supports component counts for cubic graphs yet reports aggregate numerical distributions, not this example's full state graph or a self-isomorphism. Targeted searches for the base graph, aliases, exact decomposition, and parameter implications, together with accessible historical claim comparisons, did not reveal covering statements. Residual uncertainty: an unindexed equivalent classification or a full published dataset permitting straightforward extraction may exist. This search is evidence, not proof of first discovery.

## Mathematical value: PASS

The canonical Desargues graph is a distance-transitive cubic incidence graph. Its three-edge-coloring dynamics have a surprising exact self-reproduction: a whole twenty-state Kempe component is isomorphic to the starting graph, while other states have a different mobility regime. This adds complete adjacency and metric geometry to known component-count investigations, with a verifiable intrinsic distinction by bichromatic cycle types. Unlike an arbitrary isolated numerical statistic, the exact graph structure and self-isomorphism answer a natural reconfiguration problem on an unusually symmetric graph. It is a finite result, not a claim of generality.

## Limitations

No independent external scientific audit. Historical priority is not conclusively decidable from accessible indexing. No analogous theorem for larger generalized Petersen graphs is proved. The statement concerns the global color-permutation quotient, not the named-color graph. The executable full certificate, the explicit isomorphism mapping, and two separate exact programs are included.

Self-review: passed. Independent audit: not yet performed.
