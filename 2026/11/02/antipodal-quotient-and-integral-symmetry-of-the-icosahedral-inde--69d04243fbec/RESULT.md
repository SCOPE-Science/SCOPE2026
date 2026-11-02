# Antipodal quotient and integral symmetry of the icosahedral independence complex

## Finding
For the ordinary twelve-vertex icosahedral graph \(I\), its independence complex \(K=\operatorname{Ind}(I)\) is a triangulated two-sphere together with six extra edges, each joining one antipodal pair of vertices. Hence
\[
K\simeq S^2\vee\bigvee^6 S^1,
\qquad H_1(K;\mathbb Z)\cong\mathbb Z^6,
\quad H_2(K;\mathbb Z)\cong\mathbb Z.
\]
The full automorphism group \(A_5\times C_2\) acts integrally on \(H_1\) as signed permutations of the six antipodal edges and on \(H_2\) as the orientation sign of the two-sphere. On the rotational subgroup \(A_5\), the first-homology character takes values \(6,-2,0,1\) on elements of orders \(1,2,3,5\), respectively. Over \(\mathbb C\), this is the sum of the two Galois-conjugate three-dimensional irreducible representations. The central antipodal involution acts by \(-1\) on both positive-degree homology groups.

The antipodal orbit space is homotopy equivalent to the real projective plane:
\[
K/C_2\simeq\mathbb{RP}^2,
\qquad H_1(K/C_2;\mathbb Z)\cong\mathbb Z/2.
\]
The quotient by the entire automorphism group is rationally acyclic, while the quotient by its rotational subgroup has rational Betti vector \((1,0,1)\).

## Assumptions and scope
Use a concrete labeled model of the ordinary icosahedral graph. Its vertices are \(T,B,u_i,\ell_i\), where \(i\in\mathbb Z/5\mathbb Z\). Its thirty graph edges are the five instances of each of the six patterns
\[
Tu_i,\quad B\ell_i,\quad u_i u_{i+1},\quad \ell_i\ell_{i+1},\quad u_i\ell_i,\quad u_i\ell_{i-1}.
\]
The independence complex has one simplex for each finite vertex subset containing no graph edge. The antipodal involution exchanges \(T\) with \(B\) and exchanges \(u_i\) with \(\ell_{i+2}\). The two-sphere below is the subcomplex formed by all triangles and their faces, denoted \(L\). All homology groups are ordinary unreduced integral homology unless marked otherwise.

## Proof
**Classification of simplices.** Any independent set containing \(T\) but not \(B\) consists of \(T\) and at most two nonadjacent lower-ring vertices; the analogous statement holds with \(T,B\) interchanged. The pair \(T,B\) cannot be extended. If a set contains no pole, each of its two ring intersections contains at most two elements. For the two nonadjacent upper vertices \(u_i,u_{i+2}\), the sole lower-ring vertex nonadjacent to both is \(\ell_{i+3}\); this excludes four-element independent sets. Therefore the maximal independent sets of cardinality three are precisely the twenty triples, for \(i\in\mathbb Z/5\mathbb Z\):
\[
\{T,\ell_i,\ell_{i+2}\},\quad
\{B,u_i,u_{i+2}\},\quad
\{u_i,u_{i+2},\ell_{i+3}\},\quad
\{u_i,\ell_{i+1},\ell_{i+3}\}.
\]
A direct count from these four cyclic families shows that their twenty triangles meet in thirty distinct edges, each in exactly two triangles, and that each of the twelve vertex links in \(L\) is a five-cycle. The one-skeleton is connected. Thus \(L\) is a connected closed triangulated surface, and its Euler characteristic is \(12-30+20=2\). By classification of closed surfaces, \(|L|\cong S^2\).

Every vertex has five graph neighbors, five graph-distance-two neighbors and a unique distance-three antipode. The thirty edges of \(L\) join precisely the distance-two pairs. The only other independent pairs are the six antipodal pairs \(\{T,B\}\) and \(\{u_i,\ell_{i+2}\}\). None belongs to a triangle. Accordingly \(K\) is obtained from \(L\) by attaching exactly six one-cells along endpoints on \(L\). Since \(S^2\) is simply connected, each new one-cell contributes one free circle up to ordinary homotopy, giving the displayed wedge decomposition and torsion-free integral homology.

