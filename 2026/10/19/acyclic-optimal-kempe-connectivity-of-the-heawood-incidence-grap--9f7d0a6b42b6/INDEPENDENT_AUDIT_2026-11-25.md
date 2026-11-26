# Independent mathematical audit

## correctness

PASS

The incidence model with differences {0,1,3} gives all 21 Heawood edges; those three residues have every nonzero ordered difference once, so each pair of distinct points lies on exactly one common line. A proper coloring fixes three distinct root colors, and prescribing their names in line order gives one representative per global permutation orbit. A cubic three-coloring would have a bichromatic 2-factor and is not acyclic; a proper assignment of the root names and identification of the fourth name gives all 24 labeled colorings per class. Independently enumerated all 213 unoriented simple cycles, then all 230336 root-normalized proper edge assignments in fixed edge order. A state was excluded exactly when a cycle's two parity masks were each contained in one color class; properness makes the two colors different. This leaves 119784 quotient states and 2874816 labeled states. Every two-color component was traversed as an edge set, swapped once, renormalized, and accepted exactly on lookup in the independently completed acyclic-state set; loops and duplicate neighbors were dropped. The resulting adjacency was symmetric. The histogram for degrees 8 through 21 is [672,2688,6384,8904,17584,15624,16968,16632,18480,10752,3472,1176,336,112]; it has degree sum 1664880, hence 832440 edges. Traversal from one state reached all 119784. This agrees with both frozen outputs and respects maximal nonempty paths and color-permutation quotienting, not graph-automorphism quotienting.

## originality

PASS

The supported contribution is the exact restricted Kempe graph, in particular its connectedness and degree and edge data. Credit the prior palette-existence and unrestricted proper-coloring results, and recognize the later exact overlap in the underlying state census. Neither unrestricted connectivity nor a census with single-edge moves implies the restricted maximal-path result.

## value

PASS

Heawood is the natural Fano incidence graph and a canonical cubic example for testing acyclic reconfiguration at the optimal palette. Connectivity at that palette under acyclicity-preserving swaps asks a different question from unrestricted Kempe equivalence. The exact degree and edge data complement a useful reachability determination rather than merely counting colorings; the comparison with the disconnected single-edge graph shows that allowing multi-edge path moves makes a qualitative difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
