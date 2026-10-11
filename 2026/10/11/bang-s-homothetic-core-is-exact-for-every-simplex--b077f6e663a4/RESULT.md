# Bang's homothetic core is exact for every simplex

## Finding

Let \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\subset\mathbb R^d\) be a nondegenerate simplex. Write its barycentric coordinate functions as \(\lambda_0,\ldots,\lambda_d\), so that
\[
S=\{x:\lambda_i(x)\ge0\text{ for every }i\},
\qquad
\sum_{i=0}^d\lambda_i(x)=1,
\]
and put \(g_i=\nabla\lambda_i\). Let \(w(S)\) be the minimum width of \(S\).

For every \(0<W<w(S)\) and every unit vector \(u\), define
\[
A_u=\frac W2\sum_{i=0}^d|\langle g_i,u\rangle|,
\qquad
c_u=\frac W2\sum_{i=0}^d|\langle g_i,u\rangle|v_i.
\]
Then the Minkowski subtraction used by Bakaev--Polyanskii has the exact form
\[
S\div\left\{-\frac W2u,\frac W2u}\right\}
=
c_u+(1-A_u)S.
\]
Consequently
\[
\operatorname{vol}_d\!\left(S\div\left\{-\frac W2u,\frac W2u}\right\}\right)
=(1-A_u)^d\operatorname{vol}_d(S).
\]

The directional coefficient satisfies the sharp identity
\[
\max_{|u|=1}\sum_{i=0}^d|\langle g_i,u\rangle|
=\frac2{w(S)}.
\]
Therefore
\[
\boxed{
\min_{|u|=1}
\operatorname{vol}_d\!\left(S\div\left\{-\frac W2u,\frac W2u}\right\}\right)
=
\left(1-\frac W{w(S)}\right)^d\operatorname{vol}_d(S)
}.
\]
Thus the homothetic core guaranteed by the source's Bang-type lemma is not merely a lower bound for simplices: after optimizing the segment direction, it has exactly the whole eroded-simplex volume.

There is also an exact minimizer description. For \(I\subset\{0,\ldots,d\}\), put
\[
G_I=\sum_{i\in I}g_i.
\]
A unit vector \(u\) minimizes the displayed erosion volume if and only if, up to sign,
\[
u=\frac{G_I}{|G_I|}
\qquad\text{for some }I\text{ with }|G_I|=\frac1{w(S)}.
\]
For such an \(I\), all vertices indexed by \(I\) lie on one support hyperplane orthogonal to \(u\), all complementary vertices lie on the opposite support hyperplane, and those hyperplanes are exactly \(w(S)\) apart. Hence the minimizing directions are precisely minimum-width directions supported on complementary faces.

For a regular simplex, \(|G_I|^2\) is proportional to \(|I|(d+1-|I|)\). Therefore the minimizing directions are exactly the directions separating a most balanced partition of the \(d+1\) vertices. In particular, for a regular tetrahedron they are the three directions perpendicular to pairs of opposite edges. This applies in dimensions where the source explicitly notes that a regular simplex has no facet altitude equal to its minimum width.

## Assumptions and scope

The theorem concerns Minkowski subtraction by a centered segment and the directional minimum appearing in the partial-plank reduction. The width parameter satisfies \(0<W<w(S)\), so every displayed homothety ratio is positive. The theorem does not assert that a single plank attains the resulting lower bound for every simplex, and therefore does not settle the source's partial-plank conjecture for higher-dimensional simplices.

The definition is the source convention
\[
K\div B=\{x:B+x\subset K\}.
\]
No symmetry or regularity of \(S\) is assumed in the main theorem.

## Proof

Because each \(\lambda_i\) is affine,
\[
\lambda_i\!\left(x\pm\frac W2u\right)
=\lambda_i(x)\pm\frac W2\langle g_i,u\rangle.
\]
Thus
\[
x\in S\div\left\{-\frac W2u,\frac W2u}\right\}
\quad\Longleftrightarrow\quad
\lambda_i(x)\ge\alpha_i
\quad(0\le i\le d),
\]
where
\[
\alpha_i=\frac W2|\langle g_i,u\rangle|.
\]
If \(A=\sum_i\alpha_i\), every point with these inequalities has unique barycentric coordinates
\[
\lambda_i(x)=\alpha_i+(1-A)\mu_i,
\qquad
\mu_i\ge0,
\qquad
\sum_i\mu_i=1.
\]
Hence, writing \(y=\sum_i\mu_i v_i\in S\),
\[
x=\sum_i\alpha_i v_i+(1-A)y=c_u+(1-A)S.
\]
This proves the exact homothety formula whenever \(A<1\). The identity proved below gives \(A\le W/w(S)<1\), so no separate nonemptiness argument is needed.

It remains to determine
\[
M=\max_{|u|=1}\sum_i|\langle g_i,u\rangle|.
\]
Since \(\sum_i g_i=0\), for fixed \(u\),
\[
\sum_i|\langle g_i,u\rangle|
=2\max_{I\subset\{0,\ldots,d\}}\langle G_I,u\rangle.
\]
Therefore
\[
M=2\max_I|G_I|.
\]

