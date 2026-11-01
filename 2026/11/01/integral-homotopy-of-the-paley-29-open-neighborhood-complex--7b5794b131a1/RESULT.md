# Integral homotopy of the Paley-29 open-neighborhood complex

## Finding
Let \(P_{29}\) denote the quadratic-residue Paley graph on \(\mathbb F_{29}\), and let \(\mathcal N(P_{29})\) denote its ordinary Lovász **open-neighborhood complex**. Then there is an integral homotopy equivalence
\[
\mathcal N(P_{29})\simeq\bigvee^{7}S^3\vee\bigvee^{64}S^4.
\]
The Paley graph is isomorphic to its graph complement. Consequently, for the dominance complex \(\mathcal D(P_{29})\) of vertex subsets with dominating complements, combinatorial Alexander duality gives
\[
\widetilde H_i(\mathcal D(P_{29});\mathbb Z)\cong
\begin{cases}
\mathbb Z^{64},&i=22,\\
\mathbb Z^7,&i=23,\\
0,&\text{otherwise}.
\end{cases}
\]
The second display is an integral-homology conclusion only: no homotopy type is asserted for the dominance complex.

## Assumptions and scope
The graph has vertices \(0,1,\ldots,28\), with an edge between distinct \(u,v\) precisely when \((v-u)\bmod 29\) is a nonzero quadratic residue. Explicitly,
\[
Q=\{1,4,5,6,7,9,13,16,20,22,23,24,25,28\}.
\]
The open neighborhood at vertex \(u\) is \(u+Q\); it does **not** include \(u\). A set of vertices is a simplex of \(\mathcal N(P_{29})\) if and only if it lies in at least one of the 29 fourteen-element open neighborhoods. Simplices are ordered by ascending vertex labels when assigning integral orientation signs. The empty simplex participates in face enumeration, but not in the nonaugmented discrete-Morse matching. All homotopy statements concern geometric realizations of these finite complexes.

## Proof
**Exact simplex enumeration.** Generate the 29 neighborhood bit masks from \(Q\), and take the downward closure of their fourteen-element facets. Two complete and independent procedures agree: one enumerates submasks of every neighborhood; the other adjoins vertices in increasing order while maintaining the set of their common neighbors. They find \(449{,}153\) simplices including the empty simplex and a nonempty face vector, in dimensions zero through thirteen, of
\[
(29,406,3654,19894,52577,85463,99325,87087,58058,29029,10556,2639,406,29).
\]
Its ordinary Euler characteristic is \(58\).

**Complete acyclic Morse matching.** On nonempty simplices, use a deterministic sequence of vertex pivots in the order \(0,1,\ldots,28\). At pivot \(v\), match each currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched; remove each pair before the next pivot. This defines \(224{,}409\) disjoint pairs. The remaining critical cells consist of one vertex, 138 tetrahedra (dimension three), and 195 four-simplices (dimension four). Orient each Hasse incidence from higher face to lower face except for the matched incidence, which points upward. A complete topological sort checks all \(3{,}225{,}264\) incidence arrows among \(449{,}152\) nonempty faces and visits every face; hence the matching is acyclic. Forman's theorem gives a CW complex having exactly these critical cells.

**Signed integral Morse boundary.** The only potentially nonzero cellular differential in this CW model is
\[
B:\mathbb Z^{195}\longrightarrow\mathbb Z^{138}.
\]
Critical three-simplices and four-simplices are indexed by ascending integer face mask in `morse_boundary.json`. Let \([b:a]\in\{1,-1\}\) be the alternating simplicial incidence coefficient. The projection \(R(a)\) of a three-simplex onto critical three-simplices is determined as follows: it is its corresponding basis element when critical; it is zero when paired downward with a two-simplex; and, if paired upward with a four-simplex \(b\), it satisfies
\[
R(a)=-[b:a]^{-1}\sum_{c\subset b,\,\dim c=3,\,c\ne a}[b:c]R(c).
\]
Acyclicity makes this recursion well-defined. For each critical four-simplex \(t\), the column of \(B\) is \(\sum_{a\subset t,\,\dim a=3}[t:a]R(a)\). The complete finite signed matrix is recorded as sparse integer columns in `morse_boundary.json`; it contains 3,843 nonzero entries. The verifier reconstructs every coefficient from the graph and checks the stored matrix entry by entry.

**Unit integral invariant factors.** Perform exact unimodular elimination by pivoting only on matrix entries equal to \(1\) or \(-1\), choosing minimum-fill pivots. The first 117 pivots split off 117 unit diagonal factors and leave a \(21\)-by-\(78\) integer residual. Its column Hermite normal form is \(21\)-by-\(14\), and the Smith invariant factors of that smaller Hermite basis are precisely fourteen ones. Because Hermite column transformations preserve the image lattice, and all preceding pivots were unimodular, the Smith form of \(B\) has exactly 131 nonzero invariant factors, **all equal to one**. Its rank is 131. Therefore the reduced integral homology of the Morse CW model is free of rank seven in degree three and rank 64 in degree four, with no other reduced homology.

