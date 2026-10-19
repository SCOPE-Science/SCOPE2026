# Dodecahedral cubic-harmonic erasure ranks from the Petersen–Kneser matroid

## Finding

Let \(X\) be the twenty vertices of a regular dodecahedron, normalized to lie on the unit sphere, and let \(\mathcal H_{\le3}=\bigoplus_{j=0}^3\mathcal H_j(S^2)\), the 16-dimensional space of spherical harmonics of degrees at most three. For each erased subset \(T\subseteq X\), let \(R_T\) denote evaluation of \(\mathcal H_{\le3}\) on \(X\setminus T\).

There is a natural graph on the ten antipodal pairs of \(X\): two pairs are adjacent when the squared scalar product of any two representatives of **unnormalized radius \(\sqrt3\)** is \(5\). This graph is the Petersen graph, hence can be identified with the ten two-element subsets of \(\{1,2,3,4,5\}\), adjacent when disjoint. For an erasure set \(T\), form the graph \(H_T\) on five labeled vertices whose edges are precisely the two-subsets corresponding to antipodal pairs touched by \(T\). Let \(b(H_T)\) count its bipartite connected components **including isolated vertices**. Set \(\delta(H_T)=1\) exactly when each bipartite component admits a two-coloring with equally many vertices of each color; if some component is unbalanced set \(\delta(H_T)=0\). The condition is vacuous when no bipartite component exists.

Then, for **every one of the \(2^{20}\) erasure patterns**, the evaluation rank is exactly

\[
\boxed{\operatorname{rank} R_T=16-|T|+5-b(H_T)-\delta(H_T).}
\]

In particular, among the \(\binom{20}{4}=4845\) choices of four erasures, precisely \(2960\) preserve unique reconstruction of all cubic spherical harmonics. The full four-erasure rank distribution is

\[
\#\{T:|T|=4,\operatorname{rank}R_T=j\}
=\begin{cases}45&j=14,\\1840&j=15,\\2960&j=16,\\0&\text{otherwise.}\end{cases}
\]

For four erased vertices occupying four distinct antipodal pairs, reconstruction fails **if and only if** the corresponding four edges of \(K_5\) form a four-cycle, or form a triangle together with a disjoint edge. In each other case it succeeds. Any erasure containing a complete antipodal pair fails to preserve rank sixteen.

## Assumptions and scope

Everything is over \(\mathbb R\) or \(\mathbb C\); the ranks coincide because evaluation entries are real. Sampling is by point evaluation at distinct vertices, not by integration or weighted quadrature. The result concerns precisely the ordinary regular dodecahedron and degree at most three, with *arbitrary* subsets of vertices deleted. Coordinates can be scaled without affecting rank. Write \(\varphi=(1+\sqrt5)/2\). One unnormalized realization is

\[
X_0=\{(\pm1,\pm1,\pm1)\}\cup
\{(0,\pm\varphi^{-1},\pm\varphi),
(\pm\varphi^{-1},\pm\varphi,0),
(\pm\varphi,0,\pm\varphi^{-1})\}.
\]

The coordinates have squared length \(3\); set \(X=X_0/\sqrt3\). Label the antipodal representatives in the deterministic order described in `check_dodeca.py`; the corresponding \(K_5\)-edge labels, in that order, are
\((12),(13),(14),(15),(34),(45),(35),(25),(23),(24)\), where \((ij)\) abbreviates the unordered edge with endpoints \(i,j\). This makes the graph construction entirely reproducible; a different Petersen-graph isomorphism yields the same rank.

## Proof

**1. Even–odd interpolation blocks.** On the radius-\(\sqrt3\) sphere, polynomial restrictions of degree at most three are represented by monomials with exponent of the third coordinate at most one, since \(z^2=3-x^2-y^2\). Splitting by antipodal parity gives a 6-dimensional even space (degrees zero and two) and a 10-dimensional odd space (degrees one and three). Choose one vertex \(y_i\) from each of the ten antipodal pairs. The exact determinant of the 10-by-10 odd-monomial evaluation matrix on these representatives is \(1024\); for the even basis \(1,x^2,y^2,xy,xz,yz\), the first six representatives give a 6-by-6 minor of determinant \(32\). These are exact computations in \(\mathbb Q(\sqrt5)\), explicitly reconstructed in the accompanying checker. Thus the full 20-by-16 evaluation matrix \(A\) has rank sixteen, with a four-dimensional left nullspace. The odd evaluation block is invertible on the ten representatives, so this left nullspace is constant on each antipodal pair and is the left nullspace of the ten-by-six even evaluation matrix.

**2. The Petersen spectral realization.** For the ten representatives, define \(B_{ij}=1\) when \(i\ne j\) and \((y_i\cdot y_j)^2=5\), and \(B_{ij}=0\) otherwise. Direct substitution into the displayed coordinates yields exactly the Petersen adjacency matrix, with the edge labeling given above, and the identity \(B^2=2I-B+J\) (\(J\) is the all-ones matrix). Consequently its three eigenspaces have eigenvalues \(3,1,-2\) and multiplicities \(1,5,4\), respectively.

The column of constants in the even evaluation matrix is a \(3\)-eigenvector of \(B\). Each column corresponding to one of the five independent traceless quadratics \(x^2-1,y^2-1,xy,xz,yz\) is a \(1\)-eigenvector, by direct coordinate substitution. As the six columns are independent by step 1, they fill exactly the \(3\)- and \(1\)-eigenspaces. Hence the left nullspace is the \((-2)\)-eigenspace. Its orthogonal projector is

\[
P_{-2}=\frac{5I-5B+J}{15}.
\]

**3. The centered edge-incidence Gale vectors.** Match each antipodal pair with its edge \(e=\{a,b\}\) of \(K_5\), and set

