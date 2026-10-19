# Cost-face periodic cycles have a strict risk surplus and opposite transverse Floquet shifts

## Finding

For the three-variable cooperation–risk–cost evolutionary game introduced by Wang, Hua, Liu, Zhang, Liu and Szolnoki, a natural resonant choice of risk-feedback rates generates periodic cooperation–risk trajectories on either invariant extreme-cost surface. Their **full three-dimensional** normal stability obeys an exact amplitude-dependent law. On every nonconstant periodic orbit contained in either surface, the mean cooperation level equals the feedback balance and the mean risk is *strictly larger* than the risk of the enclosed equilibrium. Consequently, the transverse Floquet exponent is strictly shifted upward on the minimum-cost face and strictly downward on the maximum-cost face, relative to its equilibrium value. At an exactly neutral transverse equilibrium on the minimum-cost face, every nearby nonconstant periodic orbit is transversely repelling; a concrete parameter family simultaneously makes the maximum-cost cycles transversely attracting.

More precisely, write \(q_*=(M-1)/(N-1)\), \(Q_*=Q(q_*)\), and \(r_*=c_0/(bQ_*)\). For each nonconstant periodic orbit \(\gamma\) of period \(T\), contained in \(c=c_0\) with \(c_0\in\{\beta,\alpha\}\), define \(\langle f\rangle=T^{-1}\int_0^T f(x(t),r(t))\,dt\). Then

\[
\langle x\rangle=q_*,\qquad
\langle r\rangle-r_* =\frac{\langle r(Q_*-Q(x))\rangle}{Q_*}>0.
\]

Let \(g(x,r)=\theta_1-(\theta_1+\theta_2)x-\theta_4+(\theta_3+\theta_4)r\), and put \(\sigma_{\beta}=1\), \(\sigma_{\alpha}=-1\). The exact transverse characteristic multiplier and real Floquet exponent are

\[
\mathcal M_{\perp}(\gamma)
=\exp\!\left(\sigma_{c_0}(\alpha-\beta)T\left[g(q_*,r_*)+(\theta_3+\theta_4)(\langle r\rangle-r_*)\right]\right),
\]
\[
\lambda_{\perp}(\gamma)=\frac1T\log \mathcal M_{\perp}(\gamma),\qquad
\lambda_{\perp}(\gamma)-\sigma_{c_0}(\alpha-\beta)g(q_*,r_*)
=\sigma_{c_0}(\alpha-\beta)(\theta_3+\theta_4)(\langle r\rangle-r_*).
\]

The last difference is strictly positive on the minimum-cost face and strictly negative on the maximum-cost face. This conclusion is nonperturbative: it holds for **every** nonconstant periodic orbit in the open cost face, whether or not it belongs to the local annulus constructed below. The exact annulus existence theorem applies at the resonance \(\mu_1/(\mu_1+\mu_2)=q_*\), with \(bQ_*>c_0\).

## Assumptions and scope

Let \(N\ge3\) and \(2\le M\le N-1\) be integers, and let \(b,\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4\) be strictly positive. Assume \(0<\beta<\alpha\). Consider the autonomous differential equations, with \(0\le x,r\le1\) and \(\beta\le c\le\alpha\):

\[
\begin{aligned}
\dot x&=x(1-x)[brQ(x)-c],\\
\dot r&=r(1-r)[\mu_1-(\mu_1+\mu_2)x],\\
\dot c&=(\alpha-c)(c-\beta)[\theta_1(1-x)-\theta_2x+\theta_3r-\theta_4(1-r)],\\
Q(x)&=\binom{N-1}{M-1}x^{M-1}(1-x)^{N-M}.
\end{aligned}
\]

The extremes \(c=\beta\) and \(c=\alpha\) are invariant **two-dimensional** faces; the full three-dimensional stability of their periodic orbits is the object of this result. Set \(\mu=\mu_1+\mu_2\). For existence of a local periodic annulus on a chosen face \(c=c_0\), impose the exact resonance
\[
\mu_1/\mu=q_*=(M-1)/(N-1),\qquad bQ_*>c_0>0.
\]

The second assumption ensures \(r_*\in(0,1)\). For both faces simultaneously, the stronger assumption \(bQ_*>\alpha\) suffices. There is **no** assumption on the signs of the cost-feedback bracket \(g\); its dependence on the parameters is part of the conclusion. Only the boundary cost face is invariant; nearby three-dimensional trajectories generally do not remain on it. Floquet terminology refers to normal linearization along an exactly periodic boundary-face trajectory.

## Proof

