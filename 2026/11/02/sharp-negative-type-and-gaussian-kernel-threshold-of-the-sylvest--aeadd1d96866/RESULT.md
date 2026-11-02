# Sharp negative type and Gaussian-kernel threshold of the Sylvester graph

## Finding
Let \(G\) be the unique distance-regular Sylvester graph on \(36\) vertices, with intersection array \(\{5,4,2;1,1,4\}\). Write \(d\) for its intrinsic shortest-path distance. Let \(p_*\) be the unique positive real solution of
\[
3^{p_*}-2^{p_*}=\frac14,
\qquad p_*=0.42196797079240764614\ldots.
\]
For every real \(p\ge0\), with \(d(x,x)^0=0\) and \(d(x,y)^0=1\) when \(x\ne y\), the powered metric matrix \(D_p=(d(x,y)^p)_{x,y\in V(G)}\) is conditionally negative semidefinite if and only if \(p\le p_*\). It is strictly negative on nonzero zero-sum real vectors for \(0\le p<p_*\). At \(p=p_*\), the zero-sum nullspace has dimension exactly \(10\). More precisely, identify the vertices via the classical isomorphism of the distance-three graph with the \(6\)-by-\(6\) rook grid: the nullspace consists exactly of \(c_{r,s}=u_r+v_s\) with \(\sum_{r=1}^6u_r=\sum_{s=1}^6v_s=0\). For \(p>p_*\) the form fails conditional negative semidefiniteness.

Equivalently, the homogeneous Gaussian kernel \(K_{t,p}(x,y)=\exp(-t\,d(x,y)^p)\) is positive definite for **every** \(t>0\) if and only if \(0\le p\le p_*\). In this range each fixed \(t>0\) gives a strictly positive definite matrix; outside it, all sufficiently small \(t>0\) give an indefinite matrix. The least Euclidean dimension in which \(d(x,y)^{p_*}\) can be realized as squared Euclidean distances is exactly \(25\); at exponents strictly below \(p_*\), the minimum dimension is \(35\).

## Assumptions and scope
The graph is connected, simple, undirected, and has the standard shortest-path metric with distances \(0,1,2,3\). Conditional negative semidefiniteness means that \(\sum_{x,y}c_xc_y d(x,y)^p\le0\) for every real vector \((c_x)\) satisfying \(\sum_x c_x=0\). Strictness excludes the zero vector. The phrase positive definite for the kernel means positive semidefinite on every coefficient vector, with strict positive definiteness explicitly noted where used. All exponents and kernel parameters are real. Uniqueness of this graph with the given intersection array is established background.

## Proof
Let \(A_i\) be the adjacency matrix of the relation \(d(x,y)=i\), so \(A_0=I\) and \(A=A_1\). The standard distance-regular intersection recurrence obtained from the given array gives
\[
A_2=A^2-5I,\qquad 4A_3=A^3-2A^2-9A+10I.
\]
The adjacency spectrum, with multiplicities, is \(5^{(1)},2^{(16)},(-1)^{(10)},(-3)^{(9)}\). Evaluating the two polynomials yields the exact relation-eigenvalue table:

| Adjacency eigenvalue | multiplicity | \(A_1\) | \(A_2\) | \(A_3\) |
| --- | ---: | ---: | ---: | ---: |
| \(5\) | 1 | 5 | 20 | 10 |
| \(2\) | 16 | 2 | -1 | -2 |
| \(-1\) | 10 | -1 | -4 | 4 |
| \(-3\) | 9 | -3 | 4 | -2 |

Since \(D_p=A_1+2^p A_2+3^p A_3\), its eigenvalues on those four eigenspaces are respectively
\[
\begin{aligned}
\Lambda_5(p)&=5+20\,2^p+10\,3^p,\\
\Lambda_2(p)&=2-2^p-2\,3^p,\\
\Lambda_{-1}(p)&=-1-4\,2^p+4\,3^p,\\
\Lambda_{-3}(p)&=-3+4\,2^p-2\,3^p.
\end{aligned}
\]
The first eigenspace consists precisely of the constants, as the graph is connected and regular. The second is strictly negative for \(p\ge0\), since \(2^p\ge1\) and \(3^p\ge1\). For the fourth, let \(u=2^{p/2}\ge1\) and \(\alpha=\log_2 3>3/2\). Then \(3^p=u^{2\alpha}\ge u^3\); hence
\[
\Lambda_{-3}(p)\le-3+4u^2-2u^3\le-\frac{17}{27}<0.
\]
The last inequality follows by maximizing the cubic over \(u\ge1\); its only interior maximum is attained at \(u=4/3\). Finally, \(\Lambda_{-1}(p)=4(3^p-2^p)-1\), which is strictly increasing on \([0,\infty)\), starts at \(-1\), and becomes positive. Its unique zero is the displayed \(p_*\). This proves the claimed sign classification and exactly \(10\) zero-sum null directions at the endpoint.

