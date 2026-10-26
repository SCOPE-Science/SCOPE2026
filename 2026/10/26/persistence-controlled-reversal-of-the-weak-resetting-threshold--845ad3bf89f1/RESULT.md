# Persistence-controlled reversal of the weak-resetting threshold under fixed-velocity active propulsion

## Finding

For the reflected and absorbed active Ornstein–Uhlenbeck search model defined below, complete Poisson resetting of both position and active velocity to the same deterministic starting state has a **locally unique onset-of-beneficial-resetting boundary**. When the active propulsion amplitude \(\varepsilon\) is small, its location is
\[
x_*(\varepsilon,\eta,\gamma)=1-\frac1{\sqrt5}+\varepsilon\eta\,\mathcal S(\gamma)+O_\gamma(\varepsilon^2),
\]
where \(\eta\) is the deterministic reset velocity, \(\gamma>0\) is the active-velocity relaxation rate, and \(\mathcal S\) is given explicitly by a positive one-dimensional Green kernel below. The sign of \(\mathcal S\) **reverses with persistence**:
\[
\lim_{\gamma\downarrow0}\mathcal S(\gamma)=\frac4{125}>0,
\qquad
\mathcal S(\gamma)=-\frac1\gamma+O(\gamma^{-2})\quad(\gamma\to\infty).
\]
Thus, for initially outward propulsion \(\eta>0\), sufficiently persistent forcing expands the starting-position region where weak resetting helps, while sufficiently rapidly relaxing forcing contracts it. Both directions reverse for \(\eta<0\). At least one intervening relaxation rate makes the first-order shift zero; **uniqueness of such a rate is not claimed**. Numerical evaluation gives a zero near \(\gamma=0.2112213694\).

The criterion is the **sign of the derivative at resetting rate zero**, not global monotonicity in resetting rate. The first-order shift is an exact mathematical result; no finite-amplitude phase boundary is asserted.

## Assumptions and scope

On the spatial interval \([0,1]\), let \(X_t\) have generator \(\partial_{xx}\) in the passive limit, reflection at \(1\), and absorption at \(0\). Until absorption, let
\[
\mathrm dX_t=\varepsilon V_t\,\mathrm dt+\sqrt2\,\mathrm dW_t-\mathrm dL_t^{(1)},
\qquad
\mathrm dV_t=-\gamma V_t\,\mathrm dt+\sqrt{2\gamma}\,\mathrm dB_t,
\]
where \(W,B\) are independent Brownian motions, \(L^{(1)}\) is the usual upper reflecting local time, \(\gamma>0\), \(X_0=x\in(0,1)\), and \(V_0=\eta\in\mathbb R\) is deterministic. A Poisson clock of rate \(r\ge0\), independent of the diffusions, **completely restarts both coordinates** at \((x,\eta)\). Its time to absorption is \(T_{r,\varepsilon}\); \(\tau_\varepsilon=T_{0,\varepsilon}\) denotes one unreset excursion.

For each fixed \(\gamma>0\), bounded \(\eta\), and \(x\) in a compact subinterval of \((0,1)\), the small-\(\varepsilon\) assertions are local with an \(O(\varepsilon^2)\) remainder. Either signed \(\varepsilon\) or positive amplitude combined with signed \(\eta\) may be used. The persistent limit \(\gamma\downarrow0\) and fast-relaxation limit \(\gamma\to\infty\) concern the *first-order coefficient* after \(\varepsilon\to0\), not a uniform simultaneous limit.

For \(\gamma>0\), set
\[
G_\gamma(x,y)=\frac{\sinh(\sqrt\gamma\min\{x,y\})\cosh(\sqrt\gamma[1-\max\{x,y\}])}{\sqrt\gamma\cosh(\sqrt\gamma)},
\qquad Q(y)=\frac23-y^2+\frac{y^3}3.
\]
This is the Green kernel of \(\gamma-\partial_{xx}\) with Dirichlet condition at \(0\) and Neumann condition at \(1\). Define
\[
A_\gamma(x)=\int_0^1G_\gamma(x,y)(1-y)\,\mathrm dy,
\qquad B_\gamma(x)=\int_0^1G_\gamma(x,y)[Q(y)+2A_\gamma(y)]\,\mathrm dy.
\]
With \(c=1-1/\sqrt5\) and \(\mu(x)=x-x^2/2\), the coefficient is
\[
\boxed{\mathcal S(\gamma)=-3\sqrt5\left[2\mu(c)A_\gamma(c)-\frac12 B_\gamma(c)\right].}
\]
In particular,
\[
A_\gamma(x)=\frac{1}{\gamma}\left[1-x-\frac{\cosh(\sqrt\gamma(1-x))}{\cosh\sqrt\gamma}+\frac{\sinh(\sqrt\gamma x)}{\sqrt\gamma\cosh\sqrt\gamma}\right].
\]
All integrals above are convergent ordinary one-dimensional integrals and specify the coefficient without an implicit stochastic solver.

