# Polynomial entropy equals velocity-image box dimension for frozen-base torus translations

## Finding
Let \(B\) be any nonempty compact metric space, let \(m\ge1\), and let \(\alpha:B\to\mathbb T^m\) be continuous. For the homeomorphism
\[
F:B\times\mathbb T^m\to B\times\mathbb T^m,\qquad F(b,y)=(b,y+\alpha(b)),
\]
write \(E=\alpha(B)\). Its polynomial entropy equals the upper box-counting dimension of its *velocity image*:
\[
\boxed{h_{\mathrm{pol}}(F)=\overline{\dim}_{\mathrm B}E.}
\]
In particular, \(h_{\mathrm{top}}(F)=0\), regardless of the modulus of continuity of \(\alpha\). There is a Haar-preserving homeomorphism of \(\mathbb T^3\), homotopic to the identity, of this form with
\[
\boxed{h_{\mathrm{pol}}(F)=\frac{\log4}{\log3}\in(1,2).}
\]
Its orbitwise rotation set is a noncollinear embedded fractal curve, while its invariant-measure rotation set is the curve’s convex hull. Both have affine-span dimension two, although its polynomial entropy is strictly less than two.

## Assumptions and scope
Give \(\mathbb T^m=\mathbb R^m/\mathbb Z^m\) its maximum coordinate geodesic distance, and give the product the maximum metric. Write
\[
d_n(x,x')=\max_{0\le j<n}d(F^j x,F^j x').
\]
Let \(s_F(n,\varepsilon)\) be the maximal cardinality of a \(d_n\)-separated set, and let \(g_F(n,\varepsilon)\) be the smallest cardinality of an \(\varepsilon\)-spanning set. Define
\[
h_{\mathrm{pol}}(F)=\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}\frac{\log s_F(n,\varepsilon)}{\log n}.
\]
For a compact subset \(E\subset\mathbb T^m\), \(N_E(r)\) is its minimum number of radius-\(r\) balls covering it, and
\[
\overline{\dim}_{\mathrm B}E=\limsup_{r\downarrow0}\frac{\log N_E(r)}{\log(1/r)}.
\]
Equivalent maximal packing and covering definitions give the same upper box dimension. The base need not be a manifold, connected, or locally connected. This theorem is not a statement about arbitrary dynamics on the base.

## Proof
**Upper bound.** Fix \(0<\varepsilon<1/16\), and cover \(B\) and \(\mathbb T^m\) by finitely many balls of radius \(\varepsilon/8\). Cover \(E\) by \(N_E(\varepsilon/(8n))\) balls of radius \(\varepsilon/(8n)\). For each nonempty intersection of one base ball with the inverse image of one velocity ball choose one point \(b_*\), and pair it with a fixed \(\varepsilon/8\)-net of fiber starting positions. For any \(b\) in the same intersection,
\[
d_B(b,b_*)<\varepsilon/4,\qquad d_{\mathbb T^m}(\alpha(b),\alpha(b_*))<\frac{\varepsilon}{4n}.
\]
For any paired initial fibers within \(\varepsilon/8\), the torus triangle inequality and translation invariance show, for \(0\le j<n\),
\[
d_{\mathbb T^m}(y+j\alpha(b),y_*+j\alpha(b_*))<\frac\varepsilon8+\frac{j\varepsilon}{4n}<\frac{3\varepsilon}{8}.
\]
Consequently, with \(C_\varepsilon\) independent of \(n\),
\[
g_F(n,\varepsilon)\le C_\varepsilon N_E\bigl(\varepsilon/(8n)\bigr).
\]
Since a maximal separated set at scale \(2\varepsilon\) is bounded by the spanning number at scale \(\varepsilon\), taking \(\limsup\) proves \(h_{\mathrm{pol}}(F)\le\overline{\dim}_{\mathrm B}E\).

