# Fano duality twists Heawood perfect-matching homology

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane. Let \(G=\operatorname{Aut}(H)\) and let \(\varepsilon:G\to\{\pm1\}\) be \(+1\) for graph automorphisms preserving the point and line classes and \(-1\) for those interchanging the classes. Write \(\mathcal M_{\mathrm p}(H)\) for the simplicial complex of graph-edge sets contained in a perfect matching, and \(\mathcal M(H)\) for the ordinary simplicial complex of all matchings. Then there is an isomorphism of rational representations of the full, order-\(336\) graph-automorphism group:
\[
\boxed{\widetilde H_2(\mathcal M_{\mathrm p}(H);\mathbb Q)\cong\widetilde H_4(\mathcal M(H);\mathbb Q)\otimes\varepsilon.}
\]
Both sides have dimension \(16\), with no other nonzero reduced rational homology in either complex. The claim is **equality of the full rational characters and hence module isomorphism**; it is not an equivariant homotopy equivalence between the two complexes.

The complete character table follows. ``Preserves'' and ``exchanges'' specify action on the two bipartition classes. The entries are traces on degree-two homology of the perfect-matching complex and degree-four homology of the ordinary matching complex, respectively.

| Bipartition action | Order | Number | Perfect-complex trace | Ordinary-complex trace |
|:---|---:|---:|---:|---:|
| Preserves | 1 | 1 | 16 | 16 |
| Preserves | 2 | 21 | 0 | 0 |
| Preserves | 3 | 56 | 1 | 1 |
| Preserves | 4 | 42 | 0 | 0 |
| Preserves | 7 | 48 | 2 | 2 |
| Exchanges | 2 | 28 | -4 | 4 |
| Exchanges | 6 | 56 | -1 | 1 |
| Exchanges | 8 | 84 | 0 | 0 |

The point–line-preserving subgroup \(B\cong\mathrm{GL}_3(\mathbb F_2)\) fixes a one-dimensional subspace of \(\widetilde H_2(\mathcal M_{\mathrm p}(H);\mathbb Q)\), while the full group fixes **no** nonzero vector. Thus the finite quotient \(|\mathcal M_{\mathrm p}(H)|/G\) has no positive-degree rational homology. This does **not** assert that the quotient is contractible or that the integral representation is a sign twist.

## Assumptions and scope
Identify the seven Fano points and seven Fano lines with the nonzero vectors of \(\mathbb F_2^3\). The graph has vertices \(p_x,\ell_y\) for nonzero \(x,y\in\mathbb F_2^3\); declare \(p_x\) adjacent to \(\ell_y\) exactly when the standard binary dot product \(x\cdot y\) is zero. There are \(14\) vertices, \(21\) edges, and every point and line has degree three. A perfect matching is a set of seven graph edges meeting every vertex once. A simplex of \(\mathcal M_{\mathrm p}(H)\) is any subset of such a seven-edge matching, including the empty face. A simplex of \(\mathcal M(H)\) is any set of pairwise disjoint graph edges. The former is a \(G\)-stable subcomplex of the latter; the complexes are not identical.

For an invertible linear map \(A\) on \(\mathbb F_2^3\), let \(p_x\mapsto p_{Ax}\), \(\ell_y\mapsto\ell_{A^{-\mathsf T}y}\). There are exactly \(168\) such automorphisms, forming \(B\). Composing with the point–line duality \(p_x\leftrightarrow\ell_x\) produces \(168\) further automorphisms. Every automorphism preserves or exchanges the unique bipartition of the connected graph; any bipartition-preserving graph automorphism is an incidence automorphism of the Fano plane and is determined by the images of a binary basis, hence is induced by one of the \(168\) invertible linear maps. Therefore these \(336\) are all automorphisms, and \(\varepsilon\) is well defined.

## Proof
**1. Exact homology concentration for the perfect-matching subcomplex.** Enumerating the seven-point-to-seven-line bijections compatible with incidence yields exactly \(24\) perfect matchings. Their full downward closure has \(2201\) nonempty faces, with face vector by dimensions \(0\) through \(6\): \((21,168,560,756,504,168,24)\). Construct an acyclic matching on its nonempty face poset by scanning the \(21\) graph edges in the deterministic lexicographic point/line order. At the stage of an edge \(e\), match every still-unmatched face \(\sigma\) not containing \(e\) to the still-unmatched larger face \(\sigma\cup\{e\}\), whenever that larger face exists. This gives exactly \(1092\) pairs and leaves one critical vertex and sixteen critical two-simplices. To certify acyclicity rather than assume it, orient every nonmatched codimension-one face inclusion downward and every matched inclusion upward; the supplied verifier constructs all \(8736\) directed Hasse incidences and exhausts the resulting \(2201\)-vertex directed graph by topological sorting. The graph is acyclic. Forman's discrete-Morse theorem therefore yields a CW complex with one zero-cell, sixteen two-cells and no other cells. All attaching maps of two-cells to the lone vertex are null, so \(\mathcal M_{\mathrm p}(H)\simeq\bigvee^{16}S^2\), integrally.

