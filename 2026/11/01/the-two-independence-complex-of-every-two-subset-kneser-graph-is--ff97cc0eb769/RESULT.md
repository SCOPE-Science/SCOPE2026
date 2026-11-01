# The two-independence complex of every two-subset Kneser graph is a three-skeleton

## Finding
For each integer \(n\ge4\), write \(G_n=\mathrm{KG}(n,2)\). Define \(X_n=\operatorname{Ind}_2(G_n)\): a face is a family of unordered pairs in \([n]\) such that each chosen pair is disjoint from at most one other chosen pair. Then
\[
X_n\simeq\operatorname{skel}_3(\Delta^{n-1})\simeq\bigvee^{\binom{n-1}{4}}S^3.
\]
The empty wedge is a point. For \(V_n=\ker(\mathbb Z^n\xrightarrow{\sum}\mathbb Z)\), the natural permutation action on integral homology is
\[
\widetilde H_3(X_n;\mathbb Z)\cong\bigwedge^4 V_n
\quad\text{as }\mathbb Z[\mathfrak S_n]\text{-modules},
\]
and all other reduced integral homology vanishes. For \(n=6\), there are five three-spheres and the rational module is the sign-twisted standard representation of \(\mathfrak S_6\). The equivalence of spaces is not asserted equivariant.

## Assumptions and scope
The Kneser graph \(\mathrm{KG}(n,2)\) has the \(\binom n2\) two-element subsets of \([n]\) as vertices, and edges precisely between disjoint pairs. We use the *closed under taking subsets* convention for simplicial complexes. Thus the condition \(\operatorname{Ind}_2\) means that connected components of the induced graph have at most two vertices, equivalently every vertex has induced degree at most one. The simplicial \(r\)-skeleton contains all faces of dimension at most \(r\). Homology has integral coefficients except where explicitly stated. All integer bounds, including \(n=4\), are included.

## Proof
**Step 1 (ordinary intersecting-family complex).** Set \(B_n=\operatorname{Ind}(G_n)\), whose faces are pairwise-intersecting collections of pairs. A family of pairs with no disjoint members is contained either in a full star \(S_i=\{\{i,j\}:j\ne i\}\) or in the three edges of a triangle on \(\{i,j,k\}\). Indeed, two distinct intersecting pairs are \(\{i,j\}\) and \(\{i,k\}\); if another pair avoids \(i\), it must be \(\{j,k\}\), and no fourth distinct pair can meet all three. Let \(U_n=\bigcup_{i=1}^n\Delta(S_i)\). Each star simplex is contractible; distinct stars meet in precisely the vertex \(\{i,j\}\); every threefold intersection is empty. By the simplicial nerve theorem, \(U_n\simeq K_n\), the complete graph on the underlying symbols. The induced correspondence of integral first homology with cycles of the complete graph is natural under permutations.

For each three-symbol subset \(T=\{i,j,k\}\), the three edges \(\{i,j\},\{i,k\},\{j,k\}\) form a 2-simplex \(F_T\) of \(B_n\), not contained in \(U_n\). Its boundary is in \(U_n\), and distinct such interiors do not meet outside \(U_n\). The attaching loop is the \(i,j,k\) triangle of the nerve \(K_n\). Hence \(B_n\simeq\operatorname{skel}_2\Delta^{n-1}\). At chain level the oriented relative triangles \(C_2(B_n,U_n;\mathbb Z)\) identify with \(\bigwedge^3\mathbb Z^n\) by \(F_{\{i,j,k\}}\mapsto e_i\wedge e_j\wedge e_k\), with the connecting homomorphism in the pair exact sequence given by the usual oriented triangular boundary in \(H_1(U_n;\mathbb Z)\). The correspondence preserves permutation signs and identifies \(H_2(B_n;\mathbb Z)\) with \(\operatorname{im}(\partial_3)\) inside the simplex's 2-chains.

**Step 2 (all added faces are four-point simplices).** Suppose \(\mathcal F\in X_n\setminus B_n\). Choose two disjoint pairs \(A,B\in\mathcal F\). Every other chosen pair must intersect each of \(A\) and \(B\), because both already have one disjoint partner. Being a two-set, it is therefore contained in the four-set \(Q=A\cup B\). Conversely all subsets of the six pairs in any four-set \(Q\) are legal, since the disjointness graph of the six pairs is three independent edges. This four-point containment is also the combinatorial observation of Frankl--Kupavskii, Claim 1.7 (2020 preprint). Put \(D_Q=\Delta(\binom Q2)\), a 5-simplex. We obtain the *exact* union
\[
X_n=B_n\cup\bigcup_{Q\in\binom{[n]}4}D_Q.
\]
The intersection \(D_Q\cap B_n=B_Q\) is the ordinary independence complex of \(\mathrm{KG}(4,2)\): its disjointness graph is a union of three edges, so \(B_Q\cong(S^0)^{*3}\cong S^2\) (the octahedral sphere). For distinct four-sets \(Q,R\), their intersection \(D_Q\cap D_R\) lies in \(B_n\), since it uses only pairs drawn from at most three shared symbols. Thus these contractible \(D_Q\)'s are attached independently, along octahedral 2-spheres. Replacing each contractible \(D_Q\) relative to \(B_Q\) by a cone on \(B_Q\) is a homotopy equivalence of the resulting homotopy pushouts. Hence \(X_n\) has a CW model obtained from \(B_n\) by attaching one 3-cell for each four-set \(Q\).