**From integral cellular data to homotopy.** The two-skeleton is a point and the three-skeleton is a wedge of 138 three-spheres. In particular, the space is 2-connected. By Hurewicz, the attaching maps of its four-cells are fully represented by their integral degree vectors in \(\pi_3(\bigvee^{138}S^3)\cong\mathbb Z^{138}\). Integral row and column basis changes of the attaching matrix can be realized by homotopy equivalences of the three-sphere bouquet and cellular four-cell slides. The 131 unit pairs cancel; the remaining seven three-cells and 64 four-cells attach trivially, proving the claimed wedge homotopy type.

**Self-complementarity and duality.** Multiplication of vertex labels by the quadratic nonresidue \(2\) interchanges edges and nonedges of \(P_{29}\), giving an explicit graph isomorphism from \(P_{29}\) to its complement. Matsushita and Wakatsuki prove that \(\mathcal D(G)^\vee=\mathcal N(\overline G)\). Their combinatorial Alexander duality identity over \(\mathbb Z\) implies \(\widetilde H_i(\mathcal D(P_{29});\mathbb Z)\cong\widetilde H^{26-i}(\mathcal N(P_{29});\mathbb Z)\). The neighborhood homology is free, so universal coefficients give the two displayed dominance ranks in degrees 22 and 23.

## Verification
Run `python3 verify_paley29.py` from the directory containing `morse_boundary.json`, with Python 3.10 or newer and SymPy 1.12 or newer. This uses no network and starts solely from the quadratic-residue definition. It reconstructs the entire simplex set by both methods, verifies the entire directed Hasse graph is acyclic, regenerates and checks every integer Morse matrix entry, performs exact unit pivots and Hermite/Smith calculations, verifies the explicit complement isomorphism, and repeats the integral Morse calculation using a **different non-affine vertex order** (all even labels followed by odd labels). The latter gives 117 critical three-cells and 174 critical four-cells; its Morse boundary has 110 unit invariant factors, again leaving seven third- and 64 fourth-homology generators. The exact run output is saved in `verification_output.txt`.

The full verifier is finite and terminating for this specified graph. Neither the finite computation nor the Hom/duality theory proves a statement for any other Paley-graph order.

## Relationship to prior work
Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* (arXiv:2312.02639; initial public submission 2023-12-05), establish the duality used above and calculate certain path and grid families, not the Paley-29 neighborhood complex. Shukla's broader neighborhood-complex classification covers graphs of degree at most three and four-regular circulants, not this degree-fourteen example. The Paley graph's exact parameters \((29,14,6,7)\) and group action are standard and independently listed by DistanceRegular.org. A previous exact computation of the Paley-17 **open-neighborhood** complex finds a Moore-space summand carrying integral three-torsion; its order-seventeen conclusion does not determine the order-twenty-nine result. Likewise, existing Paley-29 computations of the *independence* and *radius-one Vietoris–Rips/clique* complexes concern different face conditions and include two-torsion; none implies the open-neighborhood wedge decomposition. The contrast between these natural constructions is part of the motivation for computing the exact integral homotopy type.

Comparisons considered the names Paley-29, quadratic-residue graph on 29 vertices, strongly regular graph with parameters \((29,14,6,7)\), and circulant \(C_{29}(1,4,5,6,7,9,13)\). No inspected publication or indexed result implied this homotopy type, although exhaustive bibliographic uniqueness cannot be certified.

## Limitations
The homotopy classification concerns the **ordinary open** neighborhood complex for this one 29-vertex graph. It does not classify all strongly regular graphs with the same parameters, closed-neighborhood complexes, larger Paley graphs, or the dominance complex's homotopy type. The reproducible calculation needs SymPy for small integer normal forms; this does not constitute independent external validation. An equivalent calculation in unindexed or inaccessible literature remains the principal originality risk.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first public 2023-12-05), https://arxiv.org/abs/2312.02639 .
2. DistanceRegular.org, *Paley graph P29*, graph parameters, 2017, https://www.math.mun.ca/distanceregular/graphs/paley29.html .
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1 (2018), https://arxiv.org/abs/1802.04526 .
4. M. Kahle, *The Neighborhood Complex of a Random Graph*, arXiv:math/0512077 (2005), https://arxiv.org/abs/math/0512077 .
5. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, publicly available mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
6. *The Paley-29 independence complex is a wedge of spheres and a Moore space*, publicly available mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-paley-29-independence-complex-is-bigvee-28-s-2-vee-m-mathbb--378d1e51b1b2 .
7. *The Paley-29 Rips complex has 29 Klein-bottle links and integral two-torsion*, publicly available mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-paley-29-rips-complex-has-29-klein-bottle-links-and-integral--ea7b2ee04c72 .