**Integral symmetry.** Every graph automorphism preserves graph distances, hence preserves \(L\) and permutes the six antipodal one-cells. The long exact homology sequence for \((K,L)\), together with \(H_1(L)=0\) and \(H_0(L)\xrightarrow{\cong}H_0(K)\), gives natural isomorphisms
\[
H_1(K;\mathbb Z)\cong H_1(K,L;\mathbb Z)\cong\bigoplus_{e\in E_{\mathrm{opp}}}\mathbb Z[e].
\]
Choosing an orientation on each antipodal edge makes the action exactly a signed permutation action. Since there are no cells of dimension greater than two, the inclusion also gives \(H_2(K;\mathbb Z)\cong H_2(L;\mathbb Z)\), with its orientation character.

The classical full icosahedral automorphism group is \(A_5\times C_2\) of order \(120\). The rotational \(A_5\) preserves the orientation of \(L\), and the central antipodal automorphism reverses it: it acts freely on \(|L|\cong S^2\), so by the Lefschetz fixed-point theorem its degree cannot be \(+1\). On the six signed antipodal edges, direct fixed-axis counting for rotational elements of orders \(1,2,3,5\) yields traces \(6,-2,0,1\). The standard \(A_5\) character table identifies this class function with the sum of its two nonisomorphic three-dimensional characters. The central antipode reverses each oriented edge, hence acts by \(-1\) in degree one as well.

**Quotients.** The central involution preserves \(L\) and fixes no simplex setwise, because no edge of \(L\) is antipodal and a triangle has odd cardinality. It therefore acts freely on the sphere \(|L|\). The quotient is a closed connected surface with Euler characteristic \(2/2=1\), necessarily \(\mathbb{RP}^2\). Each extra antipodal edge is setwise preserved and reversed, so its quotient is a pendant closed interval attached to the image of its endpoint in \(L/C_2\). Collapsing the six pendant intervals proves \(K/C_2\simeq\mathbb{RP}^2\). In characteristic zero, finite-group quotient homology equals the invariant subspace of rational homology after equivariant subdivision. Since the signed six-axis representation has no \(A_5\)-invariants and the sphere-orientation character has no \(C_2\)-invariants, the entire-group quotient has positive-degree rational homology zero; the \(A_5\)-quotient has rational Betti vector \((1,0,1)\).

## Verification
The standalone program `verify_icosahedral.py` enumerates all independent faces, the triangular core's edge and link incidences, the six antipodal pairs, the exact full set of \(120\) graph automorphisms, orientation-chain transformations, and equivariant Lefschetz identities. It independently checks the rotational character table: order distribution \((1,15,20,24)\), traces \((6,-2,0,1)\). Run `python3 verify_icosahedral.py` using Python's standard library. The expected terminal marker is `ICOSA_HOMOLOGY_CORE_SPHERE_PLUS_SIX_ANTIPODAL_EDGES_OK`. The enumeration is exhaustive for this twelve-vertex graph; the quotient and homotopy steps are justified mathematically in the proof rather than inferred from computational samples.

## Relationship to prior work
Berghoff [1] develops a general spectral sequence for graph independence-complex homology and works out examples including the Petersen graph and cube; the inspected work does not supply the icosahedral spherical-core decomposition, the signed full-group lattice, or its projective-plane quotient. Kim [2] treats graphs without induced cycles of lengths divisible by three. The icosahedral graph has triangles, so that theorem does not apply. Saleh, Titz Mite and Witzel [3] compute Vietoris–Rips complexes of Platonic vertex sets, including the icosahedron, but these Rips complexes use distance-threshold cliques and are different from the independent-set complex studied here. The claimed structural and equivariant conclusions are not implied by their explicit results. The matching complex of the icosahedral graph is also a different functor: it is the independence complex of the line graph, not the independence complex of the original icosahedral graph.

## Limitations
The statement concerns the ordinary independence complex of the standard icosahedral graph, not its matching, neighborhood, cut, or Rips complex; it does not assert an equivariant wedge splitting. The representation decomposition is over \(\mathbb C\), while the signed edge lattice is defined integrally. The quotient is an ordinary topological quotient. Literature searches cannot establish absolute priority, and independent external validation has not been performed.

## References
[1] M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267 (first submitted 2020-08-14); Combinatorial Theory 2 (2022), article 8. https://arxiv.org/abs/2008.06267

[2] J. Kim, *The homotopy type of the independence complex of graphs with no induced cycles of length divisible by 3*, arXiv:2101.07131 (first submitted 2021-01-18). https://arxiv.org/abs/2101.07131

[3] N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first submitted 2023-02-28). https://arxiv.org/abs/2302.14388
