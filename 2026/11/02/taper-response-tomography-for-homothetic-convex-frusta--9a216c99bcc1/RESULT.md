# Taper-response tomography for homothetic convex frusta

## Finding
Let \(K\subset\mathbb R^2\) be any compact convex body with \(0\in\operatorname{int}K\), and fix a height \(H>0\). For \(0\le s<1\) set
\[
F_s(K,H)=\operatorname{conv}\left((1+s)K\times\{H/2\},\ (1-s)K\times\{-H/2\}\right)\subset\mathbb R^3.
\]
Let \(W_s\) be the Euclidean line-projection width of \(F_s(K,H)\) along a Haar-uniform unoriented direction, and let \(h_K(v)=\max_{x\in K}\langle x,v\rangle\) be the support function. Writing \(V\) for a uniform direction on \(S^1\), the complete **mean-width taper response** is
\[
\boxed{\mathbb E W_s-\mathbb E W_0
=s\,\mathbb E\!\left[h_K(V)\arctan\!\left(\frac{2s h_K(V)}H\right)\right].}\tag{1}
\]
For every fixed known \(H\), two origin-containing planar convex bodies \(K,L\) have identical functions \(s\mapsto\mathbb E W_s\) on \([0,1)\) **if and only if** the random variables \(h_K(V)\) and \(h_L(V)\) have identical probability distributions. In fact, equality on any interval containing \(s=0\) is sufficient. Thus a one-parameter sequence of unlabeled three-dimensional *mean* projection-width measurements exactly recovers the entire one-dimensional histogram of planar support values, though not the body's orientation or shape.

The response has the convergent local expansion
\[
\mathbb E W_s-\mathbb E W_0
=\sum_{j=0}^{\infty}\frac{(-1)^j2^{2j+1}}{(2j+1)H^{2j+1}}\,
 \mathbb E[h_K(V)^{2j+2}]\,s^{2j+2},\tag{2}
\]
for \(|s|<H/(2\max_{S^1}h_K)\). In particular,
\[
\boxed{\lim_{s\downarrow0}\frac{\mathbb E W_s-\mathbb E W_0}{s^2}
=\frac2H\mathbb E[h_K(V)^2]>0.}\tag{3}
\]

A separate ordering result holds in every Euclidean dimension \(d\ge2\) for an origin-containing \((d-1)\)-dimensional convex base: if \(0\le s_1<s_2<1\), then \(W_{s_1}\) is dominated by \(W_{s_2}\) in **increasing convex order**, with strict inequality in expectation for every strictly increasing convex test function. When \(K=-K\), there is the stronger pointwise coupling \(W_{s_1}\le W_{s_2}\) in every direction, and the width laws are distinct. These comparison statements do not assert shape reconstruction or finite-sample stability.

## Assumptions and scope
The homothety center \(0\), height \(H\), and scale normalization (mean of the two end scales is one) are fixed and known. The base is full dimensional, compact, convex, and contains the origin strictly inside; it may be nonsmooth, nonpolyhedral, and asymmetric. The two end sections have the same horizontal homothety center and lie in parallel planes, so the hull is a genuine solid. The width of a convex body in direction \(u\) is \(h_F(u)+h_F(-u)\). Surface Haar sampling is uniform on unoriented lines. All expectations concern exact population measurements.

The response-identification assertion is for planar bases and resulting three-dimensional frusta, because the axial absolute cosine of a uniform direction in \(\mathbb R^3\) is uniform on \([0,1]\). The convex-order and centrally symmetric stronger-order assertions extend to arbitrary \(d\ge2\) and use the same support-max argument, not the dimension-three integral.

## Proof
**1. The support-max identity.** Write an oriented unit vector with nonnegative axial component as \(u=(\sqrt{1-t^2}v,t)\), with \(0\le t\le1\) and \(v\in S^1\). Denote \(a=\sqrt{1-t^2}\), \(p=h_K(v)>0\), and \(q=h_K(-v)>0\). Since \(s\ge0\), the upper section always maximizes support in the \(u\) direction:
\[
h_{F_s}(u)=(1+s)ap+Ht/2.
\]
In the opposite direction, either end can be exposed:
\[
h_{F_s}(-u)=\max\{(1+s)aq-Ht/2,\ (1-s)aq+Ht/2\}.
\]
Therefore the exact directional width is
\[
\boxed{w_s(v,t)=a[(1+s)p+(1-s)q]+Ht+(2saq-Ht)_+.}\tag{4}
\]
At \(s=0\), this is \(w_0(v,t)=a(p+q)+Ht\). Reflecting the axial coordinate maps \(F_s\) to \(F_{-s}\), even if \(K\) is asymmetric.

**2. Exact mean integral.** Under Haar measure on \(S^2\), the variables \(T=|u_3|\) and \(V\) are independent, \(T\sim\operatorname{Uniform}[0,1]\), and \(V\) is uniform on \(S^1\). The average of \(p-q\) over \(V\) is zero. Taking means in (4) yields
\[
\mathbb E W_s-\mathbb E W_0
=\mathbb E_V\int_0^1(2s h_K(V)\sqrt{1-t^2}-Ht)_+\,dt.\tag{5}
\]
For any \(b\ge0\), the integrand \((b\sqrt{1-t^2}-Ht)_+\) is supported on \(0\le t<b/\sqrt{H^2+b^2}\); elementary integration gives
\[
\int_0^1(b\sqrt{1-t^2}-Ht)_+\,dt
=\frac b2\arctan(b/H).\tag{6}
\]
Substituting \(b=2s h_K(V)\) proves (1). For reference, \(\mathbb EW_0=\frac\pi2\mathbb E[h_K(V)]+H/2\). For a centered disk of radius \(R\), (1) reads \(\mathbb EW_s-\mathbb EW_0=sR\arctan(2sR/H)\).

