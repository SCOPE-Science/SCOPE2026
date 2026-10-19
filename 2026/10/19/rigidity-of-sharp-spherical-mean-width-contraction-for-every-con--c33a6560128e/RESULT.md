# Rigidity of sharp spherical mean-width contraction for every continuous monotone zonal kernel

## Finding

**Theorem.** Let \(n\ge 2\). Let \(k:[0,\pi]\to\mathbb R\) be continuous and nonincreasing, and let \(F:\mathbb S^{n-1}\to\overline{\mathbb B^n}\) be measurable. Define the zonal operator
\[
(T_kF)(\xi)=\int_{\mathbb S^{n-1}}k(\arccos\langle\xi,\eta\rangle)F(\eta)\,d\sigma(\eta),
\]
where \(\sigma\) is probability surface measure. Let \(\lambda_1(k)\) be its degree-one spherical-harmonic multiplier, and let \(w\) denote mean width normalized by \(w(\overline{\mathbb B^n})=2\). The sharp inequality
\[
w\bigl(\operatorname{co}T_kF(\mathbb S^{n-1})\bigr)\le 2\lambda_1(k)
\]
is due to Zhong and Kalaj [1]. Its **complete equality classification** is:

* If \(k\) is constant, equality holds for every \(F\).
* If \(k\) is nonconstant, equality holds if and only if \(F(\eta)=Q\eta\) for \(\sigma\)-almost every \(\eta\), for some \(Q\in O(n)\).

In particular, strict decrease is unnecessary: the equality rigidity also applies when \(k\) has plateaus or its Stieltjes decrease measure is singular and nonatomic. This extends the equality statement proved in [1], which assumes \(k\) strictly decreasing. The continuity hypothesis cannot simply be dropped: for the discontinuous hemispherical step kernel there are nonorthogonal equality maps.

## Assumptions and scope

Write \(c_n=|\mathbb S^{n-2}|/|\mathbb S^{n-1}|\) and, for \(0<t<\pi\), define the open cap \(C(u,t)=\{\eta:\langle u,\eta\rangle>\cos t\}\), its measure
\[
s(t)=c_n\int_0^t\sin^{n-2}v\,dv,
\]
and the first-cap moment
\[
\Phi_n(s(t))=\int_{C(u,t)}\langle u,\eta\rangle\,d\sigma(\eta)=\frac{c_n}{n-1}\sin^{n-1}t.
\]
The identity holds also for \(n=2\). The function \(\Phi_n:(0,1)\to(0,\infty)\) is strictly concave: \(\Phi_n'(s(t))=\cos t\) and \(\Phi_n''(s(t))=-\sin t/s'(t)<0\).

For nonconstant continuous nonincreasing \(k\), let \(\nu=-dk\) denote its positive **nonatomic** Stieltjes measure on \((0,\pi)\), with total mass \(k(0)-k(\pi)>0\). Integration by parts gives
\[
\lambda_1(k)=\int_{(0,\pi)}\Phi_n(s(t))\,d\nu(t)>0.
\]
All assertions concern arbitrary measurable boundary data into the closed Euclidean unit ball; no smoothness, invertibility, or injectivity of \(F\) is assumed.

## Proof

**1. The sharp inequality and an equality radius.** For \(u\in\mathbb S^{n-1}\) and \(s\in(0,1)\), set
\[
M_u(s)=\sup\left\{\int a(\eta)\langle F(\eta),u\rangle\,d\sigma(\eta):0\le a\le1,\ \int a\,d\sigma=s\right\},\qquad J(s)=\int M_u(s)\,d\sigma(u).
\]
The spherical rearrangement lemma of [1, Section 3] asserts \(J(s)\le\Phi_n(s)\). The layer-cake formula and support-function maximization, also as in [1, Section 4], give
\[
\frac12w\bigl(\operatorname{co}T_kF(\mathbb S^{n-1})\bigr)
\le\int J(s(t))\,d\nu(t)
\le\int\Phi_n(s(t))\,d\nu(t)=\lambda_1(k).\tag{1}
\]
Assume equality. Since the integrands in the second inequality are ordered, \(J(s(t))=\Phi_n(s(t))\) for \(\nu\)-almost every \(t\). Moreover, for each \(u\), compactness gives a maximizing center \(\xi(u)\) for the support function of \(T_kF\) in direction \(u\). A measurable maximizing selection exists because the integrals are jointly continuous in the center and measurable in \(u\). Equality in the first part of (1), followed by Tonelli, shows that for \(\nu\)-almost every \(t\), the selector \(\mathbf1_{C(\xi(u),t)}\) maximizes \(M_u(s(t))\) for \(\sigma\)-almost every \(u\).

