# Integral \(C_2\)-homology lattice of the triangular-prism Morse complex

## Finding
Let \(P=C_3\mathbin{\square}K_2\) be the triangular-prism graph. Its layer-interchange automorphism \(\tau\) acts on the ordinary discrete-Morse-matching complex \(X=\mathcal M(P)\). Write \(C_2=\langle\tau\rangle\), let \(\mathbb Z_-\) be the rank-one integral sign lattice on which \(\tau\) acts as \(-1\), and let \(\mathbb Z[C_2]\) be the rank-two regular integral lattice. Then the **complete integral involution module** on top homology is
\[
\boxed{H_4(X;\mathbb Z)\cong\mathbb Z[C_2]^{\oplus30}\oplus\mathbb Z_-^{\oplus4}}
\]
as an integral \(\mathbb Z[C_2]\)-module. In particular, all 30 dimensions of the rational \(+1\)-eigenspace occur inside nontrivial regular integral blocks; there is no direct trivial integral summand. The statement concerns the layer-interchange subgroup, not the entire automorphism group.

## Assumptions and scope
Label the six vertices by \(0,1,2\) in the first triangle and \(3,4,5\) in the second. The edges are the three edges of each triangle together with \(\{0,3\},\{1,4\},\{2,5\}\). The automorphism \(\tau\) sends \(i\) to \(i+3\) and \(i+3\) to \(i\) for \(i=0,1,2\). A vertex of \(X\) is a primitive incidence matching \((v,e)\), where \(v\) is an endpoint of the graph edge \(e\). A face is a set of incidence pairs in which no graph vertex or graph edge is used twice and the induced arrows from matched vertices to the opposite endpoints contain no directed cycle. All chain groups use the increasing order of these 18 primitive incidences to fix orientations. Homology is unreduced in degree zero and ordinary in positive degrees.

## Proof
**Step 1: rational concentration and an integral lattice.** There are 18 primitive incidences. Exhausting all choices of zero or one outgoing arrow at each of the six vertices, discarding reused undirected edges and directed cycles, gives 1,727 nonempty faces and the degree-zero-through-four face vector
\[
(18,126,428,705,450).
\]
The four exact mod-two simplicial boundary ranks, in degrees one through four, are
\[
(17,109,319,386).
\]
They imply that mod-two homology is one-dimensional in degree zero, 64-dimensional in degree four, and zero in degrees one through three. Every rational boundary rank is at least the corresponding mod-two rank, since a nonzero minor modulo two is a nonzero integer minor. On the other hand, \(\partial^2=0\), \(\operatorname{rank}(\partial_1)\le17\), and the displayed face dimensions successively force the rational ranks to be at most \(17,109,319,386\). Therefore those rational ranks agree with the mod-two ranks; \(H_4(X;\mathbb Q)\cong\mathbb Q^{64}\) and positive rational homology in other degrees vanishes. Since the complex is four-dimensional, \(H_4(X;\mathbb Z)=\ker(\partial_4:\mathbb Z^{450}\to\mathbb Z^{705})\) is a free abelian group of rank 64.

**Step 2: rational trace of the layer interchange.** Each primitive incidence is interchanged with a distinct primitive incidence by \(\tau\). A \(\tau\)-fixed face must contain whole two-element incidence orbits. Such an orbit is compatible precisely for one of the six directed triangle edges mirrored across the two layers; a spoke orbit would use the same spoke twice. There are exactly six compatible single orbits and exactly nine compatible pairs of distinct orbits (choose two outgoing sources among three, then exclude a pair that uses the same edge). No three such orbits form a face. Thus the signed simplicial-chain traces of \(\tau\) are \(-6\) in degree one and \(+9\) in degree three, and zero in the other degrees. The ordinary Lefschetz number is \(-3\). Since rational homology is confined to degrees zero and four, with trivial action on \(H_0\), the trace of \(\tau\) on \(H_4(X;\mathbb Q)\) is \(-4\). Accordingly its \(+1\)- and \(-1\)-eigenspaces have dimensions 30 and 34.

**Step 3: modular extension rank.** The exact binary boundary matrix in degree four has 450 columns, 705 rows and rank 386. Its binary kernel consequently has dimension 64. Reduction of the integral free rank-64 top homology induces an isomorphism \(H_4(X;\mathbb Z)\otimes\mathbb F_2\cong H_4(X;\mathbb F_2)\), by the universal-coefficient injection and equality of dimensions. On a fully enumerated binary kernel basis, the action \(\tau-I\) has rank exactly 30. Independently, stacking the 705-row binary \(\partial_4\) matrix with the 450-row binary matrix \(I+\tau\) yields rank 416. Because \(\operatorname{rank}(\partial_4)=386\), the stack also gives \(416-386=30\) for the restriction to its kernel. Both reductions are included in the executable verifier.

