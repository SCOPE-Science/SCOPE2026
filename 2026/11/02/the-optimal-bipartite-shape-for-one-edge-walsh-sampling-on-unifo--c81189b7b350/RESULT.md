# The optimal bipartite shape for one-edge Walsh sampling on uniform spanning trees

## Finding
Let \(2\le a\le b\), put \(n=a+b\), \(m=ab\), and sample uniformly from the spanning trees \(T\) of the labelled complete bipartite graph \(K_{a,b}\). On this probability space take \(\chi_\varnothing(T)=1\) and \(\chi_e(T)=(-1)^{\mathbf 1_{\{e\in T\}}}\) for each of the \(m\) edges. The probability-normalized Gram matrix \(G_{a,b}\) has the **complete spectrum**, with exponents denoting multiplicities,
\[
\begin{split}
\operatorname{spec}(G_{a,b})=\biggl\{&0^{[1]},\quad
\left(1+\frac{[m-2(n-1)]^2}{m}\right)^{[1]},\\
&\left(\frac{4(b-1)}m\right)^{[a-1]},\quad
\left(\frac{4(a-1)}m\right)^{[b-1]},\quad
\left(\frac{4(n-3)}m\right)^{[(a-1)(b-1)]}\biggr\}.
\end{split}
\]
When numerical eigenvalues coincide, their displayed multiplicities add. The only function relation is
\[
\sum_{e\in E(K_{a,b})}\chi_e=\bigl(m-2(n-1)\bigr)\chi_\varnothing.
\]
In particular, the evaluation rank is exactly \(m\). Let \(\kappa_{a,b}^2\) denote the ratio of the largest to the smallest **positive** Gram eigenvalue (the squared nonzero-singular-value condition number). Then
\[
\boxed{\kappa_{a,b}^2=\max\left\{
\frac{m+[m-2(n-1)]^2}{4(a-1)},\frac{n-3}{a-1}
\right\}.}
\]

For every fixed vertex order \(n\ge4\), minimizing this condition number over all complete bipartite graphs with both sides at least two yields the following **complete and sharp shape classification**, unique up to exchanging the sides except for the displayed tie:

| Vertex order | Minimizing unordered side sizes | Minimum \(\kappa^2\) |
| --- | --- | --- |
| \(n=4\) | \((2,2)\) | \(2\) |
| \(n=5\) | \((2,3)\) | \(5/2\) |
| \(n=6\) | \((3,3)\) | \(3/2\) |
| \(n=7\) | \((3,4)\) | \(2\) |
| \(n=8\) | \((4,4)\) | \(5/3\) |
| \(n=9\) | \((3,6)\) and \((4,5)\) | \(3\) |
| \(10\le n\le14\) | \((3,n-3)\) | \((n^2-11n+40)/8\) |
| \(n\ge15\) | \((2,n-2)\) | \(n-3\) |

Hence the design optimum changes from balanced to moderately unbalanced and finally to the thinnest permitted bipartition. On even orders, a balanced bipartition has \(\kappa^2=n^3/32+O(n^2)\), compared with the sharp minimum \(n-3\) for \(n\ge16\).

## Assumptions and scope
Graphs are simple, labelled, undirected, unweighted complete bipartite graphs, with both part sizes at least two. Every spanning tree is equally likely. The coordinate Walsh functions are real, take values \(\pm1\), and are normalized by the probability measure (not by counting measure). The Gram matrix indexes one constant plus all edge coordinates, so it has size \((m+1)\times(m+1)\). Since the spanning-tree size is fixed, its single zero eigenvalue is removed when defining the condition number. The comparison holds for a fixed **number of vertices**; the numbers of available edge coordinates vary with the bipartition.

