# A four-leaf principal-axis transition for vertex-uniform simplex-sum stellohedra

## Finding
For every integer \(m\ge 2\), put \(V=\{0,1,\ldots,m\}\), where \(0\) is the hub of the star graph, and define its *unit tube simplex-sum realization*
\[
 K_m=\sum_{S\subseteq[m]}\operatorname{conv}\{e_0,e_i:i\in S\}+\sum_{i=1}^m\{e_i\}\ \subset\mathbb R^{m+1}.
\]
The singleton terms are translations; the sum is an \(m\)-dimensional polytope in the affine hyperplane \(\sum_{i=0}^m x_i=m+2^m\). Let \(X_m\) be uniform on the *distinct vertices* of \(K_m\), not uniform in its interior. Define the truncated exponential polynomials \(F_m(z)=\sum_{j=0}^m z^j/j!\) and the rational numbers
\[
 b_m=\frac{F_m(2)}{F_m(1)},\qquad c_m=\frac{F_m(4)}{F_m(1)}.
\]
Set the unit hub-versus-leaves vector \(u=(m,-1,\ldots,-1)/\sqrt{m(m+1)}\) and the leaf-contrast projector \(P_{\perp}=\operatorname{diag}(0,I_m)-(1/m)(0,\mathbf1_m)(0,\mathbf1_m)^{\mathsf T}\). Then the exact covariance tensor and vertex barycenter are
\[
 \mathbb EX_m=\left(b_m,\ \left[1+\frac{2^m-b_m}{m}\right]\mathbf1_m\right),\quad
 \operatorname{Cov}(X_m)=\alpha_m uu^{\mathsf T}+\beta_m P_{\perp},
\]
where
\[
 \alpha_m=\frac{m+1}{m}(c_m-b_m^2),\qquad
 \beta_m=\frac{(m-3)4^m+3\cdot2^{m+1}b_m-(m+3)c_m}{3m(m-1)}.
\]
The intrinsic eigenvalues are \(\alpha_m\) once and \(\beta_m\) with multiplicity \(m-1\). There is an **exact principal-axis transition at four leaves**:
\[
 \alpha_m>\beta_m\quad(m=2,3),\qquad
 \beta_m>\alpha_m\quad(m\ge4).
\]
No equality case occurs for any integer \(m\ge2\). Moreover, as \(m\to\infty\),
\[
 b_m\to e,\qquad \alpha_m\to e^3-e^2,\qquad
 \beta_m\sim\frac{4^m}{3m},\qquad
 \frac{\beta_m}{\alpha_m}\sim\frac{4^m}{3m(e^3-e^2)}.
\]
Thus the hub-coordinate barycenter converges to Euler's number even as the leaf-contrast variance becomes exponentially larger than the hub-axis variance.

## Assumptions and scope
The ambient space uses ordinary Euclidean coordinate distance and no additional scaling. The graph has one hub and \(m\) labeled leaves, with all tube simplex-summands of coefficient one; the hub-only tube is included. The random variable is the *vertex-uniform* probability measure, not the intrinsic uniform-volume measure or a random normal direction. The theorem applies to every integer \(m\ge2\), while the one-leaf segment is excluded from the two-eigenspace assertion.

## Proof
**1. Complete vertex parametrization.** Every tube is either a singleton leaf or a hub-containing set \(\{0\}\cup S\), \(S\subseteq[m]\). Under a generic linear objective whose coordinates have distinct values, the exposed vertex of a simplex is the basis vector of the greatest-weight member. Let \(i_1,\ldots,i_k\) be the leaves ranking above the hub in decreasing objective weight; the remaining leaves rank below the hub. A hub-containing tube selects \(i_r\) exactly when its leaf subset contains \(i_r\) and none of \(i_1,\ldots,i_{r-1}\), giving \(2^{m-r}\) such tubes. The hub is selected in \(2^{m-k}\) tubes. Hence every vertex has coordinates
\[
 x_0=2^{m-k},\quad x_{i_r}=1+2^{m-r}\ (1\le r\le k),\quad x_j=1\ (j\notin\{i_1,\ldots,i_k\}).
\]
Every ordered list of distinct leaves above the hub is attained by a generic objective. Two such lists cannot give the same vertex: the hub coordinate determines \(k\), and the distinct powers of two recover the order of the \(k\) selected leaves. Since all vertices of a Minkowski sum are exposed by generic objectives, the parametrization is exhaustive. It gives \(N_m=\sum_{k=0}^m m!/(m-k)!=m!F_m(1)\) vertices.

**2. Exact hub distribution and leaf moments.** Write \(J=m-k\) and \(H=X_{m,0}=2^J\). Uniformity on the above vertices implies
\[
 \Pr\{J=j\}=\frac1{j!F_m(1)}\quad(0\le j\le m),\quad
 \mathbb EH=b_m,\quad\mathbb EH^2=c_m.
\]
Subtract the deterministic \(1\) from each leaf coordinate, obtaining the increment vector \(Y\in\mathbb R^m\). For a fixed list of length \(k\), its nonzero coordinates are exactly \(2^{m-1},\ldots,2^{m-k}\), in a uniformly random assignment to distinct leaves. Therefore, pointwise,
\[
 T=\sum_iY_i=2^m-H,\qquad U=\sum_iY_i^2=\frac{4^m-H^2}{3}.
\]
Exchangeability gives \(\mathbb EY_i=(2^m-b_m)/m\). This proves the stated barycenter.

