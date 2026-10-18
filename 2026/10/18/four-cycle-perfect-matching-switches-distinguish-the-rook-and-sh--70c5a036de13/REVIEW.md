# Scientific review

## Correctness

**PASS.** For each explicitly defined 16-vertex graph, the least-unmatched-vertex recurrence enumerates all perfect matchings and the two-pairing test enumerates all alternating-four-cycle switches. Exhaustive BFS from every configuration produces component sizes and exact eccentricities. A separately implemented C++ partner-array enumerator agrees on the counts, switch graph, component size histogram and extremal eccentricities; a certificate verifier checks every state, transition and BFS result. The 72 frozen rook states also have a non-computational counting proof via four-cycles in a four-column incidence graph.

## Originality

**PASS subject to residual literature risk.** The closest general mathematical antecedents are Dyer–Jerrum–Müller on bipartite switch chains (arXiv:1501.07725), Dyer–Müller on general-graph switch-chain ergodicity (arXiv:1705.05790) and Bonamy et al. on complexity of perfect-matching reconfiguration (arXiv:1904.06184). Their inspected definitions and main results do not give this exact finite classification. Searches for the names of the two graphs, matching-switch synonyms, component sizes and frozen one-factors found no equivalent published classification. Nearby mathematical records on matching complexes and on topological invariants of this strongly regular pair concern different objects and imply none of the component counts. An unindexed prior computation could still exist; priority has not been independently certified.

## Value

**PASS.** Whether an elementary perfect-matching switch chain is irreducible is a natural question for reconfiguration and sampling. The rook/Shrikhande pair provides a controlled test with identical strongly regular parameters but dramatically different component decomposition and frozen-state counts. Exact radii and diameters and the direct 72-state rook structure reveal bottlenecks that minimum matching cardinality or standard regularity parameters cannot explain. This is a finite exact classification, not a theorem about a whole family.

## Limits

Only perfect matchings and four-cycle alternating switches are addressed. In particular, no longer-cycle reachability or mixing-time estimate is asserted. The literature search may miss unindexed results and there has been no independent external audit.

Self-review: passed. Independent audit: not yet performed.
