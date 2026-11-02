# Exact negative type and Hilbert-rank transition of finite affine-plane incidence metrics

## Finding

Let \(\mathcal A\) be any existing finite affine plane of order \(q\ge2\), not necessarily Desarguesian. Let \(G_{\mathcal A}\) be its bipartite point–line incidence graph with unit edges and vertex shortest-path metric \(d\). Set \(N=2q^2+q\). The maximal generalized-roundness (supremal negative-type) exponent is exactly
\[
\boxed{\wp(G_{\mathcal A})=\log_2\!\left(\frac{q}{q-1}\right).}
\]
The metric has strict \(p\)-negative type for every \(0\le p<\wp\), non-strict \(\wp\)-negative type, and fails \(p\)-negative type for every \(p>\wp\).

For \(q\ge3\), every real zero-sum equality vector at \(p=\wp\) has zero coefficients at the points and a constant coefficient \(z_j\) on each of the \(q+1\) parallel classes of lines, where \(\sum_{j=1}^{q+1}z_j=0\). The equality space has dimension \(q\). For \(q=2\), the equality space instead has dimension \(5\): identify the four points with the singleton subsets of a four-element set and the six lines with its two-element subsets; the equality vectors are precisely those real coefficients \(\lambda_S\) satisfying \(\sum_S\lambda_S=0\) and \(\sum_{S\ni i}\lambda_S=0\) for each of the four underlying elements \(i\).

For every \(0<p<\wp\), the minimum Euclidean dimension of an isometric realization of the snowflake \(d^{p/2}\) is \(N-1\). At \(p=\wp\), it is exactly \(2q^2-1\) if \(q\ge3\), and exactly \(4\) if \(q=2\). The endpoint equality can always be witnessed by coefficients \(+1\) on one entire parallel class and \(-1\) on a second entire parallel class, with all other coefficients zero. In particular, the full point–line metric has the same sharp exponent as the metric on its line vertices alone, despite the extra \(q^2\) point vertices and their incidence distances.

## Assumptions and scope

An affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q\) points on each line, \(q+1\) lines through each point, and \(q+1\) parallel classes of \(q\) lines. Every two distinct points determine a unique line; two distinct lines intersect exactly when they are in different parallel classes. No field coordinatization is assumed. The graph has one vertex for each point and line, and point–line adjacency means incidence. Every edge has length one.

For \(p\ge0\), write \(D_p=(d(u,v)^p)_{u,v}\) with zero diagonal (and the convention \(d(u,v)^0=1\) for distinct vertices). The definition of \(p\)-negative type is \(\lambda^{\mathsf T}D_p\lambda\le0\) for every real coefficient vector with \(\sum_v\lambda_v=0\); strict negative type requires strict inequality for nonzero such vectors. The Euclidean embedding dimension refers to the smallest \(k\) for which there are vectors in \(\mathbb R^k\) whose pairwise Euclidean distances equal \(d(u,v)^{p/2}\).

## Proof

**1. Distances and incidence identities.** Two distinct points have distance \(2\). Two distinct intersecting lines have distance \(2\), and parallel lines have distance \(4\). A point and an incident line have distance \(1\); a nonincident point and line have distance \(3\). Let \(P=q^2\), \(L=q(q+1)\), and let \(B\) be the \(P\times L\) point–line incidence matrix. Since every two points lie on one line,
\[
BB^{\mathsf T}=qI_P+J_P.
\]
Let \(C\) be the block-diagonal \(L\times L\) matrix whose \(q+1\) diagonal blocks are \(J_q\), indexed by parallel classes. With \(a=2^p\), \(b=3^p\), and \(c=4^p=a^2\), the distance matrix is exactly
\[
D_p=\begin{pmatrix}
 a(J_P-I_P)&bJ_{P,L}+(1-b)B\\
 bJ_{L,P}+(1-b)B^{\mathsf T}&aJ_L+(c-a)C-cI_L
\end{pmatrix}.
\]
Here \(J\) means the all-ones matrix of the indicated size.

**2. Orthogonal decomposition of the zero-sum quadratic form.** Let \(X=\{x\in\mathbb R^P:\sum x=0\}\). The map \(x\mapsto q^{-1/2}B^{\mathsf T}x\) is an isometry from \(X\) onto the space of line vectors whose sum in each parallel class vanishes: the norm identity follows from \(BB^{\mathsf T}=qI+J\), and both spaces have dimension \(q^2-1\). The remaining line space consists of vectors constant within parallel classes. Its \(q\)-dimensional zero-total-sum subspace is orthogonal to the incidence image, since every point lies on exactly one line from each class.

Consequently, the quadratic form \(D_p\) on the real vertex-coefficient hyperplane \(\sum\lambda=0\) splits orthogonally into:

* a \(q\)-dimensional parallel-class contrast sector with scalar coefficient \(h_p=(q-1)c-qa\);
* \(q^2-1\) identical two-dimensional sectors with symmetric matrix
\[
M_p=\begin{pmatrix}-a&\sqrt q(1-b)\\\sqrt q(1-b)&-c\end{pmatrix};
\]
* one global sector represented by the vector equal to \(1\) at every point and \(-q/(q+1)\) at every line. Its quadratic form divided by \(P\) is
\[
F_p=a(q^2-1)-2q\bigl(1+(q-1)b\bigr)
 +\frac q{q+1}\bigl(q^2a+(q-1)c\bigr).
\]
These subspaces have combined dimension \(q+2(q^2-1)+1=N-1\); they are mutually orthogonal for the distance quadratic form, although the global coefficient vector need not be a distance-matrix eigenvector.