**2. Rational homology concentration for the ordinary complex.** Independently enumerate every ordinary graph matching. There are \(3461\) nonempty faces, with face vector \((21,168,644,1218,1050,336,24)\). All integer boundary ranks over \(\mathbb Q\) are determined by exact mod-two elimination and chain-complex upper bounds. The mod-two boundary ranks in degrees one to six are \((20,148,496,722,312,24)\). Every rational rank is at least the corresponding mod-two rank. For the first four boundary maps, the inequalities \(r_j+r_{j+1}\le\dim C_j\), beginning with \(r_1\le20\), force equality to these lower bounds successively. The top degree \(r_6\le24\) likewise forces \(r_6=24\), then \(r_5\le336-24=312\) forces \(r_5=312\). Thus the only nonzero reduced rational homology is in degree four, of dimension \(1050-722-312=16\).

**3. Two exact methods of calculating every trace.** Each of the \(336\) graph automorphisms permutes the \(21\) graph edges and acts simplicially on both complexes. For either complex \(K\), the induced trace in the unique nonzero reduced rational homology degree equals the reduced Lefschetz number. For a fixed nonempty face \(\sigma\) of cardinality \(k\), let \(c_g(\sigma)\) be the number of cycles of the induced permutation on its \(k\) vertices. Its signed simplicial contribution is \((-1)^{c_g(\sigma)+1}\). Consequently
\[
\chi_K(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}(-1)^{c_g(\sigma)+1}.
\]
Independently, decompose the edge permutation of \(g\) into disjoint cycles. Any invariant simplex is a union of some of those cycles. If \(J\) is a selected collection whose union is a face, including the empty selection, then
\[
\chi_K(g)=-\sum_{\substack{J\text{ selected edge cycles}\\\cup J\in K}}(-1)^{|J|}.
\]
The standalone checker verifies agreement of these two separately implemented exact sums for each \(g\) and each \(K\), and computes the eight table rows. For all \(336\) individual elements, not just one representative per displayed row, the trace identity \(\chi_{\mathcal M_{\mathrm p}}(g)=\varepsilon(g)\chi_{\mathcal M}(g)\) holds. Rational finite-group representations are semisimple and uniquely determined by their characters, so Maschke's theorem and the character criterion prove the announced representation isomorphism.

**4. Invariants and quotient.** Sum the perfect-complex character over all \(336\) elements: the result is zero, hence the \(G\)-invariant subspace has dimension zero. Restrict to the \(168\) point–line-preserving elements; the character sum is \(168\), hence the \(B\)-invariant subspace is one-dimensional. A finite simplicial group action may be made admissible by barycentric subdivision; over \(\mathbb Q\), the homology of its quotient is the group-invariant part of the homology. As the perfect complex is connected and has no reduced rational homology outside degree two, the quotient has vanishing reduced rational homology in all degrees.

## Verification
Run `python3 verify_heawood_perfect_duality.py` with the Python standard library. The program regenerates both complexes independently, checks the complete matching and face counts, proves the perfect-complex Morse matching acyclic by a complete Hasse-graph topological sort, determines ordinary-complex rational homology from the independently computed exact mod-two ranks and integer upper bounds, generates the full graph automorphism group, and checks the two independent signed Lefschetz formulas for all \(336\) automorphisms. It checks every perfect- vs ordinary-character sign identity and the two invariant-dimension sums. The actual checker transcript is `verify_heawood_perfect_duality.output.txt`; successful execution prints `HEAWOOD_PERFECT_DUALITY_VERIFY_OK`. All finite computations are exhaustive for these explicitly defined complexes; no sampled numerical inference is used.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega develop perfect-matching complexes for honeycomb graph families. Their theorems classify different bipartite graphs and do not establish the Fano incidence graph's homology symmetry module. Li's equivariant matching paper studies graded permutation representations on matchings, which need not coincide with homology representations of extendible-matching complexes.

The previously published *Perfect Morse reduction of the Heawood perfect-matching complex* (record `0994476b8c0d`) already establishes the perfect complex's \(16\)-sphere homotopy type, and the previously published *Full automorphism module of the Heawood matching complex* (record `d7a042784870`) already gives the **ordinary** complex's rational character. Those established results are credited, not asserted to be new. Their statements neither compare the homology representations of the two **different** complexes nor determine the perfect-complex trace under point–line duality. The new assertion is the exact equivariant sign-twist comparison, including the rational homology of the symmetry quotient.

## Limitations
The theorem concerns one finite incidence graph and rational representations. It does not assert an integral module isomorphism, a graph-family extension, an equivariant homotopy equivalence, or contractibility of the quotient. Exact character agreement proves existence of a rational module isomorphism but gives no preferred geometric intertwiner. The literature comparison cannot exclude equivalent results in unindexed publications or under different terminology. The proof relies on fully reproducible finite enumeration and discrete-Morse verification rather than a short symbolic character identity valid for all projective planes.

## References
1. S. Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828 (initially public February 17, 2022), particularly its graded matching-permutation representations.
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect matching complexes of honeycomb graphs*, arXiv:2209.02803 (initially public September 6, 2022), for the definition and graph-family motivation.
3. *Perfect Morse reduction of the Heawood perfect-matching complex*, public mathematical record `0994476b8c0d` (2026), for the established nonequivariant perfect-complex homotopy type.
4. *Full automorphism module of the Heawood matching complex*, public mathematical record `d7a042784870` (2026), for the established ordinary-complex character.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