## Proof

**Step 1: Resetting reduces the initial-rate question to two unreset moments.** Write \(\Phi_\varepsilon(r)=\mathbb E[e^{-r\tau_\varepsilon}]\). Because every Poisson reset returns both coordinates to the same deterministic state, successive excursions are independent. Conditioning on the first excursion and the reset clock yields the exact classical renewal identity
\[
\mathbb E T_{r,\varepsilon}=\frac{1-\Phi_\varepsilon(r)}{r\Phi_\varepsilon(r)}\quad(r>0).
\]
Taylor expansion at \(r=0\), with \(m_1=\mathbb E\tau_\varepsilon\) and \(m_2=\mathbb E\tau_\varepsilon^2\), gives
\[
\left.\frac{\partial}{\partial r}\mathbb E T_{r,\varepsilon}\right|_{r=0+}=m_1^2-\frac12m_2=:H_\varepsilon(x,\eta,\gamma).
\]
A negative value means sufficiently weak resetting lowers the mean first-passage time.

**Step 2: Justification of moment differentiation.** At \(\varepsilon=0\), killed reflected Brownian motion in a bounded interval has exponentially decaying survival and is independent of the Ornstein–Uhlenbeck process. For finite horizons the reflected-path Girsanov density for adding \(\varepsilon V\) is
\[
\exp\left[\frac{\varepsilon}{\sqrt2}\int_0^tV_s\,\mathrm dW_s-\frac{\varepsilon^2}4\int_0^t V_s^2\,\mathrm ds\right].
\]
For sufficiently small \(|\varepsilon|\), exponential moments of the integrated square of this finite-variance Gaussian OU process grow at most exponentially in \(t\) with arbitrarily small exponent as \(\varepsilon\to0\). Hölder's inequality combined with the passive killed-Brownian spectral gap therefore gives uniform exponential survival control on compact \(x\)-sets. Differentiating the finite-horizon densities and integrating survival times justifies two \(\varepsilon\)-derivatives of the first two hitting-time moments near zero. The remainder is \(O(\varepsilon^2)\) locally. Standard stopped Dynkin formulas then identify these derivatives with the unique polynomial-growth solutions of the backward moment equations with \(u(0,v)=0\) and \(\partial_xu(1,v)=0\).

**Step 3: Two triangular boundary-value problems.** The unreset backward generator is
\[
\mathcal L_\varepsilon=\partial_{xx}-\gamma v\partial_v+\gamma\partial_{vv}+\varepsilon v\partial_x.
\]
The two moment equations are \(\mathcal L_\varepsilon m_1=-1\) and \(\mathcal L_\varepsilon m_2=-2m_1\). At \(\varepsilon=0\), both moments are independent of the initial velocity and are
\[
\mu(x)=x-\frac{x^2}2,\qquad M(x)=\frac{2x}3-\frac{x^3}3+\frac{x^4}{12}.
\]
Use expansions \(m_1(x,v)=\mu(x)+\varepsilon v A_\gamma(x)+O(\varepsilon^2)\) and \(m_2(x,v)=M(x)+\varepsilon v B_\gamma(x)+O(\varepsilon^2)\). Equating linear terms gives
\[
(\gamma-\partial_{xx})A_\gamma=1-x,
\qquad(\gamma-\partial_{xx})B_\gamma=M'(x)+2A_\gamma(x)=Q(x)+2A_\gamma(x),
\]
with Dirichlet at \(0\) and Neumann at \(1\). Green inversion gives precisely the displayed \(A_\gamma,B_\gamma\); direct differentiation verifies the hyperbolic expression for \(A_\gamma\).

