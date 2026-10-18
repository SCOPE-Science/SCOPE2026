# Oriented unicycle imbalance determines vertex-inertia determinants of directed edge polytopes

## Finding
Let \(G=(V,E)\) be a connected finite simple graph with \(n=|V|\ge3\) and \(m=|E|\). Orient every edge arbitrarily, obtaining \(Q\). For an oriented edge \(u\to v\), set \(b_{uv}=e_u-e_v\), and consider the directed edge polytope \(P_Q=\operatorname{conv}\{b_e:e\in E\}\) in the Euclidean zero-sum space \(H=\{x\in\mathbb R^V:\sum_vx_v=0\}\). Give its \(m\) distinct vertices equal probability and let \(\Sigma_Q\) be their covariance operator on \(H\). The determinant \(\det_H\Sigma_Q\) is taken with respect to any orthonormal basis of \(H\); it is zero if the vertex cloud lies in a proper affine subspace.

For every spanning connected unicyclic edge set \(F\subseteq E\) (that is, \(|F|=n\) and \((V,F)\) is connected), let \(C(F)\) be its unique cycle, choose either direction around that cycle, and define its signed orientation imbalance
\[
\delta_Q(C)=\#\{e\in C:\text{arrow agrees with traversal}\}
-\#\{e\in C:\text{arrow opposes traversal}\}.
\]
Its square is independent of the traversal. Then the **all-graphs unicycle identity** is
\[
\boxed{\det_H\Sigma_Q=\frac{n}{m^n}\sum_{\substack{F\subseteq E:\ |F|=n\\(V,F)\ \mathrm{connected}}}\delta_Q(C(F))^2.}\tag{1}
\]
An empty sum is zero. In particular, \(\det_H\Sigma_Q>0\) if and only if at least one cycle of \(Q\) has nonzero orientation imbalance. Formula (1) is an exact Euclidean invariant of the vertex distribution, not the volume of \(P_Q\).

There is an equivalent effective-resistance or projection expression. Let \(B\) be the \(n\)-by-\(m\) oriented incidence matrix with columns \(b_e\), \(L=BB^{\mathsf T}\), \(s=B\mathbf1_m\), \(L^+\) the Moore–Penrose inverse, and \(\tau(G)\) the number of spanning trees. Then
\[
\boxed{\det_H\Sigma_Q=\frac{n\tau(G)}{m^n}\bigl(m-s^{\mathsf T}L^+s\bigr),\qquad
m-s^{\mathsf T}L^+s=\|\operatorname{proj}_{\ker B}\mathbf1_m\|^2.}\tag{2}
\]
Thus cycle-space projection of the all-ones edge vector determines an orientation-sensitive vertex-inertia determinant.

For a tournament \(Q\) on \(n\ge3\) vertices, \(G=K_n\), \(m=\binom n2\), and \(s_v=d_Q^+(v)-d_Q^-(v)\). The eigenvalues of \(\Sigma_Q\) on \(H\) are
\[
\frac nm\quad(\text{multiplicity }n-2),\qquad
\frac nm-\frac{\sum_vs_v^2}{m^2}\quad(\text{multiplicity }1),\tag{3}
\]
where coincident eigenvalues are combined. Consequently the exact orientation-weighted spanning-unicycle count is
\[
\boxed{\mathcal U(Q):=\sum_F\delta_Q(C(F))^2
=n^{n-2}\left(m-\frac1n\sum_vs_v^2\right).}\tag{4}
\]
Among all tournaments of a fixed order, \(\det_H\Sigma_Q\) and \(\mathcal U(Q)\) have **sharp, characterized extrema**: they are minimized exactly by transitive tournaments and maximized exactly by regular tournaments if \(n\) is odd, or near-regular tournaments (all \(|s_v|=1\)) if \(n\) is even. Explicitly,
\[
\boxed{\mathcal U_{\min}=n^{n-2}\frac{(n-1)(n-2)}6,\qquad
\mathcal U_{\max}=n^{n-2}\begin{cases}
\binom n2,&n\text{ odd},\\
\binom n2-1,&n\text{ even}.
\end{cases}}\tag{5}
\]
The spectral condition number of the positive-definite covariance satisfies the sharp bounds
\[
\boxed{\begin{cases}1,&n\text{ odd},\\\binom n2/(\binom n2-1),&n\text{ even}\end{cases}
\le\kappa(\Sigma_Q)\le\frac{3n}{n-2}.}\tag{6}
\]
The lower and upper equality classes are respectively regular/near-regular and transitive tournaments. For example, on four vertices, transitive and near-regular orientations have \(\mathcal U=16\) and \(80\) respectively, despite identical underlying graphs, vertex counts, and individual vertex norms.