**Step 4: elementary integral involution-lattice lemma.** Let \(L\) be any finite-rank free abelian group with an involution \(t\). Its integral eigensublattices \(P=L^+\) and \(Q=L^-\) are primitive, and \(2L\subseteq P\oplus Q\). The quotient \(W=L/(P\oplus Q)\) is therefore a binary vector space. Under \(L\subseteq\frac12P\oplus\frac12Q\), its two projections to \(P/2P\) and \(Q/2Q\) are injective: if, for example, an element has zero negative projection, subtract its integral negative part to obtain an element fixed by \(t\), which must lie in \(P\). Choose integral bases lifting bases of the two projected subspaces and extend each to a basis of its eigensublattice. The lattice then splits into one regular block for each dimension of \(W\), plus the remaining trivial and sign lines: indeed the two generators \((p_i+q_i)/2\) and \((p_i-q_i)/2\) of each regular block are exchanged by \(t\). Reduction modulo two makes \(t-I\) rank one on a regular block and zero on either rank-one block. Hence, writing \(p=\dim_{\mathbb Q}L^+_{\mathbb Q}\), \(q=\dim_{\mathbb Q}L^-_{\mathbb Q}\), and \(r=\operatorname{rank}_{\mathbb F_2}(t-I\mid L/2L)\), one has
\[
L\cong\mathbb Z[C_2]^{\oplus r}\oplus\mathbb Z_+^{\oplus(p-r)}\oplus\mathbb Z_-^{\oplus(q-r)}.
\]
For the present top-homology lattice, Steps 2 and 3 give \((p,q,r)=(30,34,30)\), proving the displayed classification.

## Verification
Run `python3 verify.py` beside this file. The stand-alone standard-library program enumerates every admissible incidence matching, all simplicial boundaries and all twelve graph automorphisms induced by permutations of triangle labels and optional layer exchange. It verifies the face vector, four exact binary boundary ranks, all six rational character values, the 64-element basis of mod-two top cycles, the rank-30 involution map on those cycles, and the independent stacked-matrix rank 416. Its final line is `integral_C2_lattice: 30 regular plus 4 sign`. Neither finite testing across additional graphs nor numerical approximations enter the proof: this is an exhaustive finite calculation for the one stated graph, combined with the integral lemma above.

## Relationship to prior work
Donovan–Lin–Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions* (2019), define these Morse complexes, compute other graph families and identify automorphism groups, but do not give this graph's homology module. Donovan–Scoville (2022) similarly study graph Morse complexes without this integral action. The published calculation *The triangular-prism Morse complex is a wedge of sixty-four four-spheres* determines the nonequivariant homotopy type; its \(64\) top generators alone do not specify any integral action. The published *Equivariant matrix–forest character formula for graph Morse complexes* determines rational alternating traces for all graph automorphisms, and thus also the rational \((30,34)\) eigenspace dimensions here, but not the integral splitting. For example, the lattices \(\mathbb Z_+^{30}\oplus\mathbb Z_-^{34}\) and \(\mathbb Z[C_2]^{30}\oplus\mathbb Z_-^4\) have identical rational characters, while their mod-two \(t-I\) ranks are zero and 30 respectively. The new assertion is the latter, integral distinction, not the known homotopy type or rational character.

## Limitations
The theorem classifies only the natural layer-interchange \(C_2\) restriction of fourth integral homology, not an integral module for the full \(S_3\times C_2\) group. It does not assert an equivariant wedge decomposition or compute Borel cohomology. Finite matrix calculations are certified by an auditable program rather than a printed 705-by-450 matrix. Searches of indexed literature and published mathematical records can miss an unindexed equivalent computation.

## References
1. C. Donovan, M. Lin, N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, first public 2019-09-25, https://arxiv.org/abs/1909.11440.
2. N. A. Scoville, M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first public 2020-04-22, https://arxiv.org/abs/2004.10481.
3. C. Donovan, N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, first public 2022-07-27, https://arxiv.org/abs/2207.13780.
4. *The triangular-prism Morse complex is a wedge of sixty-four four-spheres*, publicly accessible computational mathematics record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-triangular-prism-morse-complex-is-a-wedge-of-sixty-four-four--c3e0003f51f2.
5. *Equivariant matrix–forest character formula for graph Morse complexes*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-equivariant-matrix-forest-character-formula-for-graph-morse-comp--0f531889a464.
