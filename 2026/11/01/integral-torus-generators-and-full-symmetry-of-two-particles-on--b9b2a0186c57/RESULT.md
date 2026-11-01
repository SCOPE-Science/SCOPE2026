# Integral torus generators and full symmetry of two particles on \(K_{4,4}\)

## Finding
Let \(G=K_{4,4}\) with bipartition \(L=\{0,1,2,3\}\) and \(R=\{4,5,6,7\}\), and let \(X=\operatorname{UConf}_2(|G|)\). The complete integral homology is
\[
H_0(X;\mathbb Z)=\mathbb Z,\qquad H_1(X;\mathbb Z)=\mathbb Z^9\oplus\mathbb Z/2\mathbb Z,\qquad H_2(X;\mathbb Z)=\mathbb Z^{12},
\]
with all higher homology zero. For each partition of the two four-vertex color classes into two unordered pairs and each matching between the two pairs, take the product of the two disjoint four-cycles of the resulting complementary \(K_{2,2}\) subgraphs. There are exactly eighteen such embedded product tori. Their integral fundamental cycles generate all of \(H_2\); although there are eighteen natural generators, its rank is twelve.

Write \(W=(\mathfrak S_4\times\mathfrak S_4)\rtimes C_2\) for the full graph automorphism group. If \(S^\lambda\) denotes a rational Specht module and \(\boxtimes\) denotes the external tensor product, then
\[
H_2(X;\mathbb Q)\cong_{\mathbb Q[W]} \operatorname{Ind}^W_{\mathfrak S_4\times\mathfrak S_4}\big(S^{(2,2)}\boxtimes S^{(2,1,1)}\big).
\]
In particular \(H_2\) has character zero on the coset interchanging the bipartition classes and has no nonzero invariant vector under the subgroup preserving the classes. Moreover \(H_1(X;\mathbb Q)\), restricted to that subgroup, is \(S^{(3,1)}\boxtimes S^{(3,1)}\); the class-swapping involution acts by the negative tensor-factor flip. Consequently the full symmetry quotient has vanishing reduced rational homology.

## Assumptions and scope
Every graph edge is regarded as a closed one-cell; particles may move continuously within edges but cannot collide. The ordinary two-point discrete cubical model is valid on the un-subdivided graph: each path connecting distinct vertices of valence different from two has at least one edge, and every simple cycle has at least three edges. Its zero-cells are unordered pairs of distinct graph vertices; its one-cells are a graph vertex together with a disjoint graph edge; its two-cells are unordered pairs of vertex-disjoint graph edges.

Every one-cell is oriented by increasing edge endpoint, and every two-cell by the increasing order of its two oriented edge factors. Group actions on cubical chains carry the induced signs.

## Proof
**Integral cellular calculation.** The dimensions of the cellular chain groups \(C_0,C_1,C_2\) are respectively \(28,96,72\). Put \(\partial_1(v,e_{ab})=[v,b]-[v,a]\) for \(a<b\) and
\[
\partial_2(e_{ab},e_{cd})=(b,e_{cd})-(a,e_{cd})-(d,e_{ab})+(c,e_{ab}),
\]
where the graph edges are indexed in increasing lexicographic order. All signs in the second formula are reversed if the edge-factor order is reversed. The standalone exact verifier constructs both integer boundary matrices and checks \(\partial_1\partial_2=0\). It obtains \(\operatorname{rank}\partial_1=27\) and \(\operatorname{rank}\partial_2=60\). The nonzero Smith invariant factors of \(\partial_2\) are fifty-nine ones and one two. Because \(\partial_1\) is the incidence map of a connected graph, \(\operatorname{ker}\partial_1\) is a primitive subgroup of rank \(69\). Thus \(H_1=\operatorname{ker}\partial_1/\operatorname{im}\partial_2\cong\mathbb Z^9\oplus\mathbb Z/2\mathbb Z\). No 3-cells occur, so \(H_2=\ker\partial_2\cong\mathbb Z^{12}\).

**The torus lattice.** Give every \(K_{2,2}\) four-cycle its signed cellular orientation. For each complementary pair \((Q,Q')\) of such squares, form its product chain \(z_Q\times z_{Q'}\). The usual product boundary identity shows that all eighteen are two-cycles. The verifier constructs their exact \(72\times18\) coefficient matrix \(T\), checks \(\partial_2T=0\), computes \(\operatorname{rank} T=12\), and computes its twelve nonzero Smith factors, all equal to one. Thus \(\operatorname{im}T\) is primitive in \(C_2\). Since it is contained in the primitive rank-twelve subgroup \(\ker\partial_2\) of the same rank, the two groups coincide. This is an integral generation theorem, not merely rational spanning.