**2. A generic cap has no zero harmonic multipliers.** Let \(B_tg(u)=\int_{C(u,t)}g(\eta)\,d\sigma(\eta)\). The Funk--Hecke formula makes \(B_t\) scalar on every spherical-harmonic subspace of degree \(\ell\ge1\), with multiplier \(b_\ell(t)\). Each \(b_\ell\) is real analytic on \((0,\pi)\) and is not identically zero: \(b_\ell(t)/s(t)\to1\) as \(t\downarrow0\) under standard zonal-harmonic normalization. Therefore the exceptional set \(E_n=\bigcup_{\ell\ge1}\{t:b_\ell(t)=0\}\) is countable. In dimension two the formula is explicitly \(b_\ell(t)=\sin(\ell t)/(\pi\ell)\). Because \(\nu\) has no atoms, \(\nu(E_n)=0\). Fix a radius \(t\notin E_n\), \(0<t<\pi\), for which both equality properties in Step 1 hold; put \(s=s(t)\).

**3. Equality of the rearrangement bound makes the pushforward uniform.** Choose a jointly measurable maximizing selector \(a_u(\eta)\in[0,1]\) for \(M_u(s)\), of mass \(s\) for almost every \(u\). Such selectors follow from the quantile/bathtub principle, with a measurable allocation on a threshold level if needed. Write \(q(\eta)=\int a_u(\eta)\,d\sigma(u)\). Interchange integrals, apply the spherical cap bathtub principle in the \(u\)-variable, and use \(\|F(\eta)\|\le1\):
\[
J(s)\le\int\|F(\eta)\|\Phi_n(q(\eta))\,d\sigma(\eta)
\le\int\Phi_n(q(\eta))\,d\sigma(\eta)
\le\Phi_n\!\left(\int q\,d\sigma\right)=\Phi_n(s).\tag{2}
\]
Here \(\int q\,d\sigma=s\) follows from the fixed mass of each \(a_u\). Since equality holds and \(\Phi_n\) is strictly concave, \(q=s\) almost everywhere. As \(\Phi_n(s)>0\), equality also forces \(\|F(\eta)\|=1\) almost everywhere. Uniqueness of the maximizing spherical cap in the bathtub principle then forces
\[
a_u(\eta)=\mathbf1_{\{\langle F(\eta),u\rangle>\cos t\}}
\quad\text{for almost every pair }(u,\eta).
\]
Thus, if \(\mu=F_\#\sigma\), then \(\mu(C(u,t))=s\) for almost every \(u\). Applying the cap operator to the signed measure \(\mu-\sigma\), and testing with any spherical harmonic of degree \(\ell\ge1\), gives \(b_\ell(t)\int Y_\ell\,d(\mu-\sigma)=0\). None of these multipliers vanishes, and both measures have unit mass; density of spherical harmonics in continuous functions implies \(\mu=\sigma\).

**4. Pullbacks of one generic cap are caps.** Since \(\mu=\sigma\), the scalar field \(\langle F(\eta),u\rangle\) has the continuous spherical-coordinate distribution. Its unique optimal mass-\(s\) selector is \(\mathbf1_{F^{-1}C(u,t)}\). Equality of the selected physical cap in Step 1 and uniqueness of the bathtub selector give
\[
F^{-1}C(u,t)=C(\xi(u),t)\pmod\sigma
\qquad\text{for almost every }u.\tag{3}
\]

**5. A fixed-radius cap-pullback rigidity lemma.** Suppose a measurable map \(G:\mathbb S^{n-1}\to\mathbb S^{n-1}\) preserves \(\sigma\) and satisfies \(G^{-1}C(u,t)=C(v(u),t)\pmod\sigma\) for almost every \(u\), where \(0<t<\pi\) is fixed. Then \(G\) agrees almost everywhere with an orthogonal transformation. Indeed, set \(H_t(\theta)=\sigma(C(u,t)\mathbin\triangle C(v,t))\) when the center distance is \(\theta\). It is continuous, positive for \(\theta>0\), and strictly increasing on some interval \([0,\varepsilon]\). For \(n=2\) this follows directly from the overlap of two equal arcs. In higher dimensions, slice by the plane of the two centers: in each planar-radius slice the cap sections are equal circular arcs (or the full/empty circle); rotating their centers by a small angle strictly increases symmetric difference for a positive-measure collection of nontrivial arcs and never decreases it. This also proves the asserted local strict increase. Measure preservation and (3) yield
\[
H_t(d(v(u),v(u')))=H_t(d(u,u'))
\]
for all \(u,u'\) in a full-measure dense subset. Continuity, positivity away from zero, and strict increase near zero show that sufficiently close such pairs have equal geodesic distances. The center map therefore extends uniquely to a locally distance-preserving map on the whole sphere. On each small open spherical ball choose \(n\) linearly independent points; preservation of all their Gram products supplies one orthogonal matrix agreeing with the map throughout that ball. Matrices agree on overlapping open balls, so connectedness gives one global \(Q\in O(n)\), with \(v(u)=Qu\). The cap-pullback identities for almost all centers then give \(G(\eta)=Q^T\eta\) for almost every \(\eta\) (caps distinguish distinct sphere points). Apply this lemma to \(G=F\) to obtain the desired orthogonal form.

**6. Converse, constant case, and boundary.** If \(F(\eta)=Q\eta\), rotational symmetry gives \(T_kF(\xi)=\lambda_1(k)Q\xi\), a sphere whose convex hull has width \(2\lambda_1(k)\). If \(k\) is constant, \(T_kF\) is constant, \(\lambda_1(k)=0\), and both sides of the inequality vanish.

To see why continuity matters, take the discontinuous hemisphere kernel \(k(\theta)=\mathbf1_{[0,\pi/2)}(\theta)\) and an invertible nonconformal real matrix \(A\). Define \(F_A(\eta)=A\eta/\|A\eta\|\). It is odd but not orthogonal. For every output direction \(u\), the selector \(\{\eta:\langle F_A(\eta),u\rangle>0\}=C(A^Tu/\|A^Tu\|,\pi/2)\) is a hemisphere. The support function therefore equals \(\int\max\{0,\langle F_A(\eta),u\rangle\}\,d\sigma(\eta)\). Averaging over \(u\) gives \(\frac12w=\Phi_n(1/2)=\lambda_1(k)\), although \(F_A\) is nonorthogonal. The example is outside the continuous-kernel hypothesis.

## Verification

The proof requires the analyticity and nonzero small-cap limit of each spherical cap multiplier, uniqueness and equality in the spherical cap bathtub principle, and the fixed-radius cap-pullback lemma proved above. The included standalone `verify_examples.py` uses only the Python standard library. It numerically compares eighteen exact circle-cap multipliers with Riemann sums and checks hemisphere-step equality for a nonorthogonal circle map. These finite computations are corroborative only: neither establishes the all-dimension theorem nor replaces the compactness and harmonic-completeness arguments.

## Relationship to prior work

Zhong and Kalaj [1] proved the sharp mean-width inequality for every continuous nonincreasing zonal kernel, with equality rigidity asserted for **strictly decreasing** kernels. Here their inequality and their spherical rearrangement lemma are used as established inputs. The new assertion removes the strict-decrease condition from the equality characterization, including kernels whose decrease is confined to a singular nonatomic Stieltjes measure. The proof replaces the need for full support of that measure by the fact that all nonconstant-degree cap multipliers are simultaneously nonzero except at countably many radii. The geometric cap-pullback lemma supplies the remaining rigidity. The spherical-cap discrepancy literature [2] offers related spectral context, not the sharp mean-width equality classification.

## Limitations

The result treats nonincreasing **continuous** kernels, not all monotone kernels with jumps; the hemispherical step demonstrates an actual failure outside that hypothesis. Only equality rigidity is added; the numerical sharp mean-width bound is attributed to [1]. The proof concerns boundary sphere data, not arbitrary noneuclidean domains. Historical-priority uncertainty remains for potentially differently formulated fixed-radius cap-preserving results and equality statements, and no independent external scientific audit has been performed.

## References

[1] Deguang Zhong and David Kalaj, *Sharp mean-width and Jacobian bounds for Euclidean and hyperbolic harmonic maps*, arXiv:2609.09316, first posted 2026-09-08. https://arxiv.org/abs/2609.09316 (Sections 3 and 4).

[2] Dmitriy Bilyk, Michelle Mastrianni and Stefan Steinerberger, *Single radius spherical cap discrepancy via Gegenbadly Approximable Numbers*, arXiv:2308.00694, first posted 2023-08-01. https://arxiv.org/abs/2308.00694.
