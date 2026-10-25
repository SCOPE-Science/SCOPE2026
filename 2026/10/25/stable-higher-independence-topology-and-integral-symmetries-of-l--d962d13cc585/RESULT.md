# Stable higher-independence topology and integral symmetries of long-arm spider trees

## Finding

Let \(T=T(\ell_1,\ldots,\ell_b)\) have a common central vertex \(c\) and \(b\ge3\) pairwise disjoint arms \(c-v_{i,1}-\cdots-v_{i,\ell_i}\), each of edge length \(\ell_i\ge3\). For an integer \(r\ge L=\max_i\ell_i\), let \(\operatorname{Ind}_r(T)\) consist of the vertex subsets whose induced connected components have at most \(r\) vertices. Set
\[
N=\sum_{i=1}^b(\ell_i-1),\qquad t=r-N-1.
\]
Then
\[
|\operatorname{Ind}_r(T)|\simeq
\begin{cases}
\displaystyle\bigvee^{\binom{b-1}{t}}S^{r-1},&0\le t\le b-1,\\
\text{a point},&t<0\ \text{or}\ t\ge b.
\end{cases}
\]
This is an integral homotopy classification. In particular, for fixed \(b\) and \(N\), the stable-range homotopy type is independent of the individual arm lengths. The only possible nonzero reduced integral homology group is in degree \(r-1\), and it is free.

The full graph automorphism group is \(G=\prod_{d\ge3}S_{m_d}\), where \(m_d=|\{i:\ell_i=d\}|\). Write \(J=\{v_{i,j}:1\le j<\ell_i\}\) for the \(N\) interior arm vertices, \(Z=\{v_{i,\ell_i}:1\le i\le b\}\) for its \(b\) leaves, and
\[
U_Z=\ker\bigl(\mathbb Z^Z\xrightarrow{\sum}\mathbb Z\bigr).
\]
In the noncontractible range, the natural integral action is
\[
\widetilde H_{r-1}(\operatorname{Ind}_r(T);\mathbb Z)
\cong_{\mathbb Z[G]}
\det(\mathbb Z^J)\otimes_{\mathbb Z}\bigwedge^t U_Z.
\]
Here \(\det(\mathbb Z^J)=\bigwedge^N\mathbb Z^J\) is the orientation-sign line for permutation of the interior vertices. For equal arm length \(\ell\), the first factor is \(\operatorname{sgn}^{\ell-1}\), exhibiting a parity change between odd and even arm lengths.

## Assumptions and scope

The graph is a finite simple tree with one vertex of degree \(b\ge3\), all other vertices of degree at most two, and every arm length at least three. The parameter \(r\) is an integer at least the maximum arm length; no assertion is made for smaller \(r\). An empty wedge is interpreted as a contractible point. All homology is ordinary reduced simplicial homology over \(\mathbb Z\); the displayed homotopy equivalences are nonequivariant, whereas the homology isomorphism is equivariant over the integers. The short-arm family with every arm of length two, and two-arm graphs (ordinary paths), are outside the novelty scope.

## Proof

**1. A simplex deletion and a hub link.** Let \(K=\operatorname{Ind}_r(T)\), \(D=\operatorname{del}_c K\), and \(L=\operatorname{lk}_c K\). Every connected component of an induced subgraph not containing \(c\) lies in a single arm and has at most \(\ell_i\le r\) vertices. Hence \(D\) is the full simplex on \(J\sqcup Z\). The decomposition \(K=D\cup(c*L)\), with intersection \(L\), implies \(|K|\simeq\Sigma|L|\). The corresponding Mayer–Vietoris connecting isomorphism on positive reduced homology is natural for permutations of the arms, since both cones and their intersection are preserved by \(G\).

**2. A collapsible part of the link.** Let \(A\subset L\) be all faces that omit at least one vertex of \(J\). This is a \(G\)-invariant simplicial subcomplex. Map a face \(F\in A\) to \(F\cap J\), an order-preserving map to the Boolean poset of proper subsets of \(J\). For any fixed value \(M=F\cap J\ne J\), choose the least arm index \(i\) for which \(M\) omits some interior vertex of that arm. Toggle its terminal leaf \(z_i=v_{i,\ell_i}\). In every face in this fiber, a missing interior vertex separates \(z_i\) from \(c\); the tail component containing \(z_i\) is no larger than \(\ell_i-1\le r\), so either toggle remains a face. The fixed-fiber matching is a complete, acyclic Boolean toggle matching. The patchwork lemma for acyclic matchings applied to the order-preserving map makes their union acyclic. On the nonempty face poset, exactly one vertex is left critical (the leaf paired with the empty face in the augmented matching). Thus \(A\) is contractible.