## Proof
**1. The transfer-current projection and pair covariances.** Orient all edges from the size-\(a\) part toward the size-\(b\) part. Regard edge arrays as \(a\)-by-\(b\) real matrices. The cut space is the space of arrays \(u_i+v_j\), of dimension \(n-1\). Its orthogonal projection has matrix entries
\[
P_{(i,j),(k,l)}=\frac{\mathbf1_{\{i=k\}}}{b}+\frac{\mathbf1_{\{j=l\}}}{a}-\frac1{ab}.
\]
Indeed, \(P\) sends any matrix to its row mean plus column mean minus grand mean, an orthogonal projection onto precisely this cut space. By the finite-graph transfer-current determinantal theorem, the uniform spanning-tree edge indicators \(X_{ij}=\mathbf1_{\{(i,j)\in T\}}\) satisfy
\[
\mathbb E X_{ij}=P_{(i,j),(i,j)}=p:=\frac{n-1}{m},\qquad
\operatorname{Cov}(X_e,X_f)=-P_{e,f}^2\quad(e\ne f).
\]
The diagonal covariance is \(p(1-p)\). For two different edges sharing a vertex in the first part, the covariance is \(-(a-1)^2/m^2\); for those sharing a vertex in the second part, it is \(-(b-1)^2/m^2\); for disjoint edges, it is \(-1/m^2\). These four values completely specify the covariance matrix \(C\).

**2. Exact invariant-space diagonalization.** The coordinate edge space decomposes orthogonally as
\[
(\mathbf1_a\oplus\mathbf1_a^\perp)\otimes
(\mathbf1_b\oplus\mathbf1_b^\perp).
\]
The four tensor factors have dimensions \(1\), \(a-1\), \(b-1\), and \((a-1)(b-1)\). Substitution of the four covariance values from Step 1 shows that \(C\) is zero on the all-ones factor and has eigenvalues, respectively, \((b-1)/m\) on first-part contrasts, \((a-1)/m\) on second-part contrasts, and \((n-3)/m\) on doubly centered arrays. Each is strictly positive. The zero eigenvalue also follows directly from \(\sum_eX_e=n-1\) on every spanning tree.

Since \(\chi_e=1-2X_e\), every edge character has mean \(\mu=1-2(n-1)/m\), and the edge-character Gram block equals \(4C+\mu^2\mathbf1_m\mathbf1_m^{\mathsf T}\). The constant interacts only with the all-ones edge direction. Its two-dimensional block is
\[
\begin{pmatrix}1&\sqrt m\,\mu\\ \sqrt m\,\mu&m\mu^2\end{pmatrix},
\]
which has eigenvalues zero and \(1+m\mu^2\). The other three blocks have the asserted eigenvalues after multiplication by four. The covariance-positive blocks rule out all other relations.

**3. Sharp condition formula.** For \(a\le b\), the least positive eigenvalue is \(4(a-1)/m\): the other contrast eigenvalue and the doubly centered eigenvalue are no smaller, while \(1+m\mu^2\ge1\ge4(a-1)/m\). The maximal positive eigenvalue is \(\max\{1+m\mu^2,4(n-3)/m\}\); both contrast eigenvalues are bounded by the doubly centered one. Dividing gives the displayed formula, and also the equivalent representation
\[
\kappa_{a,b}^2=\max\left\{
\frac{m+[(a-2)(b-2)-2]^2}{4(a-1)},\frac{n-3}{a-1}\right\}.
\]

**4. Exact minimization for small orders.** For each integer \(4\le n\le15\), the only admissible pairs are \((a,n-a)\) with \(2\le a\le\lfloor n/2\rfloor\). Direct rational substitution into the previous exact formula gives the complete minimizer table above. This is an exhaustive finite algebraic calculation, not sampling or numerical approximation. The standalone verifier repeats every rational comparison; the entries at \(n=9\) are the only tied distinct shapes.

**5. Uniform exclusion of larger small sides.** For \(n\ge16\), \(4\le a\le b\), set \(m=ab\). From \((a-4)(b-4)\ge0\) we obtain \(m\ge4(n-4)\) and \((a-2)(b-2)-2\ge2n-14\). Moreover, \(4(a-1)\le2(n-2)\). Therefore
\[
\kappa_{a,b}^2\ge\frac{4(n-4)+(2n-14)^2}{2(n-2)}>n-3,
\]
where strictness is equivalent to \(n^2-21n+84>0\), valid for all integers \(n\ge16\). For the thin pair \((2,n-2)\), the exact formula gives \(\kappa^2=n-3\) when \(n\ge7\). For the other thin candidate \((3,n-3)\), the first branch of the maximum gives
\[
\kappa_{3,n-3}^2\ge\frac{n^2-11n+40}{8}>n-3
\quad(n\ge15),
\]
with strictness equivalent to \(n^2-19n+64>0\). Thus \((2,n-2)\) is the unique minimizer for every \(n\ge16\). The exact finite comparison already handles \(n=15\), completing the all-order classification.

