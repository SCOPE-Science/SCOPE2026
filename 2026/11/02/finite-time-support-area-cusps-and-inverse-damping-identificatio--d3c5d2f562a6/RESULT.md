# Finite-time support-area cusps and inverse damping identification in an inertial run-and-tumble oscillator

## Finding

**Theorem (finite-time geometric fingerprint).** An athermal harmonically trapped inertial run-and-tumble particle, started from rest at the trap center and driven by a symmetric telegraph force of any strictly positive switching rate, has a deterministic finite-horizon joint position–velocity support area \(\mathcal A(T)\). Although the joint law depends on the switching rate, the support area does not. With the definitions below, it is exactly
\[
\mathcal A(T)=\frac{4b^2}{\delta}\int_0^T\bigl(1-e^{-\delta(T-u)}\bigr)|h(u)|\,du,
\qquad
\mathcal A''(T)+\delta\mathcal A'(T)=4b^2|h(T)|.
\]
For every choice of positive physical parameters, \(\mathcal A\) is \(C^2\). It is analytic for all nonnegative times in the critically damped and overdamped regimes. In the underdamped regime, it is analytic away from exactly the positive times \(T_n=n\pi/\omega\) (\(n=1,2,\ldots\)), and it is *not* \(C^3\) at any \(T_n\). At every such time its one-sided third derivatives have the sharp jump
\[
J_n:=\mathcal A^{(3)}(T_n+)-\mathcal A^{(3)}(T_n-)=8b^2e^{-\alpha T_n}>0.
\]
Consequently the cusp spacing and consecutive cusp-height ratio uniquely determine the oscillation frequency and viscous decay, and one cusp height determines the mass-normalized force:
\[
\omega=\frac{\pi}{T_{n+1}-T_n},\qquad
\alpha=\frac{\log(J_n/J_{n+1})}{T_{n+1}-T_n},\qquad
b=\sqrt{\frac{J_n e^{\alpha T_n}}8}.
\]
This is a population-level identifiability theorem for the accessible phase-space geometry; it does not assert efficient estimation from finite noisy trajectory samples.

## Assumptions and scope

Let \(m,\gamma,\mu,a_0>0\), \(\lambda>0\), and let \(\sigma_t\in\{-1,+1\}\) be a continuous-time symmetric two-state Markov chain flipping at rate \(\lambda\), with either fixed or random initial sign. Set
\[
\dot X_t=V_t,\qquad
m\dot V_t=-\gamma V_t-\mu X_t+a_0\sigma_t,\qquad
(X_0,V_0)=(0,0),
\]
with no additional thermal Brownian forcing. Define \(\delta=\gamma/m>0\), \(\Omega^2=\mu/m>0\), \(b=a_0/m>0\), \(\alpha=\delta/2\), and let \(h\) be the unique solution of
\[
h''+\delta h'+\Omega^2h=0,\qquad h(0)=0,\quad h'(0)=1.
\]
The phase-space support \(K_T\) is the topological support of the probability law of \((X_T,V_T)\) in the ordinary \((x,v)\)-coordinate plane. Its area is two-dimensional Lebesgue measure \(\mathcal A(T)=\operatorname{Leb}_2(K_T)\). Changing the units of position or velocity changes this area, and the theorem consistently uses the stated physical coordinates. Statements about derivatives at \(T_n\) use finite one-sided derivatives. The underdamped condition is \(\delta<2\Omega\), in which case \(\omega=\sqrt{\Omega^2-\alpha^2}>0\). The critical/overdamped condition is \(\delta\ge 2\Omega\).

## Proof

