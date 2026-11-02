# Passivity-window staircase and universal square-root extinction in a lossy two-qubit battery

## Finding

Consider a resonantly coupled charger qubit and battery qubit, with only the charger subject to amplitude damping. A fully excited initial charger produces an **exact, finite staircase** of time intervals during which the battery has positive locally extractable work. The intervals disappear sequentially as the dimensionless charger decay increases, long before the underdamped/overdamped exceptional point. Each disappearance has a universal square-root time-width law. The sum of all usable charging-time intervals has a sharp weak-loss limit involving Catalan’s constant. Any nonzero initial charger ground-state coherence removes this finite-window extinction: at every nonnode time the battery retains strictly positive, although possibly arbitrarily small, ergotropy.

Precisely, fix coupling \(J>0\), battery frequency \(\omega>0\), charger loss rate \(\gamma\geq0\), and initial charger excited probability \(p\in[0,1]\). In the underdamped regime set
\[
 x=\frac{\gamma}{4J}\in(0,1),\quad G=J\sqrt{1-x^2},\quad a=\arccos x,
 \quad F_k(x)=\frac{2x}{\sqrt{1-x^2}}(a+k\pi),\qquad k\in\mathbb Z_{\geq0}.
\]
There is exactly one \(x_k\in(0,1)\) solving \(F_k(x_k)=\log 2\) for every \(k\geq0\), and
\[
1>x_0>x_1>x_2>\cdots>0,\qquad
x_k=\frac{\log 2}{\pi(2k+1)}+O(k^{-3}).
\]
For the *fully excited charger*, \(p=1\), the \(k\)-th Rabi lobe contains an open interval of strictly positive battery ergotropy **if and only if** \(x<x_k\). At \(x=x_k\) the lobe merely touches zero ergotropy at its maximum and is not counted. Thus the total number \(N(x)\) of positive-work intervals is
\[
N(x)=\max\!\left\{0,\left\lceil
 \frac{(\log2-F_0(x))\sqrt{1-x^2}}{2\pi x}
 \right\rceil\right\}\quad(0<x<1),
\]
with \(N(0)=\infty\) and \(N(x)=0\) for \(x\ge1\). In fact \(N(x)=0\) already for \(x\ge x_0=0.2552756376486518\ldots\), or \(\gamma/J\ge 1.0211025505946072\ldots\); this precedes the exceptional point \(\gamma/J=4\).

