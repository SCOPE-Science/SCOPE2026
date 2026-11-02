# Unique optimal absorption strength for a full-line quantum trap

## Finding

A single lossy site on an infinite coherent tight-binding chain has a **unique optimal absorption strength for particles released arbitrarily far from that site**. Unlike the known boundary-sink geometry, the optimal ratio is not unity.

Let \(J,\eta>0\). For the system in the next section define \(Q_m\) to be the eventual absorption probability of a particle initially localized at lattice distance \(m\in\mathbb N_0\) from the trap. For every \(m\ge0\),
\[
Q_m=Q_\infty+\frac{4\eta J}{\pi}\int_0^\infty\frac{e^{-2mu}\sinh u}{\eta^2+4J^2\sinh^2u}\,du,
\qquad Q_\infty=\frac{\eta}{\pi}\int_{-2J}^{2J}\frac{d\omega}{\bigl(\eta+\sqrt{4J^2-\omega^2}\bigr)^2}.
\]
In particular, \(Q_0>Q_1>\cdots>Q_\infty>0\), and for fixed \(J,\eta>0\),
\[
Q_m=Q_\infty+\frac{J}{\pi\eta m^2}
+\left(\frac{J}{4\pi\eta}-\frac{6J^3}{\pi\eta^3}\right)\frac1{m^4}
+O_{J,\eta}(m^{-6})\qquad(m\to\infty).
\]
Put \(a=\eta/(2J)\). Then the limiting absorption probability has the closed form
\[
Q_\infty(a)=\begin{cases}
\displaystyle\frac{2a}{\pi}\frac{\operatorname{artanh}\sqrt{1-a^2}-\sqrt{1-a^2}}{(1-a^2)^{3/2}},&0<a<1,\\[4pt]
\displaystyle\frac{2}{3\pi},&a=1,\\[4pt]
\displaystyle\frac{2a}{\pi}\frac{\sqrt{a^2-1}-\arccos(1/a)}{(a^2-1)^{3/2}},&a>1.
\end{cases}
\]
It increases strictly to one global maximum and decreases strictly thereafter. Let \(k_*\in(0,1)\) be the unique nonzero root of
\[
(3-2k^2)(\operatorname{artanh}k-k)=k^3.
\]
The maximizing ratio is
\[
\boxed{\frac{\eta_*}{J}=2\sqrt{1-k_*^2}=1.2257411236662032845\ldots},
\qquad \boxed{Q_\infty(\eta_*)=0.2227963205634460589\ldots}.
\]
Thus the maximal eventual absorption of a particle sourced far away is approximately \(22.28\%\), and the sharp optimal loss-to-hopping ratio differs from the unity optimum of the related *half-line boundary-sink model*.

## Assumptions and scope

The Hilbert space is \(\ell^2(\mathbb Z)\). Let \(S\) denote translation by one lattice site and \(P_0=|0\rangle\langle0|\). The effective non-self-adjoint Hamiltonian is
\[
H=J(S+S^*)-i\eta P_0,\qquad J>0,\ \eta>0.
\]
An initially localized particle at \(m\in\mathbb Z\) evolves as \(\psi_m(t)=e^{-itH}|m\rangle\). The loss probability up to time \(t\ge0\) is \(1-\|\psi_m(t)\|^2\). The eventual loss \(Q_{|m|}\) exists because this norm decreases. The formal absorber's Lindblad jump rate is \(2\eta\); both lattice sides are present, so the absorber is **interior**, not a half-line boundary. There are no other potentials, defects, measurements, or stochastic dephasing. All limits in distance are at fixed positive \(J\) and \(\eta\).

## Proof

**1. Loss identity and resolvent.** Differentiating the squared norm gives
\[
\frac d{dt}\|\psi_m(t)\|^2=-2\eta|\langle0|\psi_m(t)\rangle|^2,
\qquad Q_m=2\eta\int_0^\infty|\langle0|\psi_m(t)\rangle|^2dt.
\]
The right-hand side is at most one, so the trap amplitude is square integrable. Set \(A_m(t)=\langle0|\psi_m(t)\rangle\). For \(\Re s>0\), its Laplace transform can be calculated from the free lattice Green function and the rank-one resolvent identity:
\[
\widehat A_m(s)=\frac{\rho(s)^m}{\eta+\sqrt{s^2+4J^2}},\quad
\rho(s)=\frac{\sqrt{s^2+4J^2}-s}{2iJ},\quad m\ge0.
\]
Here the square root is holomorphic in the right half-plane and positive for positive real \(s\). To see this directly, the free diagonal resolvent is \((s^2+4J^2)^{-1/2}\); its \((0,m)\) matrix entry is \(\rho(s)^m/\sqrt{s^2+4J^2}\), obtained from the second-order difference equation with decay at spatial infinity. Rank-one resummation multiplies it by \((1+\eta/\sqrt{s^2+4J^2})^{-1}\).

**2. Splitting the spectral band.** Since \(A_m\in L^2(0,\infty)\), Plancherel for its Laplace boundary values yields
\[
Q_m=\frac{\eta}{\pi}\int_{-\infty}^{\infty}
\left|\widehat A_m(0^++i\omega)\right|^2d\omega.
\]
For \(|\omega|<2J\), the root is \(\sqrt{4J^2-\omega^2}\) and \(|\rho|=1\), producing \(Q_\infty\). For \(|\omega|>2J\), write \(|\omega|=2J\cosh u\), \(u>0\); then \(|\rho|=e^{-u}\) and \(|\eta+\sqrt{(0^++i\omega)^2+4J^2}|^2=\eta^2+4J^2\sinh^2u\). The change of variables \(d|\omega|=2J\sinh u\,du\) gives precisely the positive exterior-band correction in the finding.