**3. Exact inverse statement and normalization.** Let \(M=\max_{v\in S^1}h_K(v)<\infty\). Uniform convergence of the arctangent Taylor series for \(|s|<H/(2M)\), followed by termwise expectation, gives (2) and (3). Equality of two taper-response functions near zero gives equality of all the positive even support moments. Because \(h_K(V)\) and \(h_L(V)\) are bounded and strictly positive, the distributions of their squares are compactly supported probability measures on \([0,\infty)\). Polynomials are dense in the continuous functions on their common compact support; equality of all moments, including the zeroth probability moment, therefore implies equality of the squared-support distributions and hence of the positive support distributions. Conversely, equality of the support distributions makes (1) and the baseline mean equal for every \(s\). The latter follows also from the identity \(\mathbb EW_0=\frac\pi2\mathbb E h_K+H/2\). This proves the if-and-only-if assertion.

**4. Increasing convex order for arbitrary bases.** Extend \(s\) to \((-1,1)\). For fixed \(u\), each support function \(h_{F_s}(u)\) is the maximum of two affine functions of \(s\). Thus \(w_s(u)\) is convex in \(s\), and for every finite increasing convex \(\varphi\), the map \(s\mapsto\varphi(w_s(u))\) is convex. Its Haar average \(g_\varphi(s)\) is convex. Reflection in the end planes shows \(g_\varphi(-s)=g_\varphi(s)\); hence it is nondecreasing for \(s\ge0\). To prove strictness for strictly increasing \(\varphi\), pair opposite horizontal directions \(v,-v\) at fixed \(t\). By (4), their arithmetic-mean width exceeds \(w_0(v,t)\) by
\[
\frac12\big[(2sa p-Ht)_++(2sa q-Ht)_+\big],\tag{7}
\]
which is positive on an open set of directions whenever \(s>0\). Jensen's inequality and strict monotonicity of \(\varphi\) give \(g_\varphi(s)>g_\varphi(0)\); convexity then yields strict increase between every two distinct nonnegative taper parameters. This proves increasing convex order (and its strict test-function form) for any dimension, since no dimension-specific step was used.

If \(K=-K\), then \(p=q\) and (4) reduces to
\[
w_s(v,t)=2a h_K(v)+Ht+(2sa h_K(v)-Ht)_+,\tag{8}
\]
which is pointwise nondecreasing with \(s\), and strictly increasing on a positive-measure set for \(s_2>s_1\). This proves the stronger first-order stochastic order and distinction of the laws.

## Verification
Run `python3 verify.py`. The standalone program independently maximizes the support of the two generating sections, compares that direct width with (4), and checks two-dimensional midpoint quadrature against (1) for an asymmetric triangle and a centrally symmetric square at three taper levels. It also checks the quadratic coefficient, the pointwise order for the square, and the disk response via a separate high-resolution integral. On the supplied test examples the program prints `ALL_CHECKS_PASSED`. These numerical checks do not prove the all-body ordering or uniqueness; those follow from the exact support-max identities and compact moment determinacy.

## Relationship to prior work
Horváth and Lángi, *On the convex hull and homothetic convex hull functions of a convex body* (arXiv:2012.08955v1, 16 December 2020; Geometriae Dedicata, 2022), study **volume** functions of convex hulls with translates or homothetic copies, including uniqueness from the labeled translation vector. Their full open-access Sections 1–3 do not state a random directional-width response or its support-histogram inverse.

Kim, Yaskin, and Zvavitch, *Distribution functions of sections and projections of convex bodies* (arXiv:1512.07289v1, 22 December 2015), investigate tomography without directional labels and exhibit nonuniqueness in several settings. Their full text discusses the support-function distribution, but does not treat a controlled one-parameter homothetic-frustum mean-width response. The present recovery is **only of that distribution**, not of the base shape, consistent with their nonuniqueness examples.

The known convexity of shadow-system functionals and basic support-function identities motivate, and in part subsume, the qualitative convex-order observation. Originality is claimed for the exact all-base identity (1), its response-equivalence classification, and the explicit support-moment readout (2), **not** for the general fact that support functions are convex under affine parameter changes. Relevant published notes on Santaló volume products of homothetic frusta, regular prisms, and line widths of individual right circular cones concern different functionals or fixed shapes; their full statements do not imply the response-equivalence theorem without new work.

## Limitations
Observing the entire ideal taper-response curve requires measurements across a continuous parameter family; no finite set of taper levels is asserted sufficient for arbitrary bases. Even the complete response determines only the distribution of the support function, not its angular ordering and not the body's congruence class. No finite-sample, noisy-measurement, or stability guarantee is proved. The homothety center and height must be fixed and known. The natural inference of originality is provisional because older stereological treatments of conical frusta could contain an equivalent transform.

## References
1. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, arXiv:2012.08955v1 (2020-12-16), https://arxiv.org/abs/2012.08955 ; *Geometriae Dedicata* 216 (2022), 10.
2. J. Kim, V. Yaskin, and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1 (2015-12-22), https://arxiv.org/abs/1512.07289 ; *J. London Math. Soc.* 95 (2017), 1–24.
3. Y. S. Soh and V. Chandrasekaran, *Fitting Tractable Convex Sets to Support Function Evaluations*, arXiv:1903.04194v1 (2019-03-11), https://arxiv.org/abs/1903.04194 ; *Discrete Comput. Geom.* 2021.
