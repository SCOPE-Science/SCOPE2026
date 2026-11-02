# A quadratic-time reversal of electrochemical work in a detuned quantum-dot load

## Finding

In the four-population, secular load-only dynamics of a strongly detuned three-dot battery, a seemingly successful finite-time discharge can reverse its **accumulated signed electrochemical work** if the load remains connected. The mechanism is not a reversal of the elementary high-energy extraction step: it is the very slow, effectively irreversible filling of the low-energy one-electron levels by the same high-chemical-potential load. The effect has an exact singular-time profile.

Set \(\hbar=k_{\mathrm B}=1\), choose \(\Omega,\Gamma,T,c>0\), and let \(\Delta\to+\infty\). For the load at \(\mu_\Delta=E_d(\Delta)-cT\), put \(f=(1+e^c)^{-1}\). Let the initial probabilities in the energy-eigenstate basis converge to \((p_0,p_g,p_e,p_d)\), with sum one, \(p_0>0\), and \(m=p_0+p_d\). Assume the **positive-extraction condition** \((1-f)m>p_0\). Denote the net normalized electrochemical output by
\[
\Phi_\Delta(t):=\frac{W_{\mathrm{load},\Delta}(t)}{\mu_\Delta-\mu_{\mathrm{source}}}
=p_{0,\Delta}(t)-p_{0,\Delta}(0),
\]
where the denominator is positive for sufficiently large detuning.

Then the two iterated limits disagree:
\[
\lim_{t\to\infty}\lim_{\Delta\to\infty}\Phi_\Delta(t)
=(1-f)m-p_0>0,
\qquad
\lim_{\Delta\to\infty}\lim_{t\to\infty}\Phi_\Delta(t)
=-p_0<0.
\]
More precisely, with scaled time \(\theta=\Gamma\Omega^2t/\Delta^2\), for every \(\theta>0\),
\[
\boxed{\lim_{\Delta\to\infty}\Phi_\Delta\left(\frac{\Delta^2\theta}{\Gamma\Omega^2}\right)
=(1-f)m e^{-(1-f)\theta}-p_0.}
\]
Convergence is uniform on compact intervals bounded away from \(\theta=0\). This limiting function is strictly decreasing and has exactly one positive zero,
\[
\boxed{\theta_*=\frac{1}{1-f}\log\frac{(1-f)m}{p_0}.}
\]
For every sufficiently large \(\Delta\), an accumulated-work zero occurs at a time \(t_\Delta\) satisfying
\[
\boxed{\frac{\Gamma\Omega^2t_\Delta}{\Delta^2}\longrightarrow\theta_*.}
\]
The displayed statement guarantees a zero near this scale; it does not claim that the finite-detuning output has no other zeros at other times.

For the leading charged-state populations associated with a source chemical potential at the common low-dot energy, take \(C=\cosh(\Omega/T)\), \(p_0=(1+3C)^{-1}\), and \(p_d=C/(1+3C)\). Then
\[
\theta_* = \frac{\log[(1-f)(1+C)]}{1-f}
\]
whenever \((1-f)(1+C)>1\). With \(\Omega=T=1\) and \(c=4.5\), this gives \(\theta_*=0.932574593181945\ldots\), corresponding at \(\Delta=100\), \(\Gamma=0.1\) to the large-detuning prediction \(t_\Delta\approx9.33\times10^4\), rather than the finite extraction window \(t=100\).

## Assumptions and scope

The single-electron Hamiltonian in the ordered dot basis is
\[
H_\Delta=\begin{pmatrix}\Delta&-\Omega&0\\-\Omega&0&-\Omega\\0&-\Omega&0\end{pmatrix}.
\]
Write its distinct ordered eigenpairs as \((E_a,|a\rangle)\), \(a=g,e,d\), and \(u_a=\langle1|a\rangle\). Along with the empty state \(|0\rangle\), there are four populations. No charging reservoir, dephasing drive, internal phonon relaxation, or additional load channel is active during discharge. The load acts at the detuned dot 1 with global, secular, weak-coupling jump rates
\[
r_a^+=\Gamma|u_a|^2[1+e^{(E_a-\mu_\Delta)/T}]^{-1},\qquad
r_a^-=\Gamma|u_a|^2[1+e^{(\mu_\Delta-E_a)/T}]^{-1}.
\]
The two directions connect only \(0\leftrightarrow a\); initial coherences are immaterial to populations for this secular generator. Time is in \(\hbar=1\) units; restore \(\hbar\) by multiplying physical times by \(\hbar\). The initial family may depend on detuning, provided its population vector converges as stated. The result is an asymptotic of this four-state generator, not a claim about arbitrarily long physical operation when neglected charge sectors, orbitals, or decoherence become significant.