\[
 z_e=\mathbf e_a+\mathbf e_b-\tfrac25\mathbf1\in\mathbf1^\perp\subset\mathbb R^5.
\]

The direct inner-product identity is

\[
 (z_e\cdot z_f)_{e,f}=\frac{5I-5B+J}{5}=3P_{-2}.
\]

Thus the four-dimensional left nullspace of \(A\), represented as a matrix with one row at each vertex, has exactly the same row-dependence structure as the ten vectors \(z_e\), each repeated across its antipodal pair. (A common nonsingular change of Gale coordinates and nonzero uniform rescaling do not alter rank.) For a touched pair set \(S_T\) and erased vertex set \(T\), it follows that the restricted left-null matrix has rank \(\operatorname{rank}\{z_e:e\in E(H_T)\}\).

Since the full evaluation matrix has rank sixteen and left-null dimension four, deleting \(|T|\) rows yields, by the rank-nullity formula for the coordinate restriction of that left nullspace,

\[
\operatorname{rank}R_T=16-|T|+
\operatorname{rank}\{z_e:e\in E(H_T)\}.
\]

**4. Graph-theoretic rank.** Let \(C\) be the 5-by-\(|E(H_T)|\) unsigned vertex–edge incidence matrix of \(H_T\), with each column equal to \(\mathbf e_a+\mathbf e_b\), and let \(Q=I-\mathbf1\mathbf1^{\mathsf T}/5\). The matrix of Gale vectors is \(QC\). Each connected nonbipartite component has full incidence-row rank; each connected bipartite component contributes exactly one left-null vector, with signs \(+1\) and \(-1\) on its two parts. Isolated vertices are bipartite components of size one. Hence \(\operatorname{rank}C=5-b(H_T)\).

The projection \(Q\) reduces this rank by one precisely when \(\mathbf1\) lies in the column space of \(C\). By orthogonality to all the signed left-null vectors just described, this occurs precisely when every bipartite connected component is balanced. Therefore

\[
\operatorname{rank}(QC)=5-b(H_T)-\delta(H_T),
\]

which proves the all-erasure formula.

**5. Sharp four-erasure count.** If four erased vertices occupy fewer than four antipodal pairs, the Gale vectors have rank at most three, so rank sixteen is impossible. For four distinct pairs, four centered edge-incidence columns on \(K_5\) are dependent precisely in two cases: their edges form a four-cycle (the alternating unsigned-incidence relation), or form a triangle and a disjoint edge (their incidence span contains \(\mathbf1\)). This follows also by applying the rank formula in step 4 to every isomorphism type of a four-edge simple graph on five vertices. There are \(3\binom54=15\) four-cycles and \(\binom53=10\) triangle-plus-disjoint-edge sets among \(\binom{10}4=210\) choices. Every four-pair selection has \(2^4=16\) sign choices. Consequently the number of rank-sixteen erasures is \((210-15-10)16=2960\). Exactly \(\binom{10}2=45\) four-vertex erasures consist of two complete antipodal pairs; they give rank fourteen. All remaining \(4845-2960-45=1840\) give rank fifteen. This establishes the stated distribution.

## Verification

Run `python3 check_dodeca.py` with Python 3 and no optional dependencies. The checker represents every coordinate in the exact quadratic field \(\mathbb Q(\varphi)\), where \(\varphi^2=\varphi+1\), and uses rational Gaussian elimination. Its assertions verify both nonzero determinants, the Petersen-graph identification, the spectral identities, the centered-incidence Gram identity, all \(2^{10}=1024\) graph-edge subsets for the graph-rank formula, every one of the \(\binom{20}4=4845\) four-vertex erasure sets, and the six induced graph types for four touched pairs. Expected final output begins `EXACT_VERIFY_OK` and reports rank multiplicities `[(14, 45), (15, 1840), (16, 2960)]`. These exact finite checks supplement the graph-theoretic proof; there is no extrapolation from a finite census to an unspecified infinite family.

## Relationship to prior work

The classical spherical-polynomial interpolation literature establishes 16 as the degree-three dimension and constructs special unisolvent nodes, but does not in the examined statements determine which four vertices may be erased from a fixed dodecahedral sampling grid. Classical optimal spherical-harmonic design results address quadrature or information-matrix criteria rather than this deletion matroid. Recent work on antipodally symmetric interpolation–regression develops the even–odd block principle and rank-based greedy selection for general nodes, but does not identify the exact Petersen-graph or \(K_5\) incidence rank classification. The parity splitting is known; the specific cubic dodecahedral Gale identification and resulting exhaustive erasure rule are the proposed new result.

## Limitations

The result is a complete algebraic rank classification for one exact twenty-point sampling geometry. It does not estimate conditioning of nearly singular submatrices, treat perturbed dodecahedra, or classify other harmonic degrees. An equivalent description in older graph-eigenspace, spherical-design, or finite-matroid literature cannot be categorically excluded without broader independent scrutiny. Only self-review has been performed, not independent audit.

## References

1. W. zu Castell, N. Laín Fernández, and Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, arXiv:math/0407448v1 (public July 27, 2004), https://arxiv.org/abs/math/0407448.
2. H. Dette, V. B. Melas, and A. Pepelyshev, *Optimal designs for three-dimensional shape analysis with spherical harmonic descriptors*, arXiv:math/0603075v1 (public March 3, 2006), https://arxiv.org/abs/math/0603075.
3. F. Dell’Accio, F. Nudo, T. E. Pérez, and M. A. Piñar, *Polynomial interpolation–regression on the sphere*, arXiv:2605.13124v1 (public May 13, 2026), https://arxiv.org/abs/2605.13124.
