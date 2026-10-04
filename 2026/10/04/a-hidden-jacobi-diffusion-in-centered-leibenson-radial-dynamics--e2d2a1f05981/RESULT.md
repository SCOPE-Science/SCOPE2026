# A hidden Jacobi diffusion in centered Leibenson radial dynamics
## Finding
Under the standing assumptions of Braun's centered Leibenson radial process,
\[
d\in\mathbb N,\qquad p\in(1,\infty),\qquad m>0,\qquad m(p-1)>1,\qquad dp>d+1,
\]
let \(X\) be any probabilistically weak solution of the centered McKean--Vlasov SDE started at \(o\). Set
\[
q=\frac{p}{p-1},\qquad M=m(p-1)-1,\qquad
\beta=p+dM,\qquad \gamma=\frac{p-1}{M},
\]
and
\[
\kappa=\frac{M}{mp}\beta^{-1/(p-1)}.
\]
If \(C\) is the Barenblatt normalization constant, then the support radius is
\[
R(t)=\left(\frac{C}{\kappa}\right)^{1/q}t^{1/\beta}.
\]
Define the normalized radial power
\[
Q_t=\left(\frac{|X_t-o|}{R(t)}\right)^q
=\frac{\kappa}{C}\,t^{-q/\beta}|X_t-o|^q,\qquad t>0.
\]

Put \(J_s=Q_{e^s}\). Then \(J\) is exactly the stationary Jacobi diffusion on \([0,1]\)
\[
dJ_s=K\{\alpha-(\alpha+\eta)J_s\}\,ds
+\sqrt{2KJ_s(1-J_s)}\,dB_s,
\]
with
\[
K=\frac{pM}{(p-1)^2\beta},\qquad
\alpha=\frac{d}{q}=\frac{d(p-1)}p,\qquad
\eta=\gamma+1.
\]
Its stationary law is
\[
J_s\sim\operatorname{Beta}(\alpha,\eta)
\]
for every \(s\in\mathbb R\). Consequently, if
\[
\Lambda=K(\alpha+\eta),
\]
then for every \(0<s\le t\),
\[
\operatorname{Corr}(Q_s,Q_t)=\left(\frac{s}{t}\right)^\Lambda.
\]
Equivalently,
\[
\mathbb E[Q_t]=\frac{\alpha}{\alpha+\eta},
\qquad
\operatorname{Var}(Q_t)=
\frac{\alpha\eta}{(\alpha+\eta)^2(\alpha+\eta+1)},
\]
and
\[
\operatorname{Cov}(Q_s,Q_t)=
\frac{\alpha\eta}{(\alpha+\eta)^2(\alpha+\eta+1)}
\left(\frac{s}{t}\right)^\Lambda .
\]

Thus the source's time-independent one-time law for the self-similarly rescaled radius is the marginal shadow of a classical reversible diffusion in logarithmic time. This also yields an exact two-time law for the first Jacobi mode, rather than only a one-time scaling statement or a stopped moment estimate.

## Assumptions and scope
The result is for the centered process, meaning the starting point and radial center coincide. It uses precisely the slow-diffusion and integrability assumptions \(m(p-1)>1\) and \(dp>d+1\) under which Braun works with probabilistically weak solutions. No pathwise uniqueness or nonlinear Markov property of the ambient \(d\)-dimensional process is assumed.

The theorem concerns the scalar observable \(Q_t\), not the full vector process. It does not treat uncentered radial processes, the fast-diffusion regime, or the Euclidean Brownian boundary case excluded by the source assumptions. The statement that \(J\) is an ordinary Jacobi diffusion refers to its scalar path law after logarithmic time.

