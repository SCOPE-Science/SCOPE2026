# Symmetric-group homology character of constant-weight-three Hamming Rips complexes

## Finding
For every integer \(n\ge5\), let \(X_n=\operatorname{Cl}(J(n,3))\). Equivalently, \(X_n\) is the inclusive distance-two Vietoris–Rips complex of the binary Hamming-weight-three layer in \(\{0,1\}^n\). The symmetric group \(S_n\) acts by coordinate permutation. Its reduced rational homology vanishes outside dimension two. Denote by \(P_n=\mathbb Q^n\) the natural permutation module, by \(W=H_1(K_4;\mathbb Q)\) the three-dimensional cycle representation on the four-vertex complete graph, and by \(\mathbf1\) the trivial module. Then the **complete character** of the degree-two module is
\[
[\widetilde H_2(X_n;\mathbb Q)] =
[\operatorname{Ind}_{S_{n-4}\times S_4}^{S_n}(\mathbf1\boxtimes W)]
+ [\bigwedge^3 P_n]
- [\operatorname{Ind}_{S_{n-3}\times S_1\times S_2}^{S_n}(\mathbf1\boxtimes\mathbf1\boxtimes\operatorname{sgn})]
+ [\mathbb Q[\binom{[n]}{2}]]-[\mathbf1].
\]
Square brackets denote the Grothendieck representation ring. The formula is an equality of actual characters; because rational representations of finite groups are semisimple and the terms are rational modules, it uniquely determines the rational representation up to isomorphism. It **does not** claim a positive direct-sum realization of the displayed signed expression. In particular,
\[
\dim\widetilde H_2(X_n;\mathbb Q)=3\binom n4-2\binom n3+\binom n2-1.
\]
For instance, the dimensions for \(n=5,6,7,8\) are \(4,19,55,125\), and the respective transposition traces are \(-2,-5,-5,5\).

## Assumptions and scope
Vertices of \(X_n\) are triples \(U\subseteq[n]\); a finite set of vertices is a simplex precisely when every pair of triples intersects in exactly two elements (or the set has at most one vertex). All homology below is ordinary reduced simplicial homology with rational coefficients, unless integral or mod-two coefficients are specified. The symmetric group \(S_4\) acts on the four vertices of \(K_4\) by graph automorphisms; \(W\) is its first graph homology. Each copy of \(S_m\) is the symmetric group on the indicated disjoint blocks, and the last \(S_2\) acts by its sign character.

## Proof
**1. Two kinds of facets.** Every clique of triples is contained in a *star* \(A_{ab}\), formed by all triples containing the pair \(\{a,b\}\), or a *top* \(T_Q\), formed by the four triples contained in a four-element set \(Q\). This also follows from the general maximal-clique classification of Shuldiner–Oldford [2]. Let \(A\subseteq X_n\) be the union of star simplices. Stars have contractible nonempty intersections: the intersection indexed by pairs \(e_1,\dots,e_s\) is a simplex if the union of the \(e_i\) has at most three elements, and is empty otherwise. Therefore the nerve theorem yields an \(S_n\)-equivariant homotopy equivalence \(A\simeq N\), with \(N\) a two-dimensional simplicial complex whose vertices are the two-subsets of \([n]\), whose edges are two-subsets sharing one point, and whose two-simplices are \(\{ab,ac,bc\}\), indexed by three-subsets \(\{a,b,c\}\). There are no higher-dimensional simplices.

**2. Relative top attachments.** For a four-element set \(Q\), the top \(T_Q\) is a three-simplex and \(T_Q\cap A\) is the *one-skeleton* of that three-simplex, canonically a \(K_4\) graph. Distinct tops intersect only in faces lying in \(A\). Thus, as an \(S_n\)-equivariant relative chain complex,
\[
C_*(X_n,A;\mathbb Q)\cong\bigoplus_{|Q|=4}C_*(\Delta^3,K_4;\mathbb Q).
\]
The relative homology of each pair is \(H_1(K_4;\mathbb Q)=W\) in degree two and zero in every other degree, by the relative long exact sequence and contractibility of the simplex. Consequently,
\[
\widetilde H_i(X_n,A;\mathbb Q)\cong
\begin{cases}
\operatorname{Ind}_{S_{n-4}\times S_4}^{S_n}(\mathbf1\boxtimes W),&i=2,\\
0,&i\ne2.
\end{cases}
\]
Since \(A\simeq N\) has dimension two up to homotopy, \(\widetilde H_i(X_n;\mathbb Q)=0\) for \(i\ge3\).

