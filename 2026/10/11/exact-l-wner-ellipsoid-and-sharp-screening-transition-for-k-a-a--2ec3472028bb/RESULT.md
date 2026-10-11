# Exact Löwner ellipsoid and sharp screening transition for \(K_{a,a,b}\) symmetric edge polytopes

## Finding

For every pair of integers \(a\ge2\) and \(b\ge1\), the symmetric edge polytope of the complete tripartite graph with class sizes \(a,a,b\) has a uniquely determined minimum-volume enclosing Euclidean ellipsoid, with the following explicit shape, spectrum and contact transition. All metric statements refer to the intrinsic Euclidean metric on the zero-sum hyperplane, not to an arbitrary unimodular realization.

Write \(n=2a+b\), \(d=n-1\), and
\[
\Delta=16a^2-8ab-8a+b^2+14b+1,\qquad
 t=\begin{cases}
 \dfrac{2a-2b-2+\sqrt\Delta}{3(2a+b-1)},&b<2a+1,\\
0,&b\ge2a+1.
\end{cases}
\]
Let \(A_1,A_2,B\) be the vertex classes, let \(r_{uv}=e_u-e_v\), and put
\[
C_t=\frac{t}{a^2}\sum_{u\in A_1,\ v\in A_2}r_{uv}r_{uv}^{\mathsf T}
+\frac{1-t}{2ab}\sum_{u\in A_1\cup A_2,\ v\in B}r_{uv}r_{uv}^{\mathsf T}.
\]
On the hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), the **unique Löwner ellipsoid** is
\[
E=\{x\in H:\ x^{\mathsf T}(dC_t|_H)^{-1}x\le1\}.
\]
Its center is the origin; its squared semiaxes are exactly
\[
\begin{array}{c|c}
\text{squared semiaxis}&\text{multiplicity}\\\hline
\dfrac{d(1+t)}{2a}&2(a-1)\\
\dfrac{d(1-t)}{b}&b-1\\
\dfrac{d(1+3t)}{2a}&1\\
\dfrac{dn(1-t)}{2ab}&1.
\end{array}
\]
The row of multiplicity \(b-1\) is empty if \(b=1\). Consequently, with \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\), its exact intrinsic Euclidean volume is
\[
\operatorname{vol}_d(E)=\kappa_d
\left(\frac{d(1+t)}{2a}\right)^{a-1}
\left(\frac{d(1-t)}b\right)^{(b-1)/2}
\sqrt{\frac{d(1+3t)}{2a}\frac{dn(1-t)}{2ab}}.
\]

There is a sharp **edge-root screening transition**: all \(4ab\) signed roots from edges between \(A_1\cup A_2\) and \(B\) lie on \(\partial E\) for every parameter pair. The \(2a^2\) signed roots from edges between \(A_1\) and \(A_2\) also lie on \(\partial E\) precisely if \(b\le2a+1\); if \(b>2a+1\), every such root is strictly interior. Thus the number of contacting vertices is \(4ab+2a^2\) at and below the threshold and \(4ab\) above it.

Moreover, for \(b\ge2a+1\), the same ellipsoid is the Löwner ellipsoid of the strict subpolytope \(P_{K_{2a,b}}\): the extra roots between the two \(a\)-classes are geometrically screened, although they still define genuine vertices of the larger polytope. At the equality threshold they touch without changing the enclosing ellipsoid.

## Assumptions and scope

The graph \(K_{a,a,b}\) is finite and simple with three disjoint nonempty vertex classes of sizes \(a,a,b\), where \(a\) and \(b\) are positive integers satisfying \(a\ge2\). The polytope is
\[
P_G=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(G)\}\subset H.
\]
Connectivity implies that its affine span is all of the \(d\)-dimensional space \(H\). The coordinates \(e_v\) are the standard orthonormal basis of \(\mathbb R^n\). All roots have squared Euclidean norm two; any other metric or a general unimodular equivalence changes the ellipsoid data. Matrix inverses, determinants and volume are understood intrinsically on \(H\).

