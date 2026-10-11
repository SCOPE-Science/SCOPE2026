# The \(5\)-cut complex of the \(3\times3\) grid is a wedge of \(25\) three-spheres

## Finding
For the \(3	imes3\) grid graph \(G\), the ordinary \(5\)-cut complex satisfies
\[\Delta_5(G)\simeq igvee^{25}S^3.\]
Here a facet is the complement of a five-vertex set whose induced subgraph is disconnected.

## Assumptions and scope
The graph is the simple rectangular \(3	imes3\) grid with unit horizontal and vertical adjacency. The claim concerns the ordinary cut complex, not the total cut complex. It is a finite exact statement for this one natural grid instance; no shellability claim and no all-\(n\) extension is asserted.

## Proof
There are \(inom{9}{5}\) five-vertex subsets. Exhaustive connectivity testing gives exactly \(77\) disconnected five-subsets, hence \(77\) tetrahedral facets. Their downward closure contains \(203\) faces including the empty face, with face vector \((9,36,80,77)\).

Apply sequential element matching to the nonempty face poset in row-major vertex order. At each stage, pair a currently unmatched face \(\sigma\) not containing the pivot \(v\) with \(\sigma\cup\{v\}\) whenever both are faces and still unmatched. The packaged verifier constructs all pairs and checks every pair is a Hasse cover. It produces \(88\) matched pairs and leaves exactly one critical \(0\)-simplex and \(25\) critical \(3\)-simplices, with no critical cells in dimensions \(1\) or \(2\).

The verifier then orients every unmatched Hasse cover downward and every matched cover upward and topologically sorts the resulting directed graph; all \(202\) nonempty faces are visited, so the matching is acyclic. Forman's discrete Morse theorem therefore replaces the complex by a CW complex with one \(0\)-cell and \(25\) \(3\)-cells and no other cells. Every attaching map lands in the point-like \(0\)-skeleton, giving the stated wedge of \(25\) three-spheres.

## Verification
Run `python3 verify_grid_3x3_k5.py`. The expected terminal line is `VERIFY_OK`. The program independently enumerates the facets and complete face set, constructs the matching, verifies Hasse-cover incidence, verifies acyclicity of the full Morse orientation, and checks the Euler characteristic. Its recorded output is included as `verification_output.txt`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Sundaram, and Xue, *Topology of Cut Complexes II* (arXiv:2407.08158), prove the full homotopy type for grid cut complexes when \(k=4\), and for \(k=5\) they give a face-lattice/Euler-characteristic analysis. Their Table 2 records the Betti number \(25\) for the \(3	imes3\), \(k=5\) instance, but the paper does not state this instance's homotopy type. Chandrakar, Hazra, Rout, and Singh (arXiv:2408.07646) later prove ordinary cut-complex shellability for \(2	imes n\) grids and homotopy results for total cut complexes on \(3	imes n\) grids; these results do not imply the ordinary \(5\)-cut homotopy type of the \(3	imes3\) grid. The present result upgrades the known Betti count in the first \(k=5\) square-grid case to an explicit homotopy decomposition.

## Limitations
This proof is finite and instance-specific. It does not prove shellability, does not classify \(\Delta_5(G(3,n))\) for larger \(n\), and does not establish a general discrete-Morse pattern beyond this verified face poset.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158; SIAM J. Discrete Math. 39 (2025), 1123–1157.
2. H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of Total Cut Complexes and Cut Complexes of Grid Graphs*, arXiv:2408.07646.
