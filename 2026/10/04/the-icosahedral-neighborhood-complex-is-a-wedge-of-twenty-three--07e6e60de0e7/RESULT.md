# The icosahedral neighborhood complex is a wedge of twenty-three 2-spheres
## Finding
For the 12-vertex icosahedral graph \(I\), the Lovász neighborhood complex \(\mathcal N(I)\) is homotopy equivalent to
\[
\mathcal N(I)\simeq \bigvee^{23} S^2.
\]
Here \(\mathcal N(I)\) has a simplex for each nonempty vertex set having a common neighbor in \(I\).

## Assumptions and scope
The graph \(I\) is the ordinary finite simple icosahedral graph, realized explicitly in `morse_certificate.json` on vertices \(0,1,\ldots,11\). It has 12 vertices, 30 edges, and degree 5 at every vertex. The claim concerns the ordinary Lovász neighborhood complex, not a closed-neighborhood, directed, or metric Rips variant.

The neighborhood complex has face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(12,60,120,60,12),
\]
so its simplicial dimension is four.

## Proof
The certificate first constructs every nonempty face as a nonempty subset of one of the twelve open neighborhoods. This gives exactly 264 faces with the face vector above.

On the face poset, process vertices in the order
\[
7,0,4,6,10,8,1,5,3,2,9,11.
\]
At each stage, pair every still-unmatched simplex \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched. The archived certificate contains all 120 resulting cover pairs.

Orient each unmatched Hasse cover from the larger simplex to the smaller simplex and reverse the 120 matched covers. The verifier checks all 780 Hasse covers and proves the resulting directed graph is acyclic by a complete topological sort. Thus the pairs form an acyclic discrete-Morse matching in Forman's sense.

Exactly 24 simplices remain critical: one 0-simplex and twenty-three 2-simplices, with no critical simplices in dimensions 1, 3, or 4. Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(\mathcal N(I)\) with one 0-cell and twenty-three 2-cells and no other cells. Every 2-cell is attached to the single 0-cell, so this CW complex is precisely \(\bigvee^{23}S^2\).

## Verification
Run `python3 verify_icosahedral_neighborhood.py` in the directory containing the two packaged verification files. The verifier uses only the Python standard library. It reconstructs the graph and all faces, regenerates the matching byte-for-byte from its vertex order, checks every matching pair and all 780 Hasse covers, verifies acyclicity, and independently computes mod-2 simplicial homology.

The expected successful output begins with `VERIFY_OK`. As a cross-check independent of the Morse-cell count, the computed mod-2 Betti vector is \( (1,0,23,0,0) \).

## Relationship to prior work
Shukla studies exactly the Lovász neighborhood-complex functor and classifies the homotopy types for graphs of maximum degree at most 3 and for 4-regular circulant graphs. The icosahedral graph is 5-regular, so those classification theorems do not cover this graph. The inspected paper does not state the present icosahedral calculation. Matsushita's work gives a combinatorial description of fundamental groups of neighborhood complexes, but does not determine this 2-dimensional wedge multiplicity. Forman's discrete Morse theory supplies the standard implication from an acyclic face-poset matching to a CW model with one cell for each critical simplex.

The exact claim and aliases including `Hom(K_2,I)` were also searched in the checked research index and on the web. No equivalent statement or stronger theorem implying the exact wedge of twenty-three 2-spheres was located. This is evidence about the inspected literature, not an assertion that no unindexed source can contain the same finite calculation.

## Limitations
The result is for one canonical graph. It does not classify neighborhood complexes of arbitrary 5-regular graphs, nor does the mod-2 homology computation alone prove the homotopy statement; the latter is supplied by the separately verified acyclic discrete-Morse matching. Originality remains subject to the residual risk of obscure or unindexed computations under alternative box-complex or homomorphism-complex terminology.

## References
1. Samir Shukla, *Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most 3 and 4-Regular Circulant Graphs*, arXiv:1802.04526, first posted 13 February 2018; Electronic Journal of Combinatorics 26(2) (2019), P2.4, DOI 10.37236/7549.
2. Takahiro Matsushita, *Fundamental Groups of Neighborhood Complexes*, Journal of Mathematical Sciences, the University of Tokyo 24 (2017), 321–353; arXiv:1210.2803.
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI 10.1006/aima.1997.1650.
