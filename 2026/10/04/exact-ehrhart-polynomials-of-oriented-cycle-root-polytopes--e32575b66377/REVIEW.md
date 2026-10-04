# Same-model review

## Correctness
PASS. The primitive cycle dependence is sufficient to determine the lattice index in the non-semi-balanced case, and the half-open parallelepiped calculation gives all \(h^*\)-degrees with their multiplicities. The semi-balanced and extended cases use unimodular circuit triangulations into spanning-tree root simplices. Boundary cases \(p=q\), \(|p-q|=1\), and one cyclic direction only are explicitly covered. Exact finite replay through \(m=8\) agrees with every formula but is not used as the all-dimensions proof.

## Originality
PASS. The closest directly relevant full texts were compared by statement and implication. The 2021/2022 root-polytope paper establishes the cycle dependence and focuses its \(h^*\)-theory on semi-balanced graphs; the 2023 graph-polytope paper likewise scopes \(Q_G\) formulas to semi-balanced digraphs. The 2023 arbitrary-digraph interior-polynomial paper treats the extended root polytope but determines only degree and leading coefficient. Targeted database and literature searches did not locate the complete cycle formulas or the exact \(|p-q|\) volume boundary. A residual risk of an unstated equivalent circuit-simplex specialization remains.

## Value
PASS. A cycle is the first non-tree dependency in a graph, so its root polytope is a natural base case for the non-semi-balanced theory. The theorem converts orientation imbalance into the full Ehrhart numerator, shows that edge placement around the cycle is irrelevant, and isolates exactly when the non-semi-balanced root simplex is unimodular. This sharpens both the foundational cycle discussion and the later coarse degree theorem in a canonical family.

## Closest literature and limitations
Kálmán--Tóthmérész (arXiv:2105.00960) is the closest source for the non-extended root polytope; Kálmán--Tóthmérész (arXiv:2304.03221) is the closest source for the arbitrary-digraph extended root polytope. The present claim is limited to a single cycle and does not classify general unicyclic or non-semi-balanced digraphs. Broader lattice-circuit literature remains the main residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