## Assumptions and scope
Each underlying edge occurs exactly once and is given one arrow; opposite duplicate arrows, loops, and parallel edges are excluded. The zero-sum ambient subspace is equipped with its induced standard Euclidean metric. The covariance is centered and uses probabilities \(1/m\), not \(1/(m-1)\). Every incidence root is indeed an exposed vertex: its inner product with itself is \(2\), while its inner product with any distinct edge root in a simple orientation is strictly smaller than \(2\). The determinant in (1) remains well defined even in the affine-degenerate, semi-balanced case. For the complete graph \(m\ge n\); for trees, the sum in (1) is empty and the determinant vanishes.

## Proof
**1. Covariance and the augmented matrix.** Choose one graph vertex and delete its row from \(B\), giving \(B'\) of size \((n-1)\)-by-\(m\). Put \(L'=B'B'^{\mathsf T}\), \(s'=B'\mathbf1_m\). Directly from the equal-weight vertex distribution,
\[
\Sigma_Q=\frac1mBB^{\mathsf T}-\frac1{m^2}ss^{\mathsf T}.
\tag{7}
\]
Every row and column sums to zero. The determinant of the restriction of any such \(n\)-by-\(n\) symmetric matrix to \(H\) equals \(n\) times any principal cofactor (including when singular): use an orthonormal basis of \(H\) and the normal \(\mathbf1_n/\sqrt n\), or the adjugate formula. Therefore \(\det_H\Sigma_Q=n\det\Sigma'_Q\), where \(\Sigma'_Q=L'/m-s's'^{\mathsf T}/m^2\).

Form the \(n\)-by-\(m\) integer matrix \(M\) by placing the row \(\mathbf1_m^{\mathsf T}\) below \(B'\). The Schur complement of its lower-right entry \(m\) gives
\[
\det(MM^{\mathsf T})
=\det\begin{pmatrix}L'&s'\\s'^{\mathsf T}&m\end{pmatrix}
=m\det\left(L'-\frac1m s's'^{\mathsf T}\right)
=m^n\det\Sigma'_Q.
\tag{8}
\]
Cauchy–Binet now yields
\[
\det(MM^{\mathsf T})
=\sum_{S\subseteq E,\ |S|=n}\det(M_S)^2.
\tag{9}
\]

**2. Which minors survive?** If \(S\) does not connect all \(n\) vertices, the corresponding incidence matrix has rank at most \(n-c\), where \(c\ge2\) is its number of components. Appending one row increases rank by at most one, so the \(n\)-by-\(n\) determinant is zero. If \(S\) connects all vertices and has \(n\) edges, it is spanning unicyclic. Choose any edge \(f\) on its unique cycle and let \(T=S\setminus\{f\}\), a spanning tree. The reduced incidence matrix \(B'_T\) is unimodular, so \(\det B'_T=\pm1\). Write the unique tree-coordinate expansion \(b'_f=B'_T\alpha\), whose coefficients \(\alpha_e\in\{-1,0,1\}\) follow the unique path in \(T\) joining the endpoints of \(f\). In the matrix obtained by ordering the \(T\) columns before the \(f\) column, a Schur complement gives
\[
\det M_S=\pm\bigl(1-\sum_{e\in T}\alpha_e\bigr).
\tag{10}
\]
The expression in parentheses equals, up to sign, the sum of edge-orientation signs along the fundamental cycle: it is \(\delta_Q(C(S))\) or its negative, according to traversal. Therefore \(\det(M_S)^2=\delta_Q(C(S))^2\). Substituting into (8)–(9) and multiplying by \(n/m^n\) proves (1). Since every graph cycle extends to a spanning unicycle (extend the forest off that cycle without adding extra cycles), nonvanishing of (1) is equivalent to a cycle with nonzero imbalance.

**3. Laplacian pseudoinverse.** Connectivity makes \(L'\) positive definite, with \(\det L'=\tau(G)\) by the matrix-tree theorem. Schur complementing the upper-left block of (8) instead gives \(\det(MM^{\mathsf T})=\tau(G)(m-s'^{\mathsf T}L'^{-1}s')\). As \(s\perp\mathbf1_n\), the last quadratic form is \(s^{\mathsf T}L^+s\). The matrix \(B^{\mathsf T}L^+B\) is the orthogonal projection onto the row space of \(B\), so its complementary projection gives the final expression in (2).

**4. Tournament spectrum and extrema.** For \(G=K_n\), the graph Laplacian is \(L=nI-J\), hence equals \(nI\) on \(H\). Equation (7) is therefore a scalar operator minus the rank-one form \(ss^{\mathsf T}/m^2\), proving (3). Cayley’s formula gives \(\tau(K_n)=n^{n-2}\); inserting \(L^+s=s/n\) into (2) proves (4).

For each \(k\in\{1,\ldots,n-1\}\) and each \(k\)-vertex set \(A\), the internal arrows cancel in \(\sum_{v\in A}s_v\), while each cross-edge contributes at most \(1\). Thus \(\sum_{v\in A}s_v\le k(n-k)\). If the scores are put in nonincreasing order, these are precisely their partial-sum majorization inequalities against the transitive score vector \((n-1,n-3,\ldots,1-n)\), whose partial sums equal \(k(n-k)\). Strict convexity of the square function gives
\[
\sum_vs_v^2\le\sum_{j=1}^n(n+1-2j)^2=\frac{n(n^2-1)}3,
\tag{11}
\]
with equality only when that score multiset is transitive; by removing successively its unique maximal-score vertices, the whole orientation is transitive. Each \(s_v=2d_v^+-(n-1)\), so \(s_v\) is even for odd \(n\), odd for even \(n\). Hence \(\sum s_v^2\ge0\) for odd \(n\) and at least \(n\) for even \(n\), with equality precisely for regular or near-regular degree sequences. Odd cyclic tournaments attain \(s\equiv0\). For even \(n\), take a regular tournament on \(n-1\) vertices, add one vertex whose wins/losses split the old vertices into subsets of sizes \((n-2)/2\) and \(n/2\); this gives \(n/2\) scores \(+1\) and \(n/2\) scores \(-1\). Every bound is therefore attained. Inserting the endpoints into (3)–(4) proves (5)–(6); the worst condition number is \(1/(1-2(n+1)/(3n))=3n/(n-2)\).

## Verification
The accompanying pure-standard-library `checker.py` independently constructs the centered integer covariance cofactor and enumerates every spanning unicycle by selecting \(n\) edges and peeling leaves to isolate its cycle. It uses fraction-free exact determinants and integer signed cycle imbalances. It passed 172 pseudorandom but reproducibly seeded oriented simple graphs of orders \(3\) through \(6\), all 1,096 labeled tournaments on \(3\) through \(5\) vertices for the determinant and score identities (with direct cycle enumeration for selected tournaments), and all 32,768 tournaments on six vertices for the sharp score extrema. It also checked global reversal symmetry of the unicycle sum. All finite checks were exact. The proof, not those samples, establishes the theorem for every admissible order and orientation.

## Relationship to prior work
Kálmán and Tóthmérész developed directed root polytopes and distinguished semi-balanced cycle orientations through potential functions, together with spanning-tree dissections and Ehrhart theory. Numata, Takahashi, and Tamaki proved a full rank-function dimension dichotomy and characterized faces. Their dimension criteria agree with the vanishing case of (1), but neither work states the centered Euclidean vertex-covariance determinant, the sum of squared imbalances over **all spanning unicycles**, or sharp tournament covariance extrema. A published exact Ehrhart classification for a *single oriented cycle* gives lattice simplex volume equal to the absolute cycle imbalance; that supplies a related special case but not the all-graph sum or tournament optimization. Classical Cauchy–Binet and the matrix-tree theorem are used openly as established tools. Published results on transitive-tournament minimum enclosing spheres, and on rank-function common vertex spheres, concern different Euclidean extrema and do not determine (1)–(6). Signed-graph net-Laplacian determinant formulas involve signed incidence operators, rather than centered covariance of singly oriented ordinary incidence roots; they do not imply the squared integer cycle-discrepancy sum here.

## Limitations
The theorem assumes connected **simple** graphs with precisely one direction per edge. The determinant concerns the canonical centered equal-vertex-mass covariance, not the polytope's volume, its optimal enclosing ellipsoid, or a graph Laplacian's determinant. Formula (6) is a tournament statement, not a claim about arbitrary digraphs. Existing results for semibalanced or single-cycle special cases are not claimed as new. A residual bibliographic possibility is an equivalent formula expressed as an augmented-incidence or cycle-space determinant in general matrix/minor literature; it has not been eliminated by targeted searches. No independent mathematical audit has yet been performed.

## References
1. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v1, publicly posted 2021-05-03; *Mathematika* 68 (2022), 1176–1220.
2. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, publicly posted 2022-03-28; *Australasian Journal of Combinatorics* 88 (2024), 77–96.
3. *Exact Ehrhart polynomials of oriented cycle root polytopes*, publicly released 2026-10-04; compared at the statement and proof level for its single-cycle volume specialization.
4. Sudipta Mallik, *Matrix tree theorem for the net Laplacian matrix of a signed graph*, arXiv:2210.03711 (2022); a different signed-incidence determinant setting.
5. Cayley's spanning-tree formula, the matrix-tree theorem, Cauchy–Binet, and classical tournament score-sequence majorization (used as background identities).
