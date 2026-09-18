# No exponential Riesz bases on bounded strictly convex bodies without boundary regularity

## Result

Let \(n\ge 2\), let \(K\subset\mathbb R^n\) be a compact strictly convex body with nonempty interior, and put
\[
\Omega=\operatorname{int}K.
\]
Then \(L^2(\Omega)\) admits no Riesz basis of exponentials.

No differentiability, curvature, or smoothness assumption on \(\partial K\) is required.

The result follows by combining the boundary-measure obstruction of Ortega-Cerdà (arXiv:2609.18426) with the following geometric lemma.

### Boundary-translate lemma

For every nonzero \(\theta\in\mathbb R^n\),
\[
\mathcal H^{n-1}\!\left(\partial K\cap(\partial K-\theta)\right)=0.
\]

Thus the full surface measure
\[
\nu=\mathcal H^{n-1}\!\restriction_{\partial K}
\]
satisfies the non-overlap hypothesis in Ortega-Cerdà's general boundary criterion.

## Context

Ortega-Cerdà proved that balls in \(\mathbb R^n\), \(n\ge2\), admit no exponential Riesz basis and extended the conclusion to every nonempty bounded convex open set with \(C^2\) boundary. The same paper gives a more general criterion: for a bounded open set with null boundary, it suffices that the boundary carry a finite nonzero positive Borel measure \(\nu\) whose overlap with every nontrivial translate of the boundary has \(\nu\)-measure zero, together with a two-sided positive-measure neighborhood condition at \(\nu\)-almost every boundary point.

The theorem above verifies that criterion for every strictly convex body using surface measure, without any boundary regularity.

A simultaneous preprint of Wan (arXiv:2609.16674) proves nonexistence for balls, certain convex polytopes, shells, finite unions, products, and affine images. Its stated classes do not include arbitrary strictly convex bodies.

## Proof of the boundary-translate lemma

Fix \(\theta\ne0\). After an orthogonal change of coordinates, write
\[
\theta=a e_n,\qquad a=|\theta|>0.
\]
Let
\[
D=\pi(K)\subset e_n^\perp\simeq\mathbb R^{n-1},
\]
where \(\pi\) is orthogonal projection. For \(z\in D\), write the vertical section as
\[
K\cap(\{z\}\times\mathbb R)
=
\{z\}\times[\ell(z),u(z)]
\]
and define its width
\[
w(z)=u(z)-\ell(z).
\]

### 1. Boundary fibers have zero width

If \(z\in\partial D\), choose a supporting hyperplane to \(D\) at \(z\). Its lift parallel to \(e_n\) is a supporting hyperplane of \(K\). If the fiber over \(z\) contained two distinct points, the segment joining them would lie in that supporting hyperplane and therefore in \(\partial K\), contradicting strict convexity. Hence
\[
w(z)=0,\qquad z\in\partial D.
\]

For \(z\in\operatorname{int}D\), the relative interior of the vertical section lies in \(\operatorname{int}K\). Consequently the only boundary points of \(K\) in that fiber are its two endpoints.

### 2. The width is strictly concave

Take distinct \(z_1,z_2\in D\) and \(0<t<1\). Put
\[
z_t=t z_1+(1-t)z_2.
\]
The lower endpoints
\[
p_i=(z_i,\ell(z_i))
\]
are distinct boundary points. Strict convexity places
\[
t p_1+(1-t)p_2
\]
in \(\operatorname{int}K\), so
\[
\ell(z_t)
<
t\ell(z_1)+(1-t)\ell(z_2).
\]
Applying the same argument to the upper endpoints gives
\[
u(z_t)
>
t u(z_1)+(1-t)u(z_2).
\]
Subtracting,
\[
w(z_t)
>
t w(z_1)+(1-t)w(z_2).
\]
Thus \(w\) is strictly concave.

### 3. Every positive width level is null

For \(a>0\), set
\[
E_a=\{z\in D:w(z)=a\},
\qquad
C_a=\{z\in D:w(z)\ge a\}.
\]
Concavity makes \(C_a\) convex. The set \(E_a\) stays a positive distance from \(\partial D\): otherwise a sequence \(z_j\to z\in\partial D\) with \(w(z_j)=a\) would, by compactness of \(K\), yield two distinct limiting points of \(K\) in the fiber over \(z\), contradicting the singleton boundary-fiber property.