At fixed \(k\), write \(\Delta t_k(x)\) for the length of the positive-ergotropy interval in the \(k\)-th lobe. Approaching its threshold from below gives
\[
 \Delta t_k(x)=\frac{2}{J}\sqrt{F_k'(x_k)(x_k-x)}+O_k(x_k-x),
\]
and its peak ergotropy obeys
\[
 \mathcal E_k^{\max}(x)=\omega F_k'(x_k)(x_k-x)+O_k((x_k-x)^2).
\]
The width exponent is fixed by the exact curvature identity
\[
 \left.\frac{d^2}{dt^2}\log u(t)\right|_{t=t_k}=-2J^2,
 \qquad t_k=\frac{a+k\pi}{G},
\]
which does **not** depend on \(\gamma\) or the lobe number. Here \(u(t)\) is the one-excitation transfer probability defined below.


There is also a **global, sharp positive-work time budget**. For a fully excited initial charger, let \(\mathscr T(\gamma)=\operatorname{Leb}\{t>0:\mathcal E(t)>0\}\), the sum of the lengths of all positive-work windows. With \(G_{\mathrm{Cat}}=\sum_{n=0}^{\infty}(-1)^n/(2n+1)^2\) (Catalan's constant), the weak-loss law is
\[
 \boxed{\lim_{\gamma\downarrow0}\gamma\,\mathscr T(\gamma)
 =\frac{4G_{\mathrm{Cat}}}{\pi}-\log2
 =0.4730964355633298\ldots.}
\]
This is independent of the fixed exchange strength \(J\) and transition frequency \(\omega\). The limit concerns the total measure of useful *charging times*, not an integral of work output.

In contrast, for every coherent charger \(0<p<1\), ergotropy is strictly positive for each \(t>0\) with \(u(t)>0\), at all finite loss strengths. For \(0\le\gamma<4J\), its only positive-time zeros are transfer nodes \(t=n\pi/G\) (positive integers \(n\)); for \(\gamma\ge4J\), it is positive for *all* \(t>0\). For \(p=0\) it vanishes identically. These statements describe exact mathematical positivity, not a positive finite detection threshold.

## Assumptions and scope

The Hilbert space is the tensor product of two qubits. In units with \(\hbar=1\), the charging dynamics for \(t\ge0\) is the completely positive Lindblad evolution
\[
 \dot\rho=-i[H,\rho]+\gamma\left(a\rho a^\dagger-\frac12\{a^\dagger a,\rho\}\right),\qquad
 H=\omega(a^\dagger a+b^\dagger b)+J(a^\dagger b+b^\dagger a),
\]
where \(a\) and \(b\) lower respectively the charger and battery. Initially
\[
 |\psi(0)\rangle=\left(\sqrt{1-p}|0\rangle_a+e^{i\phi}\sqrt p|1\rangle_a\right)\otimes|0\rangle_b,
\]
with arbitrary phase \(\phi\). There is no battery dissipation during charging, no driving, no multilevel leakage, and no thermal excitation of the charger. For a battery state \(\rho_b(t)\) with Hamiltonian \(H_b=\omega|1\rangle\langle1|\), ergotropy \(\mathcal E(t)\) is the stored energy minus the energy of the passive rearrangement of \(\rho_b(t)\). Results concern only work available via a cyclic unitary on the battery alone at the switch-off time \(t\), not a full-cycle thermodynamic efficiency.

## Proof

**1. Transfer amplitude and reduced density matrix.** In the vacuum and single-excitation sector the no-jump conditional evolution of the initial charger excitation is generated, after removing the common \(\omega\) phase, by
\[
 M=\begin{pmatrix}-i\gamma/2&J\\ J&0\end{pmatrix}
\]
in the ordered basis \((|10\rangle,|01\rangle)\). Direct exponentiation yields the battery transfer amplitude up to an irrelevant phase,
\[
 f(t)=
 \begin{cases}
 \frac{J}{G}e^{-\gamma t/4}\sin(Gt),&0\le\gamma<4J,\quad G=\sqrt{J^2-(\gamma/4)^2},\\
 Jt e^{-Jt},&\gamma=4J,\\
 \frac{J}{h}e^{-\gamma t/4}\sinh(ht),&\gamma>4J,\quad h=\sqrt{(\gamma/4)^2-J^2}.
 \end{cases}
\]
The undamped limit is obtained by continuity. Put \(u(t)=|f(t)|^2\). The vacuum probability and single-excitation amplitudes, including jump loss to vacuum, give the reduced battery state
\[
 \rho_b(t)=\begin{pmatrix}
 1-pu(t)&z(t)\\\overline{z(t)}&pu(t)
 \end{pmatrix},\qquad |z(t)|^2=p(1-p)u(t),\qquad 0\le u(t)\le1.
\]
The eigenvalues are \(\lambda_{\pm}=(1\pm\sqrt{1-4p^2u(1-u)})/2\), hence
\[
 \mathcal E(t)=\omega\left(pu(t)-\frac{1-\sqrt{1-4p^2u(t)(1-u(t))}}{2}\right).
\]
These reproduce the previously known reduced ergotropy and transfer expressions in the underdamped regime; the remaining argument is a classification of their exact positivity in the loss parameter, including the singular damping boundary.

**2. Passivity versus charger coherence.** If \(p=1\), then \(z(t)=0\), \(\rho_b\) is diagonal, and its passive rearrangement gives
\[
 \mathcal E(t)=\omega\max\{0,2u(t)-1\}.
\]
If \(0<p<1\) and \(u(t)>0\), its off-diagonal matrix element is nonzero. A qubit with nonzero energy-basis coherence cannot commute with its nondegenerate Hamiltonian and therefore cannot be passive. Thus \(\mathcal E(t)>0\). The zeros of the transfer amplitude are just the underdamped sine nodes; the critically and overdamped transfer amplitudes are strictly positive at each \(t>0\). For \(p=0\) the state remains vacuum.

**3. Exactly one maximum in each underdamped lobe.** For \(x\in(0,1)\), the function \(u(t)=(J/G)^2 e^{-\gamma t/2}\sin^2(Gt)\) is positive on each \((k\pi/G,(k+1)\pi/G)\). Its logarithmic derivative is
\[
 \frac{d}{dt}\log u(t)=2G\cot(Gt)-\frac\gamma2.
\]
It decreases strictly on each lobe from \(+\infty\) to \(-\infty\), so has a unique zero at \(t_k=(a+k\pi)/G\), where \(a=\arccos x\). As \(\sin a=G/J\), the trigonometric prefactor cancels and
\[
 u(t_k)=\exp[-F_k(x)].
\]
For \(p=1\), a positive-ergotropy interval in lobe \(k\) therefore exists exactly when \(F_k(x)<\log2\).

**4. Thresholds, exact count and weak-loss law.** Differentiation gives
\[
 F_k'(x)=\frac{2[\arccos x+k\pi-x\sqrt{1-x^2}]}{(1-x^2)^{3/2}}>0.
\]
The inequality follows from \(\arccos x> x\sqrt{1-x^2}\) for \(0<x<1\): setting \(a=\arccos x\) this is \(a>\sin a\cos a\). Each \(F_k\) starts at zero as \(x\downarrow0\). For \(k=0\) its endpoint value as \(x\uparrow1\) is \(2>\log2\), and for \(k\ge1\) the endpoint is \(+\infty\). The intermediate value theorem and strict derivative give a unique root \(x_k\). Since \(F_{k+1}(x)>F_k(x)\), the roots strictly decrease. If their limit were positive, the additive term linear in \(k\) would diverge, so the limit is zero. Writing \(S_k=\pi(2k+1)\), the expansion \(F_k(x)=S_kx-2x^2+O(S_kx^3+x^4)\) on the root scale \(x=O(S_k^{-1})\) gives \(x_k=(\log2)/S_k+O(S_k^{-3})\). Finally \(F_k(x)=F_0(x)+2\pi kx/\sqrt{1-x^2}\). Counting precisely the nonnegative integers for which this is *strictly* less than \(\log2\) gives the stated ceiling formula, including threshold equality.

**5. Universal disappearing-window law.** Differentiating the log profile twice at its maximum yields
\[
 (\log u)''(t_k)=-2G^2\csc^2(a)=-2J^2.
\]
For each fixed \(k\), set \(\delta(x)=\log(2u(t_k))=\log2-F_k(x)\). Taylor's theorem in time, uniformly for \(x\) near \(x_k\), gives \(\log(2u(t_k+s))=\delta(x)-J^2s^2+O_k(s^3)\). Both boundary roots converge to the peak as \(x\uparrow x_k\), at distances \(\sqrt{\delta(x)}/J+O_k(\delta(x))\). Since \(\delta(x)=F_k'(x_k)(x_k-x)+O_k((x_k-x)^2)\), subtracting the roots proves the asserted width law. The maximum work is \(\omega(2u(t_k)-1)=\omega(e^{\delta(x)}-1)\), proving the linear peak law.

**6. Critical and overdamped boundary.** At \(\gamma=4J\), \(u(t)=J^2t^2e^{-2Jt}\) has maximum \(e^{-2}<1/2\). For \(\gamma>4J\), let \(r=h/(\gamma/4)\in(0,1)\). Differentiating the hyperbolic transfer gives a unique maximum whose squared height is \(\exp[-2\operatorname{artanh}(r)/r]\le e^{-2}<1/2\), because \(\operatorname{artanh}(r)\ge r\). Thus the completely excited charger cannot generate positive ergotropy at or beyond the exceptional point. More strongly, the previous \(x_0\) threshold already makes every underdamped peak passive.



**7. Universal weak-loss total duration.** Restrict to \(p=1\) and take \(\gamma\downarrow0\) at fixed \(J\). Let \(A_x=\gamma\pi/(2G)=2\pi x/\sqrt{1-x^2}\). Parameterize the \(k\)-th lobe by \(t=(k\pi+\varphi)/G\), \(0<\varphi<\pi\), so that
\[
 u(t)=\frac{e^{-kA_x}}{1-x^2}\,e^{-A_x\varphi/\pi}\sin^2\varphi.
\]
Write \(s_k=kA_x\), and let \(P(s)=\pi^{-1}\operatorname{Leb}\{\varphi\in(0,\pi):\sin^2\varphi>e^s/2\}\). For \(0\le s\le\log2\),
\[
 P(s)=\frac2\pi\arccos\!\left(\frac{e^{s/2}}{\sqrt2}\right),
\]
and \(P(s)=0\) for \(s\ge\log2\). Since \(1\le e^{A_x\varphi/\pi}\le e^{A_x}\) and \(1-x^2\to1\), the fraction of each \(k\)-th lobe with \(u>1/2\) is squeezed between the values of this continuous function \(P\) at arguments differing by at most \(A_x+O(x^2)\) from \(s_k\). All active lobes have \(s_k\le\log2+O(A_x)\), by the elementary upper bound \(u(t)\le e^{-s_k}/(1-x^2)\). Uniform continuity and Riemann summation then give
\[
 \gamma\,\mathscr T(\gamma)=2A_x\sum_{k\ge0}\frac{\operatorname{Leb}\{\varphi\in(0,\pi):u((k\pi+\varphi)/G)>1/2\}}\pi
 \longrightarrow 2\int_0^{\log2}P(s)\,ds.
\]
With \(z=e^{s/2}/\sqrt2\), the integral is \(\tfrac8\pi\int_{1/\sqrt2}^{1}\arccos(z)\,dz/z\). The substitution \(z=\cos\theta\), integration by parts and the standard Fourier-series evaluation \(\int_0^{\pi/4}\log\cos\theta\,d\theta=-\tfrac\pi4\log2+\tfrac12G_{\mathrm{Cat}}\) give the announced exact constant. The proof controls the entire set of infinitely many windows as loss vanishes, not merely any fixed window.

## Verification

The accompanying standalone script `verify.py` computes the four-dimensional GKLS Liouvillian and independently propagates the full density matrix by matrix exponential, rather than only substituting into the reduced formula. It compares density-matrix populations, coherences and ergotropy across underdamped, critically damped and overdamped cases, checks threshold uniqueness and ordering numerically, evaluates the exact interval count, and tests the local curvature, square-root boundary scaling, and globally integrated positive-time budget against the Catalan constant. Running `python verify.py` with Python, NumPy and SciPy produced **4348 passing bounded checks** in this package. Numerical checks are not a proof of the statements for all parameter values; the preceding seven arguments are.

For orientation, the first four critical values of \(\gamma_k/J=4x_k\) are \(1.021102550595\ldots\), \(0.298080963427\ldots\), \(0.177336284386\ldots\), and \(0.126377735658\ldots\). These decimals are illustrative; the threshold definition is exact.

## Relationship to prior work

Downing and Ukhtary (2026) established the model, its underdamped transfer function and ergotropy formula (their equations (60)–(70)), and analyzed the source of lossless ergotropy zero intervals (their equations (38)–(39), (50)–(56)). None of those expressions is claimed as new here. The present result identifies the complete *damping-parameter* hierarchy of nonpassive Rabi windows and its universal extinction asymptotic, and extends the classification through critical and overdamping.

Ali, Al-Kuwari and Quach (2026) established the qubit diagonal amplitude-damping passivity threshold as part of a postcharging storage-channel model (their equation (20) and Appendix B). The value one half is therefore known, not new; the comparison here is the **interlacing with successive in-stroke damped transfer peaks**, whose heights are controlled by a different exchange-dynamics model. Malavazi and collaborators (2025) considered ergotropy protection using two weak measurements, again a different protocol.

## Limitations

These claims concern exactly a two-level, resonant, Markovian, zero-temperature charger loss channel and local battery ergotropy. They neither establish optimality of a work-extraction protocol including charging cost nor claim a detectable work output at large times when coherence makes ergotropy strictly but extremely small. The square-root law is for each **fixed lobe index** and is not claimed uniform as the lobe index diverges. A stronger general theorem in undetected literature could subsume aspects of the window classification; novelty remains qualified pending independent priority review. The original transfer and single-qubit passivity formulas are known, and the contribution is the exact global hierarchy, boundary law, and Catalan total-time asymptotic. No independent audit has been conducted.

## References

1. C. A. Downing and M. S. Ukhtary, *Charging a quantum battery from the Bloch sphere*, Annalen der Physik 538 (2026), e00638, DOI: https://doi.org/10.1002/andp.202500638; preprint https://arxiv.org/abs/2601.10844 (initial submission 15 January 2026).
2. A. Ali, S. Al-Kuwari and J. Q. Quach, *Locally passive, globally charged quantum batteries: Coherence-controlled work and the robustness of the stored charge*, Advanced Quantum Technologies 9 (2026), e70397, https://arxiv.org/abs/2607.02810, DOI: https://doi.org/10.1002/qute.70397.
3. A. H. A. Malavazi and collaborators, *Two-time weak-measurement protocol for ergotropy protection in open quantum batteries*, PRX Energy 4 (2025), 023011, DOI: https://doi.org/10.1103/bv4w-jr6q.
4. A. E. Allahverdyan, R. Balian and T. M. Nieuwenhuizen, *Maximal work extraction from finite quantum systems*, EPL 67 (2004), 565–571, DOI: https://doi.org/10.1209/epl/i2004-10101-2.