**3. Vanishing of first homology.** Let \(L\) be the clique complex of the line graph of the complete graph on \([n]\). Its one-skeleton is exactly the one-skeleton of \(N\). The simplices on all edges incident to a single vertex of the original complete graph cover a subcomplex of \(L\) with nerve the graph \(K_n\). Each triangle \(\{ab,bc,ac\}\) attached to this subcomplex maps under the nerve correspondence to the triangular circuit \(a\! -\! b\! -\! c\! -\! a\) of \(K_n\). The triangular circuits generate the fundamental group normally, so \(L\) is simply connected. Consequently, every one-cycle of the common one-skeleton is a linear combination of the boundaries of its triangles. Each triangle of \(L\) is either already filled in \(N\) (the edges \(ab,ac,bc\)) or has the form \(\{ia,ib,ic\}\). The latter star-triangle maps through the nerve equivalence to a triangular loop on the vertices \(iab,ibc,iac\) in \(A\), and that triangle lies in the top \(T_{iabc}\subseteq X_n\). Therefore every first-homology generator of \(A\) bounds in \(X_n\); \(\widetilde H_1(X_n;\mathbb Q)=0\). The complex is connected, so reduced zeroth homology vanishes as well.

**4. Character computation.** The long exact sequence of \((X_n,A)\), together with the preceding vanishings, gives
\[
[\widetilde H_2(X_n)] = [\widetilde H_2(A)]-[\widetilde H_1(A)]+[H_2(X_n,A)].
\]
The reduced equivariant Euler identity applied to \(N\) gives
\[
[\widetilde H_2(A)]-[\widetilde H_1(A)] = [C_2(N)]-[C_1(N)]+[C_0(N)]-[\mathbf1].
\]
Its two-simplex module is \(C_2(N)=\bigwedge^3 P_n\), because relabeling the three edges of a triangle has the same orientation sign as relabeling its three vertices. Its one-simplex module is \(\operatorname{Ind}_{S_{n-3}\times S_1\times S_2}^{S_n}(\mathbf1\boxtimes\mathbf1\boxtimes\operatorname{sgn})\): an edge is two incident two-subsets, with a unique common center and two outer vertices; interchanging the outer vertices reverses its orientation. Its zero-simplex module is the permutation representation on two-subsets. Substitute the relative module from Step 2 to obtain the character identity. Evaluating at the identity yields the dimension formula, since \(\dim W=3\), \(\dim C_2(N)=\binom n3\), \(\dim C_1(N)=3\binom n3\), and \(\dim C_0(N)=\binom n2\). This finishes the proof for every integer \(n\ge5\).

## Verification
Run `python3 verify.py` with only the Python 3 standard library. The program independently constructs the actual face sets from the two facet types, computes exact mod-two boundary ranks, and evaluates each conjugacy-class representative twice: directly by its signed action on all simplices and by the independent five-term character formula. For \(n=5,6,7,8\), it checked 55 conjugacy-class representatives and verified mod-two Betti ranks \(4,19,55,125\) in degree two with zero in all other reduced degrees. Its successful completion prints `VERIFY_OK`. These finite checks are consistency tests, **not** a substitute for the infinite proof above.

## Relationship to prior work
Shuldiner–Oldford [2], whose full text was inspected through its available research manuscript (Sections 1–5), classifies the maximal cliques of Johnson graphs; it yields the facet input but does not determine the homology or representation of the resulting clique complex. Galetto–Montaño–Wellner [1] studies the representation on Vietoris–Rips homology of the *entire* binary hypercube; the present space is the *induced constant-weight-three layer*, not that full complex, and the representation is not a formal restriction of the earlier homology module. Only the abstract and scope of [1] could be inspected; its inaccessible full text remains an explicit residual comparison risk. Lyudogovskiy [3] treats the different partition graph; its two-sphere homotopy conclusions do not calculate this Johnson-graph action. No inspected publication established the displayed constant-layer character.

## Limitations
The result concerns the rational \(S_n\)-representation at exactly one weight layer and one inclusive Rips scale. The representation-ring expression need not be a direct-sum splitting with the displayed negative terms. The theorem neither classifies integral \(S_n\)-lattices nor determines persistence across scales or weight cutoffs. An unindexed mathematically equivalent calculation, or relevant material in the unavailable full text of [1], remains possible. No independent external audit has been performed.

## References
[1] F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1, first posted June 18, 2026, https://arxiv.org/abs/2606.20784 .

[2] P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710v1, first posted August 26, 2022, https://arxiv.org/abs/2208.12710 .

[3] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370v1, first posted March 15, 2026, https://arxiv.org/abs/2603.14370 .
