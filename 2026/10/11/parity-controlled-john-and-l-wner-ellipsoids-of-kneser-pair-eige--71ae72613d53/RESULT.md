# Parity-controlled John and Löwner ellipsoids of Kneser pair-eigenpolytopes

## Finding
For every integer \(n\ge 5\), let \(G_n=KG(n,2)\) be the Kneser graph on the two-element subsets \(E=\binom{[n]}2\), with adjacency when the subsets are disjoint. Let \(X_n\) be the \(1\)-eigenpolytope of its adjacency matrix, formed using an **orthonormal** eigenbasis. Write \(N=\binom n2\), \(d=N-n=n(n-3)/2\), and let \(B_2^W\) denote the unit Euclidean ball in the \(d\)-dimensional spectral space.

Then the unique maximum-volume inscribed ellipsoid (John ellipsoid) and unique minimum-volume enclosing ellipsoid (Löwner ellipsoid) are **concentric Euclidean balls** \(r_n B_2^W\) and \(R_n B_2^W\). Their squared radii are
\[
\boxed{\quad
r_n^2=\begin{cases}
\dfrac{2}{n(n-1)(n-2)},&n\ \text{even},\\[4pt]
\dfrac{4}{(n-1)(n-3)(2n-1)},&n\ \text{odd},
\end{cases}
\qquad R_n^2=\dfrac{n-3}{n-1}.\quad}
\]
In particular, \(0\) is the unique center of a maximum Euclidean inball and of a minimum enclosing sphere. Every spectral vertex contacts the enclosing sphere.

The **complete set of facets tangent to the inball** has a parity-dependent description. For even \(n\), they correspond exactly to the perfect matchings of \(K_n\), hence there are \((n-1)!!\), each containing \(N-n/2\) polytope vertices. For odd \(n\), they correspond exactly to a triangle on three vertices together with a perfect matching of the remaining \(n-3\) vertices, hence there are \(\binom n3(n-4)!!\), each containing \(N-(n+3)/2\) polytope vertices. The double factorial on the positive odd integers has its standard combinatorial meaning.

The new structural ingredient is an exact affine equivalence between the **polar** of \(X_n\) and the fractional perfect-matching polytope of the complete graph \(K_n\). It converts the spectral metric problem into an extremum of the number of vertices lying on odd cycles of a half-integral fractional matching.

## Assumptions and scope
The Euclidean normalization is essential: if \(B\in\mathbb R^{n\times N}\) is the unsigned vertex-edge incidence matrix of \(K_n\), put \(W=\ker B\subset\mathbb R^E\) with the **induced ambient Euclidean inner product**, and let \(P\) be the orthogonal projector onto \(W\). The polytope is
\[
X_n=\operatorname{conv}\{P\mathbf e_e:e\in E\}\subset W.
\]
An orthonormal eigenbasis for \(W\) identifies this with the customary \(1\)-eigenpolytope up to an isometry; arbitrary nonorthonormal spectral coordinates do **not** preserve the stated metric radii. The statement concerns the Kneser pair graphs for all \(n\ge5\), not general \(KG(n,k)\), arbitrary Kneser eigenvalues, or affine rescalings.

## Proof
**1. The eigenprojection and the vertex shell.** Write \(J\) for an all-ones matrix of the appropriate size. Distinct edges of \(K_n\) are adjacent in \(G_n\) exactly when they are disjoint; consequently its adjacency matrix satisfies
\[
A_{G_n}=J_N+I_N-B^{\mathsf T}B.
\]
Since \(BB^{\mathsf T}=(n-2)I_n+J_n\), the matrix \(B\) has full row rank. On \(W=\ker B\), \(J_N\) vanishes, so \(A_{G_n}|_W=I_W\). On the constant line its eigenvalue is \(\binom{n-2}{2}>1\) and on the remaining \((n-1)\)-dimensional row space it is \(-(n-3)\). Thus \(W\) is exactly the \(1\)-eigenspace, of dimension \(d=N-n\).

The projector is \(P=I_N-B^{\mathsf T}(BB^{\mathsf T})^{-1}B\), and
\[
(BB^{\mathsf T})^{-1}=\frac{I_n}{n-2}-\frac{J_n}{(n-2)(2n-2)}.
\]
Each incidence column has two entries equal to \(1\), yielding
\[
\|P\mathbf e_e\|^2=P_{ee}=1-\frac{2}{n-1}=\frac{n-3}{n-1}=R_n^2.
\]
The points \(P\mathbf e_e\) are distinct because the off-diagonal entries of \(P\) are strictly smaller than \(P_{ee}\). They all have the same norm and thus are exposed vertices. Also \(\sum_eP\mathbf e_e=0\) and they affinely span \(W\), so \(0\) belongs to the interior of \(X_n\).

