# Subtree hook sizes diagonalize covariance and sharply bound isotropy of rooted-tree marked-poset polytopes

## Finding
For any finite rooted tree \(T\) on \(n\ge 2\) vertices, order the vertices by ancestry and write \(h_v\) for the number of vertices in the subtree rooted at \(v\), including \(v\). Its order polytope is
\[
O(T)=\{x\in[0,1]^V:x_{p(v)}\le x_v\text{ for every nonroot }v\}.
\]
For parameters \(0\le t_v\le1\) on nonroot vertices, let \(K_T(t)\) be its image under the triangular transfer \(y_{\mathrm{root}}=x_{\mathrm{root}}\), \(y_v=x_v-t_vx_{p(v)}\). This is the unique-predecessor specialization of the continuous marked-poset transfer family [1]. Its volume is \(\prod_vh_v^{-1}\), independently of \(t\).

**Exact covariance and optimal Euclidean position.** At the unique parameter vector
\[
t_v^*=\frac{h_v}{h_v+1}\qquad(v\ne\mathrm{root}),
\]
the covariance matrix of the uniform measure on \(K_T(t^*)\) is diagonal in the displayed \(y\)-coordinates, with diagonal entries
\[
\beta_v=\frac{h_v}{(h_v+1)^2(h_v+2)}\prod_{a\prec v}\frac{h_a}{h_a+2},
\]
where \(a\prec v\) ranges over strict ancestors. Moreover, if \(J_T(t)\) is the centered mean squared Euclidean norm, then
\[
J_T(t)=\sum_{v\in V}\beta_v+\sum_{v\ne\mathrm{root}}(t_v-t_v^*)^2\operatorname{Var}(X_{p(v)}),
\]
where \(X\) is uniform on \(O(T)\). Thus \(t^*\) is the unique Euclidean inertia minimizer within this transfer family.

**Isotropy factorization and sharp shape extremals.** With the standard affine-invariant isotropic constant \(L\), normalized by \(L_K^{2n}=\det\operatorname{Cov}(\operatorname{Unif}(K))/\operatorname{vol}_n(K)^2\), define
\[
F(k)=\frac{k^{k+2}}{(k+1)^2(k+2)^k},\qquad k\ge1.
\]
Then every transfer parameter has precisely the same invariant
\[
L_{K_T(t)}^{2n}=L_{O(T)}^{2n}=\prod_{v\in V}F(h_v).
\]
Over all rooted trees on \(n\) vertices this gives the sharp bounds
\[
F(n)12^{-(n-1)}\ \le\ L_{O(T)}^{2n}\ \le\ \frac{(n!)^2}{(n+1)^{n+1}(n+2)^n}.
\]
For \(n\ge3\), equality on the left holds precisely for rooted stars, and equality on the right precisely for rooted paths. The corresponding isotropic constants approach \(1/\sqrt{12}\) along stars and \(1/e\) along paths.

## Assumptions and scope
The rooted tree is finite, with one distinguished minimal root; every other vertex has exactly one parent. The order polytope has the standard ambient Euclidean metric of \(\mathbb R^n\). The transfer parameters are real and lie in \([0,1]\). All variances and covariances are with respect to normalized \(n\)-dimensional Lebesgue measure. The extremal classifications refer to rooted-tree isomorphism classes. The root's transfer parameter is omitted because its predecessor is fixed at zero. The marked-poset interpretation adjoins fixed lower and upper endpoints with markings \(0\) and \(1\).

## Proof
**1. Independent subtree spacings.** For a uniform point \(X\) in the order polytope, set \(X_{p(r)}=0\) for the root and
\[
B_v=\frac{X_v-X_{p(v)}}{1-X_{p(v)}}.
\]
This is defined almost surely since parent coordinates equal one only on a null set. The inverse is \(X_v=X_{p(v)}+(1-X_{p(v)})B_v\). In parent-first order the Jacobian determinant is \(\prod_v(1-X_{p(v)})\). Because \(1-X_v=(1-X_{p(v)})(1-B_v)\), each \(1-B_v\) occurs once for each strict descendant and therefore the Jacobian is \(\prod_v(1-B_v)^{h_v-1}\). Integrating over the unit cube proves
\[
\operatorname{vol}_n O(T)=\prod_v h_v^{-1},\qquad B_v\stackrel{\mathrm{ind}}\sim\operatorname{Beta}(1,h_v).
\]
In particular \(\mathbb EB_v=(h_v+1)^{-1}\), \(\operatorname{Var}(B_v)=h_v/[(h_v+1)^2(h_v+2)]\), and \(\mathbb E(1-B_v)^2=h_v/(h_v+2)\).

