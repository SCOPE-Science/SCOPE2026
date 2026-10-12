# Generic convex-order incomparability within every prescribed-mean fiber
## Finding
For every real number \(m\in(0,1)\), define
\[
\mathcal P_m=\left\{\mu\in\mathcal P([0,1]):\int_0^1 x\,\mu(dx)=m\right\},
\]
with the topology of weak convergence. A probability law \(\mu\) is below \(\nu\) in convex order, written \(\mu\le_{\mathrm{cx}}\nu\), when
\[
\int\varphi\,d\mu\le\int\varphi\,d\nu
\]
for all continuous convex functions \(\varphi:[0,1]\to\mathbb R\).

**Theorem.** The set of comparable pairs
\[
\mathcal K_m=\{(\mu,\nu)\in\mathcal P_m^2:\mu\le_{\mathrm{cx}}\nu\text{ or }\nu\le_{\mathrm{cx}}\mu\}
\]
is closed and nowhere dense in \(\mathcal P_m^2\). Consequently the incomparable pairs form an **open dense**, hence co-meager, subset of this compact complete space.

The density statement holds with regular representatives: every nonempty product-weak neighborhood in \(\mathcal P_m^2\) contains two incomparable laws of mean exactly \(m\), each possessing a strictly positive \(C^\infty\) density on \([0,1]\).

The common-mean restriction is substantive. Convex ordering always forces equality of means; an ambient Baire-category assertion for increasing convex order on *all* bounded-support laws does not imply a relative category assertion on the prescribed-mean subspace.

## Assumptions and scope
The support interval is \([0,1]\), and \(0<m<1\) is fixed. By an affine transformation, the theorem holds for every compact nondegenerate real interval and every mean strictly inside it. Both measures are required to have **the same exact mean** at every stage of the perturbation; no approximation that changes the mean is used.

For each \(\mu\in\mathcal P_m\), let
\[
C_\mu(t)=\int_0^1(x-t)_+\,\mu(dx),\qquad
P_\mu(t)=\int_0^1(t-x)_+\,\mu(dx).
\]
The equal-mean identities are
\[
C_\mu(t)-P_\mu(t)=m-t,
\]
and
\[
\mu\le_{\mathrm{cx}}\nu
\quad\Longleftrightarrow\quad
C_\mu(t)\le C_\nu(t)\quad(0\le t\le1).
\tag{1}
\]
The second characterization follows from the hinge decomposition of convex functions; it is also a standard univariate convex-order criterion.

## Proof
**1. Closedness.** The space \(\mathcal P([0,1])\) is weakly compact and metrizable. Since \(x\mapsto x\) is bounded continuous, the exact-mean fiber \(\mathcal P_m\) is closed and hence compact. For each \(t\in[0,1]\), the map \(\mu\mapsto C_\mu(t)\) is weakly continuous. By (1), each oriented convex-order relation is an intersection of closed halfspaces in \(\mathcal P_m^2\). Their union \(\mathcal K_m\) is closed.

**2. Perturb a strict comparable pair.** Fix \(\mu\le_{\mathrm{cx}}\nu\) with \(\mu\ne\nu\). Their stop-loss transforms cannot agree at every strike, since those transforms determine the distributions. Hence there is a \(t_0\in(0,1)\) with
\[
C_\mu(t_0)<C_\nu(t_0).
\tag{2}
\]
Let
\[
B_m=(1-m)\delta_0+m\delta_1
\]
be the endpoint Bernoulli law with mean \(m\), and let
\[
T_\delta(x)=m+(1-\delta)(x-m),\qquad0<\delta<1.
\]
This affine compression preserves the mean, and
\[
T_\delta([0,1])=[\delta m,\ 1-\delta(1-m)]\subset(0,1).
\]
For \(0<\varepsilon<1\), put
\[
\mu_\varepsilon=(1-\varepsilon)\mu+\varepsilon B_m,
\qquad
\nu_\delta=(T_\delta)_\#\nu.
\]
Both remain in \(\mathcal P_m\). As \(\varepsilon,\delta\downarrow0\), they converge weakly to \(\mu,\nu\). For sufficiently small parameters, (2) remains strict for \(\mu_\varepsilon,\nu_\delta\), so
\[
\nu_\delta\not\le_{\mathrm{cx}}\mu_\varepsilon.
\]
But for any
\[
1-\delta(1-m)<t<1,
\]
we have
\[
C_{\nu_\delta}(t)=0,
\qquad
C_{\mu_\varepsilon}(t)\ge\varepsilon m(1-t)>0.
\]
Therefore \(\mu_\varepsilon\not\le_{\mathrm{cx}}\nu_\delta\) as well. This constructs incomparable pairs arbitrarily near every *strict* comparable pair. The case \(\nu\le_{\mathrm{cx}}\mu\) is symmetric.

