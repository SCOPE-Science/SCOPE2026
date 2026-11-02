# Sharp loss–fluence frontier for counterdiabatic charging of a lossy coherent-state cavity

## Finding

Consider a zero-temperature, linearly driven lossy cavity initially in vacuum and charged by exact counterdiabatic tracking along a real, nondecreasing reference envelope. Fix charging duration \(T>0\), final envelope amplitude \(A>0\), damping \(\kappa>0\), real effective detuning \(\omega\), and a specified cumulative cavity-loss budget. Among **all** absolutely continuous monotone envelopes with the prescribed endpoints and loss, there is a unique minimum-total-field-fluence envelope. It undergoes **two sharp shape transitions**: from hyperbolic sine to ordinary sine at normalized loss \(q=1/3\), and from ordinary sine to a sine followed by a saturated plateau at \(q=1/2\). The value and the complete minimizing trajectory are explicit, including both transition points.

Write \(a=\kappa/2\), \(\gamma=a+i\omega\), \(G=|\gamma|>0\), and \(s=t/T\). The dimensionless normalized loss \(q\) ranges over \(0<q<1\). The unique optimal ramp \(f_*(t)=A F_q(s)\) is as follows:

\[
F_q(s)=\begin{cases}
\sinh(us)/\sinh u,&0<q<1/3,\\
s,&q=1/3,\\
\sin(us)/\sin u,&1/3<q<1/2,\\
\sin(\pi s/2),&q=1/2,\\
\sin\!\bigl(\pi s/[4(1-q)]\bigr),&1/2<q<1,\;0\le s\le2(1-q),\\
1,&1/2<q<1,\;2(1-q)\le s\le1.
\end{cases}
\]

For the hyperbolic branch \(u>0\) is uniquely determined by
\[
q=\frac{\coth u}{2u}-\frac{1}{2\sinh^2u}.
\]
For the oscillatory branch \(0<u<\pi/2\) is uniquely determined by
\[
q=\frac{1}{2\sin^2u}-\frac{\cot u}{2u}.
\]
The optimum total physical complex-drive fluence is
\[
\boxed{\mathcal F_{\min}(q;T,A,\gamma)=A^2\left[Tq+\frac{H(q)}{TG^2}+\frac{a}{G^2}\right]},
\]
where the sharp dimensionless derivative cost is
\[
H(q)=\begin{cases}
\dfrac{u\coth u}{2}+\dfrac{u^2}{2\sinh^2u},&0<q<1/3,\\
1,&q=1/3,\\
\dfrac{u\cot u}{2}+\dfrac{u^2}{2\sin^2u},&1/3<q<1/2,\\
\dfrac{\pi^2}{16(1-q)},&1/2\le q<1.
\end{cases}
\]
All endpoints \(q=1/3\) and \(q=1/2\) join continuously in the ramp and cost; the formulas give the global minimum, not merely a stationary pulse.

The source's natural quarter-period \(\sin^2\) charging ramp has normalized loss \(q=3/8\). At exactly that loss budget, its dimensionless derivative expenditure is \(\pi^2/8\), while the unique best sine ramp costs \(H(3/8)=1.01795484272487\ldots\), strictly reducing the counterdiabatic derivative contribution by \(17.4876883525\ldots\) percent. The final coherent-state ergotropy and total cavity loss are held fixed in this comparison.

## Assumptions and scope

The effective cavity Hamiltonian is \(H(t)=\omega\,b^\dagger b-\lambda\bigl(U(t)b^\dagger+\overline{U(t)}b\bigr)\), with real nonzero coupling \(\lambda\). The density matrix obeys the vacuum amplitude-damping Lindblad equation \(\dot\rho=-i[H(t),\rho]+\kappa\mathcal D[b]\rho\) and \(\rho(0)=|0\rangle\langle0|\). This complex two-quadrature drive extends the reference real-drive Hamiltonian and implements the same exact counterdiabatic correction as in the motivating model. Throughout, \(T,A,\kappa,\omega,\lambda\) are fixed with \(T,A,\kappa>0\), \(\omega\in\mathbb R\), and \(\lambda\ne0\). The bare cavity energy gap \(\omega_B>0\) is fixed.

The admissible reference envelope \(f:[0,T]\to[0,A]\) belongs to \(H^1(0,T)\), is nondecreasing almost everywhere, and satisfies \(f(0)=0\), \(f(T)=A\). Define
\[
I(f)=\int_0^T f(t)^2\,dt=A^2 Tq,\qquad 0<q<1.
\]
The exactly tracking total complex drive is \(U_f(t)=f(t)+\dot f(t)/\gamma\). The cavity state remains coherent with \(\alpha_f(t)=i\lambda f(t)/\gamma\). Its terminal ergotropy is \(W_B=\omega_B\lambda^2 A^2/G^2\), independent of the shape. Cumulative physical cavity dissipation is \(L_B=\kappa\omega_B\lambda^2 I(f)/G^2\). The objective is the full field-intensity functional \(\mathcal F(f)=\int_0^T|U_f(t)|^2dt\), not the reservoir input work or the Hilbert-space geodesic length. The admissible class imposes no pointwise drive-amplitude or bandwidth bound beyond finite \(L^2\) fluence.

