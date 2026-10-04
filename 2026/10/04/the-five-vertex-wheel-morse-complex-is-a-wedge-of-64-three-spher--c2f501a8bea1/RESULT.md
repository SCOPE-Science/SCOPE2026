# The five-vertex wheel Morse complex is a wedge of 64 three-spheres
## Finding
Let \(W=C_4*K_1\) be the five-vertex wheel: a four-cycle rim together with a hub adjacent to all rim vertices. Then
\[\mathcal M(W)\simeq\bigvee^{64}S^3.\]

## Assumptions and scope
A vertex of \(\mathcal M(W)\) is an incident pair \((v,e)\). A simplex is a set of such pairs with no repeated cell and no closed \(V\)-path. Equivalently for a graph, orient each paired edge away from its paired vertex; chosen arcs have distinct tails, distinct underlying edges, and no directed cycle.

## Proof
Exhaustive enumeration from the definition gives nonempty face vector \((16,94,240,225)\). The verifier applies the fixed primitive-vertex order \((8,12,3,9,6,11,15,14,13,0,2,4,10,7,1,5)\) and pairs every still-unmatched face with the face obtained by adjoining the current primitive vertex whenever possible. This gives \(255\) disjoint Hasse pairs. Orienting unmatched Hasse covers downward and matched covers upward yields an acyclic directed graph on all \(575\) nonempty faces. The only critical cells are one cell in dimension \(0\) and sixty-four in dimension \(3\). Forman's theorem therefore gives a CW complex with one \(0\)-cell and sixty-four \(3\)-cells, hence the stated wedge.

## Verification
Run `python3 verify_wheel_morse.py`. It rebuilds all \(576\) faces including the empty face, checks the face vector, matching size, critical-cell vector, and acyclicity of the full directed Hasse diagram. Successful replay prints `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville study exact homotopy types of complexes of discrete Morse functions using star clusters and the Cluster Lemma. Their checked full text treats extended-star, path, cycle-related, and Dutch-windmill families; a full-text search found no occurrence of “wheel,” and the five-vertex wheel result above is not stated. Scoville and Zaremsky give general graph-Morse-complex connectivity bounds, which do not determine an exact wedge decomposition or the multiplicity \(64\).

## Limitations
Only the explicitly defined five-vertex wheel is claimed. No formula for larger wheels is asserted. The general-connectivity source was compared through its stated theorem and bibliographic record rather than a fresh page-by-page full-text reading. Independent audit has not been performed.

## References
1. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780v1, first submitted 2022-07-27; New York J. Math. 29 (2023), 1393–1412. Primary MSC2020: 57Q70.
2. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481, first submitted 2020-04-22.