For the embedding statement, put \(H=I-\mathbf1\mathbf1^\mathsf T/36\). Schoenberg's finite negative-type criterion identifies the centered matrix \(-HD_pH/2\) as the Gram matrix for squared Euclidean distances. For \(p<p_*\) its rank is \(35\); for \(p=p_*\) the rank is \(35-10=25\). These ranks are minimum possible affine embedding dimensions. The classical distance-three graph is the \(6\)-by-\(6\) rook graph, whose eigenvalue \(4\) space consists exactly of row-plus-column contrast functions \(c_{r,s}=u_r+v_s\), with zero row and column coefficient sums. The table shows that this eigenvalue-\(4\) space of \(A_3\) is exactly the adjacency \(-1\) eigenspace, so it is precisely the ten-dimensional critical nullspace. In any centered critical Euclidean embedding, each of the six row centroids and six column centroids is therefore at the origin; the canonical minimal embedding can be realized in the \(25\)-dimensional space of doubly centered \(6\)-by-\(6\) arrays. Schoenberg's exponential criterion yields positive semidefiniteness of \(\exp(-tD_p)\) for every \(t>0\) exactly in the conditionally negative range. Strictness follows from the ordinary Gaussian kernel's strict positive definiteness on finitely many distinct Euclidean points. Conversely, if \(p>p_*\), choose a nonzero zero-sum vector in the adjacency \(-1\) eigenspace; it satisfies \(c^\mathsf{T}D_pc>0\), so \(c^\mathsf{T}\exp(-tD_p)c=-t c^\mathsf{T}D_pc+O(t^2)<0\) for every sufficiently small positive \(t\).

## Verification
The accompanying `verify.py` reconstructs the graph **independently** as the induced subgraph on the \(36\) vertices outside the closed neighborhoods of an edge of the Hoffman--Singleton graph. It runs with Python, NetworkX, and NumPy, and verifies all \(1296\) intersection-array instances, exact integer distance-polynomial identities, the adjacency spectrum, and the complete powered-distance spectra at five exponents, recovers the twelve maximal \(6\)-cliques of the distance-three rook graph, and verifies ten explicit independent row/column contrast eigenvectors. Its endpoint computation checks a ten-dimensional numerical nullspace. The checker succeeds with output `SYLVESTER_POWERED_DISTANCE_OK`. The finite checks are corroboration; the proof for all real exponents is the analytic calculation above.

## Relationship to prior work
The graph's construction, intersection array, and ordinary adjacency spectrum are classical and are not claimed as new. Sánchez (2011) established a general determinant method for the supremal negative-type exponent of finite metric spaces, including a complete-bipartite example. Murugan (2011) treated generalized roundness and endpoint equality for vertex-transitive graphs, including a general reduction to the powered-distance nullspace. Aalipour and collaborators (2015) studied ordinary graph distance spectra, principally family-wide results, rather than the whole family of real powered distances on this graph. The contribution here is this specific graph's complete exponent threshold, its unique obstructing row-and-column spectral sector, its exact doubly centered endpoint embedding, and the equivalent sharp range of positive-definite radial Gaussian kernels. These results are not asserted to be independent of classical predistance spectral machinery; their novelty is at the level of the explicit optimized invariant and consequences.

## Limitations
This concerns a single named finite homogeneous graph, not all distance-regular graphs. Nothing is claimed about kernels for individual non-small values of \(t\) outside the universal exponent range. The adjacency spectrum and distance-recursion formulas are established inputs. Exhaustive older combinatorial and embedding literature may contain an equivalent computation; absence from the inspected sources is not a proof of historical novelty. Independent validation or audit has not been performed.

## References
1. DistanceRegular.org, "Sylvester graph," graph data and spectrum (page dated 2017-02-04), https://www.math.mun.ca/distanceregular/graphs/sylvester.html .
2. E. W. Weisstein, "Sylvester Graph," MathWorld, https://mathworld.wolfram.com/SylvesterGraph.html .
3. S. Sánchez, "On the supremal p-negative type of a finite metric space," first public arXiv version 2011-08-02, arXiv:1108.0451v1, https://arxiv.org/abs/1108.0451 .
4. M. K. Murugan, "Generalized roundness of vertex transitive graphs," first public arXiv version 2011-12-23, arXiv:1112.5657v1, https://arxiv.org/abs/1112.5657 .
5. G. Aalipour et al., "On the distance spectra of graphs," first public arXiv version 2015-09-03, arXiv:1509.01196v1, https://arxiv.org/abs/1509.01196 .
6. C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups*, Springer, 1984 (general positive-definiteness background).
7. A. E. Brouwer, "Sylvester graph" (extended construction notes; distance-three rook graph), https://jaanos.github.io/tables/graphs/Sylvester.html .
