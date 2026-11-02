# Sharp \(\ell_1\) distortion and regular-cut rigidity for \(K_n\times K_n\)

## Finding
For every integer \(n\ge3\), let \(G_n=K_n\times K_n\) denote the **categorical (tensor) graph product**, not the Cartesian product: its vertices are ordered pairs \((i,j)\in[n]^2\), with distinct vertices adjacent precisely when both coordinates differ. Give every edge length one and use the shortest-path metric \(d_n\). Its least distortion into real \(\ell_1\) is
\[
\boxed{c_{\ell_1}(G_n)=\frac{2(n-2)}{n-1}=2-\frac2{n-1}.}
\]
The result includes two rigidity statements. After scaling any optimal embedding to be noncontracting, its image distances are **exactly** \(2\) for pairs agreeing in one coordinate and **exactly** \(2(n-2)/(n-1)\) for pairs differing in both coordinates. Moreover, in any nonnegative cut decomposition of the induced optimal \(\ell_1\) metric, each cut with positive coefficient (other than trivial zero cuts) has exactly \(k\) selected cells in every row and every column for an integer \(1\le k\le n-1\). Equivalently, every supporting cut is the incidence matrix of a nonempty proper regular bipartite graph on two parts of size \(n\).

The case \(n=3\) is isometrically embeddable; for \(n\ge4\) the optimal distortion is strictly greater than one and increases strictly to two.

## Assumptions and scope
The metric is finite, unweighted, and undirected. Throughout, \(n\) is an integer with \(n\ge3\), and \(\ell_1\) is a real normed space (finite-dimensional or countably infinite dimensional). The distortion of an injective map \(f\) is
\[
\operatorname{dist}(f)=
\left(\max_{x\ne y}\frac{\|f(x)-f(y)\|_1}{d_n(x,y)}\right)
\left(\max_{x\ne y}\frac{d_n(x,y)}{\|f(x)-f(y)\|_1}\right).
\]
A positive rescaling lets us assume \(d_n(x,y)\le\|f(x)-f(y)\|_1\le Dd_n(x,y)\). The claimed value is the infimum of \(D\) over such embeddings.

The graph has diameter two: if both coordinates differ, vertices are adjacent; if exactly one coordinate agrees, choose an intermediate vertex differing from both coordinates in the other position (possible because \(n\ge3\)), obtaining a path of length two. Thus the distance is one on the different-row-and-column pairs, and two on the two same-coordinate classes.

## Proof
**1. Cut decomposition.** For any finite set \(X\), each real \(\ell_1\) distance on \(X\) is a nonnegative combination of cut semimetrics \(\delta_S(x,y)=|\mathbf1_S(x)-\mathbf1_S(y)|\). Indeed, for each scalar coordinate \(g\), the identity \(|g(x)-g(y)|=\int_{\mathbb R}|\mathbf1_{g(x)>t}-\mathbf1_{g(y)>t}|\,dt\) gives the decomposition; sum/integrate over coordinates. Since \(X\) is finite, these contributions can be consolidated into finitely many cut coefficients. No sign assumptions on \(f\) are needed.

**2. Exact balance certificate.** Fix an arbitrary cut \(S\subseteq[n]^2\). Let \(K=|S|\). Write \(r_i=|S\cap(\{i\}\times[n])|\) and \(s_j=|S\cap([n]\times\{j\})|\). Set
\[
T=K(n^2-K),\quad U=\sum_i r_i(n-r_i),\quad V=\sum_j s_j(n-s_j),\quad W=T-U-V.
\]
Here \(T\) counts all unordered pairs separated by the cut, \(U\) counts separated pairs in the same row, \(V\) those in the same column, and \(W\) those in different rows and different columns. These classes partition all unordered vertex pairs. In particular \(W\ge0\).

Let \(A_S\), \(B_S\), and \(C_S\) be the average values of \(\delta_S\) on, respectively, the same-row class, same-column class, and different-row-and-column class. Counting their pair populations gives
\[
 A_S=\frac{2U}{n^2(n-1)},\quad
 B_S=\frac{2V}{n^2(n-1)},\quad
 C_S=\frac{2W}{n^2(n-1)^2}.
\]
The following **sum-of-squares identity** holds exactly:
\[
\boxed{\;2(n-1)C_S-(n-2)(A_S+B_S)
=\frac{2}{n(n-1)}
\left(\sum_i(r_i-K/n)^2+\sum_j(s_j-K/n)^2\right).\;}
\]
To verify it, multiply the left-hand side by \(n^2(n-1)/2\), obtaining \(2T-n(U+V)\). Since \(\sum_i r_i=\sum_j s_j=K\), this is
\[
2T-n(U+V)=n\sum_i(r_i-K/n)^2+n\sum_j(s_j-K/n)^2.
\]
The right-hand side of the boxed identity follows by division. Consequently
\[
 (n-2)(A_S+B_S)\le2(n-1)C_S.
\]
Equality holds precisely when every row sum and every column sum is the same constant \(K/n\). For a nontrivial cut, this common value is an integer \(k\in\{1,\ldots,n-1\}\). Thus equality cuts are exactly nontrivial \(k\)-regular bipartite incidence matrices (and the two trivial constant cuts).