Now let \(C=S-S\) be the difference body and let
\[
C^\circ=\{y:h_C(y)\le1\}
\]
be its polar. We claim
\[
C^\circ=\operatorname{conv}\{G_I:I\subset\{0,\ldots,d\}\}\}.
\]
For any vertices \(v_j,v_k\), barycentric interpolation gives
\[
\langle G_I,v_j-v_k\rangle
=\mathbf1_{j\in I}-\mathbf1_{k\in I},
\]
so \(h_C(G_I)\le1\), proving that every \(G_I\) belongs to \(C^\circ\).

Conversely, take \(y\in C^\circ\). Put \(t_i=\langle y,v_i\rangle\) and \(m=\min_i t_i\). Since \(h_C(y)=\max_i t_i-\min_i t_i\le1\), the numbers \(s_i=t_i-m\) lie in \([0,1]\). Differentiating the barycentric identity \(x=\sum_i\lambda_i(x)v_i\), and transposing, gives
\[
y=\sum_i\langle y,v_i\rangle g_i.
\]
Because \(\sum_i g_i=0\),
\[
y=\sum_i s_i g_i.
\]
The image of the cube \([0,1]^{d+1}\) under \(s\mapsto\sum_i s_i g_i\) is exactly the convex hull of the subset sums \(G_I\). This proves the claim.

Finally,
\[
w(S)=\min_{|u|=1}h_{S-S}(u).
\]
For a centrally symmetric convex body, the reciprocal of this minimum support value is the circumradius of its polar. Hence
\[
\max_I|G_I|
=\max_{y\in C^\circ}|y|
=\frac1{w(S)}.
\]
Combining this with \(M=2\max_I|G_I|\) proves
\[
M=\frac2{w(S)}
\]
and the minimum-volume formula.

For the equality directions, if \(u\) attains \(M\), choose the indices with nonnegative \(\langle g_i,u\rangle\). Then equality in the preceding maximization and in Cauchy--Schwarz forces \(G_I=u/w(S)\). Conversely, any subset sum of norm \(1/w(S)\), normalized to a unit vector, attains \(M\). The identity
\[
\langle G_I,v_j-v_k\rangle=1
\qquad(j\in I,\ k\notin I)
\]
then shows that the two complementary faces lie on parallel supports separated by \(w(S)\).

For the regular-simplex corollary, normalize the vertices \(q_i\) by
\[
|q_i|=1,
\qquad
\langle q_i,q_j\rangle=-\frac1d
\quad(i\ne j).
\]
Then
\[
g_i=\frac d{d+1}q_i,
\qquad
|G_I|^2=\frac{d\,|I|(d+1-|I|)}{(d+1)^2},
\]
which is maximal exactly when the two block sizes differ by at most one.

## Verification

Every step is algebraic or finite-dimensional convex duality. No finite computation is used to infer the theorem. The critical verification is the exact polar identity \((S-S)^\circ=\operatorname{conv}\{G_I\}\), proved in both directions above from barycentric interpolation, together with the reciprocal relation between minimum support of \(S-S\) and circumradius of its polar.

Boundary behavior is explicit. At \(W=0\) the subtraction is \(S\). As \(W\uparrow w(S)\), the minimum homothety ratio tends to zero. The theorem does not infer any statement for \(W>w(S)\), where a total plank width already exceeds the threshold relevant to Bang's covering theorem.

## Relationship to prior work

Bakaev--Polyanskii prove a general reduction from finite plank families to the directional minimum of
\[
\operatorname{vol}_d\!\left(K\div\left\{-\frac W2u,\frac W2u}\right\}\right)
\]
and prove that this erosion contains a translate of \(\left(1-W/w(K)\right)K\). They then treat a special simplex class in which a facet altitude already equals the minimum width; a facet-adjacent plank attains the resulting volume bound. Their discussion explicitly notes that, among regular simplices of dimension at least two, only the regular triangle has that altitude property.

The theorem above addresses a different implication: for every simplex, without an altitude hypothesis, the source's homothetic lower bound is exactly the optimized erosion volume, and all optimizing directions are classified by complementary minimum-width faces. It does not claim the source's later single-plank attainment step outside the class they prove.

A recent published finding gives an exact minimum-width formula and an altitude criterion for convex pyramids. That statement determines when a particular base altitude equals width. It does not compute Minkowski subtraction by a centered segment, prove the polar subset-gradient identity, or show that the Bang homothetic core is exact after directional optimization for every simplex.

## Limitations

The exactness proved here is exactness of the erosion stage in the plank-family reduction. In dimensions above two it does not provide a plank whose uncovered region has the same volume as the minimizing erosion, so it does not prove the full single-plank conjecture for arbitrary simplices.

The originality search found no equivalent statement under Minkowski-subtraction, erosion, barycentric-gradient, complementary-face, or width terminology. An elementary equivalent may nevertheless occur in older convex-geometry literature under different language; this is the principal residual literature risk.

## References

1. E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483v1, 29 July 2026. In particular Corollary 7, Lemma 8, and Section 5.
2. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, Cambridge University Press, cited by the source for Minkowski subtraction.
