# Exact generalized roundness and critical Hilbert dimension of finite projective-plane incidence metrics

## Finding

Let \(\Pi\) be **any** finite projective plane of order \(q\ge2\), including a plane not coordinatizable over a finite field, if one exists. Let \(G_\Pi\) be its simple point–line incidence graph and \(d\) its unweighted vertex shortest-path metric. Write \(v=q^2+q+1\), so the metric space has \(2v\) vertices.

Its supremal generalized roundness, equivalently supremal \(p\)-negative type, is the **unique** number \(\wp_q\in(0,1)\) satisfying
\[
\boxed{\sqrt q\,(3^{\wp_q}-1)=2^{\wp_q}.}
\]
This number depends only on \(q\), not on the isomorphism type of the plane. The space has strict \(p\)-negative type for \(0\le p<\wp_q\), has non-strict \(\wp_q\)-negative type, and fails \(p\)-negative type for every \(p>\wp_q\).

At the endpoint, the complete real vector space of equality coefficients has dimension exactly \(v-1\). If \(B\) is the \(v\)-by-\(v\) point–line incidence matrix, an equality coefficient vector, partitioned as point and line coordinates, is precisely
\[
\boxed{(x,y)=(-q^{-1/2}By,\ y),\qquad \mathbf1^\mathsf{T}y=0.}
\]
In particular, for two distinct lines \(L_1,L_2\), one gets a nontrivial equality supported on exactly \(2q+2\) vertices: coefficient \(+1\) at \(L_1\), \(-1\) at \(L_2\), \(-q^{-1/2}\) on the \(q\) points of \(L_1\setminus L_2\), and \(+q^{-1/2}\) on the \(q\) points of \(L_2\setminus L_1\). All unspecified coefficients vanish. Its positive and negative masses are equal to \(1+\sqrt q\), so division by that quantity gives a normalized generalized-roundness equality simplex.

The snowflaked metric \(d^{\wp_q/2}\) embeds isometrically into real Euclidean space of **minimum possible dimension exactly** \(v\). For every \(0<p<\wp_q\), the minimum Hilbert dimension of \(d^{p/2}\) instead equals \(2v-1\). For \(p>\wp_q\), no isometric Hilbert realization of \(d^{p/2}\) exists.

Furthermore, \(\wp_q\) is strictly decreasing in \(q\) (among orders for which planes exist), and
\[
\wp_q=\frac1{\log 3\,\sqrt q}+
\left(\frac{\log2}{(\log3)^2}-\frac1{2\log3}\right)\frac1q
+O(q^{-3/2}).
\]
For example \(\wp_2\approx0.69428009277719\), \(\wp_3\approx0.56076276012972\), and \(\wp_4\approx0.48214718518210\).

## Assumptions and scope

The objects are vertices, not points in the geometric realization of the edges. A finite projective plane of order \(q\) has exactly \(v=q^2+q+1\) points and \(v\) lines, with each point incident to \(q+1\) lines and every two distinct points incident to a unique common line; the dual statements hold for lines. The graph has one vertex for each point or line and edges only for incidences. Every edge has length one. There is no weighting, normalization, or assumption that the plane is Desarguesian.

For \(p>0\), \(p\)-negative type means that every real coefficient family \((a_z)_{z\in V(G_\Pi)}\) with \(\sum_z a_z=0\) satisfies
\[
\sum_{z,w}a_z a_w d(z,w)^p\le0.
\]
At \(p=0\), the diagonal of the powered-distance matrix is defined to be zero and its off-diagonal entries one. Strict negative type means strict inequality whenever the coefficients are not all zero. Generalized roundness is its equivalent finite-metric formulation. The Euclidean snowflake conclusion refers to squared Euclidean distances \(d(z,w)^p\), so the Euclidean metric itself is \(d^{p/2}\).

## Proof

**1. Exact graph-distance shells.** Two distinct points have distance two through their unique common line, and dually two distinct lines have distance two through their unique common point. Incident point–line pairs have distance one. Nonincident point–line pairs have distance three: choose any point on the given line, join it to the given point by the unique line, and use the resulting length-three path. Bipartiteness rules out even paths between opposite colors, and nonincidence rules out length one. Hence graph distances belong to \(\{0,1,2,3\}\) with the stated incidence dependence.