**Step 3 (the attaching maps are tetrahedral boundaries).** Fix \(Q=\{i,j,k,l\}\) with \(i<j<k<l\). The octahedral fundamental cycle in \(B_Q\) comprises four star triangles (lying in \(U_n\)) and four nonstar triangles \(F_{Q\setminus\{q\}}\). Its image in \(C_2(B_n,U_n)\) is, up to the choice of global orientation,
\[
\partial[e_i,e_j,e_k,e_l]
=[e_j,e_k,e_l]-[e_i,e_k,e_l]+[e_i,e_j,e_l]-[e_i,e_j,e_k].
\]
Each coefficient is a unit: each nonstar triangle occurs precisely once. The relative chain is an actual cycle because it comes from the octahedral fundamental cycle. Since the underlying two-skeleton is simply connected, Hurewicz identifies homotopy classes of 2-sphere attaching maps with integral 2-homology. Therefore the 3-cell for each \(Q\) attaches, up to homotopy, by the same map as the tetrahedral face on \(Q\). Attaching all these cells yields a space homotopy equivalent to \(\operatorname{skel}_3\Delta^{n-1}\). In particular, no unverified extension from finitely many \(n\) is needed.

**Step 4 (wedge decomposition).** Fix symbol \(1\). The union of all simplices of dimension at most three containing \(1\), together with their faces, is a cone on the 2-skeleton of the simplex spanned by the remaining symbols. Contracting this contractible subcomplex leaves one 3-sphere for every four-subset of \(\{2,\ldots,n\}\), attached along its entire boundary to the basepoint. Thus the third skeleton has homotopy type \(\bigvee^{\binom{n-1}{4}}S^3\). For \(n=4\) this is contractible, as required.

**Step 5 (the integral permutation module).** The relative 3-cell for \(Q\) is oriented by the fundamental octahedral cycle of \(B_Q\) so that its image in the pairwise-intersecting relative 2-chains is the alternating tetrahedron boundary. Permutations preserve this orientation rule: reordering \(Q\) multiplies its oriented generator by the sign of that reordering. Consequently the relative third cellular chain module identifies, including its full integral permutation signs, with \(\bigwedge^4 E\), where \(E=\mathbb Z^n\) is the symbol permutation lattice. The cellular boundary to \(H_2(B_n)\) is the standard simplex map \(\partial_3:\bigwedge^4E\to\operatorname{im}(\partial_3)\subset\bigwedge^3 E\). The integral augmented simplex chain complex is exact. If \(V=\ker(E\xrightarrow{\sum}\mathbb Z)\), then \(\partial_3\) is the contraction with the sum functional, and its kernel is exactly \(\bigwedge^4 V\) (choose an integral splitting \(E=V\oplus\mathbb Z e_1\)). The result follows, including for \(n=4\) when the kernel is zero.

## Verification
The two standalone Python files `verify_kneser.py` and `verify_family.py` give independently reproducible finite checks; use `python3 verify_kneser.py` and `python3 verify_family.py` in the same directory. For \(n=6\), two separate face predicates agree on all \(2^{15}=32768\) ambient subsets; exactly 747 including the empty face are legal. The script exhaustively checks 2,580 face incidences for an acyclic matching with one critical vertex and five critical 3-cells; independent mod-two ranks agree. It enumerates all 720 permutations and finds the rational character \(\operatorname{sgn}(\sigma)(\#\operatorname{Fix}(\sigma)-1)\). The second script checks the structural union and complete Morse acyclicity for each \(4\le n\le9\), yielding respective sphere multiplicities \(0,1,5,15,35,70\). These are finite corroborations only; Steps 1--5 supply the universal proof.

## Relationship to prior work
Braun, *Independence Complexes of Stable Kneser Graphs* (2009 preprint), treats ordinary independence of stable Kneser graphs; Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs* (2015 preprint), supplies the path-devoid/matching-tree framework. Deshpande--Singh, *Higher independence complexes of graphs and their homotopy types* (2020 preprint), studies various graph families but does not give this \(\mathrm{KG}(n,2)\) family. Frankl--Kupavskii, *Almost intersecting families* (2020 preprint), explicitly proves the four-point containment in Claim 1.7; this combinatorial lemma is **not** claimed new. Feng--Wang (2024) studies ordinary independence of Kneser graphs, a distinct simplicial complex. The novel mathematical statement here is the integral three-skeleton homotopy classification together with the natural integral homology module. No decisive covering result was found in checked records, but unindexed equivalent work remains possible.

## Limitations
The theorem is specific to two-element Kneser vertices and the higher-independence parameter two. It does not classify \(\mathrm{KG}(n,k)\) for \(k>2\), higher permitted induced degree, or the full equivariant homotopy type. The non-equivariant equivalence and integral module should not be conflated with equivariant homotopy equivalence. The independent audit and a definitive global publication-priority assessment have not been performed.

## References
- B. Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (first posted 2009-12-03); https://arxiv.org/abs/0912.0720.
- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first posted 2015-01-27); https://arxiv.org/abs/1501.06754.
- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (2020); https://arxiv.org/abs/2001.05448.
- P. Frankl and A. Kupavskii, *Almost intersecting families*, arXiv:2004.08714v1 (first posted 2020-04-18), especially Claim 1.7; https://arxiv.org/abs/2004.08714.
- J. Feng and X. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (2024); https://arxiv.org/abs/2404.10566.
