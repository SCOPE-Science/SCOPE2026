# Five-edge spider complexes: sphere wedges and integral arm-permutation homology

## Finding
Let \(T_k\) be the tree with a central vertex \(z\) and \(k\) pairwise disjoint arms \(z-a_i-b_i-c_i-d_i-e_i\), each containing exactly five edges. Thus \(T_k\) has \(5k+1\) vertices. Let \(K_k=\operatorname{Ind}_2(T_k)\), the simplicial complex of vertex subsets whose induced connected components have at most two vertices, equivalently the induced-three-vertex-path-free complex. For every integer \(k\ge3\),

\[
K_k\simeq\bigvee^{k-1}S^{2k+1}.
\]

Moreover, the full graph automorphism group is \(S_k\), acting by permuting arms, and its **integral** action on the sole nonzero reduced homology is the augmentation lattice

\[
\widetilde H_{2k+1}(K_k;\mathbb Z)\cong_{\mathbb Z[S_k]}\ker\!\left(\mathbb Z^k\xrightarrow{\sum}\mathbb Z\right).
\]

In particular, for \(g\in S_k\), the rational character is the number of arms fixed by \(g\), minus one. The same formulas extend to \(k=2\), where the tree is an eleven-vertex path; the genuinely branching case begins at \(k=3\). Other reduced integral homology groups vanish.

## Assumptions and scope
All graphs are finite, undirected and simple. Write each arm as \(z-a_i-b_i-c_i-d_i-e_i\), for \(i=1,\ldots,k\); each such list has exactly five edges after \(z\). A selected set is a face precisely when it contains no three vertices spanning a connected three-vertex path. All homotopy equivalences are of geometric realizations. The arm-permutation module is an integral statement, rather than merely a rational character computation. No assertion is made for arbitrary spider lengths or for higher independence parameters.

## Proof
**Path base cases.** Let \(Q_j=\operatorname{Ind}_2(P_j)\), with \(P_j\) the path on \(j\) vertices. The complex \(Q_3\) is the boundary of a triangle, hence \(S^1\). The complex \(Q_4\) simplicially collapses to the induced copy of \(Q_3\) on its last three vertices. Indeed, label \(P_4\) by \(0,1,2,3\). Delete the free-face pairs \((\{0,1\},\{0,1,3\})\), \((\{0,2\},\{0,2,3\})\), and \((\{0\},\{0,3\})\), in order. Each listed first face has the listed second face as its unique remaining maximal coface. Thus inclusion of \(Q_3\) into \(Q_4\) induces an integral isomorphism on reduced first homology.

The complex \(Q_5\) is collapsible. An elementary-collapse list is given next, with each pair written as (free face, unique maximal coface), in the indicated order, using path labels \(0,1,2,3,4\):

```
(013, 0134), (01, 014), (12, 124), (13, 134),
(23, 023), (02, 024), (03, 034), (0, 04),
(1, 14), (2, 24), (3, 34).
```

Here a string such as `013` denotes the subset \(\{0,1,3\}\), and the final remaining vertex is \(4\). The standalone verifier reconstructs both complexes and checks every elementary collapse against the entire current face set.

**Center deletion and link.** Deleting the vertex \(z\) from \(K_k\) leaves the join \(D=Q_5^{*k}\), which is contractible. Put \(J=Q_4\) and \(B=Q_3\), with \(B\subset J\) via the last-three-vertices inclusion above. The center link \(L=\operatorname{lk}_{K_k}(z)\) has an exact decomposition

\[
L=A\ \cup\ \bigcup_{i=1}^k (a_i*B_i),\qquad
A=J^{*k},\qquad
B_i=J^{*(i-1)}*B*J^{*(k-i)}\subset A.
\]

Here \(a_i*B_i\) denotes a simplicial cone with apex \(a_i\), not an additional join factor in \(A\). To verify the decomposition, in a face containing \(z\) at most one \(a_i\) can occur; if none occurs, each arm contributes any face of \(J\) on \(b_i,c_i,d_i,e_i\). If \(a_i\) occurs, \(b_i\) is forbidden and the remaining \(c_i,d_i,e_i\) form a face of \(B\); all other arms contribute \(J\). Conversely all these combinations are valid. Thus the displayed equality is exact, not merely up to homotopy. Cones intersect each other only in their common subcomplex \(A\).

Since \(J\) collapses onto \(B\), the inclusion \(B_i\hookrightarrow A\) is a homotopy equivalence for every \(i\). Also \(A\simeq(S^1)^{*k}\cong S^{2k-1}\). Glue the first cone \(a_1*B_1\) to \(A\): the resulting complex is contractible because it is the mapping cone of a homotopy equivalence. Each remaining cone has its attaching map through the original \(A\), now lying in a contractible subcomplex; consequently its attachment is a wedge summand \(\Sigma B_i\simeq S^{2k}\). It follows that