**2. The polar is a fractional perfect-matching polytope.** By the definition of polarity within \(W\),
\[
X_n^\circ=\{h\in W:\langle h,P\mathbf e_e\rangle=h_e\le1\ \text{for every }e\in E\}.
\]
The affine substitution \(h=\mathbf1_E-(n-1)y\) gives
\[
X_n^\circ\simeq F_n:=\{y\in\mathbb R^E_{\ge0}:By=\mathbf1_n\},
\]
because \(B\mathbf1_E=(n-1)\mathbf1_n\). This map is bijective and maps the uniform point \(y_e=1/(n-1)\) to \(h=0\).

We classify the vertices of \(F_n\) without relying on a black-box matching theorem. At a feasible point \(y\), an independent feasible perturbation in the set of positive coordinates exists precisely when the corresponding columns of \(B\) are linearly dependent. Therefore \(y\) is a vertex exactly when those columns are independent. In its positive-support graph, any leaf has a unique incident edge, whose weight must equal \(1\); the other endpoint has no additional positive edges, so this component is a single matched edge. Each other connected component has minimum degree at least two. Such a component has at least as many edges as vertices, while column independence allows at most as many edges as vertices, so it is a cycle. An even cycle has an alternating column dependence and is excluded. An odd cycle has independent unsigned incidence columns and forces each edge weight to equal \(1/2\). Conversely any disjoint union of matching edges of weight \(1\) and odd cycles of weight \(1/2\) has independent positive-support columns and is an extreme point.

**3. Exact norm maximization and the parity law.** Summing the equations \(By=\mathbf1_n\) gives \(\sum_e y_e=n/2\). Therefore, for \(h=\mathbf1_E-(n-1)y\),
\[
\|h\|^2=N-2(n-1)\sum_e y_e+(n-1)^2\sum_e y_e^2
=-N+(n-1)^2\sum_e y_e^2.
\]
For an extreme point let \(q\) denote the number of vertices covered by odd cycles. Then exactly \((n-q)/2\) other edges have weight \(1\), and \(q\) cycle edges have weight \(1/2\). Hence
\[
\sum_e y_e^2=\frac{n-q}{2}+\frac q4=\frac n2-\frac q4,
\qquad
\|h\|^2=\frac{n(n-1)(n-2)}2-\frac{(n-1)^2q}{4}.
\]
For even \(n\), the smallest feasible \(q\) is \(0\), attained precisely by perfect matchings. For odd \(n\), the smallest feasible \(q\) is \(3\), attained precisely by one triangle plus a perfect matching of the remaining vertices. Every other extreme point has strictly smaller norm. The resulting maximum squared norm of a polar vertex is
\[
M_n^2=\begin{cases}
\dfrac{n(n-1)(n-2)}2,&n\ \text{even},\\[4pt]
\dfrac{(n-1)(n-3)(2n-1)}4,&n\ \text{odd}.
\end{cases}
\]
The Euclidean norm is convex, so its maximum over the polar is attained at a vertex. The exact centered-inball radius is therefore \(r_n=1/M_n\). Each polar vertex indexes one facet of \(X_n\); equality \(\|h\|=M_n\) is exactly the condition for its supporting hyperplane \(\langle h,x\rangle=1\) to touch \(r_nB_2^W\). The corresponding facet vertices are those indexed by \(e\) for which \(h_e=1\), equivalently \(y_e=0\). The matching and triangle-plus-matching counts and vertex counts stated above follow.

**4. Uniqueness and the John–Löwner statement.** The symmetric group \(S_n\) permutes edges of \(K_n\) and acts orthogonally and transitively on the vertices of \(X_n\). Its action on \(W\) is irreducible over the reals: any matrix commuting with the pair-permutation action on \(\mathbb R^E\) has entries constant according as two edges are equal, intersect, or are disjoint. Hence it lies in the linear span of \(I_N\), \(B^{\mathsf T}B\), and \(J_N\). Its restriction to \(W\) is scalar. The orthogonal projector onto a nonzero proper invariant subspace of \(W\) would contradict this scalar restriction. Moreover the only \(S_n\)-fixed vector in \(W\) is \(0\).

Existence and uniqueness of the John and Löwner ellipsoids imply that each is invariant under this action. Its center is consequently \(0\), and its positive quadratic-form operator is a scalar by irreducibility. Each ellipsoid is therefore a Euclidean ball. The polar calculation fixes the John radius \(r_n\); the common vertex norm fixes the Löwner radius \(R_n\). As these extremal ellipsoids are unique, their centers are unique; a second maximum-radius inball or minimum-radius circumball would furnish a second volume-extremal ellipsoid, impossible.