**2. Incidence spectral identity.** Let \(B\) be indexed by points (rows) and lines (columns), with entries one for incidence. Counting common lines gives
\[
BB^\mathsf T=qI+J,\qquad
B\mathbf1=(q+1)\mathbf1,\qquad B^\mathsf T\mathbf1=(q+1)\mathbf1.
\]
On the zero-sum hyperplane \(\mathbf1^\perp\), \(B\) therefore gives a singular-value isomorphism of constant singular value \(\sqrt q\). These identities depend only on the projective-plane axioms.

**3. Diagonalization of every powered-distance matrix.** Write \(u=2^p\), \(w=3^p\), and let \(D_p=(d(z,w)^p)_{z,w}\) for \(p\ge0\), with a zero diagonal. In point–line block order,
\[
D_p=\begin{pmatrix}
u(J-I)&wJ+(1-w)B\\
wJ+(1-w)B^\mathsf T&u(J-I)
\end{pmatrix},
\]
The global constant direction has positive eigenvalue
\[
\lambda_\mathrm{const}(p)=q(q+1)u+(q+1)+q^2w.
\]
The direction constant on points and opposite constant on lines has eigenvalue
\[
\lambda_\mathrm{opp}(p)=q(q+1)u-(q+1)-q^2w.
\]
The remaining \(2(v-1)\) dimensions split into two equal-multiplicity spectral branches
\[
\lambda_\pm(p)=-u\pm\sqrt q\,(w-1),
\qquad \operatorname{mult}(\lambda_\pm)=v-1.
\]
To see this explicitly, on \(\mathbf1^\perp\oplus\mathbf1^\perp\) the diagonal blocks are \(-uI\), the off-diagonal blocks are \(-(w-1)B\) and \(-(w-1)B^\mathsf T\), and \(BB^\mathsf T=qI\) there. There are no other eigenvalues.

**4. Identification of the unique obstruction.** The global constant eigenvalue is irrelevant to conditional negative type. The opposite-color constant eigenvalue is strictly negative for every \(p\ge0\): it equals \(-1\) at \(p=0\), and
\[
\lambda_\mathrm{opp}'(p)=q(q+1)(\log2)2^p-q^2(\log3)3^p<0,
\]
because \((q+1)/q\le3/2<\log3/\log2\) and \((3/2)^p\ge1\). Also \(\lambda_-(p)<0\) for all \(p\ge0\). Finally,
\[
\lambda_+(p)=-2^p+\sqrt q\,(3^p-1)
\]
is strictly increasing for \(p\ge0\), since its derivative is \(\sqrt q(\log3)3^p-(\log2)2^p>0\). It starts at \(-1\) and is positive at \(p=1\), where it equals \(2(\sqrt q-1)\). Consequently it has exactly one zero \(\wp_q\in(0,1)\); all conditional eigenvalues are negative below, one branch vanishes at, and one branch is positive above that exponent. This proves the sharp negative-type claims without relying on a numerical root search.

**5. Endpoint equality and minimum Hilbert dimension.** At \(p=\wp_q\), let \(y\in\mathbf1^\perp\) be arbitrary and set \(x=-q^{-1/2}By\). The root identity \(u=\sqrt q(w-1)\) gives \(D_{\wp_q}(x,y)=0\); conversely the above complete eigenspace decomposition shows that every nontrivial zero-sum quadratic equality lies in exactly this \((v-1)\)-dimensional nullspace. The two-line witness in the finding follows by taking \(y=e_{L_1}-e_{L_2}\), since distinct lines meet in exactly one point.

Let \(H=I-(2v)^{-1}\mathbf1\mathbf1^\mathsf T\). By the elementary Schoenberg centered-Gram construction, \(-\frac12 HD_pH\) is the Gram matrix of a Euclidean realization with squared distances \(d^p\) if and only if it is positive semidefinite; its rank is the least possible ambient Euclidean dimension. For \(0<p<\wp_q\) its rank is \(2v-1\). At \(p=\wp_q\) exactly \(v-1\) additional centered eigenvalues vanish, giving rank \(2v-1-(v-1)=v\). Above \(\wp_q\) the Gram matrix is indefinite, so there is no such realization.