## Proof

**1. Exact dynamical reduction.** For the vacuum-driven harmonic Lindbladian, coherent states are preserved and \(\dot\alpha=-\gamma\alpha+i\lambda U_f\). Direct substitution of \(\alpha_f=i\lambda f/\gamma\) gives \(\dot\alpha_f=i\lambda\dot f/\gamma=-\gamma(i\lambda f/\gamma)+i\lambda(f+\dot f/\gamma)\). Since \(f(0)=0\), uniqueness of the linear ODE proves exact tracking. Consequently \(\omega_B|\alpha_f|^2=(\omega_B\lambda^2/G^2)f^2\); the terminal work and the loss formula follow. Expansion of the **total** drive intensity gives
\[
\mathcal F(f)=I(f)+\frac1{G^2}\int_0^T\dot f^2\,dt+2\operatorname{Re}(1/\gamma)\int_0^T f\dot f\,dt
=I(f)+\frac{E(f)}{G^2}+\frac{aA^2}{G^2},
\]
where \(E(f)=\int_0^T\dot f^2\,dt\). The nonzero endpoint mixed term is constant for every admissible envelope and does not affect the optimizer. Therefore, fixing the physical loss is exactly equivalent to fixing \(I(f)\), and the stated problem reduces to the sharp isoperimetric Dirichlet-energy problem.