**3. The sharp endpoint for \(q\ge3\).** Put \(p_*=\log_2(q/(q-1))\), so \(a=q/(q-1)\), \(c=a^2\), \(0<p_*<1\). Then \(h_{p_*}=0\), so the parallel-class contrast sector gives equality. For \(0<p\le1\), concavity of \(t\mapsto t^p\) gives \(3^p-1\le2(2^p-1)\). Therefore
\[
\det M_{p_*}=a^3-q(b-1)^2
\ge a^3-4q(a-1)^2
 =a(a-2)^2>0.
\]
Since both diagonal entries are negative, \(M_{p_*}\) is strictly negative definite.

The global sector is also strictly negative. Indeed, \(3>2^{3/2}\), and convexity of \(x^{3/2}\) on \([1,\infty)\) implies
\[
b=3^{p_*}>a^{3/2}\ge1+\tfrac32(a-1).
\]
Using \(a=q/(q-1)\) in the preceding formula for \(F_p\), we obtain
\[
F_{p_*}=q(q-1)(1-2b)+q^2a
 <q(a-2)<0.
\]
Thus the only endpoint equality sector is the \(q\)-dimensional line-class contrast space. The metric has \(p_*\)-negative type but not strict \(p_*\)-negative type. For every \(p>p_*\), the coefficient \(h_p=a((q-1)a-q)\) is positive, and a vector supported on two parallel classes violates negative type. Hence \(\wp=p_*\) exactly.

**4. The exceptional order \(q=2\).** The four points form a set \(\{1,2,3,4\}\), and the six affine lines are its six unordered pairs. Map point \(i\) to the indicator of \(\{i\}\) in \(\mathbb R^4\) and line \(\{i,j\}\) to the indicator of \(\{i,j\}\). Their squared Euclidean distances are exactly the graph distances: \(2\) between points, \(1\) or \(3\) between points and lines, and \(2\) or \(4\) between lines. Therefore the whole metric has \(1\)-negative type. The class-contrast coefficient \(h_p=4^p-2\cdot2^p\) is positive for every \(p>1\), so \(\wp=1\). The four indicator-coordinate functions together with the constant function are independent on the ten subsets, hence the centered squared-distance Gram matrix has rank \(4\). Its zero-sum equality space has dimension \(10-1-4=5\), characterized by vanishing sum and vanishing four coordinate moments, exactly as stated.

**5. Exponents below the endpoint and embedding dimensions.** The strict-negative-type inheritance theorem (Li–Weston, Theorem 5.4) says that a metric with positive \(p_*\)-negative type has strict \(p\)-negative type for every \(0\le p<p_*\). For a finite metric, Schoenberg's centered Gram matrix \(-\tfrac12HD_pH\), where \(H=I-N^{-1}J\), is positive semidefinite precisely for \(p\)-negative type, and its rank is the smallest Euclidean dimension for \(d^{p/2}\). Strictness gives rank \(N-1\) for \(0<p<p_*\). At the endpoint the proved nullities give ranks \(N-1-q=2q^2-1\) for \(q\ge3\) and \(4\) for \(q=2\). Finally, the two-class coefficient vector has quadratic value \(2q((q-1)c-qa)\), exhibiting both endpoint equality and failure above the endpoint.

## Verification

The included standard-library script `verify_affine_negative_type.py` constructs Desarguesian affine planes of orders \(2,3,4,5,7\) from finite-field arithmetic, builds their incidence graphs independently, and checks every all-pairs shortest-path distance and the identity \(BB^{\mathsf T}=qI+J\). A separate Jacobi diagonalization of the centered Gram matrix checks strict positivity below the predicted exponent, endpoint nullities, and negative eigenvalues above the endpoint. It also checks the explicit two-parallel-class equality. The script is not relied upon for the general theorem; the proof applies without finite-field coordinates.

## Relationship to prior work

Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (arXiv:1108.0451, first public August 2, 2011), gives general finite-distance-matrix tests and exact complete-bipartite examples. Li and Weston, *Strict \(p\)-negative type of a metric space* (arXiv:0901.0695, first public January 6, 2009), prove strict-negative-type inheritance for lower exponents. These general tools do not themselves evaluate the point–line metric of an affine plane or its critical equality space. Restriction to the line vertices gives a scaled balanced complete-multipartite metric and already supplies the upper bound; the new issue is proving that adding every point vertex does not reduce the sharp exponent, and determining the additional exceptional equality directions at order two.

Finite projective-plane incidence metrics have no parallel lines and are not distance-preserving restrictions or supergraphs of the present affine incidence metrics: parallel affine lines have distance four, whereas their projective completions meet at a point at infinity. Thus the two negative-type problems are not related by an immediate submetric restriction.

## Limitations

No affine plane existence is claimed at orders where existence is unknown or impossible. The exact formulas concern the unweighted **vertex** shortest-path metric and ordinary real negative type; no weighted-edge, continuum metric-graph, or other incidence-design generalization is proved. The equality classification is for real zero-sum coefficients. The finite-field verifier covers only the stated orders, and neither computation nor absence of a matching search result establishes historical novelty. An independently established equivalent formula in unindexed literature remains possible.

## References

1. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first version August 2, 2011), https://arxiv.org/abs/1108.0451.
2. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first version January 6, 2009), https://arxiv.org/abs/0901.0695.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, DOI:10.1090/S0002-9947-1938-1501980-0.