**1. Exact invariant and existence of cycles.** On \(c=c_0\), the equations reduce to
\[
\dot x=x(1-x)(brQ(x)-c_0),\qquad
\dot r=\mu r(1-r)(q_*-x).
\]
The binomial kernel has the exact logarithmic derivative
\[
\frac{Q'(x)}{Q(x)}=\frac{(N-1)(q_*-x)}{x(1-x)}.
\]
Introduce \(\kappa=(N-1)c_0/\mu\), \(A(r)=((1-r)/r)^\kappa\) and \(K=(N-1)b/\mu\). On the open square define
\[
H(x,r)=\frac{A(r)}{Q(x)}+K\int_{r_*}^{r}t^{-\kappa}(1-t)^{\kappa-1}\,dt.
\]
The integral is finite and smooth for each interior \(r\), since it never crosses an endpoint. Direct differentiation gives
\[
\begin{aligned}
H_x&=-A(r)Q'(x)/Q(x)^2,\\
H_r&=\frac{A(r)}{1-r}\left[K-\frac{\kappa}{rQ(x)}\right].
\end{aligned}
\]
Substituting the planar equations and the identity for \(Q'/Q\), the terms cancel exactly: \(H_x\dot x+H_r\dot r=0\).

The unique equilibrium in the open square is \((q_*,r_*)\). It is a critical point of \(H\) and its Hessian there is diagonal with
\[
H_{xx}(q_*,r_*)=\frac{A(r_*)(N-1)}{Q_*q_*(1-q_*)}>0,
\qquad
H_{rr}(q_*,r_*)=\frac{A(r_*)\kappa}{Q_*r_*^2(1-r_*)}>0.
\]
The mixed Hessian entry vanishes because \(Q'(q_*)=0\). Thus this equilibrium is a nondegenerate strict local minimum of the first integral. By the Morse lemma, all sufficiently small positive regular level sets \(H=H(q_*,r_*)+\delta\) are simple closed curves. The vector field is nowhere zero on each curve, since the interior equilibrium is unique. It is everywhere tangent to these curves; every such level curve is therefore exactly one periodic orbit. This proves an open annulus of nonconstant cycles around each admissible cost-face equilibrium, not an isolated limit cycle.

The linearized planar Jacobian at the center is
\[
J=\begin{pmatrix}
0&bQ_*q_*(1-q_*)\\
-\mu r_*(1-r_*)&0
\end{pmatrix}.
\]
Its eigenvalues are \(\pm i\omega\), where \(\omega^2=\mu c_0q_*(1-q_*)(1-r_*)>0\). For cycles shrinking to the center, smooth dependence on initial conditions and standard small-oscillation theory give the limiting period
\[
T\longrightarrow \frac{2\pi}{\sqrt{\mu c_0q_*(1-q_*)(1-r_*)}}.
\]
This period limit is **not** an assertion that finite-amplitude periods are constant.

**2. Exact averages and strict risk surplus.** Let \((x(t),r(t))\) be any nonconstant \(T\)-periodic solution lying in \((0,1)^2\) on a fixed-cost surface, under the same resonance. The logarithmic-odds identities are
\[
\frac{d}{dt}\log\frac{r}{1-r}=\mu(q_*-x),\qquad
\frac{d}{dt}\log\frac{x}{1-x}=brQ(x)-c_0.
\]
Integrating them over one full period yields \(\langle x\rangle=q_*\) and \(\langle rQ(x)\rangle=c_0/b=r_*Q_*\). Since \(Q\) has a **unique** maximum \(Q_*\) at \(q_*\), and \(r>0\),
\[
\langle r\rangle-r_*=\frac{\langle r[Q_*-Q(x)]\rangle}{Q_*}\ge0.
\]
Equality would require \(x(t)\equiv q_*\), forcing \(r(t)\equiv r_*\) by the first equation. Since the orbit is nonconstant, the inequality is strict. In the specific three-player, two-contributor case \(Q(x)=2x(1-x)\), this refines to
\[
\langle r\rangle-r_*=4\langle r(x-1/2)^2\rangle>0.
\]
This formula does not invoke an equilibrium approximation or assume that fluctuations are small.

**3. Exact three-dimensional transverse multiplier.** The derivative of the cost equation in the normal \(c\)-direction at \(c=c_0\) is
\[
\partial_c\dot c\big|_{c=c_0}=\sigma_{c_0}(\alpha-\beta)g(x,r),
\quad \sigma_{\beta}=+1,\quad \sigma_{\alpha}=-1.
\]
The derivatives in the tangential \((x,r)\)-directions of \(\dot c\) vanish identically at either invariant cost face, so the full three-dimensional variational system is block triangular. The normal scalar equation is exactly
\[
\dot\zeta=\sigma_{c_0}(\alpha-\beta)g(x(t),r(t))\zeta,
\]
which has the stated exponential Floquet multiplier. Substitute the time-average identities and linearity of \(g\) to obtain
\[
\langle g\rangle=g(q_*,r_*)+(\theta_3+\theta_4)(\langle r\rangle-r_*).
\]
All feedback coefficients are strictly positive, so the strict sign of the amplitude-induced exponent shift follows. The two tangential Floquet multipliers of each local center cycle are both \(1\) (they need not have a semisimple monodromy). The theorem does **not** assert that a transverse attracting orbit is asymptotically attracting within its invariant cost face.

**4. One parameter example separates the two extreme-cost faces.** Set
\[
N=3,\quad M=2,\quad b=10,\quad \mu_1=\mu_2=1,\quad
\beta=1,\quad\alpha=2,
\]
\[
(\theta_1,\theta_2,\theta_3,\theta_4)=(2,1,1,7/8).
\]
Then \(q_*=1/2\), \(Q_*=1/2\); both cost faces contain small periodic annuli with \(r_{*,\beta}=1/5\) and \(r_{*,\alpha}=2/5\). On the minimum-cost face, \(g(q_*,1/5)=0\) and
\[
\lambda_{\perp}=(15/8)(\langle r\rangle-1/5)>0.
\]
Every nonconstant local cycle therefore repels three-dimensional cost perturbations despite its center equilibrium having zero normal eigenvalue. On the maximum-cost face, \(g(q_*,2/5)=3/8\) and
\[
\lambda_{\perp}=-\left[3/8+(15/8)(\langle r\rangle-2/5)\right]<0.
\]
Every local cycle there attracts **transverse** cost perturbations. These opposite conclusions hold with exactly the same globally defined parameters. In each case the in-face family remains neutrally foliated by conserved levels.

## Verification

The standalone script `verify.py` checks the symbolic zero of \(H_x\dot x+H_r\dot r\) for four distinct group sizes/thresholds and validates the Jacobian frequency and Hessian signs. High-precision numerical integration on both cost faces of the concrete example checks conservation of \(H\), return to a Poincaré section, the two exact orbit-average identities, and the predicted sign of the normal Floquet exponent. The script prints its own quantitative results. These finite checks are consistency tests; the exact analytical identities and Morse-level-set argument establish the theorem for every parameter tuple within the assumptions.

## Relationship to prior work

Wang et al. (2026), *PLOS Computational Biology* 22(2):e1013512, introduced the three-variable system and classified equilibria and several attracting regimes, with strict inequalities at cost-face equilibria. Their published main text does not establish the local periodic annulus, the exact mean-risk surplus, or the three-dimensional Floquet selection of the boundary cycles.

Liu, Chen and Szolnoki (2023), *eLife* 12:e82954, previously introduced the **same two-dimensional fixed-cost cooperation–risk subsystem** (up to parameter relabeling and update-rate normalization). Their analysis includes Hopf/oscillation discussion. Therefore the planar model and the general possibility of oscillations are **not** presented as new here. The specific strict risk-surplus law and its interaction with the **additional dynamic cost coordinate introduced in 2026**, including opposite extreme-cost transverse Floquet shifts, are the subject of the present statement.

Hua, Xu, Liu and Chen (2024), *Physical Review Research* 6:023313, consider cooperation feedback with evolving dilemma strength, but not this simultaneous three-coordinate risk/cost feedback on its two invariant faces.

## Limitations

All assertions refer to the stated deterministic well-mixed model and the exact parameter resonance, with periodic trajectories **on invariant extreme-cost faces**. Normal attraction or repulsion is linearized Floquet behavior, not a theorem on global basin geometry or selection of one unique stable orbit. The relative normal shift is strict on every nonconstant periodic orbit, but the proof only guarantees the existence of a **local** annulus; it does not classify all global periodic orbits. The formula does not automatically extend to a modified risk-feedback equation with cost dependence, to stochastic finite populations, or to non-constant update rates without a new normalization. The published 2026 supplementary PDF could not be materially inspected; a historical-coverage check of that supplementary material remains a priority risk. The 2023 subsystem is acknowledged as direct prior art. No independent audit has been performed.

## References

1. L. Wang, S. Hua, Y. Liu, L. Zhang, L. Liu, and A. Szolnoki (2026), *Coevolutionary dynamics of cooperation, risk, and cost in collective risk games*, PLOS Computational Biology 22(2):e1013512, DOI: 10.1371/journal.pcbi.1013512, first public February 20, 2026. Open preprint: arXiv:2603.20706v1.
2. L. Liu, X. Chen, and A. Szolnoki (2023), *Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game*, eLife 12:e82954, DOI: 10.7554/eLife.82954, arXiv:2305.00253 (earlier two-variable subsystem).
3. S. Hua, M. Xu, L. Liu, and X. Chen (2024), *Coevolutionary dynamics of collective cooperation and dilemma strength in a collective-risk game*, Physical Review Research 6:023313, DOI: 10.1103/PhysRevResearch.6.023313.