## Proof

**1. Particle conservation gives exact work identity.** The population equations are
\[
\dot p_0=\sum_a(r_a^-p_a-r_a^+p_0),\qquad
\dot p_a=r_a^+p_0-r_a^-p_a.
\]
The load's net particle current is \(I=\dot p_0\). Therefore its time-integrated signed particle flow, and its signed electrochemical work divided by \(\mu_\Delta-\mu_{\mathrm{source}}\), equal \(p_0(t)-p_0(0)\) at every time, with no time-integration approximation.

**2. Finite-detuning equilibrium fixes the opposite infinite-time sign.** Since \(\Omega>0\), every eigenvector of the irreducible tridiagonal Hamiltonian has a nonzero first component: if its first component vanished, the first and then second row force all components to vanish. Thus all \(r_a^\pm>0\) for finite \(\Delta\), \(T>0\). The four-state chain is irreducible and has the unique reversible stationary law
\[
\pi_0=Z^{-1},\qquad \pi_a=Z^{-1}e^{(\mu_\Delta-E_a)/T},\qquad
Z=1+\sum_ae^{(\mu_\Delta-E_a)/T},
\]
because \(r_a^+\pi_0=r_a^-\pi_a\). Since \(\mu_\Delta=E_d-cT\to\infty\) while \(E_g,E_e\) remain bounded, \(\pi_0\to0\). Exponential convergence of this finite irreducible chain yields the second iterated limit \(-p_0\).

**3. Detuning produces two distinct time scales.** Nondegenerate perturbation of the tridiagonal matrix about its high-level decoupling gives
\[
E_g\to-\Omega,\quad E_e\to\Omega,\quad E_d=\Delta+O(\Delta^{-1}),
\]
\[
|u_g|^2=\frac{\Omega^2}{2\Delta^2}[1+O(\Delta^{-1})],\quad
|u_e|^2=\frac{\Omega^2}{2\Delta^2}[1+O(\Delta^{-1})],\quad
|u_d|^2\to1.
\]
The high-state Fermi factor equals \(f\) exactly, and the two low-state factors tend to one exponentially fast in detuning. At any fixed \(t\), the low states become absorbing while \(0\leftrightarrow d\) remains a two-state chain with rates \(\Gamma f\) and \(\Gamma(1-f)\). Its conserved total mass is \(m\), and direct solution gives
\[
\lim_{\Delta\to\infty}p_{0,\Delta}(t)
=(1-f)m+[p_0-(1-f)m]e^{-\Gamma t}.
\]
This proves the first iterated limit.

**4. The slow Markov reduction determines the sharp cutoff.** Put \(\epsilon_\Delta=\Gamma\Omega^2/\Delta^2\). On the rescaled time \(\theta=\epsilon_\Delta t\), the \(0\leftrightarrow d\) block relaxes on vanishing \(\theta\)-time to its conditional distribution \((1-f,f)\). Its mass \(m_\Delta=p_0+p_d\) leaks to each low-energy level at rate \(\epsilon_\Delta p_0/2+o(\epsilon_\Delta)\), and the reverse low-energy rates are exponentially smaller than \(\epsilon_\Delta\). Thus the effective projected equation is
\[
\frac{dm}{d\theta}=-(1-f)m,\qquad m(0+)=m.
\]
To justify projection without informal adiabatic assumptions, decompose the finite generator into its fast eigenprojection and complementary three-dimensional kernel at \(\epsilon_\Delta=0\). The fast eigenvalue is \(-\Gamma\); the remaining restricted generator is \(\epsilon_\Delta A+o(\epsilon_\Delta)\), where its first coordinate is exactly the displayed scalar equation and its two other coordinates accumulate the exiting mass. Variation of constants for finite matrices (equivalently, the Schur complement of the fast block) gives uniform convergence on each compact \(\theta\in[\delta,R]\), \(0<\delta<R<\infty\). Hence \(p_{0,\Delta}(\theta/\epsilon_\Delta)\to(1-f)m e^{-(1-f)\theta}\), proving the boxed limit.