For explicit optimality certificates, put \(u_h=h/M_n\) for polar vertices with maximal norm, and let \(T_n\) be this complete set. Symmetry makes \(T_n\) a single transitive orbit. The same scalar-commutant argument and trace imply
\[
\frac1{|T_n|}\sum_{h\in T_n}u_h=0,
\qquad \frac{d}{|T_n|}\sum_{h\in T_n}u_hu_h^{\mathsf T}=I_W.
\]
The corresponding inball tangent points are \(r_nu_h\), yielding a John contact certificate. For the enclosing ball, \(z_e=P\mathbf e_e/R_n\) obey
\[
\sum_{e\in E}z_e=0,
\qquad \frac dN\sum_{e\in E}z_ez_e^{\mathsf T}=I_W.
\]
These give an independent Löwner contact certificate.

## Verification
The standalone, integer-and-rational checker `artifacts/verify.py` exhaustively enumerates all fractional matching extreme supports and replays the norm and polar-center calculations for \(5\le n\le8\). It checks the exact spectral projector identity \(P^2=P\) and its diagonals. The respective numbers of polar extreme points for \(n=5,6,7,8\) are \(22,25,717,1057\); the inball touches \(10,15,105,105\) facets. A separate numerical convex-hull reconstruction for the Petersen case, `artifacts/check_petersen_hull.py`, independently finds \(22\) facets in two classes \((10\text{ of size }6,12\text{ of size }5)\) and \(10\) nearest facets. The all-dimensional theorem is proved in the four steps above; finite computations are not used as an infinite-dimensional certificate.

## Relationship to prior work
Martin Winter's 2020 eigenpolytope construction uses orthonormal eigenvectors and establishes the geometric normalization and symmetry framework; his complete preprint does not provide the fractional-matching polar description or these Euclidean ellipsoid formulas. Godsil's earlier distance-regular eigenpolytope work studies reconstruction of graph skeletons. Babecki's 2023 study of graphical designs, notably the Petersen eigenpolytope example, reports \(10\) vertices and \(22\) facets split into classes of \(10\) and \(12\), but does not give their Euclidean distances to the origin or the all-\(n\) metric theorem. The half-integrality of fractional perfect matchings is classical; the novelty asserted here is **not** that lemma, but its exact affine spectral-polar identification and the resulting metric parity law, full tangent-facet classification, and John–Löwner ellipsoids. The cited inaccessible earlier accounts of Petersen/distance-regular eigenpolytopes remain an originality risk; their available abstracts and secondary references do not establish a theorem implying the all-\(n\) result.

## Limitations
The formulas require the orthonormal eigenbasis normalization and \(n\ge5\). They do not extend automatically to other eigenspaces or higher-set Kneser graphs. The complete classification of every non-tangent facet is not a new claim; it follows as a consequence of the known fractional-matching extreme-point description. Historical coverage beyond the retrieved full texts cannot be excluded, including possible unlocated earlier calculations for the Petersen special case. The included finite checks reach only \(n=8\); the proof supplies the all-\(n\) argument.

## References
1. M. Winter, *Eigenpolytopes, Spectral Polytopes and Edge-Transitivity*, arXiv:2009.02179v1, first submitted 2020-09-04, §2 (definition and orthonormal normalization), https://arxiv.org/html/2009.02179v1 . First-listed mathematics classification: `51M20`.
2. M. Winter, *Spectral Realizations of Symmetric Graphs, Spectral Polytopes and Edge-Transitivity*, PhD dissertation, Technische Universität Chemnitz, 2021, ch. 3, https://martinwintermath.github.io/pdf/phd/thesis.pdf .
3. C. Babecki, *The Polyhedral Geometry of Graphical Designs*, PhD dissertation, University of Washington, 2023, Example 2.3.10, https://digital.lib.washington.edu/researchworks/items/0c48fe40-f79d-41c5-9492-8154ec8debd1 .
4. C. D. Godsil, *Eigenpolytopes of Distance Regular Graphs*, Canadian Journal of Mathematics 50 (1998), 739–755, https://doi.org/10.4153/CJM-1998-040-8 .
5. K. Chandrasekaran, L. A. Végh, S. S. Vempala, *The Cutting Plane Method is Polynomial for Perfect Matchings*, Mathematics of Operations Research 41 (2016), 23–48, https://doi.org/10.1287/moor.2015.0714 (classical half-integral odd-cycle support context).
