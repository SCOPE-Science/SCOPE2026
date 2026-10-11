# A sharp beta stochastic bound for difference-body distances

## Finding

Let \(d\ge2\) and let \(K\subset\mathbb R^d\) be a compact convex body with nonempty interior. Let \(X,Y\) be independent points uniform in \(K\), let \(D=K-K\), and let \(\gamma_D(z)=\inf\{r\ge0:z\in rD\}\) denote the Minkowski gauge of \(D\). Then the affine-invariant random variable \(T=\gamma_D(X-Y)\) is supported in \([0,1]\) and satisfies, for every \(0\le t\le1\),

\[
\mathbb P(T\le t)\le I_t(d,d+1)
=\frac{\int_0^t r^{d-1}(1-r)^d\,dr}{B(d,d+1)}.
\]

Here \(B(d,d+1)=\int_0^1 r^{d-1}(1-r)^d\,dr\). Equality at **any** fixed \(t\in(0,1)\) holds if and only if \(K\) is a simplex; for every simplex, equality holds simultaneously at all thresholds. Equivalently, \(T\) first-order stochastically dominates a \(\mathrm{Beta}(d,d+1)\) variable, with strict domination at every interior threshold for nonsimplices.

For every real \(p>0\), the following sharp moment inequality follows, again with equality if and only if \(K\) is a simplex:

\[
\mathbb E[T^p]\ge
\frac{\Gamma(d+p)\Gamma(2d+1)}{\Gamma(d)\Gamma(2d+p+1)}.
\]

For a simplex the exact mean is \(d/(2d+1)\) and the variance is \(d(d+1)/((2d+1)^2(2d+2))\).

## Assumptions and scope

The dimension is an integer \(d\ge2\). No smoothness, symmetry, or polytope assumption on \(K\) is required. Volume means \(d\)-dimensional Lebesgue measure, all probability measures are normalized uniform volume measures, and the difference-body gauge is taken relative to the **whole** set \(K-K\), not to \(K\) or the Euclidean unit ball. The full-dimensional hypothesis ensures \(0\in\operatorname{int}(K-K)\), so the gauge is finite and continuous. The central inequality holds at both endpoints; its strictness and equality characterization concern \(0<t<1\).

## Proof

**1. The covariogram is root-concave.** Put \(V=\operatorname{vol}_d(K)\) and \(g(z)=\operatorname{vol}_d(K\cap(K+z))\). The random difference \(Z=X-Y\) has density \(g(z)/V^2\) (by symmetry, the sign convention for the translation is immaterial). Its support is \(D\), and \(g(0)=V\). For all \(z_0,z_1\in D\) and \(0\le a\le1\), convexity gives

\[
(1-a)(K\cap(K+z_0))+a(K\cap(K+z_1))
\subseteq K\cap(K+(1-a)z_0+az_1).
\]

The Brunn–Minkowski inequality therefore makes \(g^{1/d}\) concave on \(D\). At each boundary point of \(D\) the overlap has zero \(d\)-volume: a positive-volume overlap would have nonempty interior and would force that displacement into \(\operatorname{int}D\).

**2. A universal increasing radial likelihood ratio.** Fix a Euclidean unit direction \(\theta\in\mathbb S^{d-1}\), let \(R(\theta)=\max\{r\ge0:r\theta\in D\}\), and define

\[
h_\theta(r)=\left(\frac{g(rR(\theta)\theta)}{V}\right)^{1/d},
\qquad 0\le r\le1.
\]

The function \(h_\theta\) is continuous, concave, and satisfies \(h_\theta(0)=1\), \(h_\theta(1)=0\). For \(0\le s<r<1\), applying concavity to \(r=(1-a)s+a\cdot1\) yields

\[
h_\theta(r)\ge \frac{1-r}{1-s}h_\theta(s).
\]

Thus \(h_\theta(r)/(1-r)\) is nondecreasing in \(r\in[0,1)\). Consequently

\[
w_\theta(r)=\frac{g(rR(\theta)\theta)}{V(1-r)^d}
=\left(\frac{h_\theta(r)}{1-r}\right)^d
\]

is nondecreasing, nonnegative, and satisfies \(w_\theta(0)=1\). In particular \(g(rR(\theta)\theta)\ge V(1-r)^d\) for every interior radius.

**3. Conditional stochastic comparison.** Euclidean polar coordinates on the difference variable \(Z\), followed by the substitution \(z=rR(\theta)\theta\), give joint density (relative to surface measure in \(\theta\) and Lebesgue measure in \(r\)) proportional to

\[
R(\theta)^d r^{d-1}(1-r)^d w_\theta(r),
\qquad 0<r<1.
\]

The conditional law of \(T\) given the direction \(\theta=Z/\|Z\|_2\) is therefore obtained by tilting the \(\mathrm{Beta}(d,d+1)\) density with a nondecreasing weight \(w_\theta\). For an independent baseline beta variable \(B\), the Chebyshev covariance identity gives

\[
\operatorname{Cov}\bigl(w_\theta(B),\mathbf1_{\{B\le t\}}\bigr)\le0,
\]

because the weight is nondecreasing and the indicator is nonincreasing. Dividing by \(\mathbb E[w_\theta(B)]>0\) proves

\[
\mathbb P(T\le t\mid\theta)
=\frac{\mathbb E[w_\theta(B)\mathbf1_{\{B\le t\}}]}{\mathbb E[w_\theta(B)]}
\le\mathbb P(B\le t).
\]

All conditional integrals are finite: they are bounded by the finite integral of the covariogram along a fixed bounded ray. Integrating over the actual direction distribution of \(Z\) proves the theorem for every \(t\).