**3. Perturb an equal pair.** Let \(\mu=\nu\in\mathcal P_m\), and let
\[
H_\delta=(T_\delta)_\#\mu.
\]
Define two two-point laws, both with mean \(m\):
\[
B_m^{\mathrm{upper}}
=\frac{2(1-m)}{2-m}\delta_{m/2}
+\frac{m}{2-m}\delta_1,
\tag{3}
\]
\[
B_m^{\mathrm{lower}}
=\frac{1-m}{1+m}\delta_0
+\frac{2m}{1+m}\delta_{(1+m)/2}.
\tag{4}
\]
Put
\[
F_{\varepsilon,\delta}=(1-\varepsilon)H_\delta+\varepsilon B_m^{\mathrm{upper}},
\quad
G_{\varepsilon,\delta}=(1-\varepsilon)H_\delta+\varepsilon B_m^{\mathrm{lower}}.
\]
Both converge weakly to \(\mu\) as \(\varepsilon,\delta\downarrow0\), and both retain the exact mean \(m\). Every support point of \(F_{\varepsilon,\delta}\) lies strictly above zero, whereas \(G_{\varepsilon,\delta}\) has an atom \(\varepsilon(1-m)/(1+m)>0\) at zero. Choose a strike \(t_-\) strictly between zero and the smallest possible support point of \(F_{\varepsilon,\delta}\). Then
\[
P_F(t_-)=0<P_G(t_-),
\]
so by equal means,
\[
C_F(t_-)<C_G(t_-).
\tag{5}
\]
Likewise every support point of \(G_{\varepsilon,\delta}\) is strictly below one, whereas \(F_{\varepsilon,\delta}\) has an atom \(\varepsilon m/(2-m)>0\) at one. Choose \(t_+\) above the largest possible support point of \(G_{\varepsilon,\delta}\) and below one. Then
\[
C_G(t_+)=0<C_F(t_+).
\tag{6}
\]
The opposite inequalities (5)–(6) make this pair incomparable. Thus incomparable pairs are dense even at the diagonal, completing the proof that \(\mathcal K_m\) has empty interior. Combined with closedness, this proves it is nowhere dense.

**4. Smooth, strictly positive witnesses.** It suffices to show that each member of \(\mathcal P_m\) can be weakly approximated by smooth, strictly positive densities with the *same* mean. Compress its law by \(T_\delta\), then convolve with a symmetric, centered \(C^\infty\) probability mollifier supported in a sufficiently small interval around zero. Because the compressed support is bounded away from both endpoints, the mollified law remains on \([0,1]\), is smooth, and still has mean \(m\).

For each \(m\in(0,1)\) there exists a unique parameter \(a\in\mathbb R\) such that the strictly positive smooth density
\[
f_a(x)=\frac{e^{ax}}{\int_0^1e^{ay}\,dy}
\quad(0\le x\le1)
\]
has mean \(m\). Indeed its mean is strictly increasing in \(a\), with derivative equal to its positive variance and limits zero and one at the two infinities. Mix an arbitrarily small positive amount of this density with the mollified law. The result is strictly positive, smooth, and mean-preserving. Applying this approximation separately to the two incomparable laws above and preserving the strict inequalities (5)–(6), or their counterparts from step 2, proves the smooth density assertion.