Moreover,
\[
E_a\subset\partial C_a.
\]
Indeed, if \(z\in E_a\) were an interior point of \(C_a\), then for sufficiently small nonzero \(h\) both \(z-h\) and \(z+h\) would lie in \(C_a\). Strict concavity at the midpoint would give
\[
a=w(z)>
\frac{w(z-h)+w(z+h)}2\ge a,
\]
a contradiction.

The boundary of a convex subset of \(\mathbb R^{n-1}\) has \((n-1)\)-dimensional Lebesgue measure zero. Hence
\[
|E_a|_{n-1}=0.
\]

### 4. Translate intersection is a Lipschitz graph over \(E_a\)

If
\[
x=(z,s)\in\partial K\cap(\partial K-ae_n),
\]
then both \(x\) and \(x+a e_n\) lie on \(\partial K\) in the same vertical fiber. The fiber cannot lie over \(\partial D\), because it contains two distinct points. Hence \(z\in\operatorname{int}D\), and the preceding endpoint observation forces
\[
s=\ell(z),\qquad u(z)-\ell(z)=a.
\]
Therefore
\[
\partial K\cap(\partial K-ae_n)
=
\{(z,\ell(z)):z\in E_a\}.
\]

The lower endpoint function \(\ell\) is convex and finite on the open convex set \(\operatorname{int}D\), hence locally Lipschitz there. Since \(E_a\) is compactly contained in \(\operatorname{int}D\), it is covered by finitely many regions on which the graph map
\[
z\longmapsto(z,\ell(z))
\]
is Lipschitz. A Lipschitz map sends \(\mathcal H^{n-1}\)-null sets to \(\mathcal H^{n-1}\)-null sets. Thus
\[
\mathcal H^{n-1}\!\left(\partial K\cap(\partial K-ae_n)\right)=0.
\]
Undoing the rotation proves the lemma for every \(\theta\ne0\).

## Proof of the Riesz-basis theorem

For a convex body,
\[
0<\mathcal H^{n-1}(\partial K)<\infty,
\qquad
|\partial K|_n=0.
\]
Take
\[
\nu=\mathcal H^{n-1}\!\restriction_{\partial K}.
\]
The boundary-translate lemma gives the required non-overlap with every nonzero translate.

Finally, every neighborhood of every \(x\in\partial K\) meets both \(\Omega\) and the strict exterior \(\mathbb R^n\setminus K\) in sets of positive \(n\)-dimensional Lebesgue measure. The interior statement follows because \(x\in\overline{\Omega}\) and \(\Omega\) is open. For the exterior statement, a supporting hyperplane to \(K\) at \(x\) leaves an open half-ball on its exterior side.

All hypotheses of Ortega-Cerdà's general boundary criterion are therefore satisfied, so \(L^2(\Omega)\) cannot admit a Riesz basis of exponentials.

## What is new and what is prior

Prior work used here:

- Ortega-Cerdà, arXiv:2609.18426: the general boundary-measure obstruction and the \(C^2\) convex-domain theorem.
- Wan, arXiv:2609.16674: independent nonexistence results for balls and several other geometric classes.
- Standard convex geometry: finite surface area of convex bodies, local Lipschitz regularity of finite convex functions, and null Lebesgue measure of convex-set boundaries.

The new contribution claimed here is the boundary-translate lemma for arbitrary strictly convex bodies in the form needed by the Riesz-basis obstruction, and the resulting removal of all boundary regularity assumptions under strict convexity.

## Limitations

Strict convexity is essential to this proof: flat boundary segments can create positive surface-measure overlap with a tangential translate. The result does not classify general nonsmooth convex bodies with flat faces, and it does not subsume positive Riesz-basis results for special centrally symmetric polytopes. It also does not address dimension one.

Originality is asserted only to the best of our knowledge. The principal source papers are extremely recent, so unindexed simultaneous observations remain possible.

## References

1. J. Ortega-Cerdà, *There are no Riesz bases of exponentials in balls and triangles*, arXiv:2609.18426 (2026). https://arxiv.org/abs/2609.18426
2. Z. Wan, *Sets with no Riesz bases of exponentials*, arXiv:2609.16674 (2026). https://arxiv.org/abs/2609.16674
3. G. Kozma, S. Nitzan, A. Olevskii, *A set with no Riesz basis of exponentials*, arXiv:2110.02090; published 2023. https://arxiv.org/abs/2110.02090
4. A. Debernardi, N. Lev, *Riesz bases of exponentials for convex polytopes with symmetric faces*, arXiv:1907.04561; J. Eur. Math. Soc. 24 (2022), 3017–3029. https://arxiv.org/abs/1907.04561
