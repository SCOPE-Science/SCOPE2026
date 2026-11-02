# Full occupation large deviations and the sluggish Lamperti edge exponent under Poisson resetting

## Finding
Consider the continuum sluggish diffusion started from the origin and independently reset to the origin at Poisson rate \(r>0\). Fix \(\alpha>0\) and set \(\mu=1/(\alpha+2)\in(0,1/2)\). Let
\[
 A_T=\int_0^T\mathbf 1_{\{X_t>0\}}\,dt,\qquad U_T=A_T/T.
\]
Then \((U_T)_{T>0}\) obeys a full large-deviation principle with speed \(T\) and an exact good rate \(I_{\mu,r}\), zero only at \(1/2\). Its scaled cumulant generating function is the unique real \(\psi_{\mu,r}(k)\), for each \(k\in\mathbb R\), satisfying
\[
 r\,\frac{(r+\psi)^{\mu-1}+(r+\psi-k)^{\mu-1}}
 {(r+\psi)^\mu+(r+\psi-k)^\mu}=1,
 \qquad r+\psi>\max\{0,k\}.
\]
The rate is
\[
 I_{\mu,r}(u)=\sup_{k\in\mathbb R}\{ku-\psi_{\mu,r}(k)\},\quad 0\le u\le1,
\]
and is \(+\infty\) otherwise. This implicit formula also admits an elementary one-parameter representation: for \(q>0\),
\[
 k(q)=r\frac{(1-q)(1+q^{\mu-1})}{1+q^\mu},\qquad
 \psi(k(q))=r\frac{(1-q)q^{\mu-1}}{1+q^\mu}.
\]
The map \(q\mapsto k(q)\) is a bijection from \((0,\infty)\) to \(\mathbb R\), with decreasing orientation. In particular, \(\psi\) is strictly convex and analytic, \(\psi'(0)=1/2\), \(\psi''(0)=(1-\mu)/(2r)\), and \(\psi(k)=k+\psi(-k)\). The rate is strictly convex and symmetric about \(1/2\), with \(I_{\mu,r}(0)=I_{\mu,r}(1)=r\).

The non-Gaussian edges have the sharp exponent dictated by sluggishness: as \(\varepsilon\downarrow0\),
\[
 I_{\mu,r}(\varepsilon)=I_{\mu,r}(1-\varepsilon)
 =r-\frac{r}{\mu}\left(\frac{\mu}{1-\mu}\right)^{1-\mu}
 \varepsilon^\mu+o(\varepsilon^\mu).
\]
For \(\alpha=0\), or \(\mu=1/2\), the formulas reduce to the already-known reset Brownian rate \(r[1-2\sqrt{u(1-u)}]\); this Brownian case is not claimed as a discovery. The assessed contribution is the full explicit \(\alpha>0\) rate characterization and its exact sluggish endpoint exponent and coefficient, not the generic resetting-renewal principle.

## Assumptions and scope
The *continuum* free process \(X_t\) has forward equation \(\partial_t p=\partial_x^2(|x|^{-\alpha}p)\), starts at \(0\), and uses the symmetric self-similar diffusion realization underlying the Lamperti occupation law in [1]. Each Poisson reset independently restarts its complete free-path dynamics at \(0\). A positive-sojourn indicator is defined by strict positivity; occupation of the single point zero has zero Lebesgue time. We require finite \(\alpha>0\) and \(r>0\), so \(0<\mu<1/2\). The extension to \(\alpha=0\) is a check against prior Brownian work [2]. The theorem concerns the continuous diffusion limit rather than a fixed lattice spacing, and makes no assertions about finite-time density prefactors at \(u=0\) or \(u=1\).

The full LDP means: for every Borel set \(B\subset\mathbb R\), with interior \(B^\circ\) and closure \(\overline B\),
\[
 -\inf_{u\in B^\circ}I_{\mu,r}(u)\le
 \liminf_{T\to\infty}T^{-1}\log\mathbb P(U_T\in B)
 \le\limsup_{T\to\infty}T^{-1}\log\mathbb P(U_T\in B)
 \le-\inf_{u\in\overline B}I_{\mu,r}(u).
\]

## Proof
**1. The free occupation law and its transform.** The self-similar sluggish diffusion has free positive occupation fraction \(V_t=t^{-1}\int_0^t\mathbf1_{\{X_s>0\}}ds\) with the same symmetric Lamperti distribution for every deterministic \(t>0\), as established in [1]. Its density, for \(0<u<1\), is
\[
 f_\mu(u)=\frac{\sin(\pi\mu)}\pi\,
 \frac{u^{\mu-1}(1-u)^{\mu-1}}
 {u^{2\mu}+(1-u)^{2\mu}+2u^\mu(1-u)^\mu\cos(\pi\mu)}.
\]
Equivalently, \(V\) has the law of \(S_1/(S_1+S_2)\) for independent positive \(\mu\)-stable variables with \(\mathbb E e^{-zS_i}=e^{-z^\mu}\). This representation yields the Stieltjes identity, for \(a,b>0\),
\[
 \mathbb E\frac1{a(1-V)+bV}
 =\frac{a^{\mu-1}+b^{\mu-1}}{a^\mu+b^\mu}.
\]
Indeed, multiply the integrand by \(S_1+S_2\), represent the denominator inverse by \(\int_0^\infty e^{-s(aS_2+bS_1)}ds\), differentiate both stable Laplace transforms and integrate \(\mu s^{\mu-1}e^{-(a^\mu+b^\mu)s^\mu}\). Relabeling the independent variables permits either orientation of \(a,b\).

**2. The reset renewal equation.** Put \(M_k(t)=\mathbb E[e^{kA_t}]\) and \(g_k(t)=\mathbb E[e^{ktV}]\) for a fresh free excursion of deterministic duration \(t\). The first-reset decomposition gives, for \(t\ge0\),
\[
 M_k(t)=e^{-rt}g_k(t)+r\int_0^t e^{-rs}g_k(s)M_k(t-s)\,ds.
\]
Self-similarity is essential: the free-sojourn fraction of an interval, conditional on its length \(s\), has the same law \(V\). For \(a>\max\{0,k\}\), Tonelli's theorem and Step 1 give
\[
 G_k(a)=\int_0^\infty e^{-at}g_k(t)\,dt
 =\mathbb E\frac1{a-kV}
 =\frac{a^{\mu-1}+(a-k)^{\mu-1}}{a^\mu+(a-k)^\mu}.
\]
Consequently \(\int_0^\infty e^{-st}M_k(t)dt=G_k(r+s)/[1-rG_k(r+s)]\) whenever the denominator is positive. This is the general resetting-renewal identity already available in [2,3], here explicitly evaluated for the sluggish Lamperti law.

**3. Existence of the growth exponent, analyticity, and the LDP.** The strictly decreasing continuous function \(a\mapsto rG_k(a)\) tends to \(+\infty\) as \(a\downarrow\max\{0,k\}\), because the Lamperti measure has singular but integrable mass at both endpoints, and tends to zero as \(a\to\infty\). Thus there is a unique \(a=r+\psi(k)>\max\{0,k\}\) with \(rG_k(a)=1\).

Multiply the renewal equation by \(e^{-\psi(k)t}\). Its convolution kernel \(re^{-(r+\psi(k))t}g_k(t)\,dt\) is a non-arithmetic probability measure, of finite strictly positive mean. The forcing term \(e^{-(r+\psi(k))t}g_k(t)\) is continuous, positive and exponentially integrable because \(r+\psi(k)>\max\{0,k\}\). The ordinary key-renewal theorem therefore gives \(M_k(t)e^{-\psi(k)t}\to C(k)\in(0,\infty)\). In particular, \(\lim_{t\to\infty}t^{-1}\log M_k(t)=\psi(k)\).

The pole equation is real analytic in \((k,\psi)\), and the partial derivative with respect to \(\psi\) is strictly negative, so \(\psi\) is real analytic on all \(\mathbb R\). For strict convexity, tilt the probability kernel in the preceding paragraph and call the resulting positive joint law of excursion time and occupation fraction \(Q_k(dt,du)\). Implicit differentiation yields
\[
 \psi'(k)=\frac{\mathbb E_{Q_k}[t u]}{\mathbb E_{Q_k}[t]}\in(0,1),
 \qquad
 \psi''(k)=\frac{\mathbb E_{Q_k}[t^2(u-\psi'(k))^2]}{\mathbb E_{Q_k}[t]}>0.
\]
The last inequality is strict because the Lamperti fraction has a positive density on \((0,1)\). The law of \(U_T\) is supported by the compact interval \([0,1]\), so exponential tightness is automatic. The differentiable finite scaled cumulant generating function and the Gärtner–Ellis theorem establish the full LDP on \((0,1)\), with its Legendre rate; the boundary lower bounds for open neighborhoods follow by taking interior points approaching the respective endpoints. The compact support gives the upper bound and a good rate on all of \(\mathbb R\). Strict convexity, the symmetry of \(V\) about \(1/2\), and the mean of \(V\) yield the indicated symmetry and unique zero.

**4. Explicit branch, quadratic core, and non-Gaussian edges.** Write \(q=(r+\psi-k)/(r+\psi)>0\). Solving the pole equation for \(r+\psi\) gives exactly the parameterization in the Finding. Uniqueness of the pole ensures \(k(q)\) traverses all real tilts once; equivalently its strict decreasingness follows from the positive Stieltjes derivative or directly from the displayed formulas. Differentiating at zero and using \(\mathbb EV=1/2\), \(\operatorname{Var}(V)=(1-\mu)/4\), and \(\mathbb E\tau^2/\mathbb E\tau=2/r\) for an exponential excursion duration gives \(\psi''(0)=(1-\mu)/(2r)\).

As \(q\downarrow0\), elementary expansion of the parameterization gives
\[
 k\sim rq^{\mu-1},\qquad b:=r+\psi-k\sim rq^\mu,
 \qquad 1-\psi'(k)\sim\frac\mu{1-\mu}q.
\]
In particular \(\psi(k)=k-r+r^{1/(1-\mu)}k^{-\mu/(1-\mu)}(1+o(1))\). Setting \(u=\psi'(k)=1-\varepsilon\), the Legendre equality \(I(u)=ku-\psi(k)\) gives
\[
 r-I(u)=k\varepsilon+b\sim\frac r{1-\mu}q^\mu,
 \qquad \varepsilon\sim\frac\mu{1-\mu}q,
\]
which yields the claimed exact edge coefficient. The opposite edge follows from \(V\overset{d}{=}1-V\). The same asymptotics give the endpoint values \(I(0)=I(1)=r\). For \(\mu=1/2\), the pole equation reduces to \((r+\psi)(r+\psi-k)=r^2\); its Legendre transform is the known Brownian formula in [2].

## Verification
Run `python verify.py` using Python 3 and its standard library. The program checks the Lamperti integral against an independently evaluated Stieltjes formula, normalisation and symmetry, root uniqueness in sampled parameter ranges, Gaussian curvature, the Brownian limiting formula, strict convexity samples, and endpoint scaling from the exact parameterization. It executes 298 deterministic numerical/algebraic checks. This program does not establish the infinite-time LDP, the analytic continuation, or the exact asymptotic statements; those depend on the proof above.

## Relationship to prior work
Frimpong, Bresque and Roldán [1] establish the sluggish model, free Lamperti occupation fraction, the Poisson-reset double-Laplace description, and Gaussian long-time core with variance \((1-\mu)/(2rT)\). Those are inputs and not claimed as new. Meylahn, Sabhapandit and Touchette [3] provide the general generating-function resetting identity and LDP methodology. Den Hollander, Majumdar, Meylahn and Touchette [2], particularly their Section IV, give the exact *Brownian* occupation LDP \(r[1-2\sqrt{u(1-u)}]\). Bressloff [4] applies related pole/LDP methods to run-and-tumble resetting. The present claim identifies, for the distinct nonconstant-diffusivity continuum sluggish family \(\alpha>0\), the exact Lamperti-dependent pole parameterization, entire rate and sharp endpoint exponent \(\mu\) with coefficient. The generic LDP mechanism and Brownian specialization are fully attributed to prior work. A broad prior treatment of positive stable occupation fractions within general resetting could imply portions of the present specialization and remains a priority risk.

## Limitations
No lattice-spacing-uniform assertion is made. The statements require complete memory-erasing Poisson resets to the symmetric origin, independent excursions, self-similar dynamics and finite sluggishness exponent. The result gives the large-deviation rate but not finite-time distributional prefactors or a computationally explicit elementary formula for \(I(u)\) at general \(u\). The endpoints describe rates for neighborhoods, not atoms at exactly \(0\) or \(1\). The independent scientific audit and broad priority certification have not been performed.

## References
[1] T. Dwamena Frimpong, L. Bresque and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1, first publicly submitted 2026-10-15. https://arxiv.org/abs/2610.21962 . The full-text Section 6.1 and conclusions were examined through https://www.paperpeel.com/paper/2610.21962 .

[2] F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018), *J. Phys. A* 52 (2019) 175001. Accessible full preprint: https://www.eurandom.tue.nl/reports/2018/002-report.pdf .

[3] J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, *Phys. Rev. E* 92 (2015) 062148, arXiv:1510.02431. https://arxiv.org/abs/1510.02431 .

[4] P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, *Phys. Rev. E* 102 (2020) 042135, arXiv:2009.01968. https://arxiv.org/abs/2009.01968 .