**5. Root and noncommutation.** The derivative of the limiting work profile is \(-(1-f)^2m e^{-(1-f)\theta}<0\), and its value at \(0+\) is positive by hypothesis, while its limit as \(\theta\to\infty\) is \(-p_0<0\). The intermediate-value theorem supplies the unique limiting root. For any sufficiently small \(\delta>0\), uniform convergence and the strict opposite signs at \(\theta_*\pm\delta\) produce at least one finite-detuning zero inside that bracket. Letting \(\delta\downarrow0\) gives the asserted asymptotic. The noncommuting iterated limits now follow from Steps 2 and 3.

## Verification

The standalone `verify.py` builds the exact three-by-three Hamiltonian, diagonalizes it, constructs the four-state generator, checks column conservation and finite-temperature detailed balance, evaluates matrix exponentials at fixed and quadratic times, and finds finite-detuning accumulated-output zeros. In a fresh execution it passed 265 deterministic assertions for eight detunings from 40 through 500. The rescaled zero at detuning 100 is approximately \(0.9326348044\); at detuning 500 it is approximately \(0.9325769995\), approaching \(\theta_*=0.9325745932\). These computations corroborate but do not prove the all-detuning asymptotics; the proof is Steps 1–5.

Run `python verify.py` with Python, NumPy, and SciPy. No external private data or intermediate files are needed.

## Relationship to prior work

Singh, Sánchez, and Jordan introduced the charged triple-dot device, the load reservoir, the secular jump rates, and the finite-time electrochemical work integral. Their load study evaluates a specific finite discharge protocol ending at \(\Omega t/\hbar=100\) and quantifies positive output. The elementary grand-canonical detailed-balance law itself is standard thermodynamics, not claimed as new. The assessed result combines those known ingredients into an explicit **singular long-time discharge phase**, including noncommutation of detuning and time limits and the sharp quadratic-scale zero of the accumulated work. The work does not dispute the finite-time extraction demonstrated in the motivating paper. Other quantum-battery studies of non-Markovian dephasing and extractable-work fluctuations address different dynamical and objective questions.

## Limitations

The parameter \(\mu_\Delta\) grows with detuning; if fixed instead, the stated limiting law changes. Every \(\Delta\) is finite before the equilibrium limit; the weak-coupling secular population master equation is assumed valid. Extremely long laboratory times may involve omitted phonon processes, orbital excitations, many-electron sectors, chemical-potential drift, or finite reservoir capacity. The theorem describes **signed accumulated electrochemical work**, not ergotropy, total internal energy, a permanently connected two-reservoir steady-state engine, or a guarantee of physical reversibility. The limiting profile does not exclude additional zeros of the exact finite-detuning function away from the quadratic window. Source-level priority remains subject to independent literature review; general grand-canonical re-equilibration and singular perturbations are established methods, and novelty is only claimed for this device-specific explicit crossover combination.

## References

1. A. N. Singh, R. Sánchez, and A. N. Jordan, *Dephasing-powered open quantum-dot battery*, arXiv:2610.33408v1 (first submitted 2026-10-24), Sections II, III, IV.2 and appendices. https://arxiv.org/html/2610.33408v1
2. Y. Wang and J. Jin, *Early-stage memory effect on the dephasing charger-mediated quantum battery*, Physical Review A **114**, 032407 (2026), DOI:10.1103/21db-dxvt. Different two-qubit memory-assisted charge dynamics, not the present load asymptotic. https://journals.aps.org/pra/abstract/10.1103/21db-dxvt
3. N. Yunger Halpern, P. Faist, J. Oppenheim, and A. Winter, *Microcanonical and resource-theoretic derivations of the thermal state of a quantum system with noncommuting charges*, Nature Communications **7**, 12051 (2016); arXiv:1512.01189. Background for equilibrium-state thermodynamics; not a priority claim for this model. https://arxiv.org/abs/1512.01189