**6. Order dependence and asymptotics.** The equation \(\sqrt q(3^p-1)=2^p\) has a strictly increasing left-minus-right function in \(p\ge0\); increasing \(q\) strictly reduces its root. Put \(t=q^{-1/2}\), so the equation becomes \(3^p-1=t2^p\). The implicit-function theorem at \((p,t)=(0,0)\), with \(p\)-derivative \(\log3\ne0\), supplies an analytic expansion. Equating coefficients through \(t^2\) yields
\[
p=\frac{t}{\log3}+\left(\frac{\log2}{(\log3)^2}-\frac1{2\log3}\right)t^2+O(t^3),
\]
proving the stated estimate.

## Verification

The standalone script `check_projective_negative_type.py` constructs the classical finite projective planes of orders \(2,3,4,5,7\) from normalized homogeneous coordinates (including the nonprime field \(\mathbb F_4\)). It checks every entry of \(BB^\mathsf T=qI+J\) by integer arithmetic; independently performs breadth-first search from every graph vertex to check every ordered shortest-path distance; brackets the unique threshold root at 65-digit decimal precision; and evaluates the conditional-eigenvalue and sparse-equality identities at that root. The five examples contain respectively \(14,26,42,62,114\) vertices, for a total of \(19{,}476\) ordered-pair distance checks. The script reports `ALL_PROJECTIVE_NEGATIVE_TYPE_CHECKS_OK` when all checks pass.

These finite tests do not establish the theorem for every projective plane: that conclusion is proved by the incidence-axiom argument above. Approximate root values are illustrations and are not substituted for exact root definitions.

## Relationship to prior work

Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (arXiv:1108.0451v1, 2011), establishes general finite-distance-matrix criteria and evaluates complete bipartite graph metrics. Murugan, *Generalized roundness of vertex transitive graphs* (arXiv:1112.5657v1, 2011), gives a determinant criterion and endpoint equality principles for constant-distance-row metrics, including a class to which projective-plane incidence graphs belong. These provide the conceptual framework but do not state the order-uniform projective-plane root, the exact endpoint equality subspace, the sparse two-line equality, or the critical rank in the inspected material. Horak–LaRose–Moore–Rooney–Rosenthal (2010) treat four-point **roundness** of graphs, a different invariant; their explicit families are cycles and triangulated cycles, not this all-coefficient generalized-roundness computation.

Standard references record the incidence spectrum of the Heawood graph (the order-two case). That ordinary adjacency spectrum by itself does not supply the powered-distance threshold, its uniqueness proof, or the critical snowflake dimension. The present statement is a direct spectral computation specific to projective-plane incidence relations, not a claim to invent the general negative-type criterion. Other finite metric spaces can share an algebraic threshold without possessing the projective-plane equality-space or embedding-rank conclusions.

## Limitations

The theorem concerns finite projective planes of order \(q\ge2\) **that exist**, their unweighted vertex graph metric, and real Hilbert embeddings. It asserts neither existence of planes for arbitrary integers nor classification of non-Desarguesian planes. It does not give sharp generalized roundness for arbitrary symmetric block designs, weighted incidence graphs, their metric-edge realizations, or other graph families. The endpoint equality vectors are fully classified as a linear subspace, but no claim is made that the displayed two-line witness is minimum-support among all possible equality vectors. Publication-priority searches are not a proof that no equivalent formula has appeared in uncatalogued literature.

## References

1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, posted 2011-08-02, https://arxiv.org/abs/1108.0451.
2. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1, posted 2011-12-23, https://arxiv.org/abs/1112.5657.
3. Matthew Horak, Eric LaRose, Jessica Moore, Michael Rooney and Hannah Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), 67–91, https://doi.org/10.2140/involve.2010.3.67.
4. Andries Brouwer, *Heawood graph*, distance-regular graph reference page, https://aeb.win.tue.nl/drg/graphs/Heawood.html (accessed 2026-10-29 UTC).
5. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536.
