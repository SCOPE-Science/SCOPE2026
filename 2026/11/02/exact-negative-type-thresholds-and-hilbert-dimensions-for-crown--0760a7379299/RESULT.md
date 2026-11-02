# Exact negative-type thresholds and Hilbert dimensions for crown graph metrics

## Finding
For every integer \(n\ge3\), let the crown graph \(\operatorname{Cr}_n=K_{n,n}\setminus M_n\) be the complete bipartite graph with one perfect matching removed, equipped with the unit-edge shortest-path metric \(d\). Its supremal \(p\)-negative-type exponent \(\wp_n\) is
\[
\wp_n=\begin{cases}
1,&n=3,4,\\
\text{the unique }p\in(0,1)\text{ with }(n-1)(2^p-1)=3^p,&n\ge5.
\end{cases}
\]
For \(0\le p<\wp_n\), the metric has strict \(p\)-negative type; it has nonstrict \(\wp_n\)-negative type at its endpoint and fails \(p\)-negative type for every \(p>\wp_n\).

The minimum affine dimension of a real Hilbert-space isometric realization of the snowflake \((\operatorname{Cr}_n,d^{p/2})\) is \(2n-1\) for \(0<p<\wp_n\). At \(p=\wp_n\), that dimension is \(3\) when \(n=3,4\), and \(2n-2\) when \(n\ge5\). At the endpoint the nullity on the zero-sum coefficient space is \(2\), \(4\), or \(1\), respectively. For \(p>\wp_n\) no such isometric realization exists.

For \(n\ge5\), the exponent is strictly decreasing in \(n\), and, writing \(N=n-1\),
\[
\wp_n=\frac{1}{N\log 2}
+\left(\frac{\log 3}{(\log2)^2}-\frac{1}{2\log2}\right)\frac1{N^2}
+O(N^{-3}).
\]
In comparison, the previously known supremal exponent for \(K_{n,n}\) is \(\log_2(n/(n-1))\). Deleting a perfect matching yields the strictly positive gain
\[
\wp_n-\log_2\frac n{n-1}
=\frac{\log3}{(\log2)^2(n-1)^2}+O((n-1)^{-3}),
\qquad n\longrightarrow\infty.
\]
The well-known cases \(\operatorname{Cr}_3=C_6\) and \(\operatorname{Cr}_4=Q_3\) are included as boundary cases and not asserted to be previously unknown.

## Assumptions and scope
Let the bipartition classes be \(x_1,\dots,x_n\) and \(y_1,\dots,y_n\). An edge joins \(x_i\) to \(y_j\) exactly when \(i\ne j\); \(n\ge3\) ensures connectedness. For distinct vertices in the same class the distance is \(2\); for \(x_i,y_j\) it is \(1\) if \(i\ne j\), and \(3\) if \(i=j\). Distance is zero on the diagonal. For \(p=0\), the usual zero-distance convention makes every distinct-point off-diagonal entry equal to \(1\).

The definition of \(p\)-negative type is: for every real vector \(z\in\mathbb R^{2n}\) with coordinate sum zero,
\[
 z^{\mathsf T}D_p z\le0,
\qquad D_p=(d(u,v)^p)_{u,v}.
\]
Strictness means that equality requires \(z=0\). Every Hilbert dimension assertion concerns real affine span and squared Hilbert distances equal to \(d^p\), so it is equivalent to the isometric embedding statement for \(d^{p/2}\).

## Proof
Let \(J\) and \(I\) denote the \(n\times n\) all-ones and identity matrices, and put \(a=2^p\), \(b=3^p\). The complete powered-distance matrix is
\[
 D_p=\begin{pmatrix}
 a(J-I)&J+(b-1)I\\
 J+(b-1)I&a(J-I)
 \end{pmatrix}.
\]
The constant vector \((\mathbf1,\mathbf1)\) has positive eigenvalue \((n-1)a+(n-1)+b\) and lies orthogonal to the zero-sum subspace. The latter decomposes as an orthogonal direct sum of three invariant subspaces, with exact eigenvalues:
\[
\begin{array}{c|c|c}
\text{coefficient subspace}&\text{dimension}&\text{eigenvalue}\\\hline
\{(w,w):\sum_iw_i=0\}&n-1&\lambda_+=b-a-1\\
\{(w,-w):\sum_iw_i=0\}&n-1&\lambda_-=1-a-b\\
\operatorname{span}\{(\mathbf1,-\mathbf1)\}&1&\lambda_{\mathrm s}=(n-1)(a-1)-b.
\end{array}
\]
These formulas follow immediately from \(Jw=0\) whenever \(\sum_iw_i=0\), and from \(J\mathbf1=n\mathbf1\). Hence the entire (strict) negative-type question is exactly the (strict) nonpositivity of these three scalar eigenvalues; no untested eigenmodes remain.

For \(0\le p\le1\), concavity of the \(p\)-power gives \(3^p\le2^p+1\), with equality for \(p=1\), so \(\lambda_+\le0\), strictly for \(p<1\). The eigenvalue \(\lambda_-\) is strictly negative for all \(p\ge0\). For \(p>1\), strict convexity gives \(3^p>2^p+1\), making \(\lambda_+>0\) and proving failure of negative type regardless of the remaining modes.