## Proof

**1. Eigenvalues of the weighted Laplacian.** The coefficients of \(C_t\) are nonnegative for \(0\le t<1\), and its total edge weight equals
\[
a^2(t/a^2)+2ab((1-t)/(2ab))=1.
\]
The graph of strictly positive-weight edges is connected for \(t<1\), so \(C_t\) is positive definite on \(H\). Splitting \(H\) orthogonally into within-\(A_1\) and within-\(A_2\) zero-sum spaces (total dimension \(2a-2\)), the within-\(B\) zero-sum space (dimension \(b-1\)), the difference of the two \(A\)-class means (dimension one), and the contrast between the combined \(A\) classes and \(B\) (dimension one), direct Laplacian multiplication gives the four eigenvalues of \(C_t|_H\):
\[
\frac{1+t}{2a},\qquad
\frac{1-t}{b},\qquad
\frac{1+3t}{2a},\qquad
\frac{n(1-t)}{2ab},
\]
with the multiplicities recorded above. This proves the proposed spectrum and volume once optimality is established.

**2. Solve the single design parameter.** Up to a constant independent of \(t\), the log determinant on \(H\) is
\[
F(t)=(2a-2)\log(1+t)+\log(1+3t)+b\log(1-t).
\]
Its second derivative is strictly negative on \([0,1)\). Since \(F'(0)=2a+1-b\) and \(F'(t)\to-\infty\) as \(t\uparrow1\), the maximum is at \(t=0\) exactly when \(b\ge2a+1\), and otherwise at the unique positive solution of
\[
\frac{2a-2}{1+t}+\frac{3}{1+3t}-\frac b{1-t}=0.
\]
Multiplying by its positive denominator and applying the quadratic formula yields the stated radical expression. Strict concavity ensures it lies in \((0,1)\).

