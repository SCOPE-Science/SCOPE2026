# Integral symmetric-group homology of the six-vertex non-perfect-matching complex

## Finding
Let \(E=\binom{[6]}2\) and let \(X\) be the simplicial complex whose faces are the subsets \(F\subseteq E\) that do **not** contain a perfect matching of the complete graph \(K_6\). Let \(\mathcal P\) be the ten unordered partitions \(P=\{A,B\}\) of \([6]\) into two triples, and write
\[
\operatorname{Aug}(\mathcal P)
=\ker\!\left(\mathbb Z[\mathcal P]\xrightarrow{\sum}\mathbb Z\right).
\]
The natural permutation action of \(S_6\) on the six graph vertices induces the following **integral**, not just rational, homology representation:
\[
\boxed{\widetilde H_5(X;\mathbb Z)\cong_{\mathbb Z[S_6]}
\operatorname{sgn}_6\otimes\operatorname{Aug}(\mathcal P).}
\]
All other reduced integral homology groups vanish. In particular the fifth homology is free of rank nine, with an integral basis indexed by the differences \(e_P-e_{P_0}\), for any fixed \(P_0\in\mathcal P\), after the sign-twisted identification.

The identification is geometric: for each \(P=\{A,B\}\), the union of the two triangular edge sets \(E(K_A)\cup E(K_B)\) is a maximal five-simplex \(T_P\) of \(X\). The coefficient of an integral five-cycle on these ten simplices, suitably reoriented by its integral attaching degree, defines the displayed isomorphism. The subcomplex \(Y=X\setminus\{T_P:P\in\mathcal P\}\) has the homotopy type of \(S^4\), and the ten boundaries \(\partial T_P\) are all primitive generators of \(H_4(Y;\mathbb Z)\).

As a rational representation, the answer is the irreducible Specht module \(S^{(2,2,1,1)}\). Its precise integral form is material: the augmentation kernel is **not** isomorphic, as a \(\mathbb Z[S_6]\)-lattice, to the augmentation quotient \(\mathbb Z[\mathcal P]/\mathbb Z\sum_Pe_P\).

## Assumptions and scope
The vertex set \([6]\) is \(\{0,1,2,3,4,5\}\) for the exhaustive certificate. An abstract face of \(X\) is an edge subset of \(K_6\) without three pairwise vertex-disjoint edges. Homology is reduced simplicial homology with its ordinary signed integer differential. The group \(S_6\) acts by relabeling the underlying six graph vertices, thereby permuting the fifteen vertices of \(X\). Each five-simplex \(T_P\) is oriented by the increasing lexicographic ordering of its six graph edges. No assertions are made for \(n\ne6\) or for more general graph complexes.

The archived source motivating this object is Linusson–Shareshian–Welker, arXiv:math/0410345v1, publicly posted 2004-10-15. Its Corollary 1.2 already gives the nonequivariant homotopy type \(X\simeq\bigvee^9 S^5\). That prior theorem is **not** claimed as new here. The present result determines the exact integral \(S_6\)-lattice through natural ten-facet coefficients and the intermediate four-sphere.

## Proof
**1. Ten distinguished facets.** For any unordered split \(P=\{A,B\}\) into triples, the six internal edges of the two triangles contain no perfect matching: a matching within a disjoint union of two odd triangles covers at most four of the six graph vertices. Adding any cross-edge gives a perfect matching, by pairing the two remaining vertices of each triangle. Hence \(T_P\) is a maximal five-simplex. There are exactly ten such partitions. Removing only the ten maximal simplices, while retaining all their proper faces, produces a genuine simplicial subcomplex \(Y\).