**2. Profiles, constraints, and branch ranges.** Rescale \(F(s)=f(Ts)/A\), so \(\int_0^1F^2=q\), \(E(f)=(A^2/T)\int_0^1(F')^2\). The positive hyperbolic profile solves \(F''=u^2F\), \(F(0)=0\), \(F(1)=1\). Integration of \(\sinh^2(us)\) gives the displayed \(q(u)\), with limits \(q(0+)=1/3\), \(q(+\infty)=0\). The pointwise ratio \(\sinh(us)/\sinh u\) strictly decreases in \(u\) for \(0<s<1\), because \(x\coth x\) is strictly increasing on \(x>0\). Hence this branch determines precisely one \(u\) for every \(0<q<1/3\).

For the sine profile, \(F''=-u^2F\); integration gives the displayed second \(q(u)\), with limits \(q(0+)=1/3\) and \(q(\pi/2)=1/2\). The ratio \(\sin(us)/\sin u\) strictly increases in \(u\) when \(0<s<1\) and \(0<u<\pi/2\), because \(x\cot x\) strictly decreases there. Thus there is one \(u\) per \(1/3<q<1/2\), and all these profiles are strictly increasing. For \(q\ge1/2\), a quarter sine on \([0,t_*]\), followed by its saturating plateau, has \(I=A^2[T-t_*/2]\); solving \(I=A^2Tq\) gives \(t_*=2T(1-q)\). Its derivative is nonnegative, and it is continuously differentiable at the joining point.

**3. Global optimality for \(0<q\le1/2\).** Let \(F_*\) denote the profile, \(F\) any other admissible profile with the same \(q\), and \(h=F-F_*\). Then \(h(0)=h(1)=0\) and
\[
2\int_0^1F_*h=-\int_0^1h^2.
\]
Writing \(F_*''=\sigma F_*\), with \(\sigma=u^2\) for hyperbolic, \(\sigma=0\) for linear, and \(\sigma=-u^2\) for sine, integration by parts gives the exact energy-defect identity
\[
\int_0^1F'^2-\int_0^1F_*'^2=\int_0^1h'^2+\sigma\int_0^1h^2.
\]
This is strictly positive for any nonzero \(h\) if \(\sigma\ge0\). For sine, the Dirichlet Poincaré inequality \(\int h'^2\ge\pi^2\int h^2\) and \(u\le\pi/2\) yield strict positivity for every nonzero \(h\). This proves **global uniqueness**, including the linear and quarter-sine boundaries, even in the larger unconstrained-sign class with these endpoints and the same quadratic integral.

**4. Global optimality after saturation.** Work in physical dimensionless time \(s\in[0,1]\), put \(b=2(1-q)\in(0,1)\), \(k=\pi/(2b)\), and \(F_*(s)=\sin(ks)\) on \([0,b]\), \(F_*(s)=1\) on \([b,1]\). For any competitor \(F\), define \(h=F-F_*\). The equal-budget identity remains \(2\int F_*h=-\int h^2\). Integrating \(F_*''=-k^2F_*\) on \([0,b]\) and using \(F_*'(b)=0\) gives the **exact identity**
\[
\int_0^1(F'^2-F_*'^2)\,ds=\underbrace{\int_0^b(h'^2-k^2h^2)\,ds}_{\ge0}+\underbrace{\int_b^1h'^2\,ds}_{\ge0}+\underbrace{k^2\int_b^1(1-F^2)\,ds}_{\ge0}.
\]
The first term is nonnegative by the sharp Dirichlet–Neumann Poincaré inequality \(\int_0^b h'^2\ge[\pi/(2b)]^2\int_0^b h^2\), which holds for every \(H^1\) function with \(h(0)=0\) regardless of \(h(b)\). The final term is nonnegative because \(0\le F\le1\). Equality requires \(F=1\) almost everywhere on the plateau and \(h'=0\) there, hence \(h(b)=0\). Equality in the first Dirichlet–Neumann bound would require \(h\) proportional to \(\sin(ks)\), but \(h(b)=0\) forces that constant to vanish. Thus the global minimizer is unique.

**5. Explicit sharp values.** Direct integration of the squared derivatives of the hyperbolic and sine solutions gives the two displayed expressions for \(H\). For the plateau solution the derivative energy is \(\int_0^b k^2\cos^2(ks)ds=\pi^2/(8b)=\pi^2/[16(1-q)]\). Multiplication by \(A^2/T\) and insertion into the exact drive-fluence identity proves the boxed formula. The reference ramp \(F_0(s)=\sin^2(\pi s/2)\) has \(q=3/8\), \(\int_0^1F_0'^2ds=\pi^2/8\). Its strict suboptimality follows from uniqueness, and the stated quantitative reduction follows from the unique sine root and direct evaluation. This proves every claimed branch and threshold.

## Verification

The included standard-library program `verify.py` numerically integrates the reference profiles and derivatives, checks the displayed branch formulas against quadrature across all regimes, verifies endpoint constraints and monotonicity, checks the sharp cost against explicitly feasible power-law or linear-plateau competitors, and independently integrates the damped oscillator equation under the full complex drive. Its output is `PASS: 149 deterministic checks; universal claims use the analytical proof.` The script was executed from the actual packaged source; it uses no prior outputs or external files. The Poincaré comparison identities above, rather than these finite tests, prove global optimality over infinitely many admissible controls.

## Relationship to prior work

Ahmadi and Salimi (2026), arXiv:2610.32610v1, introduced this effective cavity model, exact CD tracking rule and the specific smooth \(\sin^2\) protocol, and optimized the duration within that envelope family. Those mechanisms and formulas are prior work, not new claims. The result here optimizes **over the full class of nondecreasing admissible envelopes at fixed actual dissipated cavity energy**, gives a complete three-regime Pareto frontier with global uniqueness, and keeps the cross-quadrature drive term explicitly. No arbitrary-profile exact frontier or sine-plus-plateau threshold was located in that paper's full text.

Abah et al. (2019), *Energetic cost of quantum control protocols*, DOI 10.1088/1367-2630/ab4c8c, previously optimized ramp costs for counterdiabatic protocols and included a parametrically driven harmonic oscillator. Their objectives involve Frobenius norms of Hamiltonians and Landau–Zener/parametric-oscillator examples; the inspected text describes no fixed-loss, monotone saturating displaced-cavity fluence frontier. Cavina et al. (2018), arXiv:1807.07450, developed a general variational framework for open-quantum-system control and applied it to two-level systems. General variational necessary conditions do not by themselves supply the exact three-branch global inequality and saturated obstacle optimizer proved here. This is a best-knowledge statement of specific mathematical contribution, not proof of absolute publication uniqueness.

## Limitations

The calculation concerns the effective linear, zero-temperature, Markovian cavity model with exact complex two-quadrature control, ideal coherent-state tracking, and a *fixed dissipated-energy budget*. Finite control bandwidth, a cap on microwave amplitude, nonzero thermal occupation, nonlinear cavity dynamics, and errors in the dispersive approximation may change the admissible set or the optimum. The extremal profiles generally have a nonzero initial derivative, so they need not satisfy stricter hardware endpoint-slew conditions; the exact displayed minimizer is not asserted to be attainable within such a smaller class. No conclusion about total input thermodynamic work follows from minimization of field fluence alone. A simple calculus-of-variations framework is standard; whether a broader previously published theorem implicitly contains the exact fixed-loss cavity frontier remains a priority risk. This is not an independent mathematical audit or an experimental validation.

## References

1. F. Ahmadi and S. Salimi, *Optimizing Quantum Battery via Counterdiabatic driving*, arXiv:2610.32610v1, first posted 23 October 2026. https://arxiv.org/html/2610.32610v1
2. O. Abah, R. Puebla, A. Kiely, G. De Chiara, M. Paternostro and S. Campbell, *Energetic cost of quantum control protocols*, New J. Phys. **21** (2019), 103048. https://doi.org/10.1088/1367-2630/ab4c8c ; open text https://pure.qub.ac.uk/files/195496390/Abah_2019_New_J._Phys._21_103048.pdf
3. V. Cavina, A. Mari, A. Carlini and V. Giovannetti, *A variational approach to the optimal control of coherently driven, open quantum system dynamics*, Phys. Rev. A **98** (2018), 052125, arXiv:1807.07450. https://arxiv.org/pdf/1807.07450
4. I. Čepaitė, A. Polkovnikov, A. J. Daley and C. W. Duncan, *Counterdiabatic optimized local driving*, PRX Quantum **4** (2023), 010312. https://doi.org/10.1103/PRXQuantum.4.010312