**6. Asymptotic comparison.** For even \(n\), take \(a=b=n/2\) in the exact formula: \(m=n^2/4\), \(m-2(n-1)=n^2/4-2n+2\), and the first branch is \(n^3/32+O(n^2)\). The second branch remains bounded. The claimed asymptotic separation follows from the exact optimal value \(n-3\).

## Verification
Run `python verify.py` with Python 3.10 or newer; it has no third-party dependencies. The checker independently enumerates all **4,657 labelled spanning trees** of the six graphs \(K_{a,b}\) with \(2\le a\le b\le4\), computes their Gram matrices exactly with rational arithmetic, compares them entrywise to the transfer-current prediction, verifies all invariant-sector eigenvector equations and exact ranks, and checks the condition formula. It exhausts all candidate partitions for every integer \(4\le n\le15\), and tests the symbolic large-order lower-bound formula for \(16\le n\le200\). The entire infinite-range proof uses the algebraic inequalities of Step 5, not extrapolation from those finite checks.

## Relationship to prior work
The transfer-current determinantal theorem of Burton and Pemantle and its discrete-matroid formulation by Lyons are used as known inputs; this finding does **not** claim their discovery. The later formula of Dong and Ge counts spanning trees of complete bipartite graphs containing any prescribed forest, and therefore determines the one-edge and two-edge marginals underlying this construction. Their inspected statement and argument do not themselves provide the complete Walsh-frame Gram spectrum or solve the fixed-vertex-count condition-minimization problem. The new contribution is the exact spectral reconstruction invariant and its all-order optimizer transition, especially the reentrant optimum \((3,n-3)\) for intermediate orders and the eventual switch to \((2,n-2)\).

The published calculation of Minkowski asymmetry of complete-bipartite spanning-tree polytopes concerns a different convex-geometric invariant; its balancing anomaly neither gives this Gram spectrum nor implies the condition-number minimization. Likewise, existing Fourier sampling results for perfect matchings, Hamiltonian tours, and complete-graph spanning-tree quadratic characters concern different sampling domains or different degrees. A general unpublished or differently named treatment of covariance spectra could still overlap this result; absence from targeted searches is not a proof of absolute priority.

## Limitations
Only uniform spanning-tree sampling and the one-coordinate Walsh band are covered; no claim is made about nonuniform tree laws, all graph families, erasure robustness, or full higher-degree Fourier sampling. The positive-spectrum condition number explicitly quotients the single deterministic cardinality relation. While the optimization theorem is exact, its use as a comparison across graphs with different numbers of potential edges is a deliberate fixed-vertex-count design criterion. The literature comparison is bounded by sources actually inspected, and no independent priority determination or independent validation has been conducted.

## References
1. R. Lyons, “Determinantal probability measures,” arXiv:math/0204325 (first public 26 April 2002), *Publications Mathématiques de l'IHÉS* 98 (2003), 167–212. https://arxiv.org/abs/math/0204325
2. R. Burton and R. Pemantle, “Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances,” arXiv:math/0404048 (first public 2 April 2004), *Annals of Probability* 21 (1993), 1329–1371. https://arxiv.org/abs/math/0404048
3. F. Dong and J. Ge, “Counting spanning trees in a complete bipartite graph which contain a given spanning forest,” arXiv:2103.05294 (first public 9 March 2021), *Journal of Graph Theory* 101 (2022), 79–94. https://arxiv.org/html/2103.05294v2
4. “Balanced anomaly in the Minkowski asymmetry of complete-bipartite spanning-tree polytopes,” publicly available mathematical record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-balanced-anomaly-in-the-minkowski-asymmetry-of-complete-bipartit--d8f52c73c4c4