**3. Verify every vertex and its contact.** Let \(S_A\) be the average \(r_{uv}r_{uv}^{\mathsf T}\) over the \(a^2\) edges joining the two \(A\)-classes, and let \(S_B\) be the corresponding average over the \(2ab\) cross-\(B\) edges. Then \(C_t=tS_A+(1-t)S_B\). Define
\[
\ell_A=\operatorname{tr}((dC_t|_H)^{-1}S_A),\qquad
\ell_B=\operatorname{tr}((dC_t|_H)^{-1}S_B).
\]
Permutation symmetry gives the same squared ellipsoid gauge \(\ell_A\) to each signed root of the first class and \(\ell_B\) to each signed root of the second class. By differentiating the determinant and using \(\operatorname{tr}(C_t^{-1}C_t)=d\),
\[
F'(t)=d(\ell_A-\ell_B),\qquad t\ell_A+(1-t)\ell_B=1.
\]
At an interior maximizer \(F'(t)=0\), both leverages equal one. At \(t=0\), the cross-\(B\) leverage is one, and
\[
\ell_A=1+\frac{F'(0)}d=\frac{4a}{2a+b-1}.
\]
This is at most one precisely if \(b\ge2a+1\), with equality exactly at the threshold. Thus **every** generating signed root lies in the proposed ellipsoid and the contact classification is sharp. Convexity of the ellipsoid implies containment of their convex hull. Each generating root is a distinct vertex of the symmetric edge polytope: a linear functional given by its own inner product has unique maximum there, since all roots have norm \(\sqrt2\) and distinct ones have strictly smaller inner product by Cauchy–Schwarz. Strict convexity of the quadratic gauge shows no other point of the convex hull can be a boundary contact.

**4. Establish global minimum volume and uniqueness.** Consider any positive definite precision matrix \(K\) on \(H\) for an origin-centered ellipsoid containing every signed root. Each root satisfies \(r^{\mathsf T}Kr\le1\). Since \(C_t\) is a convex combination of these outer products, \(\operatorname{tr}(KC_t)\le1\). The arithmetic-geometric mean inequality for the \(d\) positive eigenvalues of \(C_t^{1/2}KC_t^{1/2}\) gives
\[
\det(K)\det(C_t)\le\left(\frac{\operatorname{tr}(KC_t)}d\right)^d\le d^{-d}.
\]
Equality is attained by \(K=(dC_t)^{-1}\), whose root-containment was just proved, and equality forces that very \(K\). Hence this is the unique minimum-volume origin-centered containing ellipsoid. Existence and uniqueness of the general Löwner ellipsoid for a full-dimensional convex body, together with central symmetry \(P_G=-P_G\), force its center to be the origin: reflection about zero would otherwise produce a distinct ellipsoid of equal minimum volume. Thus this is the unique global Löwner ellipsoid, even among off-center and symmetry-breaking competitors.

**5. Sharp screening.** For the complete bipartite subgraph \(K_{2a,b}\), the signed roots are exactly the cross-\(B\) roots, with one transitive orbit under graph automorphisms. Its unique Löwner ellipsoid is given by the uniform cross-\(B\) design \(C_0\): all those roots have leverage one and the trace-determinant certificate above applies. For \(b\ge2a+1\), \(t=0\), so the larger tripartite polytope has precisely the same enclosing ellipsoid. For \(b>2a+1\), the omitted within-\(A\) roots have strict leverage \(4a/(2a+b-1)<1\). At \(b=2a+1\), they contact with leverage one but no positive weight is needed in the optimum design. Below the threshold the unique maximizer has \(t>0\), and the ellipsoid differs from that of the bipartite subpolytope. This completes the classification.

## Verification

The accompanying `verify.py` independently assembles each incidence outer-product matrix and numerically diagonalizes the resulting covariance. On \(265\) integer parameter pairs \((a,b)\) with \(2\le a\le11\) and \(1\le b\le3a+7\), it checks all proposed eigenvalues with multiplicities, root-containment inequalities and the sharp equality/strictness classification. It also checks the total design weight and the matrix identity \(\Sigma^{-1} C_t\Sigma^{-1}=\Sigma^{-1}/d\). Direct numerical optimization over general precision matrices was separately performed on six small cases as a corroboration, initialized at the displayed candidate. Both checks are finite, floating-point corroborations; the universal conclusion follows from the exact algebraic and convex-geometric argument above. Run `python3 verify.py` with NumPy installed.

## Relationship to prior work

D’Alì, Juhnke-Kubitzke and Koch develop symmetric edge polytopes and their regular-matroid generalizations, proving unimodular-equivalence and combinatorial facet/triangulation theorems. A unimodular change of coordinates does not in general preserve the particular Euclidean metric used here; their classification does not imply the metric ellipsoid formula. Mori, Mori and Ohsugi study facet numbers of join-graph symmetric edge polytopes, a setting naturally including complete multipartite graphs. D’Alì, Delucchi and Michałek study combinatorial and Ehrhart structures of symmetric edge polytopes. In the inspected versions of these works, no exact minimum-enclosing-ellipsoid classification with the present two-parameter screening transition was identified. The proof uses the classical trace-determinant characterization of Löwner ellipsoids; that general characterization alone does not give the optimized weights, spectrum or threshold without the graph-specific calculation.

## Limitations

The result is for the standard intrinsic Euclidean realization, exactly the complete tripartite family with two equal parts of size at least two, and no claim about arbitrary graph joins or arbitrary metrics is made. The numerical checks are finite and do not prove the infinite-family theorem. A prior equivalent classification phrased as D-optimal design, weighted spanning-tree optimization, effective-resistance equalization, or Kantorovich–Rubinstein polytope geometry cannot be ruled out by the inspected literature alone. No independent mathematical or bibliographic priority audit has been performed.

## References

- A. D’Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (2023-07-10), https://arxiv.org/abs/2307.04933.
- K. Mori, T. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (first posted 2023-12-18), https://arxiv.org/abs/2312.11287.
- A. D’Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019), https://arxiv.org/abs/1910.05193.
- Standard Löwner ellipsoid uniqueness and the trace-determinant/D-optimal-design equivalence are used as classical convex-geometric facts.