**2. Exact sphere reduction of \(Y\).** Order the fifteen graph edges lexicographically, with indices beginning at zero. Run the following finite matching algorithm on the complete face poset of \(Y\), *including* the empty face. At each successive pivot index
\[
(10,2,0,11,6,14,8,12,4,5,9,3,1,13,7),
\]
pair each as-yet-unpaired face lacking that edge with the corresponding face containing it, provided both are still unpaired. The supplied standalone verifier enumerates **all** \(2^{15}\) possible edge subsets, finds precisely \(7935\) faces of \(Y\), constructs \(3967\) matched pairs, and leaves one unmatched four-simplex, of edge-mask \(18501\). Independently it enumerates all \(43920\) codimension-one Hasse incidences, reverses the \(3967\) matched incidences, and checks the resulting full directed graph is acyclic by complete topological sorting (all \(7935\) nodes are visited). By integral discrete Morse theory, the reduced complex has a single four-dimensional critical cell and consequently \(Y\simeq S^4\). This is a finite exhaustive certificate, not an inference from sampled instances.

**3. Primitive attaching degree.** An explicit integral four-cocycle \(\varphi\) on \(Y\) is reconstructed by the verifier. Begin with value one on the unmatched four-simplex and zero on all four-simplices paired with three-simplices. For every pair \((\ell,u)\) with \(\ell\) a four-simplex and \(u\) a five-simplex, use the unit coefficient of \(\ell\) in \(\partial u\) to solve \((\delta\varphi)(u)=0\) for \(\varphi(\ell)\). The dependency order is reversed from a verified acyclic gradient order, so the construction uses only integer arithmetic. The resulting cochain has exactly \(52\) nonzero coefficients, each \(+1\) or \(-1\). Direct substitution into **every** five-simplex of \(Y\) verifies \(\delta\varphi=0\), while for \(P_0=\{\{0,1,2\},\{3,4,5\}\}\),
\[
\langle\varphi,\partial T_{P_0}\rangle=1.
\]
Since \(H_4(Y;\mathbb Z)\cong\mathbb Z\), this proves that \([\partial T_{P_0}]\) is a primitive generator, with \(\varphi\) the dual integral generator. The \(S_6\)-action is transitive on \(\mathcal P\), so **every** \(\partial T_P\) is primitive. The ten attaching degrees, with the stated lexicographic orientations and choice of \(\varphi\), are \((1,-1,1,-1,1,-1,1,-1,1,-1)\) in increasing order of the triple containing zero.

**4. Integral homology and the canonical lattice.** The pair \((X,Y)\) adds exactly ten five-dimensional relative cells and no other relative cells. Its relative homology is \(H_5(X,Y;\mathbb Z)\cong\mathbb Z[\mathcal P]\), with the orientations just specified, and the connecting map
\[
\partial_{\mathrm{rel}}:\mathbb Z[\mathcal P]\longrightarrow H_4(Y;\mathbb Z)\cong\mathbb Z
\]
sends each \(T_P\) to its primitive boundary with coefficient \(d_P\in\{+1,-1\}\). The integral long exact sequence, together with \(\widetilde H_*(Y;\mathbb Z)\) concentrated in degree four, identifies \(H_5(X;\mathbb Z)\) with the kernel of this surjective map and proves that all other reduced homology of \(X\) vanishes. Multiplying the basis element \(T_P\) by \(d_P\) identifies the map with ordinary augmentation of the ten-element permutation lattice. Because no six-simplex contains a maximal \(T_P\), the coefficient of a five-cycle on each \(T_P\) is unchanged by adding boundaries, so this is an explicit homology-coordinate map.

**5. The sign twist.** A transposition interchanging \(0\) and \(1\) fixes \(P_0\) and reverses the orientation of the five-simplex \(T_{P_0}\): it swaps two of the three edges of its first triangle. Naturality of the connecting homomorphism and the nonzero primitive class \([\partial T_{P_0}]\) show that this transposition acts by \(-1\) on the rank-one group \(H_4(Y;\mathbb Z)\). Since all transpositions in \(S_6\) are conjugate and generate the group, its action on that group is the sign character. Once the ten relative basis vectors are reoriented to have boundary \(+1\), equivariance forces each permutation \(g\) to send the vector indexed by \(P\) to \(\operatorname{sgn}(g)\) times the one indexed by \(gP\). Thus the kernel carries precisely \(\operatorname{sgn}_6\otimes\operatorname{Aug}(\mathcal P)\) over \(\mathbb Z\), with no saturation ambiguity.