**3. Lower bound.** Apply the preceding inequality to every cut in a nonnegative decomposition of the metric induced by a noncontracting embedding. With \(A,B,C\) denoting averages of that metric over the same three pair classes, linearity yields
\[
 (n-2)(A+B)\le2(n-1)C.
\]
The shortest-path distances give \(A\ge2\), \(B\ge2\), and \(C\le D\). Therefore
\[
4(n-2)\le2(n-1)D,\quad\text{hence}\quad D\ge\frac{2(n-2)}{n-1}.
\]
For \(n=3\), this already gives the universal lower bound one; for larger \(n\), it is strictly stronger.

**4. Matching-cut embedding.** Index coordinates by all permutations \(\pi\in S_n\), and define
\[
 f_n(i,j)_\pi=\frac{n}{n!}\,\mathbf1_{\{\pi(i)=j\}}.
\]
Each coordinate represents a cut comprising the \(n\) cells of a perfect matching. For distinct cells in a common row or column, the two indicators cannot both equal one and exactly one equals one for a uniformly random permutation with probability \(2/n\). For cells with both coordinates different, the two indicators equal one simultaneously with probability \(1/[n(n-1)]\), so their separation probability is \(2/n-2/[n(n-1)]\). Summation with the factor \(n\) yields respectively
\[
 \|f_n(i,j)-f_n(i',j')\|_1=
 \begin{cases}
 2,&i=i'\text{ or }j=j',\quad (i,j)\ne(i',j'),\\
 2(n-2)/(n-1),&i\ne i',\ j\ne j'.
 \end{cases}
\]
Because \(2(n-2)/(n-1)\ge1\) for \(n\ge3\), this embedding is noncontracting with maximum stretch exactly \(2(n-2)/(n-1)\). It attains the lower bound.

**5. Rigidity at the optimum.** For any optimal noncontracting embedding, the lower-bound chain is an equality. Hence \(A=B=2\) and \(C=2(n-2)/(n-1)\). Every pair in the first two classes has image distance at least two, so equality of each class average forces **every** such distance to equal two. Every transverse pair has image distance at most the optimum, so its class average similarly forces every transverse distance to equal the optimum. Finally, the sum-of-squares gap for the induced metric vanishes. In its nonnegative cut decomposition, every positive-weight cut must have zero individual gap; by step 2 it is a nontrivial regular bipartite incidence cut, up to a zero semimetric. This applies to any decomposition, not only to the exhibited permutation construction.

## Verification
The accompanying standalone `check.py` uses only exact integers and rational numbers. It independently constructs the graph and breadth-first distances for \(n=3,\ldots,8\), exhausts all \(2^{n^2}\) cut masks for \(n=3,4\), checks randomly sampled cut masks and perfect-matching masks for \(n=5,\ldots,12\), and enumerates every embedding coordinate and every vertex pair for \(n=3,\ldots,6\). It verifies the integer multiple of the boxed sum-of-squares identity, the equality-cut condition, the exact distance classes, and the exact embedding distances. The observed run completed successfully with `CHECK_OK` and category counts of 8755 distance comparisons, 80088 cut-certificate checks, and 1086 embedding-pair checks. These are supplementary finite checks; the proof above is uniform in all \(n\ge3\).

## Relationship to prior work
Abraham, Filtser, Gupta, and Neiman study low-distortion embeddings of graph shortest-path metrics into \(\ell_p\), proving bounds controlled by shortest-path decomposition depth. Their main results are general estimates, not the exact distortion of this tensor product. Wang, Li, and Wang study preservation of isometric \(\ell_1\)-embeddability under gate-sums of graphs, not optimal distortion for tensor products. The qualitative literature on complementary \(\ell_1\)-graphs is additionally relevant to the isometric boundary at \(n=3\), but a qualitative classification alone does not determine the explicit nonisometric distortion for \(n\ge4\).

This graph is the complement of the rook (lattice) graph on an \(n\times n\) board. That is distinct from the two-subset Kneser graph (unordered edges of a complete graph) and from a complete bipartite graph metric (vertices are the original part vertices). The main novelty claim concerns the all-size sharp distortion and the equality-cut and optimal-metric rigidity for this particular **ordered-pair** metric; it is not a claim about all tensor products, arbitrary rectangular boards, or general edge-weighted metrics.

## Limitations
The result assumes equal numbers of rows and columns, simple unweighted graphs, and real \(\ell_1\) as the target. The same argument does not directly supply the exact distortion for unequal rectangular products \(K_m\times K_n\). No claim is made about the smallest dimension of an optimal embedding. Historical priority is subject to independent confirmation, especially against older work on complementary \(\ell_1\)-graphs and cut-cone inequalities under different names.

## References
1. I. Abraham, A. Filtser, A. Gupta, O. Neiman, *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073 (first posted 2017-08-14), https://arxiv.org/abs/1708.04073 .
2. G. Wang, C. Li, F. Wang, *\(\ell_1\)-Embeddability Under Gate-Sum Operation of Two \(\ell_1\)-Graphs*, Frontiers in Physics 8, article 146 (2020-06-04), https://doi.org/10.3389/fphy.2020.00146 .
3. S. Shpectorov, *Complementary \(\ell_1\)-graphs*, Discrete Mathematics (1998), DOI 10.1016/S0012-365X(98)0007X-1 (bibliographic metadata reviewed; full text not verified).