**1. Support equals a bounded-input zonoid.** Write
\[
A=\begin{pmatrix}0&1\\-\Omega^2&-\delta\end{pmatrix},\qquad e_2=\begin{pmatrix}0\\1\end{pmatrix},\qquad g(s)=e^{As}e_2=(h(s),h'(s))^{\mathsf T}.
\]
The variation-of-constants formula gives \((X_T,V_T)^{\mathsf T}=b\int_0^Tg(T-s)\sigma_s\,ds\). Each finite prescribed alternating sign history, allowing arbitrary positive holding times, lies in the topological support: the corresponding finite collection of Poisson switch times has positive probability of lying in arbitrarily small prescribed neighborhoods, with no other switches. If the initial sign is fixed, a switch arbitrarily close to time zero permits approximating the opposite initial sign. Conversely every sample path is bounded by \(|\sigma_s|\le1\). For a measurable control \(u:[0,T]\to[-1,1]\), approximate it by finite step functions and on each sufficiently small step use \(+1\) for the prescribed fraction \((1+u)/2\) and \(-1\) for the rest. Uniform continuity of \(g\) makes the resulting endpoint integrals converge. Thus
\[
K_T=\left\{b\int_0^Tg(s)u(s)\,ds:\ u\text{ measurable, } |u(s)|\le1\text{ a.e.}\right\}.
\]
The set is compact and convex (for example by weak-star compactness of the unit ball of \(L^\infty\) and continuity of the two coordinate linear functionals); equality therefore includes its boundary. This establishes, in particular, independence from every positive value of \(\lambda\).

**2. Exact area.** For a finite collection \(w_1,\ldots,w_N\in\mathbb R^2\), the centrally symmetric zonotope \(\sum_j[-w_j,w_j]\) has area \(4\sum_{i<j}|\det(w_i,w_j)|\), obtained by tiling the Minkowski sum into parallelograms or, equivalently, by a support-function polygon computation. Approximate the integral zonoid by the Riemann zonotopes with generators \(w_j=b\Delta t\,g(t_j)\). Hausdorff convergence of compact convex sets and continuity of planar convex-body area, together with continuity of the determinant kernel, give
\[
\mathcal A(T)=4b^2\int_{0\le s<t\le T}|\det(g(s),g(t))|\,ds\,dt.
\]
Because \(\operatorname{tr}A=-\delta\), \(\det(e^{As})=e^{-\delta s}\), and \(g(t)=e^{As}g(t-s)\) when \(t>s\), one has
\[
\det(g(s),g(t))=e^{-\delta s}\det(e_2,g(t-s))=-e^{-\delta s}h(t-s).
\]
Setting \(u=t-s\), integrating in \(s\), and using \(\delta>0\) yield the asserted one-dimensional integral. Differentiate by Leibniz's rule: the boundary term vanishes in the first derivative because \(1-e^{-\delta(T-T)}=0\); hence
\[
\mathcal A'(T)=4b^2\int_0^T e^{-\delta(T-u)}|h(u)|\,du>0\quad(T>0).
\]
A further derivative gives the stated inhomogeneous equation, proving \(C^2\) regularity. As a normalization check, \(h(t)=t+O(t^2)\) implies \(\mathcal A(T)=\frac23b^2T^3+O(T^4)\) as \(T\downarrow0\).

**3. Exact nonsmoothness classification.** If \(\delta>2\Omega\), write \(\kappa=\sqrt{\alpha^2-\Omega^2}>0\): then \(h(t)=e^{-\alpha t}\sinh(\kappa t)/\kappa>0\) for every \(t>0\). At critical damping \(h(t)=te^{-\alpha t}>0\). Thus in both regimes \(|h|=h\) for \(t\ge0\), and the area convolution is analytic. If \(\delta<2\Omega\), then \(h(t)=e^{-\alpha t}\sin(\omega t)/\omega\), whose positive simple zeros are exactly \(T_n=n\pi/\omega\). On every interval avoiding these zeros, \(|h|\) is an analytic signed multiple of \(h\), so the convolution is analytic. At any such zero, \(|h(T)|=e^{-\alpha T_n}|T-T_n|+O((T-T_n)^2)\) on both sides in the corresponding one-sided sense. Therefore
\[
\bigl(|h|\bigr)'(T_n+)-\bigl(|h|\bigr)'(T_n-)=2e^{-\alpha T_n}.
\]
Differentiating \(\mathcal A''+\delta\mathcal A'=4b^2|h|\) on each side shows that the smooth \(\delta\mathcal A''\) contribution has zero jump, yielding \(J_n=8b^2e^{-\alpha T_n}\). Because it is strictly positive, \(\mathcal A\notin C^3\) at each \(T_n\), and there are no other positive-time failures of analyticity.

**4. Identifiability and boundary behavior.** The spacings determine \(\omega\). The jump ratio \(J_{n+1}/J_n=e^{-\alpha\pi/\omega}\) determines \(\alpha>0\) uniquely, and the amplitude determines \(b>0\) uniquely. Thus \(\gamma/m=2\alpha\), \(\mu/m=\alpha^2+\omega^2\), and \(a_0/m=b\) are identifiable. If the physical force amplitude \(a_0\) is independently known, then \(m=a_0/b\), \(\gamma=2\alpha m\), and \(\mu=(\alpha^2+\omega^2)m\). The switching rate \(\lambda\) is *not* identifiable from support area since step 1 is independent of it. For completeness the monotone area tends to
\[
\mathcal A(\infty)=\frac{4a_0^2}{\gamma\mu}\times
\begin{cases}
1,&\delta\ge2\Omega,\\
\coth\!\bigl(\pi\alpha/(2\omega)\bigr),&\delta<2\Omega.
\end{cases}
\]
Indeed \(\mathcal A(\infty)=4b^2\delta^{-1}\int_0^\infty |h(u)|du\), the nonoscillatory integral equals \(1/\Omega^2\), and the oscillatory integral sums over half-periods to \(\Omega^{-2}\coth(\pi\alpha/(2\omega))\). This last limiting-area identity is context, not a novelty claim about generic reachable sets.

## Verification

`CHECKER.py` is a standalone Python 3 (standard-library-only) numerical checker distributed alongside this document. Execute `python CHECKER.py`. It independently computes the area by (i) the one-dimensional kernel formula and (ii) a discrete two-dimensional Minkowski-sum zonotope area formula using pairwise determinants. It compares the limiting-area expression, underdamped one-sided cusp jumps, and the small-time cubic law across underdamped, critical, and overdamped parameter choices. It passed **39** finite assertions on the supplied package. These checks are diagnostics; the support equality, area formula, global cusp locations, and inverse theorem are established by the proof above, not by finite sampling. All numerical quadratures use specified finite mesh sizes in the checker.

## Relationship to prior work

Dutta, Kundu, Sabhapandit and Basu (2024) introduce the identical athermal inertial run-and-tumble trap and derive stationary joint-support boundaries, marginal distributions, and parameter-dependent fluctuation regimes (Sections II–V and Appendix C). The general bounded-input reachability correspondence, support geometry, and existence of exact reach-set volume algorithms were already established in control literature, notably Haddad, Khodary and Halder (2023), Theorem 5, and Zhao (2020) for discrete-time zonotopes and real-eigenvalue cases. Neither their general volume machinery nor the motivating particle paper is claimed new here. The specific assessed contribution is the finite-*horizon* third-derivative cusp spectrum and sharp jump-to-mechanical-parameter reconstruction for this stochastic oscillator. The general formula for arbitrary LTI reach-set volume is a substantial antecedent; independently determining the novelty of all implied special-case consequences remains a residual publication-priority issue.

## Limitations

The support is topological and includes extremal points reached only as limits of exceptionally unlikely switching histories; no finite-data statistical estimator or robust noise guarantee is asserted. Additional unbounded Gaussian thermal forcing changes the support to the full plane, invalidating finite-area tomography. The inverse theorem works in the underdamped regime with at least two cusp heights available; the absence of cusps in other regimes does not by itself give full parameter identifiability. Without a separately known force scale only the normalized mechanical parameters can be determined. The switching rate cannot be inferred from support geometry. Claims concern fixed-time supports from the specified initial state, not entropy, occupation measures, finite-sample efficiency, or already-established generic reachable-set volume theory. Independent audit and publication-priority verification have not been performed.

## References

1. Dutta, D., Kundu, A., Sabhapandit, S., Basu, U., *Hamonically trapped inertial run-and-tumble particle in one-dimension*, arXiv:2406.06120v1 (2024-06-10), https://arxiv.org/html/2406.06120v1.
2. Haddad, S., Khodary, P., Halder, A., *Exact Computation of LTI Reach Set from Integrator Reach Set with Bounded Input*, arXiv:2309.08222 (2023), https://arxiv.org/pdf/2309.08222.
3. Zhao, M., *Exact Volume of Zonotopes Generated by a Matrix Pair*, arXiv:2004.05530v1 (2020), https://arxiv.org/pdf/2004.05530.
