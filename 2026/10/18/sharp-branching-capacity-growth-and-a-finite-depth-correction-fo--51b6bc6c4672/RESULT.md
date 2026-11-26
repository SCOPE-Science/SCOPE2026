# Sharp large-height norm of ancestor summation on complete branching trees

## Finding

Let \(b\ge2\) be an integer. On the complete rooted \(b\)-ary tree of height \(N\ge1\), associate each nonroot vertex with the edge entering it and use counting measure on the nonroot vertices. Define ancestor summation by
\[
(H_{b,N}g)(v)=\sum_{w\preceq v,\ w\ne o}g(w),\qquad v\ne o,
\]
where \(o\) is the root and the sum includes \(v\) itself. For each fixed \(1<p<\infty\),
\[
\lim_{N\to\infty}b^{-(N+1)/p}\|H_{b,N}\|_{\ell^p\to\ell^p}
=\big[(b-1)(b^{1/(p-1)}-1)^{p-1}\big]^{-1/p}.
\]
The radial edge data \(g(v)=b^{-|v|/(p-1)}\) attain this limit asymptotically. The new claim is the fixed-exponent norm equivalent across the range \(1<p<\infty\); the Hilbert instance is included for consistency with the spectral description, not claimed separately as original.

## Assumptions and scope

The tree includes all \(b^j\) vertices at depth \(j\) for \(0\le j\le N\). Inputs and outputs are indexed only by depths \(1,\ldots,N\), and the norms do not divide level masses by their sizes. Both \(b\) and \(p\) are fixed in the height limit. There is no claim at \(p=1,\infty\), for decaying vertex measures, or about uniform errors in \(b,p\).

## Proof

Let \(E_i=\sum_{|v|=i}|g(v)|^p\) and \(S_j=\sum_{i=1}^j b^{-i/(p-1)}\). Extending level-\(i\) data to their level-\(j\) descendants repeats each value exactly \(b^{j-i}\) times. Applying Minkowski to the sum of these extensions and then Hölder gives
\[
\left(\sum_{|v|=j}|(H_{b,N}g)(v)|^p\right)^{1/p}
\le b^{j/p}\sum_{i=1}^j b^{-i/p}E_i^{1/p}
\le b^{j/p}S_j^{(p-1)/p}\left(\sum_{i=1}^jE_i\right)^{1/p}.
\]
Summing over output depths gives an upper bound on the \(p\)-th power of the norm. For radial data \(g(v)=b^{-|v|/(p-1)}\), the input \(p\)-mass is \(S_N\) and the output on level \(j\) is the constant \(S_j\). Consequently
\[
\frac{\sum_{j=1}^N b^j S_j^p}{S_N}
\le \|H_{b,N}\|_{p\to p}^p
\le \sum_{j=1}^N b^j S_j^{p-1}.
\]
Here \(S_j\to S_\infty=(b^{1/(p-1)}-1)^{-1}\). For every \(s>0\), the sum \(b^{-(N+1)}\sum_{j=1}^N b^j S_j^s\) tends to \(S_\infty^s/(b-1)\): rewrite it with \(k=N-j\), so that the weights are \(b^{-k-1}\); for each fixed \(k\), the factor \(S_{N-k}^s\) converges, and it is dominated throughout by \(S_\infty^s\). Both bounds thus have the same limit after division by \(b^{N+1}\), equal to \(S_\infty^{p-1}/(b-1)\). Taking the \(p\)-th root proves sharpness and the asymptotic attainment statement.

## Verification

As an exact finite check of the two different bounds, when \(b=4,p=3,N=2\) they give \(29/3\le\|H_{4,2}\|_{3\to3}^3\le10\), using \(S_1=1/2,S_2=3/4\). The bounded checks of level estimates in the original `verify_tree_hardy.py` are relevant as finite diagnostics only. The proof of the limit is the analytical squeeze above.

## Relationship to prior work

Evans, Harris and Lang, *The approximation numbers of Hardy-type operators on trees* (arXiv:math/0003215), study continuous metric-tree Hardy operators and asymptotic approximation numbers as the rank tends to infinity for a fixed tree. Wang, *Mixed eigenvalues of p-Laplacian on trees* (arXiv:1512.04770), gives general weighted variational formulas and estimates; its Example 2.4 uses decaying vertex masses. Those frameworks do not state the sharp fixed-\(p\) equivalent for unweighted counting measure as the depth grows. The two estimates here use the asymptotic concentration of output mass at late levels and the same radial input across all those levels. Wang and Zhang's *The first Dirichlet eigenvalue of birth–death process on trees* (DOI: 10.1016/j.spl.2013.05.001) has a related variational formulation; the accessible abstract does not resolve all possible historical overlap.

The Hilbert branch is already accessible by established spectral methods. Molitierno, Neumann and Shader, *Tight bounds on the algebraic connectivity of a balanced binary tree* (Electronic Journal of Linear Algebra 6, 2000, 62–71), Eq. (2) and Theorem 3.7, use the exact binary tridiagonal block and bound its least eigenvalue. More generally, under the radial level normalization by square roots of the level counts, the grounded branch compression is a Jacobi matrix with diagonal \(b+1\) except for the leaf diagonal \(1\), and off-diagonals \(-\sqrt b\). After shifting and rescaling this is a special case of Veerman, Hammond and Baldivieso, *Spectra of Tridiagonal Matrices* (arXiv:1801.04977), Definition 2.1 and Proposition 2.2. The Hilbert correction can be extracted from that exact polynomial and is not asserted separately here.