For \(0<t<1\), the covariance is strictly negative whenever \(w_\theta\) is not almost everywhere constant. Indeed, under the positive beta density, a nonconstant nondecreasing function has strictly larger mean on \((t,1)\) than on \((0,t)\). Therefore equality at any interior \(t\) forces \(w_\theta\) to be constant almost everywhere in \(r\) for almost every direction \(\theta\). Continuity and its value at the origin make that constant \(1\). By continuity of \(g\) and \(R\),

\[
g(z)=V(1-\gamma_D(z))^d\quad(z\in D).
\]

Integrating this equality in polar coordinates and using \(\int_{\mathbb R^d}g(z)\,dz=V^2\) gives

\[
V^2=V\operatorname{vol}_d(D)\,dB(d,d+1)
=\frac{V\operatorname{vol}_d(D)}{\binom{2d}{d}},
\]

and hence \(\operatorname{vol}_d(K-K)=\binom{2d}{d}\operatorname{vol}_d(K)\). The equality characterization in the Rogers–Shephard difference-body inequality implies \(K\) is a simplex.

**4. Every simplex attains equality.** Write a simplex as \(\Delta=\operatorname{conv}\{v_0,\ldots,v_d\}\), with affine barycentric functions \(\lambda_i\). For each displacement \(z\), write \(a_i=\lambda_i(x+z)-\lambda_i(x)\), independent of \(x\), so \(\sum_i a_i=0\). The overlap \(\Delta\cap(\Delta+z)\) is the barycentric region \(\lambda_i(x)\ge\max(0,a_i)\) for all \(i\), a translated copy of \(\Delta\) with scale \(1-\sum_i\max(0,a_i)\), whenever that scale is nonnegative. Moreover

\[
\gamma_{\Delta-\Delta}(z)=\sum_i\max(0,a_i).
\]

It follows that \(g_\Delta(z)=\operatorname{vol}_d(\Delta)(1-\gamma_{\Delta-\Delta}(z))^d\) throughout the difference body. Therefore \(w_\theta\equiv1\) and \(T\sim\mathrm{Beta}(d,d+1)\).

**5. Moments and strictness.** Integrating the survival-function inequality against \(p t^{p-1}\) shows \(\mathbb E T^p\ge\mathbb E B^p\) for every \(p>0\). The standard beta integral evaluates the right side as stated. If \(K\) is not a simplex, the strict CDF comparison holds at every interior threshold, so every such moment inequality is strict. The simplex mean and variance are the standard moments of \(\mathrm{Beta}(d,d+1)\).

## Verification

The supplied `verify.py` uses exact rational arithmetic to check beta normalization, the first two moments and the variance identity for dimensions \(1\) through \(40\). It verifies the exact planar-square example, in which

\[
\mathbb P(T\le t)=(2t-t^2)^2,
\qquad
I_t(2,3)-(2t-t^2)^2=2t^2(1-t)^2.
\]

The program additionally runs \(100000\) seeded barycentric simplex samples over five dimensions, comparing empirical and exact means. These finite diagnostics are **not** a replacement for the all-dimensional geometric proof. The proof's essential noncomputational steps are the root-concavity lemma, monotone likelihood-ratio comparison, and Rogers–Shephard equality case.

Reproduce with Python 3 standard library: `python3 verify.py`.

## Relationship to prior work

Averkov and Bianchi (2007) describe the covariogram as the density of a difference of two independent uniform points and study recovery of convex bodies from covariogram information, rather than a sharp stochastic order for the shape-adaptive gauge of their differences. Gardner and Zhang (1998), as restated explicitly by Wang and Zhang (2014), establish inequalities for radial mean bodies and the sharp Rogers–Shephard theorem, using related concavity mechanisms. Langharst (2022), Proposition 2.5 and Proposition 2.6, states the covariogram's root concavity and characterizes its affine-ray equality in simplices; his Section 3 concerns weighted Zhang-type bounds, not the normalized beta comparison at every difference-body gauge threshold. Haddad and collaborators (2025) investigate higher-order difference bodies and integral inequalities. The present assertion is a **first-order stochastic comparison of a normalized random pair distance**, not simply an inequality of volumes, fixed directional moments or support functions.

## Limitations

The result assumes uniform independent interior points and full-dimensional convexity, and uses the intrinsic gauge of the entire difference body. It does not compare unnormalized Euclidean distances, derive quantitative stability in a distance between bodies, or extend to nonconvex sets. The Rogers–Shephard and Brunn–Minkowski ingredients are classical; the originality claim concerns their stated beta-distribution comparison and equality formulation, not those ingredients. An equivalent older statement under covariogram or radial-mean-body terminology remains possible, especially because the full text of Gardner and Zhang (1998) was not retrieved; no independent historical certification is claimed.

## References

1. G. Averkov and G. Bianchi, *Retrieving convex bodies from restricted covariogram functions*, arXiv:math/0702892v1, publicly posted 28 February 2007, https://arxiv.org/abs/math/0702892.
2. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220–233, https://doi.org/10.1007/BF01899997.
3. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, American Journal of Mathematics 120 (1998), 505–528, https://doi.org/10.1353/ajm.1998.0021.
4. W. Wang and T. Zhang, *Inequalities for dual quermassintegrals of the radial p th mean bodies*, Journal of Inequalities and Applications 2014:252, https://doi.org/10.1186/1029-242X-2014-252.
5. D. Langharst, *General measure extensions of projection bodies*, Proceedings of the London Mathematical Society 125 (2022), 1083–1129, https://doi.org/10.1112/plms.12477.
6. J. Haddad, D. Langharst, E. Putterman, M. Roysdon, and D. Ye, *Affine isoperimetric inequalities for higher-order projection and centroid bodies*, Mathematische Annalen (2025), https://doi.org/10.1007/s00208-025-03271-x.