**Lower bound.** Fix \(0<\varepsilon<1/16\) and choose a maximal \(4\varepsilon/n\)-separated subset \(\{u_i\}\) of \(E\). For each velocity choose a base point \(b_i\) with \(\alpha(b_i)=u_i\), and initialize every fiber at zero. For two different velocities, a coordinate difference \(\delta\) has circular distance at least \(4\varepsilon/n\). If \(\delta\ge\varepsilon\), the first iterate separates the points. Otherwise, choose
\[
j=\left\lceil\frac\varepsilon\delta\right\rceil\le n
\]
for sufficiently large \(n\). Since \(\varepsilon\le j\delta<2\varepsilon<1/2\), no torus wraparound occurs, and the \(j\)th images are at least \(\varepsilon\) apart. The index \(j\) can be chosen strictly less than \(n\) for all sufficiently large \(n\). Thus the points \((b_i,0)\) are \((n,\varepsilon)\)-separated. A maximal separated subset of \(E\) is also a covering net of that radius, whence
\[
s_F(n,\varepsilon)\ge N_E\bigl(4\varepsilon/n\bigr).
\]
The exponent obtained by taking \(\limsup_{n\to\infty}\log(\cdot)/\log n\) is precisely the upper box dimension, because the radii form a complete asymptotic scale as \(n\) grows. This proves the reverse inequality.

Since polynomial orbit-separation grows subexponentially at every fixed scale, the usual topological entropy is zero.

**Fractal torus realization.** Let \(K\subset\mathbb R^2\) be the boundary of a standard Koch snowflake, scaled and translated into \((-1/8,1/8)^2\). It is a Jordan curve and has upper box dimension \(\log4/\log3\), by its fourfold self-similar replacement at ratio one-third and separation of pieces. Choose a continuous surjective parametrization \(\gamma:\mathbb T\to K\) and set \(\alpha(t)=\gamma(t)\bmod\mathbb Z^2\). Then
\[
F(t,y)=(t,y+\alpha(t))\quad\text{on }\mathbb T^3
\]
is a homeomorphism, with inverse subtracting \(\alpha(t)\), homotopic to identity by shrinking the real-valued lift \(\gamma\), and preserves product Haar measure because its fiber maps are translations. For its natural lift, the rotation vector along any orbit is the constant \((0,\gamma(t))\); allowing invariant measures gives exactly the set \(\{0\}\times K\), not its convex hull, when rotation vectors are defined as pointwise limits. Invariant-measure averages include convex combinations, so their set is \(\{0\}\times\operatorname{conv}(K)\). The orbitwise displacement rotation set, formed from accumulation points of normalized displacements, is exactly \(\{0\}\times K\). Both sets have affine span dimension two. The displayed polynomial-entropy value follows from the theorem.

## Verification
A standalone standard-library script `verify_velocity_entropy.py` checks the key finite angular-separation lemma for 973 exact-rational parameter instances and checks the eight finite Koch similarity identities. It was run successfully as packaged. The infinite covering argument, entropy identity, and the dimension of the Koch boundary are mathematical arguments, not certified by those finite tests.

## Relationship to prior work
Corrêa (2026), Section 5, proves a linear upper polynomial-entropy bound for a *Lipschitz scalar* frozen-base torus skew product, and proves that a nontrivial torus rotation set imposes a lower bound of one. The present statement concerns arbitrary compact bases, arbitrary continuous multidimensional velocity images, and exact potentially noninteger growth given by their upper box dimensions. The previously established scalar zero–one law is a covered special case, not a separate novelty claim. Classical Koch-curve dimension is likewise used, not claimed as original. Existing studies of polynomial entropy of integrable Hamiltonian flows and circle dynamics address other dynamical classes.

## Limitations
The formula requires the base to be fixed, the fibers to be torus translations, and the base–fiber product to be compact. It does not determine the polynomial entropy of general skew products or flows, and it does not answer singleton-rotation-set or minimality questions. The fractal example is a torus homeomorphism but need not be differentiable. The literature comparison has a residual risk of an equivalent theorem formulated in terms of metric entropy growth or a general family of isometries. Independent scientific audit has not been performed.

## References
1. H. Corrêa, *Polynomial entropy and rotation sets*, Archiv der Mathematik, published 12 September 2026, https://doi.org/10.1007/s00013-026-02286-3.
2. J. Correa and E. R. Pujals, *Orders of growth and generalized entropy*, Journal de l'Institut de Mathématiques de Jussieu **22** (2023), 1581–1613 (as referenced by Corrêa, 2026).
3. J.-P. Marco, *Polynomial entropies and integrable Hamiltonian systems*, Regular and Chaotic Dynamics **18** (2013), 623–655.
4. E. P. Pearse, *Canonical self-similar tilings by iterated function systems* and related Koch snowflake geometry; the standard four-at-one-third snowflake dimension identity is used here.
