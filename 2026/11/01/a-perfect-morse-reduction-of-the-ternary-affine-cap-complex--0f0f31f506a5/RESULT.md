# A perfect Morse reduction of the ternary affine cap complex

## Finding
Let \(K\) be the simplicial complex of subsets of the nine points of the affine plane \(\operatorname{AG}(2,3)\) containing no three collinear points. Then
\[
K\simeq S^2\vee\bigvee^{11}S^3.
\]
There is an explicit acyclic face-poset matching with exactly one critical vertex, one critical triangle, and eleven critical tetrahedra. This is a constructive homotopy refinement of the previously published integral Betti numbers.

## Assumptions and scope
Label the nine points by \(i=3a+b\), with \(a,b\in\{0,1,2\}\), representing \((a,b)\in\mathbb F_3^2\). A subset is a face iff it contains no triple of distinct points whose determinant \((b-a)\wedge(c-a)\) vanishes modulo three. This determines precisely twelve forbidden affine lines. Face masks use \(\sum_{i\in S}2^i\), and the empty simplex is excluded from the Morse matching. The full face vector is \((9,36,72,54)\); there are no simplices above dimension three.

## Proof
First, enumerate all \(2^9\) bitmasks and retain the 171 nonempty masks avoiding the twelve forbidden lines. For each vertex \(v=0,1,\ldots,8\) in increasing order, pair every currently unmatched face \(\sigma\) that omits \(v\) with \(\sigma\cup\{v\}\) whenever both faces remain unmatched. Within each pass, iterate the retained faces in increasing integer-mask order. The resulting matching has 79 disjoint pairs; the remaining critical masks, in increasing order, are \(1,54,70,216,232,240,344,360,368,390,408,424,432\). Their dimensions are \(0\) once, \(2\) once, and \(3\) eleven times.

To certify acyclicity, orient every Hasse cover \(\tau\supset\sigma\) downward from \(\tau\) to \(\sigma\), except for matched covers, which are oriented upward. The complete graph has 171 vertices and 504 directed edges. Kahn's topological sort deletes all 171 vertices; thus no closed gradient path exists. Forman's discrete Morse theorem gives a CW model with one zero-cell, one two-cell, eleven three-cells, and no other cells.

It remains to prove that the attaching degrees of the three-cells vanish. On the original simplicial chain complex, the boundary \(\partial_3:C_3(K;\mathbb Q)\to C_2(K;\mathbb Q)\) is the signed incidence matrix of size \(72\times54\). Exact rational row-reduction yields rank 43. Since \(C_4=0\), rational third homology has dimension \(54-43=11\). Homotopy invariance transfers this dimension to the Morse CW complex. Its degree-three cellular boundary is a map \(\mathbb Z^{11}\to\mathbb Z\). If it had any nonzero coefficient, it would have rank one after tensoring with \(\mathbb Q\), contradicting rational third-homology dimension eleven. Hence this boundary vanishes over \(\mathbb Z\), not merely modulo a prime.

The two-skeleton of the Morse CW model is \(S^2\), since it has one zero-cell, no one-cells, and one two-cell. Each three-cell is attached via an element of \(\pi_2(S^2)\cong\mathbb Z\); its degree equals its cellular boundary coefficient, hence is zero. All attaching maps are null-homotopic. The asserted wedge follows.

## Verification
The standalone file `verify.py` independently enumerates lines and faces, executes the exact face matching, topologically sorts every oriented Hasse edge, and performs exact fraction arithmetic to compute the rational boundary rank. Running `python verify.py` terminates with `VERIFY_OK`. The matching and boundary are finite exhaustive certificates, not probabilistic sampling.

## Relationship to prior work
Conant and Thistlethwaite (initially public 2008-08-05, arXiv:0808.0739, Definitions 2–3) explain the hypergraph independence complex and its Alexander dual. The twelve affine lines give one such hypergraph. Lew, *Spectral gaps of generalized flag complexes*, Chapter 6, Figure 6.2 (2017), explicitly computes the same nine-point cap complex's integral reduced homology as \(\mathbb Z\) in degree two and \(\mathbb Z^{11}\) in degree three. **Those groups are not new.** The additional assertion here is an explicit acyclic perfect Morse matching and resulting complete homotopy classification; the cited sources' inspected discussions do not state those stronger results.

## Limitations
The theorem is specific to the order-three affine plane; it asserts no analogous classification for arbitrary finite affine spaces. Its matching is not claimed to be equivariant under affine collineations. There may be equivalent unpublished, unindexed, or differently formulated homotopy calculations. The computational certificate and mathematical argument have not undergone independent validation.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first public 2008-08-05), https://arxiv.org/abs/0808.0739.
2. A. Lew, *Spectral gaps of generalized flag complexes*, thesis (2017), Chapter 6, Figure 6.2, https://www.math.cmu.edu/~alanlew/files/theses/msc%20thesis.pdf.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
