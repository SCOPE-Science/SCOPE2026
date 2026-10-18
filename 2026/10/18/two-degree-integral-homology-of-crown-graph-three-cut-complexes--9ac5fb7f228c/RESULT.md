# Two-degree integral homology of crown-graph three-cut complexes

## Finding
Let \(n\ge5\) and let \(G_n=K_{n,n}\setminus M\) be the crown graph obtained by deleting a fixed perfect matching \(M\) from the complete bipartite graph. Write \(\Delta_3(G_n)\) for the **ordinary** three-cut complex: its facets are complements of three-vertex subsets inducing disconnected subgraphs. Define the positive integer
\[
B_n=\frac{n^4-10n^3+31n^2-30n+4}{4}.
\]
Then its **integral reduced homology, in every degree**, is
\[
\widetilde H_j(\Delta_3(G_n);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{B_n},&j=2n-6,\\
\mathbb Z^n,&j=2n-4,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is pure of dimension \(2n-4\), contains the complete \((2n-6)\)-skeleton of the simplex on its \(2n\) vertices, and is **not shellable**. In particular, at \(n=5\) it has \(\widetilde H_4\cong\mathbb Z\) and \(\widetilde H_6\cong\mathbb Z^5\).

The structural identification underlying the result is an integral homotopy classification of the **Alexander dual**:
\[
\Delta_3(G_n)^*\simeq\left(\bigvee^{B_n} S^3\right)\vee\left(\bigvee^n S^1\right).
\]
No corresponding wedge-of-spheres homotopy equivalence is asserted for \(\Delta_3(G_n)\) itself.

## Assumptions and scope
All graphs are finite, simple, and undirected. Label the bipartition \(A=\{a_1,\ldots,a_n\}\) and \(C=\{b_1,\ldots,b_n\}\). The crown graph has exactly those cross edges \(a_i b_j\) with \(i\ne j\). Here \(n\) ranges over every integer at least five. For a complex \(K\) on vertex set \(V\), its combinatorial Alexander dual is \(K^*=\{F\subseteq V:V\setminus F\notin K\}\). Reduced integral homology includes the empty and boundary degrees under the standard augmented-chain convention.

## Proof
**1. Identify every minimal nonface of the Alexander dual.** By the definition of a cut complex, \(F\in\Delta_3(G_n)^*\) if and only if \(F\) contains **no disconnected three-vertex subset**. A three-vertex subset is disconnected exactly when it lies wholly in \(A\), wholly in \(C\), or contains one forbidden matched pair \(\{a_i,b_i\}\). For a mixed triple with two vertices in one part and one in the other, the absence of a matched pair is equivalent to the single opposite-part vertex being adjacent to both same-part vertices, which makes that triple connected.

**2. Separate the chessboard complex from exceptional edges.** Let \(X_n\) be the simplicial complex of subsets \(F\subseteq A\cup C\) having at most two vertices from each part, and never both \(a_i\) and \(b_i\) for any index. Equivalently, \(X_n=\Delta_{n,2}^{2,2;1}\), the two-row multiple chessboard complex with row capacities two and column capacity one. The characterization in Step 1 shows the exact equality of simplicial complexes
\[
\Delta_3(G_n)^*=X_n\cup\bigcup_{i=1}^n\langle\{a_i,b_i\}\rangle.
\]
The added sets are precisely \(n\) one-simplices, each with endpoints already in \(X_n\), and none is contained in \(X_n\). There are no additional higher-dimensional simplices with matched pairs.

**3. Invoke the precise published shellability range.** Theorem 4.4 of Jojić, Vrećica and Živaljević [2] states that \(\Delta_{m,r}^{k_1,\ldots,k_r;1}\) is shellable for \(m\ge\sum_i k_i+r-1\). With \(r=2\), both capacities equal to two, and \(m=n\), this hypothesis is \(n\ge5\). Every facet of \(X_n\) has two vertices from each part at four distinct indices, so \(X_n\) is pure of dimension three. Consequently,
\[
X_n\simeq\bigvee^{B_n}S^3,
\]
for some nonnegative integer \(B_n\), and all its reduced integral homology outside degree three vanishes. This uses the general shellability theorem as an explicitly credited premise, not a newly proved shelling.

**4. Calculate the number of three-spheres exactly.** The four nonempty face counts of \(X_n\), in dimensions zero through three, are respectively
\[
2n,\quad 2n(n-1),\quad n(n-1)(n-2),\quad
\binom n2\binom{n-2}2.
\]
Thus \(\widetilde\chi(X_n)=2n-2n(n-1)+n(n-1)(n-2)-\binom n2\binom{n-2}2-1=-B_n\), where
\[
B_n=1-2n+2n(n-1)-n(n-1)(n-2)+\binom n2\binom{n-2}2
=\frac{n^4-10n^3+31n^2-30n+4}{4}.
\]
In particular \(B_5=1\), and \(B_{n+1}-B_n=(n-2)(n^2-4n+1)>0\) for every \(n\ge5\).

**5. Attach the exceptional edges.** The one-skeleton of \(X_n\) contains every pair of vertices except the \(n\) matched pairs, so \(X_n\) is path-connected. Attaching an interval between two points of a path-connected complex adds one circle up to homotopy; attaching these \(n\) distinct intervals therefore gives
\[
\Delta_3(G_n)^*\simeq X_n\vee\bigvee^n S^1.
\]
It follows that the only nonzero reduced **integral cohomology** of the dual is \(H^1\cong\mathbb Z^n\) and \(H^3\cong\mathbb Z^{B_n}\), with no torsion.

**6. Apply integral combinatorial Alexander duality.** For a complex on \(2n\) vertices, the standard duality isomorphism reads
\[
\widetilde H_j(\Delta_3(G_n);\mathbb Z)
\cong\widetilde H^{2n-j-3}(\Delta_3(G_n)^*;\mathbb Z).
\]
The degrees three and one on the right correspond exactly to \(j=2n-6\) and \(j=2n-4\) on the left, proving the full integral homology formula including torsion-freeness.

**7. Dimension, skeleton, and non-shellability.** Every disconnected triple yields a facet of cardinality \(2n-3\), so \(\Delta_3(G_n)\) is pure of dimension \(2n-4\). Every subset whose complement has at least five vertices is a face, because among any five vertices of a bipartite graph at least three lie in one independent part, giving a disconnected triple. Hence the complete \((2n-6)\)-skeleton lies in the cut complex. Since \(B_n>0\), homology in degree \(2n-6\) is nonzero, two dimensions below the facets. A pure shellable complex has reduced homology only in its top dimension, so this cut complex is not shellable.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and no third-party dependencies. The checker starts from the crown adjacency relation, independently enumerates all disconnected triples, constructs the cut complex and its Alexander dual, and separately constructs the two-row chessboard complex. It confirms the dual decomposition, all four face-count formulas, and mod-two boundary ranks for \(n=5,6,7\); it separately computes all reduced mod-two cut-complex boundary ranks for \(n=5,6\). The result is `VERIFY_OK cases=5`. These finite calculations check definitions and arithmetic but do not establish the all-\(n\) statement or torsion-freeness; the proof above uses the published shellability theorem plus integral Alexander duality for those conclusions.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue [1] introduce ordinary cut complexes and determine their topology for complete bipartite and complete multipartite graphs, cycles, trees, and clique prisms. Their complete-bipartite theorem gives, for \(n\ge5\), homology of \(\Delta_3(K_{n,n})\) concentrated in degree \(2n-6\) with rank \(\binom{n-1}{2}^2\). **Deleting one perfect matching changes this picture:** the crown complex has rank \(B_n\) in that degree and creates an additional \(n\) integral top-dimensional classes in degree \(2n-4\).

The shellability and homotopy concentration of \(X_n\) are prior results of Jojić, Vrećica and Živaljević [2], here used directly. The new mathematical step is the exact Alexander-dual identification of the crown cut complex with that chessboard complex **plus \(n\) exceptional edges**, which produces the two-degree integral classification. The sequel [3] addresses disjoint unions, squared paths, grids and related representation formulas, not crown graphs. Existing ordinary three-cut counterexamples on other individual graphs do not imply these exact ranks for the crown family.

## Limitations
The theorem covers \(n\ge5\) only; the shellability theorem invoked above has precisely that range. It does not determine the integral homotopy type of the original cut complex, possible nontrivial attaching operations between its two nonzero homology degrees, or its full symmetry representation. Free homology in two separated degrees alone does **not** justify a wedge-of-spheres claim for that cut complex. The role of unindexed equivalent treatments of crown graphs or alternate dual descriptions remains a bibliographic risk. The calculations in the verifier are finite mod-two checks, not a substitute for the integral proof.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first publicly posted 2023-04-26), especially Definition 2.1, the introductory classification table, and Theorems 7.4 and 7.18. https://arxiv.org/abs/2304.13675

[2] D. Jojić, S. T. Vrećica and R. T. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386 (2014), especially the multiple-chessboard definition and Theorem 4.4 with proof. https://arxiv.org/abs/1412.0386

[3] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted 2024-07-11), especially Sections 1, 3, 5 and 6. https://arxiv.org/abs/2407.08158