## Verification
The standalone `verify.py` replays the mean-preserving perturbation formulas with exact rational arithmetic for several values of \(m\), including near-endpoint means. In the illustrative equal-law case \(m=1/2\), with original law \(\delta_{1/2}\) and mixture weight \(1/10\), equations (3)–(4) give
\[
F=\frac9{10}\delta_{1/2}+\frac1{10}
\left(\frac23\delta_{1/4}+\frac13\delta_1\right),
\]
\[
G=\frac9{10}\delta_{1/2}+\frac1{10}
\left(\frac13\delta_0+\frac23\delta_{3/4}\right).
\]
Their stop-loss differences are exactly
\[
C_F(1/8)-C_G(1/8)=-\frac1{240},
\qquad
C_F(7/8)-C_G(7/8)=\frac1{240}.
\]
The verifier also replays the strict-comparison perturbation of \(\delta_{1/2}\le_{\mathrm{cx}}\frac12(\delta_0+\delta_1)\), and checks all constructed means exactly. A successful run ends with
`VERIFY_OK mean=1/2 low_gap=-1/240 high_gap=1/240 smooth_margin_positive=true`.

The finite tests do not establish the topological theorem; its proof is steps 1–4 above.

## Relationship to prior work
Durante, Fernández-Sánchez, and Ignazzi (2022), Theorem 4, establish that comparable pairs under increasing convex order, usual stochastic order, and mean residual life order are nowhere dense in the **full** weak space of bounded-support univariate distributions. The paper does not impose equality of the means. Its endpoint perturbation for increasing convex order changes the means and does not remain within \(\mathcal P_m^2\). The full-space nowhere-density result logically cannot be restricted to this closed, nowhere-dense mean fiber: an ambient nowhere-dense set could contain an entire such fiber.

The theorem here addresses the specific equal-mean fiber on which genuine convex order naturally lives. Every perturbation maintains the first moment *exactly*, and the proof handles separately strict comparable pairs and diagonal equal pairs. The smooth full-support approximation shows that this is not an artifact of introducing atoms at the endpoints.

Wiesel and Zhang (2023) give optimal-transport characterizations of convex order, including standard univariate characterizations, but do not address Baire-category genericity in a fixed moment fiber in the inspected material. Rodríguez-Griñolo and Úbeda-Flores (2026) study generic incomparability for convex orders on pairs of **bivariate copulas with fixed uniform marginals**; this is a different state space and does not imply the univariate prescribed-mean statement by a known direct restriction or reduction.

For comparison, on a *fixed three-point support grid* with prescribed mean, the feasible probability vectors form at most a one-dimensional segment and are totally ordered in convex order. Therefore generic incomparability in the full infinite-dimensional \(\mathcal P_m\) is a genuinely topology-dependent phenomenon and should not be inferred for every finite-support parametric submodel.

## Limitations
The result is topological, not probabilistic prevalence: a co-meager set need not have full measure under any given prior or sampling law on the space of distributions. It does not give quantitative rates of stochastic-order incomparability under random perturbations.

The smooth-density assertion concerns the *weak* topology and does not claim the same category result under a strong \(C^k\)-norm topology on densities. Endpoints \(m=0\) or \(m=1\) are excluded: each corresponding mean fiber consists of a single point, so the conclusion is false there.

The principal bibliographic risk is an equivalent theorem in older order-theoretic or probability-measure topology literature under prescribed barycenter, majorization, or stop-loss terminology.

## References
1. F. Durante, J. Fernández-Sánchez, and C. Ignazzi, “Baire category results for stochastic orders,” *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* **116**, article 188 (2022). DOI: 10.1007/s13398-022-01324-3. First publicly available date verified: 30 September 2022.
2. J. Wiesel and E. Zhang, “An optimal transport-based characterization of convex order,” *Dependence Modeling* **11** (2023), article 20230102. DOI: 10.1515/demo-2023-0102; arXiv:2207.01235.
3. M. del R. Rodríguez-Griñolo and M. Úbeda-Flores, “New Baire category results for stochastic orders on bivariate copulas,” arXiv:2606.09660 (8 June 2026). Compared through its publicly indexed abstract; full-text comparison remains a residual literature risk.