**2. Orthogonal innovations.** At \(t_v^*=h_v/(h_v+1)\), the transferred coordinate is
\[
Y_v^*=\frac1{h_v+1}+(1-X_{p(v)})\left(B_v-\frac1{h_v+1}\right).
\]
The root case uses \(X_{p(r)}=0\). Conditional on the independent preceding spacing variables, the centered parenthesized term has mean zero. For any two distinct vertices, condition on the later one in a parent-first order: its centered innovation has conditional mean zero, whereas every earlier coordinate is measurable. Hence all off-diagonal covariances vanish. Also
\[
\mathbb E(1-X_{p(v)})^2=\prod_{a\prec v}\mathbb E(1-B_a)^2=\prod_{a\prec v}\frac{h_a}{h_a+2},
\]
proving \(\operatorname{Var}(Y_v^*)=\beta_v>0\). For general \(t\), the exact decomposition \(Y_v(t)=Y_v^*+(t_v^*-t_v)X_{p(v)}\) and conditional orthogonality \(\operatorname{Cov}(Y_v^*,X_{p(v)})=0\) imply \(\operatorname{Var}(Y_v(t))=\beta_v+(t_v-t_v^*)^2\operatorname{Var}(X_{p(v)})\). Sum the variances to obtain \(J_T(t)\). Every nonroot parent has positive variance because its coordinate is nonconstant on an open subset; hence uniqueness.

**3. Isotropic product.** The transfer map is triangular with unit diagonal, so it preserves volume and covariance determinant. Multiplying \(\beta_v\), each ancestor \(a\) contributes its factor \(h_a/(h_a+2)\) for exactly \(h_a-1\) strict descendants. Consequently
\[
\det\operatorname{Cov}(Y^*)=\prod_v\frac{h_v^{h_v}}{(h_v+1)^2(h_v+2)^{h_v}}.
\]
Divide by \(\operatorname{vol}_n(O(T))^2=(\prod_vh_v)^{-2}\) to obtain the asserted \(\prod_vF(h_v)\).

**4. Strict monotonicity and sharp trees.** Extend \(F\) to \(x>0\). Direct differentiation gives
\[
\frac{d}{dx}\log F(x)=-\log(1+2/x)+\frac2{x+2}+\frac2{x(x+1)}>0.
\]
Indeed \(\log(1+y)<y-y^2/[2(1+y)]\) for \(y>0\) follows by integrating \(t/(1+t)\); substituting \(y=2/x\) leaves the strictly positive lower bound \(2/[x(x+1)(x+2)]\). Every rooted tree has one vertex of subtree size \(n\) and all others have sizes at least one. This yields the star lower bound, with equality exactly when every nonroot vertex is a leaf.

For the upper bound, write the subtree sizes in descending order as \(h_{(1)}\ge\cdots\ge h_{(n)}\). Then \(h_{(j)}\le n-j+1\): among any \(j\) vertices with subtree size at least \(h_{(j)}\), choose one of maximum depth. Its subtree contains at least \(h_{(j)}\) vertices, and the remaining \(j-1\) chosen vertices are outside that subtree, so \(n\ge h_{(j)}+j-1\). Strict increase of \(F\) gives \(\prod_jF(h_{(j)})\le\prod_{k=1}^nF(k)\). The factors telescope to the asserted factorial expression. Equality requires a subtree of size \(n-1\) and then recursively the rooted path. The star and path asymptotics follow from \(F(n)\to e^{-2}\) and Stirling's formula for the factorial expression, respectively.

## Verification
The standalone \(\texttt{checker.py}\) performs independent rational-moment integrations over every linear extension of each of 154 parent-labeled rooted trees through six vertices and three additional seven-vertex examples. It checks the known hook-volume, all coordinate means and covariances, the full diagonal innovation formula, and both sharp extremal inequalities and their equality criteria. Executing \(\texttt{python checker.py}\) prints \(\texttt{VERIFY_OK exact_rooted_trees= 157 rational_equalities= 7602}\). The arbitrary-size theorem is proved above; a finite exact checker is corroboration, not an exhaustive proof of the infinite family.

## Relationship to prior work
Fang, Fourier, Litza and Pegel [1] introduced the continuous marked-poset family and its transfer-map geometry; the unique-parent shear used here is their specialization, not a new polytope definition. Stanley [2] established the order-polytope framework, and the rooted-tree hook product is a classical linear-extension/volume consequence. The new assertions concern the exact covariance diagonalization, unique minimal inertia parameter, all-tree isotropic product and sharp star/path rigidity. Previous results about inradii of marked/order polytopes and isotropic constants of Hanner polytopes cover different metric functionals or different polytope families; no implication giving these claims was found in the searched literature. Equivalent but differently formulated moment formulas remain possible.

## Limitations
Only rooted trees (every nonroot element has one lower cover) are covered; arbitrary posets can have multiple predecessors and the independent-beta argument fails. The Euclidean inertia optimization is only among this specified transfer family, not among arbitrary volume-preserving affine images. This is an analytical proof with exact low-dimensional checks, not an independent audit or an exhaustive bibliographic uniqueness certificate. Stronger general isotropic inequalities are not claimed.

## References
[1] X. Fang, G. Fourier, J.-P. Litza, C. Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037v1 (first posted 2017-12-04); SIAM Journal on Discrete Mathematics 34 (2020), 611–639. DOI: 10.1137/18M1228529.

[2] R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. DOI: 10.1007/BF02187680.
