# Two-mode pinning in off-centre resetting of sluggish diffusion

## Finding

Fix a sluggishness exponent \(\alpha>0\), a Poisson reset rate \(r>0\), and a reset location \(b>0\) relative to the fixed heterogeneity centre at zero. Write \(a=\alpha+2\), \(\nu=1/a\), and \(c=2\sqrt r/a\). Define the decreasing decaying solution of \(q''(x)=r x^\alpha q(x)\) on \([0,\infty)\) by
\[
q(x)=\frac{2(c/2)^\nu}{\Gamma(\nu)}\sqrt{x}\,K_\nu(c x^{a/2})\quad(x>0),\qquad q(0)=1,
\]
and put \(h=-q'(0)=(c/2)^{2\nu}\Gamma(1-\nu)/\Gamma(1+\nu)>0\). Let \(s\) solve the same ODE with \(s(0)=1\) and \(s'(0)=h\). The unique stationary probability density is
\[
p_{b,r}(x)=\frac{r|x|^\alpha}{2h}\begin{cases}
q(b)q(-x), &x<0,\\
q(b)s(x),&0<x<b,\\
s(b)q(x),&x>b.
\end{cases}
\]
Set \(p_{b,r}(0)=0\) and define the value at \(b\) by continuity.

There exists a unique \(m_{\alpha,r}>0\) maximizing \(x^\alpha q(x)\). This number is specified by the unique positive solution \(z_\alpha\) of
\[
\alpha=\frac{a}{2}z_\alpha\frac{K_{1-\nu}(z_\alpha)}{K_\nu(z_\alpha)},\qquad
m_{\alpha,r}=\left(\frac{a z_\alpha}{2\sqrt r}\right)^{2/a}.
\]
For every \(\alpha,r,b>0\) the stationary density has **exactly two strict local maxima**, at \(-m_{\alpha,r}\) and at \(\max\{b,m_{\alpha,r}\}\), separated by a strict zero at the origin. The positive maximum is strictly higher. In particular the right peak is pinned precisely at the reset point if and only if
\[
r\ge r_{\rm pin}=\left(\frac{a z_\alpha}{2}\right)^2 b^{-a}.
\]
The stationary probability on the opposite side of the mobility centre has the exact formula
\[
\mathbb P_{\rm st}(X<0)=\frac{q(b)}2=\frac12\mathbb E_b[e^{-r\tau_0}],
\]
where \(\tau_0\) is the first arrival at zero for the unreset diffusion. Reflection gives the corresponding statement for negative reset positions. No claim is made at \(\alpha=0\), where ordinary Brownian resetting has a single density maximum at its reset point.

## Assumptions and scope

The unreset motion is the conservative, non-sticky natural-scale diffusion on \(\mathbb R\) with infinitesimal generator \(Lf(x)=|x|^{-\alpha}f''(x)\) off zero and speed density \(|x|^\alpha\), with its unique continuous passage across zero in natural scale. The forward equation away from resets is \(\partial_t p=\partial_x^2(|x|^{-\alpha}p)\). Independent resets to the fixed location \(b\) occur at Poisson rate \(r\); the center of the spatially heterogeneous diffusivity remains fixed at zero when the reset location is varied. There are no absorbing boundaries, holding times at zero, or additional drifts. The named probability distribution is a spatial density with respect to Lebesgue measure.

The normalizations set the diffusivity prefactor to one. If \(Lf=D_0|x|^{-\alpha} f''\), replace \(r\) throughout the ODE and the pinning criterion by \(r/D_0\), with the physical stationary resetting rate retained in the renewal representation.

## Proof