**The full symmetry representation.** Permutations of vertices preserving or exchanging the two color classes act by signed permutations on the seventy-two oriented two-cells. Choose twelve independent columns of \(T\); their coefficient vectors are a rational basis of \(H_2\). The verifier calculates the action of every one of the \(2(4!)^2=1152\) graph automorphisms in this basis using integer matrices and checks the following character formula. For an element \((\sigma,\tau)\) preserving the two classes,
\[
\chi_{H_2}(\sigma,\tau)=\chi_{(2,2)}(\sigma)\chi_{(2,1,1)}(\tau)+\chi_{(2,1,1)}(\sigma)\chi_{(2,2)}(\tau).
\]
For every element exchanging the classes, this character is zero. Here, writing \(f\) for the number of fixed points, \(t\) for the number of two-cycles and \(\epsilon\) for the sign of a permutation of four letters,
\[\chi_{(2,2)}=\binom f2+t-f,\qquad\chi_{(2,1,1)}=\epsilon(f-1).\]
The displayed formula identifies the claimed induced rational \(W\)-module, since characteristic-zero representations of finite groups are determined by their characters. As a separate check, signed cellular Lefschetz traces on \(C_0,C_1,C_2\), together with the graph-cycle character, reproduce all 1152 traces on \(H_2\).

For first rational homology, the known maturity theorem for complete bipartite graphs \(K_{p,q}\), with \(p,q\ge3\), identifies ordered two-point rational \(H_1\) with two copies of graph \(H_1\). Transfer to unordered points takes the label-swap invariant diagonal. The graph cycle space for \(K_{4,4}\), as a \(\mathfrak S_4\times\mathfrak S_4\)-module, is the tensor product of the two augmentation representations, giving \(S^{(3,1)}\boxtimes S^{(3,1)}\). Interchanging graph color classes reverses all left-to-right edge orientations, giving minus the tensor-factor flip. Neither positive-degree rational homology representation has an invariant vector under \(W\), so transfer identifies the rational homology of the finite-group quotient with the invariant part of \(H_*(X;\mathbb Q)\).

## Verification
Run `python k44_verify.py` with Python 3, SymPy and NumPy. The verifier constructs the original graph and all cubical cells, both signed integer boundaries, all eighteen torus chains, Smith forms of the torus and boundary matrices, and all 1152 full-group actions. It independently checks the representation character through cellular Lefschetz traces, and finishes with `VERIFY_OK`. The embedded `verification_output.txt` is a record of an actual standalone execution. No floating-point ranks, probabilistic sampling, or unverified external data are used for the proof.

## Relationship to prior work
Abrams's original cubical model underlies the cellular construction. Barnett–Farber (arXiv:0903.2180) and Farber–Hanbury (arXiv:1005.2300, Proposition 22 and Corollary 24) provide the intersection-form and maturity framework and the **ordered** complete-bipartite Betti numbers. Neither their ordered ranks nor the general product-cycle construction specify this integral relation lattice together with the complete \(1152\)-element automorphism character for the **unordered** space. Published work on two-point **sink** configurations allows a different collision rule and does not imply this conclusion. The known nonplanar order-two first-homology phenomenon is not claimed to be new in isolation.

## Limitations
This is one finite graph, not a uniform classification of all complete bipartite graphs. The ordinary quotient's rational acyclicity does not assert contractibility or integral acyclicity. The exact computation certifies the finite case, not uncomputed graphs. A relevant 2010 Durham thesis treats ordered configurations of complete bipartite graphs but its full text was inaccessible for direct comparison, so unindexed equivalent treatment of torus relations remains a publication-priority risk. The result has not been independently audited.

## References
- A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118, first posted September 12, 2000.
- K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180, first posted March 12, 2009.
- M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first posted May 13, 2010, especially Proposition 22 and Corollary 24.
- K. Barnett, *The Configuration Space of Two Particles Moving on a Graph*, Durham University doctoral thesis, deposited May 27, 2010; abstract inspected, full text unavailable.
- T. Maciążek et al., *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics (2019); Section 5.1 on product cycles.