\[
L\simeq\bigvee^{k-1}S^{2k}.
\]

The vertex decomposition is \(K_k=D\cup_L(z*L)\). As \(D\) is contractible and the inclusion \(L\hookrightarrow D\) is nullhomotopic, its homotopy pushout gives \(K_k\simeq\Sigma L\), proving the wedge formula and the integral homology assertions. This applies uniformly to every \(k\ge2\) and does not rely on finite enumeration.

**Integral symmetry.** For \(k\ge2\), the pair \((L,A)\) has quotient \(L/A=\bigvee_i\Sigma B_i\). Its long exact integral homology sequence, together with the homotopy equivalences \(B_i\to A\), gives the exact sequence

\[
0\longrightarrow \widetilde H_{2k}(L;\mathbb Z)\longrightarrow
\bigoplus_{i=1}^k\widetilde H_{2k-1}(B_i;\mathbb Z)
\xrightarrow{\sum_i}\widetilde H_{2k-1}(A;\mathbb Z)
\longrightarrow0.
\]

Choose on each copy of \(B=Q_3\) the same oriented triangular cycle, and orient \(J\) by its restriction to \(B\). Orient each join in increasing arm order. Exchanging two arm factors of reduced homological degree one introduces sign \((-1)^{(1+1)(1+1)}=+1\). Hence these choices are compatible with every arm permutation, and all \(B_i\to A\) have degree \(+1\). The middle group is exactly the permutation lattice \(\mathbb Z^k\), with the map displayed equal to augmentation. Because the cone-deletion sequence \(K_k=D\cup_L(z*L)\) is equivariant and \(D\) is contractible, \(\widetilde H_{2k+1}(K_k;\mathbb Z)\cong\widetilde H_{2k}(L;\mathbb Z)\) is an isomorphism of integral \(S_k\)-modules. This establishes the stated character and augmentation lattice, including integral rather than just rational structure.

## Verification
Running `python3 verify_spider5.py` uses only the Python standard library. It independently enumerates every admissible face from forbidden induced three-vertex paths, checks the three collapses \(Q_4\searrow Q_3\) and eleven collapses \(Q_5\searrow\text{point}\), performs exact mod-two boundary reductions on the complete face sets for \(k=2,3\), and computes signed simplicial Lefschetz traces for every element of \(S_2\) and \(S_3\). The predicted traces are \(1- (\#\text{fixed arms}-1)\) because the homology dimension \(2k+1\) is odd and ordinary \(H_0\) contributes one. All checks pass and the output is embedded as `verify_spider5_output.txt`. These finite checks corroborate, but do not replace, the uniform proof.

## Relationship to prior work
Sawant [1] proves vertex decomposability of \(\operatorname{Ind}_r(T)\) for every tree and parameter, and explicitly identifies the induced-three-vertex-path-free model with \(r=2\). This does not determine the dimension and multiplicity of spheres or the integral automorphism module for this family. Deshpande and Singh [2] give explicit homotopy types for paths, fully whiskered graphs, perfect regular branching trees, complete multipartite graphs and cycles; the trees here with \(k\ge3\) have a single degree-\(k\) center and five-edge unbranched arms, so are neither paths nor perfectly branched nor fully whiskered (and have no perfect matching). Ghosh and Selvaraja [3] study shellability of the same class of complexes under graph hypotheses; shellability alone does not imply the asserted exact Betti multiplicity or integral permutation representation. Kumar and Sarkar [4] study regularity of three-path ideals, not this full integral equivariant homotopy classification.

## Limitations
The result is restricted to exactly five edges per arm and \(r=2\); it does not classify unequal-arm spiders. The proof is an ordinary homotopy equivalence, not a claim that the full simplicial complex collapses to a wedge subcomplex. The short base-case collapses and exact center-link decomposition are necessary premises and are explicitly reproducible. No independent scientific audit has been performed. An equivalent result in unindexed literature remains possible; targeted searches cannot certify uniqueness.

## References
[1] R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first public 2026-05-24), https://arxiv.org/abs/2605.25150.

[2] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v2 (2021), https://arxiv.org/html/2001.05448v2.

[3] A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614v3 (2025), https://arxiv.org/html/2505.06614v3.

[4] R. Kumar and R. Sarkar, *Regularity of 3-Path Ideals of Trees and Unicyclic Graphs*, arXiv:2503.12111v1 (2025), https://arxiv.org/html/2503.12111v1.