## Proof
Braun writes the centered radial process \(r_t=|X_t-o|\) as
\[
dr_t=\sqrt{2a(t,r_t)}\,dB_t+
\left\{a(t,r_t)\frac{d-1}{r_t}+a_r(t,r_t)\right\}dt,
\]
with no centered local-time term. His exact Barenblatt coefficient computation gives, for \(0<r<R(t)\),
\[
a(t,r)=m^{p-1}(\gamma\kappa q)^{p-2}
t^{-1+q/\beta}r^{2-q}
\left\{C-\kappa(t^{-1/\beta}r)^q\right\}.
\]
Since
\[
\gamma\kappa q=\frac1m\,\beta^{-1/(p-1)},
\]
the constant
\[
A:=m^{p-1}(\gamma\kappa q)^{p-2}
\]
simplifies to
\[
A=m\,\beta^{-(p-2)/(p-1)}.
\]
For \(y=t^{-1/\beta}r\), therefore,
\[
a(t,t^{1/\beta}y)=t^{-1+2/\beta}\bar a(y),
\qquad
\bar a(y)=A y^{2-q}(C-\kappa y^q).
\]

Now put \(t=e^s\) and \(Y_s=e^{-s/\beta}r_{e^s}\). The deterministic time change and Itô's formula yield
\[
dY_s=\sqrt{2\bar a(Y_s)}\,d\widetilde B_s+
\left\{\bar a(Y_s)\frac{d-1}{Y_s}
+\bar a'(Y_s)-\frac{Y_s}{\beta}\right\}ds.
\]
This identity is valid on every bounded logarithmic-time interval. At \(Y_s=0\), when \(1<q<2\), one may obtain the next calculation by applying Itô's formula to a smooth approximation of \(y\mapsto y^q\) and letting the approximation parameter vanish. The apparent second-derivative singularity is harmless because
\[
\bar a(y)y^{q-2}=A(C-\kappa y^q)
\]
remains bounded at zero.

Let
\[
J_s=\frac{\kappa}{C}Y_s^q.
\]
Writing \(u=(\kappa/C)y^q\), direct differentiation gives
\[
\bar a(y)\left(\frac{du}{dy}\right)^2
=A\kappa q^2\,u(1-u).
\]
Define
\[
K=A\kappa q^2.
\]
Using the displayed values of \(A\), \(\kappa\), and \(q\),
\[
K=\frac{pM}{(p-1)^2\beta}.
\]
For the drift, the same substitution gives
\[
\frac{du}{dy}
\left\{\bar a'(y)+\bar a(y)\frac{d-1}{y}-\frac y\beta\right\}
+\bar a(y)\frac{d^2u}{dy^2}
=
A\kappa q\{d-(d+q)u\}-\frac{q}{\beta}u.
\]
Because
\[
\frac{q}{\beta K}=\gamma,
\]
this becomes
\[
K\left\{\frac d q-\left(\frac d q+1+\gamma\right)u\right\}
=
K\{\alpha-(\alpha+\eta)u\}.
\]
The quadratic variation term is \(2Ku(1-u)\,ds\), which proves the Jacobi SDE.

Braun proves that \(Y_s\) has, for every \(s\), density proportional on \([0,\rho]\) to
\[
(C-\kappa y^q)^\gamma y^{d-1},
\qquad
\rho=(C/\kappa)^{1/q}.
\]
Under \(u=(\kappa/C)y^q\), this density becomes
\[
u^{d/q-1}(1-u)^\gamma\,du,
\]
hence exactly \(\operatorname{Beta}(\alpha,\eta)\).

The Jacobi generator is
\[
\mathcal L f(u)
=
K\left[u(1-u)f''(u)+\{\alpha-(\alpha+\eta)u\}f'(u)\right].
\]
If \(\pi(u)\) denotes the \(\operatorname{Beta}(\alpha,\eta)\) density, then
\[
\mathcal L f
=
K\pi^{-1}\frac{d}{du}
\left\{u(1-u)\pi f'\right\},
\]
so the Beta law is invariant and the diffusion is reversible. The drift is Lipschitz on \([0,1]\), while
\[
\left|\sqrt{u(1-u)}-\sqrt{v(1-v)}\right|^2\le |u-v|,
\]
so the standard one-dimensional pathwise-uniqueness criterion applies. Thus the transformed scalar process has the unique ordinary stationary Jacobi law.

Finally, with
\[
\mu=\frac{\alpha}{\alpha+\eta},
\qquad
\Lambda=K(\alpha+\eta),
\]
the Jacobi SDE gives
\[
d(J_s-\mu)=-\Lambda(J_s-\mu)\,ds
+\sqrt{2KJ_s(1-J_s)}\,dB_s.
\]
The stochastic integral is square-integrable because \(0\le J_s\le1\). Hence, for \(v\ge u\),
\[
\mathbb E[J_v-\mu\mid\mathcal F_u]
=e^{-\Lambda(v-u)}(J_u-\mu).
\]
Using the common Beta variance yields
\[
\operatorname{Corr}(J_u,J_v)=e^{-\Lambda(v-u)}.
\]
Substituting \(u=\log s\) and \(v=\log t\) gives
\[
\operatorname{Corr}(Q_s,Q_t)=\left(\frac{s}{t}\right)^\Lambda.
\]

## Verification
Every constant reduction was checked algebraically from the source definitions:
\[
\gamma\kappa q=m^{-1}\beta^{-1/(p-1)},
\qquad
A=m\beta^{-(p-2)/(p-1)},
\qquad
K=A\kappa q^2=\frac{pM}{(p-1)^2\beta},
\qquad
\frac{q}{\beta K}=\gamma.
\]
The transformed diffusion coefficient and drift were independently expanded before packaging. The endpoint \(Y=0\) was checked separately: the only potentially singular Itô factor is canceled by the exact \(y^{2-q}\) degeneracy of \(\bar a\). The Beta law follows by an explicit change of variables, not by numerical fitting. The correlation identity follows from an integrating-factor martingale argument and therefore does not require estimating transition densities.

## Relationship to prior work
Braun's 2026 paper supplies the exact centered radial semimartingale, the exact Barenblatt coefficient, and Proposition 3.20 showing that \(t^{-1/\beta}|X_t-o|\) has a time-independent one-time law. The paper then develops stopped moment and moving-boundary estimates for that rescaled radius. It does not identify the logarithmic-time radial-power path as a Jacobi diffusion or give the resulting exact temporal correlation.

Barbu, Grube, Rehmeier, and Röckner construct the Leibenson process and its McKean--Vlasov representation, while Barbu, Rehmeier, and Röckner construct the \(p\)-Brownian special case. Their inspected formulations establish the nonlinear probabilistic counterpart and Barenblatt marginals, not the scalar Jacobi reduction.

Braun also notes that earlier random-flight representations can reproduce the same self-similar Barenblatt radial marginal but are unrelated to the McKean--Vlasov path dynamics. That distinction is essential here: the Jacobi identification is a statement about the actual centered radial path, and the power-law correlation uses its two-time structure.

## Limitations
The result does not identify the full vector process after self-similar rescaling and does not claim a Jacobi reduction away from the center. It is confined to Braun's slow-diffusion parameter range. The exact correlation concerns the normalized radial \(q\)-power, not the raw radius. The literature search found no implication-equivalent published pathwise reduction, but a classical diffusion transformation under different terminology remains a residual originality risk.

## References
1. Mathias Braun, *The radial part of \(p\)-Brownian motion*, arXiv:2609.11558v1, first public September 10, 2026.
2. Viorel Barbu, Sebastian Grube, Marco Rehmeier, and Michael Röckner, *The Leibenson process*, arXiv:2508.12979v1, first public August 18, 2025.
3. Viorel Barbu, Marco Rehmeier, and Michael Röckner, *\(p\)-Brownian motion and the \(p\)-Laplacian*, arXiv:2409.18744v1; Annals of Probability 54 (2026), 1877--1907.
