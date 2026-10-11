# Laplacian spectrum and tree complexity of complete-bipartite symmetric edge polytopes

## Finding

For integers \(p,q\ge2\), let
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_{p+j}):1\le i\le p,\ 1\le j\le q\}\subset\mathbb R^{p+q},
\]
and let \(G_{p,q}\) denote its unweighted one-skeleton. The graph \(G_{p,q}\) has \(2pq\) vertices and is \((pq-1)\)-regular. It is the signed two-lift of the complete graph \(K_{pq}\): two grid positions have same-sign adjacency exactly when they share one coordinate, and opposite-sign adjacency exactly when they differ in both coordinates.

Its **complete** combinatorial Laplacian characteristic polynomial is
\[
\begin{aligned}
\det(tI-L_{p,q})={}&t(t-pq)^{pq-1}
\bigl[t-2(p-1)(q-1)\bigr]\\
&\cdot\bigl[t-(p(q-2)+2)\bigr]^{q-1}
\bigl[t-(q(p-2)+2)\bigr]^{p-1}\\
&\cdot(t-pq-2)^{(p-1)(q-1)}.
\end{aligned}
\]
The expression has degree \(2pq\); when eigenvalues coincide their multiplicities add. The number of (unweighted, undirected) spanning trees of the **polytope's graph**, not of its defining complete bipartite graph, is
\[
\boxed{\tau(G_{p,q})=(p-1)(q-1)(pq)^{pq-2}
[p(q-2)+2]^{q-1}[q(p-2)+2]^{p-1}(pq+2)^{(p-1)(q-1)}.}
\]
The algebraic connectivity and its multiplicity are
\[
\boxed{\lambda_2(G_{p,q})=pq-2\max\{p,q\}+2},\qquad
\operatorname{mult}(\lambda_2)=
\begin{cases}
\min\{p,q\}-1,&p\ne q,\\
2(p-1),&p=q\ge3,\\
3,&p=q=2.
\end{cases}
\]
Hence the spectral gap is \(2\) for every \(p=2\), even when \(q\) grows without bound, whereas balanced partitions have a growing gap.

## Assumptions and scope

The labels \(i\in[p]\), \(j\in[q]\), and \(\varepsilon\in\{+1,-1\}\) index vertices \(v^\varepsilon_{ij}=\varepsilon(e_i-e_{p+j})\). The ambient hyperplane has coordinate sum zero; all edge adjacency and all spectra are independent of the choice of Euclidean realization within that hyperplane. The graph Laplacian is \(L=D-A\), with unit weights and each unordered edge counted once. The family assumes \(p,q\ge2\); the star boundary \(p=1\) or \(q=1\) is not included.

## Proof

**Vertices and adjacency.** The linear functional assigning value \(1\) to coordinate \(i\), value \(-1\) to coordinate \(p+j\), and zero to other coordinates uniquely maximizes at \(v^+_{ij}\), and negation treats \(v^-_{ij}\). Thus all \(2pq\) displayed points are vertices. The functional \(x\mapsto\sum_{i=1}^p x_i\) has maximum \(1\) precisely on the positive vertices and minimum \(-1\) on the negative vertices. These opposing facets are products \(\Delta_{p-1}\times\Delta_{q-1}\), so two same-sign vertices are joined by an edge exactly when they share exactly one of their grid coordinates.

A supporting functional has the form \(\ell(x)=\sum_i\alpha_i x_i+\sum_j\beta_j x_{p+j}\). For an opposite-sign pair \(v^+_{ij},v^-_{kl}\) to constitute exactly its maximizing face, \(i\) must be the **unique maximum** of \(\alpha\) and \(k\) the **unique minimum**, while \(j\) must be the **unique minimum** of \(\beta\) and \(l\) the **unique maximum**. Hence \(i\ne k\) and \(j\ne l\). Conversely, when both inequalities hold choose \(\alpha_i=1\), \(\alpha_k=-1\), \(\beta_j=-1\), \(\beta_l=1\), all other potential entries zero. This exposes precisely those two vertices, each of value \(2\); every other vertex has lower value. Therefore opposite-sign edges occur exactly when both coordinates differ. There are \((p-1)+(q-1)+(p-1)(q-1)=pq-1\) neighbors at each vertex.

**Spectral blocks.** Set \(R=(J_p-I_p)\otimes I_q+I_p\otimes(J_q-I_q)\), and \(S=(J_p-I_p)\otimes(J_q-I_q)\). Ordering all positive labels followed by their negative copies, the adjacency matrix is
\[
A=\begin{pmatrix}R&S\\S&R\end{pmatrix}.
\]
The even/odd subspaces \((x,x)\), \((x,-x)\) each have dimension \(pq\) and exhaust the space. In the even subspace, \(R+S=J_{pq}-I_{pq}\), giving Laplacian eigenvalues \(0\) once and \(pq\) with multiplicity \(pq-1\).

