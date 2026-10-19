# Scientific review: degree-five Clebsch zero forcing

## Correctness: PASS

The graph is defined unambiguously as the 16-vertex Cayley graph with generator set \(\{1,2,4,8,15\}\). Its Walsh-diagonalized adjacency matrix has spectrum \(\{5^1,1^{10},(-3)^5\}\), so \(A-I\) supplies a ten-dimensional kernel. The zero-forcing row-equation argument gives a lower bound of ten on any zero-forcing set. The complement of \(\{0,1,2,3,5,8\}\) explicitly forces four vertices and then two, giving the matching upper bound. Separately written Python and C++ programs exhaust all 65,536 initial subsets with exact arithmetic and agree on the polynomial, inclusion-minimal spectrum, and synchronous propagation. The Python program verifies all 1,920 explicitly generated automorphisms and all 18 six-white symmetry orbits; the structural neighbor-pair argument shows these comprise the full automorphism group. The seven successful orbits sum to precisely 3,872. The limitations are the finite stated graph and lack of external formal proof certification.

## Originality: PASS, subject to historical-priority risk

The exact object, both standard graph aliases and complement distinction, all coefficients, all seven orbit sizes, minimum-zero-forcing and well-forced assertions, and propagation-time phrases were compared with semantically retrieved published mathematical results and accessible primary literature. The 2014 propagation-time paper gives the definitions and examples of behavior, not an enumeration of the Clebsch graph. The 2018 polynomial paper treats special graph families but does not state this graph-specific polynomial. The 2023 well-forced paper focuses principally on trees and other separate families. A 2012 paper on powers of the Clebsch graph calculates the trivial complete-graph forcing number of nontrivial graph powers, not the original degree-five graph; its Theorem 3.3 and Table 1 were inspected directly. Earlier maximum-nullity theory gives the lower-bound mechanism, not this seven-orbit or well-forced classification. The full text of the foundational 2008 minimum-rank publisher article was unavailable for comparison; its accessible abstract does not settle the exact graph-specific priority question, and an unindexed classification could exist. Search absence does not establish global novelty.

## Value: PASS

The degree-five Clebsch graph is a canonical primitive strongly regular and Cayley graph, so its exact zero-forcing dynamics constitute a motivated finite structural invariant rather than an arbitrary slice. The simultaneous determination of \(Z=M=10\), well-forcedness, seven inequivalent minimum configurations, and a uniform two-round propagation time exposes structural behavior invisible in a scalar forcing number. A complete orbit certificate makes this finite benchmark reproducible. No general-family theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