**1. Canonical solutions.** The modified Bessel equation gives the stated positive decaying \(q\). The small-argument expansion of \(K_\nu\), valid for \(0<\nu<1/2\), shows \(q(0)=1\) and computes \(q'(0)=-h\). A convenient explicit growing counterpart is
\[
s(x)=\Gamma(1-\nu)(c/2)^\nu\sqrt{x}\,[I_{-\nu}(c x^{a/2})+I_\nu(c x^{a/2})],\qquad x>0.
\]
Its expansion at zero establishes \(s(0)=1\), \(s'(0)=h\). Since \(s''=r x^\alpha s\), \(s\) and \(s'\) stay strictly positive on \((0,\infty)\). The Wronskian \(s'q-sq'\) equals \(2h\) identically.

**2. The resolvent density.** Put \(u(x)=|x|^{-\alpha}p(x)\). Stationarity in distributions requires
\[
u''(x)-r|x|^\alpha u(x)=-r\delta_b.
\]
On the left half-line the decaying solution is \(q(-x)\), and continuity of \(u,u'\) across zero forces its continuation on \((0,b)\) to be \(s(x)\). On \((b,\infty)\) the decaying solution is \(q(x)\). The value of \(u\) is continuous at \(b\), and its derivative has jump \(u'(b+)-u'(b-)=-r\). The Wronskian identity therefore fixes the common prefactor to \(r/(2h)\), giving the stated piecewise formula. At infinity \(u'\to0\) on both sides; integrating the distributional equation over \(\mathbb R\) yields \(r\int p=r\), so the density is normalized. Positivity is immediate. The reset process regenerates at each independent exponential reset; its unique invariant law is the resolvent \(r\int_0^\infty e^{-rt}P_t(b,\cdot)dt\). The formula is that law by the normalized resolvent equation, establishing existence and uniqueness without treating a numerical solution as a proof.

**3. Strict unimodality of the decaying branch.** Let \(E(x)=q'(x)^2-rx^\alpha q(x)^2\). Direct differentiation and the ODE give
\[
E'(x)=-r\alpha x^{\alpha-1}q(x)^2<0.
\]
The Bessel asymptotics give \(E(x)\to0\) as \(x\to\infty\). Consequently \(E(x)>0\) at every finite positive \(x\), so
\[
(\log q)''(x)=rx^\alpha-(q'/q)^2<0.
\]
Thus \(\log(x^\alpha q(x))\) is strictly concave on \((0,\infty)\). Its argument tends to zero at both endpoints: near zero because \(\alpha>0\), and at infinity by the compressed-exponential decay of \(K_\nu\). It therefore has exactly one maximizer \(m_{\alpha,r}\). The Bessel derivative identity \((z^\nu K_\nu(z))'=-z^\nu K_{1-\nu}(z)\) yields the displayed scalar equation and proves uniqueness of its positive root. Its scaling \(m_{\alpha,r}\propto r^{-1/a}\) gives the pinning threshold.

**4. Counting all maxima and ordering their heights.** On the negative half-line the density is a positive constant times \(y^\alpha q(y)\) with \(y=-x\), so it has precisely one maximum at \(-m_{\alpha,r}\). On \((0,b)\), both factors \(x^\alpha\) and \(s(x)\) increase strictly; on \((b,\infty)\), the branch is a positive multiple of \(x^\alpha q(x)\). Thus the positive half-line has precisely one strict maximum at \(\max\{b,m_{\alpha,r}\}\), including the one-sided cusp case \(b\ge m_{\alpha,r}\). At zero the density vanishes and both neighboring values are positive. For \(0<x<b\), \(s(x)>q(x)\) since their common initial value and opposite initial slopes imply \(s-q>0\). For \(x\ge b\), \(s(b)>q(b)\). Consequently \(p(x)>p(-x)\) for every \(x>0\), and in particular the positive peak is higher than the negative peak.

**5. Opposite-side mass.** From the ODE, \(q''=rx^\alpha q\), and \(q'(\infty)=0\), hence
\[
\int_0^\infty x^\alpha q(x)\,dx=h/r.
\]
Integrating the negative branch of the density gives \(\mathbb P(X<0)=q(b)/2\). The backward Feynman–Kac boundary-value problem for hitting zero is \(Lf=rq\), with \(q(0)=1\) and \(q(\infty)=0\); uniqueness gives \(q(b)=\mathbb E_b[e^{-r\tau_0}]\).

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. It reconstructs the Bessel functions independently of the piecewise PDE proof, computes three stationary mass integrals, checks the opposite-side probability, the strict two-mode geometry, the distributional derivative jump, and two weak stationarity test-function identities. Seven parameter triples covering \(\alpha=0.35,0.5,1,2\), both pinned and unpinned regimes, passed **112 deterministic numerical assertions**. The printout is reproducible. Quadratures have finite numerical tolerance; all-parameter assertions follow from the analytic proof above, not from tests.

## Relationship to prior work

Frimpong, Bresque and Roldán (2026), arXiv:2610.21962v1, equations (15), (17)–(23) and §8, provide the same **Itô** sluggish forward operator, solve its origin-reset stationary distribution, and establish the single-sided Bessel first-hitting transform. Those pieces are prior work. Equation (15) formally permits a general source point, but the stationary analysis explicitly specializes to source zero; §8 identifies a nonzero source as a possible extension. The contribution here is the explicit off-centre matched resolvent together with the **complete peak-count and exact pinning classification** and the opposite-side mass identity. The centered bimodal shape and its radial single-peak branch are not claimed as new.

Lenzi et al. (2022), arXiv:2201.05598v1, already provide a powerful Green-function construction for **off-origin** resetting in power-law heterogeneous media (their equations (1) and (15)–(16)). Their governing forward diffusion term is \(\partial_x(D(x)\partial_x\rho)\), whereas here it is \(\partial_x^2(D(x)\rho)\). The operators differ by a nonzero drift term for nonconstant \(D\), so their published off-centre formula does not directly furnish this stationary law or its peak classification. General resetting resolvent principles are also standard and are not claimed as new.

## Limitations

The theorem concerns the specific conservative nonsticky Itô extension at the singular centre and the continuum model, not discrete finite-spacing regularizations or alternative interface conditions. It treats deterministic off-origin resets and positive \(\alpha\), with no higher-dimensional or randomized-location extension. The reset-centre location is held fixed as the rate varies. Existing general resolvent/Green methods may imply the explicit formula as a specialization; what is newly assessed is the sharp all-parameter two-peak pinning structure and satellite-mass law. The result has not undergone independent mathematical audit or an exhaustive external priority review.

## References

1. T. D. Frimpong, L. Bresque and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first posted 2026-10-15), https://arxiv.org/html/2610.21962v1.
2. M. K. Lenzi, E. K. Lenzi, L. M. S. Guilherme, L. R. Evangelista and H. V. Ribeiro, *Transient anomalous diffusion in heterogeneous media with stochastic resetting*, arXiv:2201.05598v1 (2022), https://arxiv.org/abs/2201.05598.
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters 106, 160601 (2011), general renewal-resolvent background.