Write \(B_p=J_p-I_p\), \(B_q=J_q-I_q\). In the odd subspace the adjacency is \(B_p\otimes I_q+I_p\otimes B_q-B_p\otimes B_q\). The two eigenvalues of \(B_p\) are \(p-1\) on constants (dimension \(1\)) and \(-1\) on their orthogonal complement (dimension \(p-1\)); similarly for \(B_q\). Thus a tensor eigenvector with \(B_p\)-eigenvalue \(a\) and \(B_q\)-eigenvalue \(b\) has Laplacian eigenvalue \(pq-1-a-b+ab\), giving exactly

| \((a,b)\) | Laplacian eigenvalue | Multiplicity |
|---|---|---|
| \((p-1,q-1)\) | \(2(p-1)(q-1)\) | \(1\) |
| \((p-1,-1)\) | \(p(q-2)+2\) | \(q-1\) |
| \((-1,q-1)\) | \(q(p-2)+2\) | \(p-1\) |
| \((-1,-1)\) | \(pq+2\) | \((p-1)(q-1)\) |

All odd-block eigenvalues are positive for \(p,q\ge2\). The resulting eigenvalues, together with the even block, give the characteristic polynomial and show graph connectivity.

**Trees and the Fiedler eigenspace.** By Kirchhoff's matrix-tree theorem, the product of all \(2pq-1\) nonzero Laplacian eigenvalues divided by \(2pq\) is the tree count displayed above. Suppose \(p\ge q\). Among the two nonconstant odd tensor eigenvalues, \(p(q-2)+2\) is the smaller; its gap to \(q(p-2)+2\) is \(2(p-q)\). The difference between the constant odd eigenvalue and \(p(q-2)+2\) is \(q(p-2)\ge0\), with equality only at \(p=q=2\). The remaining values \(pq\) and \(pq+2\) are strictly larger. This proves the claimed Fiedler formula and, by counting any coinciding tensor components, the stated multiplicities. Interchange \(p,q\) for the other order. No asymptotic or finite-census inference is needed.

## Verification

Running `python3 verify.py` requires SymPy. It constructs the graph from the geometric adjacency criterion and checks exact characteristic polynomials and Kirchhoff cofactors for the ten parameter pairs with \(2\le p,q\le5\) and \(2pq\le24\). For all sixteen pairs with \(2\le p,q\le5\), it checks exact eigenvalue multiplicity sums, trace sums, and the gap formula. If NumPy and SciPy are installed, an additional, logically independent linear-programming support-face test checks 313 vertex pairs in dimensions corresponding to \((p,q)\in\{(2,2),(2,3),(3,2),(3,3)\}\); these feasibility tests are numerical only. The symbolic proof, not the finite calculations, establishes every parameter case. The initial case \(p=q=2\) gives the cubical spectrum \(\{0,2^{(3)},4^{(3)},6\}\) and exactly \(384\) spanning trees.

## Relationship to prior work

Higashitani, Jochemko, and Michałek compute the \(h^*\)-polynomial and facet structure of the same symmetric edge polytope family of complete bipartite graphs [1]. D'Alì, Delucchi, and Michałek investigate these polytopes as adjacency/Kantorovich–Rubinstein polytopes and detail their geometric face structure, including the cubic \(K_{2,2}\) example [2]. Chen, Davis, and Korchevskaia analyze the graph-to-face correspondence [3], while Kálmán and Tóthmérész study spanning-tree dissections of these and related graph polytopes [4]. Their spanning trees are subgraphs of the **defining graph**, rather than the spanning trees counted here in the one-skeleton of its polytope. Bilu and Linial's general signed two-lift spectral lemma [5] explains the even/odd spectral method; it does not identify the specific polytope one-skeleton or evaluate its spectrum. The graph-structure identification plus the full parameter-dependent spectral evaluation is the present contribution.

## Limitations

The analysis concerns the **unweighted graph** of the polytope, not its Euclidean edge lengths, polytope volume, \(h^*\)-vector, or the spanning trees of \(K_{p,q}\). It excludes \(p=1\) and \(q=1\). All eigenvalues and multiplicities count algebraic multiplicity and coincide when parameters force equality. An equivalent formulation under two-cover, Seidel-switching, adjacency-polytope, or graph-spectrum terminology is a residual literature risk; no independent external audit of novelty or proof has been performed.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public 2018-07-20, Sections 3–4.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public 2019-10-11, Sections 2 and 4; primary MSC 52B20.
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, Theorem 3 and Sections 4–5.
4. T. Kálmán, L. Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127, first public 2022-03-31; primary MSC 52B20.
5. Y. Bilu, N. Linial, *Constructing expander graphs by 2-lifts and discrepancy vs. spectral gap*, arXiv:math/0312022, Lemma 3.1.