**Step 4: A simple passive crossover root.** Substitution into the renewal slope gives
\[
H_\varepsilon(x,\eta,\gamma)=H_0(x)+\varepsilon\eta\left(2\mu(x)A_\gamma(x)-\tfrac12B_\gamma(x)\right)+O(\varepsilon^2),
\]
where
\[
H_0(x)=\frac{x(5x^3-20x^2+24x-8)}{24}.
\]
Its unique root in \((0,1)\) is \(c=1-1/\sqrt5\), with \(H_0'(c)=1/(3\sqrt5)>0\). The implicit-function theorem yields a unique nearby root and the claimed first-order displacement. The near-root sign agrees with resetting helpful on the \(x<c\) side and harmful on the \(x>c\) side.

**Step 5: Persistent and rapidly relaxing limits.** The Green kernel tends pointwise to \(G_0(x,y)=\min(x,y)\). Applying this kernel twice gives exact polynomial limits
\[
A_0(x)=\frac x2-\frac{x^2}2+\frac{x^3}6,
\qquad B_0(x)=\frac{2x}3-\frac{x^2}3-\frac{x^3}6+\frac{x^4}6-\frac{x^5}{30}.
\]
Substituting \(x=c\) gives \(\mathcal S(0)=4/125\) exactly. At fixed interior \(x\), Green-resolvent asymptotics (or the displayed explicit \(A_\gamma\) and the equation for \(B_\gamma\)) yield
\[
A_\gamma(x)=\frac{1-x}{\gamma}+O(\gamma^{-2}),\qquad B_\gamma(x)=\frac{Q(x)}\gamma+O(\gamma^{-2}).
\]
At \(c\), one has \(2\mu(c)(1-c)-Q(c)/2=1/(3\sqrt5)\). Hence \(\mathcal S(\gamma)=-1/\gamma+O(\gamma^{-2})\). Finally the resolvent kernels depend continuously on \(\gamma>0\), so the opposite limiting signs force at least one zero of \(\mathcal S\). No uniqueness or monotonicity property of this function is used or proved.

## Verification

Run the included standard-library script `verify.py` with `python3 verify.py`. It executes 905 deterministic checks: passive polynomial identities; the persistent-limit polynomial Green solutions; Green integration versus an independent finite-difference solve of both boundary-value problems; local differential-equation and boundary residuals; the sign-changing coefficient and a numerical root; and the high-relaxation asymptotic. The script outputs \(\mathcal S(0)=0.032\), \(\mathcal S(0.1)\approx0.015585415510\), \(\mathcal S(1)\approx-0.061343172483\), and a numerical root near \(0.211221369410\). These finite checks corroborate, but do not replace, the analytic argument. A separate continuous-drift boundary-value computation checks the \(\gamma\downarrow0\) shift coefficient against finite-amplitude first-passage moments; it is not required by the standalone script or the proof.

## Relationship to prior work

Georgiou, Bressloff and Bertrand (arXiv:2609.21124v1, September 17, 2026) formulate precisely the absorbing–reflecting active Ornstein–Uhlenbeck reset problem and derive weak-activity first-passage statistics for **Gaussian-distributed initial/reset active velocity**. Their Section 3.4 studies **fixed initial/reset velocity** through simulations; Fig. 9 reports approximate linear dependence on square-root activity and does not give a boundary-value-derived coefficient or prove a change in the sign of that coefficient with persistence. The passive threshold \(1-1/\sqrt5\), their resetting criterion, and the observed fixed-velocity sensitivity are prior results, not claimed here.

Pal and Reuveni's generic first-passage-under-restart renewal formula (arXiv:1607.06048) covers the reduction in Step 1, but does not evaluate active OU fixed-velocity first-passage moment derivatives or their persistence-dependent sign. Baouche and Kurzthaler (DOI:10.1039/D5SM00340G) derive direction-sensitive first-passage resetting for active Brownian particles near a wall in a distinct two-dimensional, unbounded geometry; their result neither supplies the absorbing–reflecting AOUP Green kernel nor its sign crossover. Shankari and Sahoo (arXiv:2509.18515) study unconstrained active OU motion and resetting chiefly via mean-square displacement and stationary distributions, not this finite-interval absorption criterion.

The contribution assessed here is the **exact, model-calibrated first-order threshold displacement for deterministic velocity resetting and its provable sign reversal**. General renewal identities and generic weak-force perturbation methods are not asserted to be novel.

## Limitations

This result addresses only the zero-reset-rate derivative and the locally unique threshold near the passive root for sufficiently small active amplitude. The sign-change rate \(\gamma\approx0.2112213694\) is numerical, and no uniqueness of roots in \(\gamma\) is established. The \(\gamma\downarrow0\) and \(\gamma\to\infty\) limits are sequential in the first-order response; no uniform two-parameter limit is claimed. Independent numerical validation is not an independent mathematical audit. The model assumes completely renewed deterministic active velocity at resetting, additive independent Gaussian noises, reflection at one wall, and perfect absorption at the other. Claims about a partially renewed velocity, nonlinear confinement, general activity strengths, or global resetting-rate optimality are outside scope.

## References

1. D. K. Georgiou, P. C. Bressloff, T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein–Uhlenbeck particle*, arXiv:2609.21124v1 (public September 17, 2026). https://arxiv.org/abs/2609.21124
2. A. Pal, S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 and *Physical Review Letters* **118**, 030603 (2017). https://arxiv.org/abs/1607.06048
3. Y. Baouche, C. Kurzthaler, *Optimal first-passage times of active Brownian particles under stochastic resetting*, *Soft Matter* **21**, 5998–6011 (2025), DOI:10.1039/D5SM00340G. https://doi.org/10.1039/D5SM00340G
4. U. Shankari, M. Sahoo, *Active Ornstein-Uhlenbeck particle under stochastic resetting*, arXiv:2509.18515 (2025). https://arxiv.org/abs/2509.18515
5. Mathematical Reviews / AMS MSC2020 classification, 82C31: stochastic methods applied to time-dependent statistical mechanics. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C31