**3. Intrinsic covariance eigenspaces.** Leaf permutation invariance forces the covariance tensor on the \(m\)-dimensional affine tangent space \(\{v:\sum_i v_i=0\}\) to act by scalars on the one-dimensional hub-versus-leaf axis and on the \((m-1)\)-dimensional leaf-contrast subspace. Along the displayed unit vector \(u\), the centered coordinate is \(\sqrt{(m+1)/m}(H-b_m)\), giving \(\alpha_m=(m+1)(c_m-b_m^2)/m\). The trace on the contrast subspace is \(\mathbb E\|Y-(T/m)\mathbf1_m\|^2=\mathbb E[U-T^2/m]\). Dividing by its dimension \(m-1\), substituting \(T,U\), and simplifying yields exactly the displayed formula for \(\beta_m\). This also proves the full covariance formula, including its zero eigenvalue on the ambient all-ones axis.

**4. Sharp transition.** Direct exact rational substitution gives
\[
\begin{array}{c|cc}
 m&\alpha_m&\beta_m\\\hline
2&9/5&1\\
3&69/16&27/8\\
4&6334/845&150/13\\
5&274968/26569&6616/163
\end{array}
\]
so the asserted strict inequalities hold for these four values. For every \(m\ge6\), a vertex with \(k\ge1\) has one largest leaf increment \(2^{m-1}\), with each other increment at most \(2^{m-2}\). The identity \(\sum_i(Y_i-T/m)^2=m^{-1}\sum_{i<j}(Y_i-Y_j)^2\) implies
\[
 \frac{\|Y-(T/m)\mathbf1_m\|^2}{m-1}\ \ge\ \frac{4^{m-2}}m
\]
for such a vertex. Because \(\Pr\{k\ge1\}=1-1/N_m\ge4/5\), we have \(\beta_m\ge(4/5)4^{m-2}/m\ge 512/15\). Meanwhile \(F_m(1)\ge5/2\), \(F_m(4)<e^4<(11/4)^4\), and \(\operatorname{Var}(H)\le\mathbb EH^2\), giving
\[
 \alpha_m<\frac76\cdot\frac25\left(\frac{11}{4}\right)^4<27.
\]
The lower bound for \(\beta_m\) exceeds \(34\); hence \(\beta_m>\alpha_m\) for all \(m\ge6\). The bound \(e<11/4\) follows, for instance, by bounding the factorial-series tail beyond its fourth term by a geometric series. Thus the transition proof has no unverified numerical step.

**5. Asymptotics.** The truncations satisfy \(F_m(t)\to e^t\) for each fixed positive \(t\), whence \(b_m\to e\) and \(c_m\to e^3\). The exact formula for \(\alpha_m\) gives its stated limit. In \(\beta_m\), the leading term is \((m-3)4^m/[3m(m-1)]\), while \(b_m,c_m\) are bounded and the remaining terms are lower order. This proves all four limits.

## Verification
Run `python verify.py` from a directory containing the accompanying standalone file. It independently computes every vertex as a generic-objective maximizer of every tube simplex for \(m=2,3,4,5,6\), removes duplicate vertices, constructs the full exact-rational covariance matrix, and compares the two intrinsic eigenvalues and barycenter with the formulas above. It additionally tests exact rational eigenvalue ordering for all integers from \(2\) through \(64\). Expected output is `STELLOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED dimensions=5 vertices= 2369 spectral_tests=63`. The all-dimensional conclusion follows from the proof, not from finite testing.

## Relationship to prior work
Padrol–Pilaud–Poullot (2021, arXiv:2109.09200, Theorem 2.2) gives the simplex-sum realization for graph associahedra, including stars. Eur–Huh–Larson (2022, arXiv:2207.10605) studies the stellahedron in a *different* uniform-matroid-independence-polytope realization; the two share a normal fan but must not be identified by Euclidean isometry. Berry–Forcey–Ronco–Showers (2016, arXiv:1608.08546) studies the combinatorial and algebraic structure of star-graph associahedra. These sources establish the natural objects and much of their face combinatorics but do not yield the exact uniform-*vertex* inertia spectrum or the strict four-leaf principal-axis switch. Known results on standard stellohedron inradii, enclosing spheres, Minkowski asymmetry, and directional-width distributions address different functionals or probability measures. No exhaustive priority guarantee is claimed.

## Limitations
The theorem concerns only the unit tube simplex-sum metric realization and vertex-uniform measure. A different stellohedron realization, different tube weights, or uniform intrinsic volume may have different covariance axes and transition parameters. The source checks reduce but cannot eliminate the possibility of an unindexed equivalent earlier result. No independent mathematical audit has been performed.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200 (first submitted September 19, 2021), especially §2.1.3 and Theorem 2.2.
2. C. Eur, J. Huh, M. Larson, *Stellahedral geometry of matroids*, arXiv:2207.10605 (first submitted July 21, 2022), pp. 3–4.
3. L. Berry, S. Forcey, M. Ronco, P. Showers, *Species substitution, graph suspension, and graded Hopf algebras of painted tree polytopes*, arXiv:1608.08546 (first submitted August 30, 2016).
4. S. Forcey, M. Ronco, *Algebraic structures on graph associahedra*, Journal of the London Mathematical Society 106 (2022), 1189–1231, DOI 10.1112/jlms.12596.