**3. Strict spatial ordering and its rate.** The exterior-band integrand is strictly positive for every \(u>0\). Therefore its exponential factor decreases strictly with integer \(m\), and dominated convergence gives convergence to zero. Near \(u=0\), its smooth factor has the expansion
\[
\frac{\sinh u}{\eta^2+4J^2\sinh^2u}
=\frac u{\eta^2}+\left(\frac1{6\eta^2}-\frac{4J^2}{\eta^4}\right)u^3+O_{J,\eta}(u^5).
\]
Watson's Laplace-endpoint lemma, or splitting the integral at fixed small positive \(u\) and integrating the Taylor remainder, gives the two displayed asymptotic terms and the \(O_{J,\eta}(m^{-6})\) remainder. The tail away from \(u=0\) is exponentially small for \(m\ge1\).

**4. Closed form and unique optimizer.** With \(\omega=2J\sin\theta\), the band term becomes
\[
Q_\infty(a)=\frac{2a}{\pi}\int_0^{\pi/2}\frac{\cos\theta}{(a+\cos\theta)^2}\,d\theta.
\]
The substitution \(t=\tan(\theta/2)\) evaluates this elementary integral to the three-case formula above. The function tends to zero as \(a\downarrow0\) and \(a\to\infty\). For \(a\ge1\), differentiating under the integral shows
\[
Q_\infty'(a)=\frac2\pi\int_0^{\pi/2}
\frac{\cos\theta(\cos\theta-a)}{(a+\cos\theta)^3}\,d\theta<0.
\]
For \(0<a<1\) put \(k=\sqrt{1-a^2}\). Direct differentiation of the closed form shows \(\operatorname{sgn}Q_\infty'(a)=\operatorname{sgn}H(k)\), where
\[
H(k)=(3-2k^2)(\operatorname{artanh}k-k)-k^3
=k^5\left[-\frac1{15}+\sum_{j=3}^\infty
\frac{2j-5}{(2j-1)(2j+1)}k^{2j-4}\right].
\]
The bracket is strictly increasing from \(-1/15\) at \(k=0\) to \(+\infty\) as \(k\uparrow1\): all series coefficients are positive and the divergence follows from \(\operatorname{artanh}k\to\infty\). Thus it has exactly one zero \(k_*\in(0,1)\). As \(a\) increases, \(k\) decreases, so \(Q_\infty\) increases up to \(a_*\) and decreases thereafter. The displayed sharp optimizer follows.

## Verification

The standalone `verify.py` uses independent numerical spectral and direct time-domain calculations. It checks the closed form against quadrature for four positive parameter pairs; exact exterior-band integrals and strict spatial ordering; the two-term large-distance expansion; a high-precision root of the critical equation; and the non-Hermitian finite-lattice evolution for four initial distances, before reflection from finite-volume boundaries becomes relevant. It also separately integrates the interior/exterior spectral frequency ranges. Run `python verify.py` with `mpmath`, `numpy`, and `scipy` installed. Numerical checks support the calculations; the infinite claims follow from the analytic proof, not from sampling.

## Relationship to prior work

Longhi, *Photonic random walks with traps* (2024), proves survival can remain positive for coherent walks with finitely many traps, including the whole-line continuous-time Hamiltonian above. It does **not** state a global optimum for the remote-source single-trap absorption fraction, the strict starting-distance ordering, or the explicit inverse-square correction in its accessible main text. These features, not quantum survival itself, are assessed here.

Riberi, *An Exactly Solvable Absorbing Quantum Walk* (2026), obtains a closed absorption formula for a **semi-infinite chain with a boundary absorber**. Its absorption is invariant under reciprocal loss coupling and optimized at its normalized coupling one. That boundary result and its spatial asymptotics are closely related, but its exact kernel does not cover the full-line interior defect: the latter has a different band kernel, breaks reciprocal-coupling symmetry, and has the nontrivial optimal normalized strength above. Rank-one resolvent techniques and the existence of partial absorption are established techniques, not new claims here.

## Limitations

The theorem is for one loss site on the infinite homogeneous line, not arbitrary finite multi-trap configurations, site disorder, or continuous monitoring protocols. The optimization concerns \(\lim_{m\to\infty}Q_m\) at fixed strength, not a global optimum of \(Q_m\) at each finite distance. The large-distance expansion is not uniform as the loss strength tends to zero or infinity. Independent scientific review and exhaustive priority determination have not been performed. Longhi's separately hosted supplemental analysis was not accessible during the comparison; it is a residual prior-art risk.

## References

- S. Longhi, *Photonic random walks with traps*, Optics Letters **49** (2024), 2809–2812. DOI: 10.1364/OL.522686. Accessible manuscript: https://arxiv.org/html/2405.07192v1. Original online posting April 22, 2024 (Optica article history and preprint record).
- F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056v1 (2026), https://arxiv.org/html/2605.08056v1. See its half-line boundary model and absorption Eq. (14).
- M. Sabri, E. Segawa and M. Štefaňák, *Conditional limit measure of a one-dimensional quantum walk with an absorbing sink*, Physical Review A **98** (2018), 012136. DOI: 10.1103/PhysRevA.98.012136. This is a discrete-time walk with an absorbing sink, not the present continuous-time interior-defect optimization.