For \(p\in(0,1]\), define \(h(p)=3^p/(2^p-1)\). Its logarithmic derivative is
\[
\frac{h'(p)}{h(p)}
=\log3-\frac{2^p\log2}{2^p-1}
\le\log3-2\log2<0.
\]
Also \(h(p)\to\infty\) as \(p\downarrow0\), and \(h(1)=3\). Thus \(\lambda_{\mathrm s}\le0\) iff \(n-1\le h(p)\). For \(n=3\) it is strictly negative at \(p=1\); for \(n=4\) it vanishes there; for every \(n\ge5\) it has a unique zero \(\wp_n\in(0,1)\), with strictly negative values below and positive values above \(\wp_n\) within \((0,1]\). Together with the \(p>1\) argument, this proves the sharp exponents and all strictness assertions.

At the endpoint, \(\lambda_+=0\) precisely when \(p=1\), i.e., for \(n=3,4\). The side-antisymmetric eigenvalue vanishes at \(p=1\) only for \(n=4\); for \(n\ge5\) it is the unique zero mode. This gives nullities \(n-1=2\) at \(n=3\), \((n-1)+1=4\) at \(n=4\), and \(1\) otherwise. Let \(H=I_{2n}-\mathbf1\mathbf1^{\mathsf T}/(2n)\). By the elementary Euclidean distance-matrix correspondence, \(-\tfrac12HD_pH\) is the centered Gram matrix, positive semidefinite exactly when the graph metric has \(p\)-negative type. Its rank is the minimum affine Hilbert embedding dimension. Its zero on the constant vector, together with the calculated zero-sum nullities, gives the stated ranks. Because this correspondence explicitly constructs the embedding through any Gram factorization, these are existence as well as lower-bound statements.

Strict decrease of \(\wp_n\) for \(n\ge5\) follows from strict decrease of \(h\). For asymptotics let \(N=n-1\), \(s=1/N\), and solve \(e^{p\log2}-1=s e^{p\log3}\). At \((s,p)=(0,0)\), the derivative in \(p\) is \(\log2\ne0\); the analytic implicit-function theorem applies. Substituting \(p=c_1s+c_2s^2+O(s^3)\) yields \(c_1=1/\log2\) and \(c_2=\log3/(\log2)^2-1/(2\log2)\). Sánchez's established formula for \(K_{n,n}\) is \(\log_2(n/(n-1))=(\log2)^{-1}\log(1+1/N)\); subtracting its Taylor expansion yields the gain. Strict gain for every \(n\ge5\) also follows because at the complete-graph threshold the crown left side \(N(2^p-1)=1\) is smaller than \(3^p\).

## Verification
The file `verify_crown.py` is a standalone supplementary checker. It independently constructs each tested crown graph by its edge set, calculates graph distances using breadth-first search, forms powered-distance matrices and centered Gram matrices, checks their numerical spectra against the three proved eigenmode formulas, and checks endpoint multiplicities and large-size asymptotic behavior. It reported 178 passing numerical assertions on a bounded collection of graph orders. The proof above, not finite sampling, establishes every quantifier and the infinite family.

Some numerical reference values are \(\wp_5\approx0.537048034477\), \(\wp_6\approx0.384010941242\), and \(\wp_{10}\approx0.183958496342\).

## Relationship to prior work
Sánchez's 2011 theorem supplies a general finite-metric matrix criterion and the exact supremal exponent of complete bipartite graphs. Murugan's vertex-transitive theorem reduces generalized roundness to the first vanishing powered-distance determinant and characterizes equality loads; the crown graph falls within this broad framework. Robertson's 2020 simplification addresses general finite metrics, while his 2023 treatment explicitly examines complete bipartite graphs and Hamming cubes rather than deletion of a perfect matching. The tabulated ordinary crown distance characteristic polynomial records the unpowered case \(p=1\), which is not sufficient for the \(p\in(0,1)\) classification without a new powered-distance calculation.

The specific contributions asserted here are the complete exponent function for all \(n\ge3\), its endpoint kernel and minimal affine embedding dimensions, and the exact second-order matching-deletion gain. No novelty is asserted for the general determinant method, the known complete bipartite formula, or the standard six-cycle and cube graph identifications. Earlier equivalent treatments in distance-spectral or generalized-roundness literature remain a possible historical-priority risk.

## Limitations
Only unweighted connected crown graphs of order \(2n\) with \(n\ge3\) are covered. No statement is made about arbitrary matching-deleted bipartite graphs, weighted graphs, other graph families, or other notions of embedding distortion. Numerical tests are finite, do not certify infinite statements, and cannot establish literature novelty. No independent mathematical audit has been performed.

## References
1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (2011), Section 3; https://arxiv.org/abs/1108.0451.
2. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1 (2011), Theorem 3.1; https://arxiv.org/abs/1112.5657.
3. G. Robertson, *The Maximal Generalised Roundness of Finite Metric Spaces*, arXiv:2004.10923v1 (first public April 23, 2020); https://arxiv.org/abs/2004.10923.
4. G. Robertson, *Negative Type and Bi-Lipschitz Embeddings into Hilbert Space*, arXiv:2309.16070v1 (2023), Section 4.1; https://arxiv.org/abs/2309.16070.
5. E. W. Weisstein, *Crown Graph* and *Distance Polynomial*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html and https://mathworld.wolfram.com/DistancePolynomial.html (ordinary distance-spectrum table).