**6. Rational identification and integral distinction.** The stabilizer of one partition of six vertices into triples acts transitively on the other nine partitions. Hence the action of \(S_6\) on \(\mathcal P\) is two-transitive, and its rational augmentation representation is the irreducible nine-dimensional \(S^{(4,2)}\); tensoring with sign gives \(S^{(2,2,1,1)}\). Let \(A=\operatorname{Aug}(\mathcal P)\) and \(Q=\mathbb Z[\mathcal P]/\mathbb Z\sum_Pe_P\). The canonical equivariant map \(A\to Q\) has matrix \(I_9+J_9\) in the natural bases and determinant \(10\). Two-transitivity makes \(A\otimes\mathbb Q\) absolutely irreducible, so by Schur's lemma every rational equivariant map \(A\otimes\mathbb Q\to Q\otimes\mathbb Q\) is a scalar multiple of this canonical map. Since its entries have greatest common divisor one, a scalar multiple integral in those bases must have integral scalar, and its determinant has absolute value \(10|c|^9\), never one. Thus \(A\not\cong_{\mathbb Z[S_6]}Q\).

## Verification
Run `python3 verify.py` from the directory containing this document. The verifier is self-contained and uses only Python's standard library. It enumerates all \(32768\) edge subsets, all \(15\) perfect matchings, all ten distinguished maximal facets, and all \(43920\) relevant Hasse incidences; it checks complete gradient acyclicity, an integer four-cocycle on every five-face, all ten primitive boundary evaluations, and all \(720\) elements of \(S_6\). It independently checks the transitive-partition action and the expected signs and traces on all eleven conjugacy types. Its terminal success token is `VERIFY_OK_NPM6_INTEGRAL_SIGNED_AUGMENTATION`.

The exact mathematical conclusion uses a **finite exhaustive** acyclic matching and cocycle certificate for a fixed finite complex, followed by the ordinary integral long exact sequence and group-equivariance. No sampled computation is substituted for an all-parameter argument.

## Relationship to prior work
Linusson, Shareshian and Welker (2004, Corollary 1.2) determine \(X\simeq\bigvee^9 S^5\), and their Theorem 1.11 gives a representation comparison after restriction to \(S_5\); they explicitly raise the full \(S_n\)-module question in Section 1 (Question 1.13 in their 2004 arXiv text). These statements neither specify the ten natural five-simplex coefficients nor identify the **integral** full-\(S_6\) augmentation kernel and its distinction from the augmentation quotient. The present result refines, rather than replaces, their ordinary homotopy result.

Jonsson's 2008 chapter on graphs avoiding matchings summarizes the same nonequivariant sphere-wedge theorem; the accessible chapter abstract does not discuss the integral full-\(S_6\) representation. The chapter's full text was not inspected and remains a bibliographic risk. Ordinary matching complexes, two-matchings with vertex-degree bounds, and bounded matching-number graph complexes are different constructions; results for the first two do not automatically cover the present integral lattice.

## Limitations
This is a complete result for the single natural case \(\mathrm{NM}_3(6)\), not a solution of the full representation problem for arbitrary \(n,k\), and not a claim that the known wedge-of-spheres homotopy type is new. The integral representation identification is established by a finite exact certificate plus standard topology. No external independent validation has been performed. A less-indexed treatment could contain an equivalent integral representation; the accessible-source search cannot rule that out.

## References
1. S. Linusson, J. Shareshian, and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345v1 (first publicly posted 2004-10-15), especially Corollary 1.2, Theorem 1.11, and Question 1.13. https://arxiv.org/pdf/math/0410345
2. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928 (2008), chapter *Graphs Avoiding k-matchings*, pp. 329–331, DOI:10.1007/978-3-540-75859-4_24. The chapter's accessible abstract was checked, not its entire text.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Classical discrete Morse theory used for the finite acyclicity-to-homotopy implication.