**3. The remaining critical faces.** A face \(F\in L\setminus A\) contains every interior vertex \(J\), and is uniquely \(J\cup S\) for some \(S\subseteq Z\). Because the central induced component is now connected, it has \(1+N+|S|\) vertices; hence the condition is exactly \(|S|\le t\). If \(t<0\), there are no such faces and the first matching contracts \(L\). If \(t\ge b\), toggle \(z_1\) on every \(M=J\) fiber face, giving no additional critical cells. If \(0\le t\le b-1\), toggle \(z_1\) on faces \(J\cup S\) with \(z_1\notin S\) and \(|S|<t\). The unpaired faces are precisely
\[
J\cup S,\qquad S\subseteq Z\setminus\{z_1\},\quad |S|=t.
\]
There are \(\binom{b-1}{t}\) such faces, all of dimension \(N+t-1=r-2\). Matching each fiber of the map \(F\mapsto F\cap J\) is acyclic, and patchwork is acyclic globally. Together with the single critical vertex, the entire link has an acyclic matching with cells in dimensions \(0\) and \(r-2\) only. Since \(r-2\ge N-1\ge5\), the reduced Morse CW complex is a wedge of \(\binom{b-1}{t}\) spheres \(S^{r-2}\), or a point when that number is zero. Suspending proves the homotopy formula.

**4. Integral equivariance.** The contractible subcomplex \(A\) is invariant under \(G\); hence \(\widetilde H_*(L;\mathbb Z)\cong H_*(L,A;\mathbb Z)\) as integral \(G\)-modules. Give the vertices of \(J\) a fixed order before the leaves. The relative chain group in degree \(N+s-1\) is
\[
C_{N+s-1}(L,A;\mathbb Z)
\cong \det(\mathbb Z^J)\otimes\bigwedge^s\mathbb Z^Z,
\qquad 0\le s\le t,
\]
with differential \((-1)^N\) times contraction by the all-ones functional \(\varepsilon:\mathbb Z^Z\to\mathbb Z\). When a face loses an interior vertex it enters \(A\), so those boundary terms are zero in the relative complex. Since \(\varepsilon\) has an integral splitting (choose any one leaf), the contraction complex is exact below the top degree, and its top kernel is canonically \(\bigwedge^t\ker\varepsilon=\bigwedge^t U_Z\). The construction and the kernel identification commute with every permutation preserving arm lengths. The Mayer–Vietoris connecting isomorphism shifts this integral module from degree \(r-2\) in \(L\) to degree \(r-1\) in \(K\), proving the stated action, torsion-freeness, and vanishing outside that degree. When \(t<0\) or \(t\ge b\), \(L\), hence \(K\), is contractible.

## Verification

`verify_spider.py` generates the actual graph adjacency lists and independently decides every admissible face by a breadth-first component test, rather than using the proof's face characterization. For \(b=3,4\), arm lengths in \(\{3,4,5\}\), total non-hub vertices at most \(12\), and all \(r\) in the tested stable range, it checked **158** full mod-two homology computations and explicit link matching acyclicity tests, and **576** integral signed-Lefschetz trace comparisons for length-preserving arm permutations. All tests passed. The script checks all Hasse cover relations when verifying matching acyclicity. Execute with `python3 verify_spider.py`; Python's standard library suffices. These bounded tests corroborate but do not replace the all-parameter proof.

For example, for arm lengths \((3,4,5)\), \(N=9\); the complexes are contractible for \(5\le r\le9\) and \(r\ge13\), and for \(r=10,11,12\) are respectively \(S^9\), \(S^{10}\vee S^{10}\), and \(S^{11}\). Equal-length arms of odd versus even length give opposite integral orientation twists.

## Relationship to prior work

Deshpande–Singh (2020/2021), Theorems 3.8 and 3.10, compute higher-independence homotopy types of fully whiskered graphs and graphs in which **every non-leaf vertex has an adjacent leaf**; the present long-arm spiders violate that hypothesis. Their path theorem concerns only the excluded two-arm case. Ghosh–Selvaraja (2025) establish shellability/chordality criteria for broad graph families without these stable-range ranks or integral symmetry modules. Sawant (2026) proves vertex decomposability for the higher-independence complex of **every tree**, which ensures general topological regularity but does not determine these binomial multiplicities, the sharp stable-range transition, or the integral automorphism action. The excluded two-edge-arm case is not presented as new.

## Limitations

The theorem does not classify arbitrary trees, lower parameters \(r<L\), or cases with fewer than three arms. Its displayed wedge homotopy equivalence is not claimed equivariant; only the integral homology representation is computed equivariantly. While targeted primary-source and mathematical-record comparisons did not locate an equivalent long-arm formula, an unindexed equivalent formulation in the graph-complex literature remains possible. The finite verifier is not a proof of unbounded cases, and no independent scientific audit has been performed.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees* (2026), arXiv:2605.25150v1, https://arxiv.org/abs/2605.25150. First publicly available 2026-05-24 (UTC).
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types* (2020/2021), arXiv:2001.05448, Theorems 3.8, 3.10, https://arxiv.org/abs/2001.05448.
3. Arka Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes* (first posted 2025), arXiv:2505.06614, https://arxiv.org/abs/2505.06614.
