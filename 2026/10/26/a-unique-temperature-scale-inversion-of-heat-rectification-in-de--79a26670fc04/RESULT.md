# A unique temperature-scale inversion of heat rectification in detuned coupled qubits

## Finding
For a pair of unequal-frequency exchange-coupled qubits contacting independent bosonic thermal reservoirs with identical frequency-independent coupling, **reversing the two reservoir temperatures changes which orientation carries the larger absolute heat current exactly once as the common temperature scale varies**, provided the hot-to-cold temperature ratio is fixed and strictly larger than one. This is an all-parameter uniqueness statement within the global Born–Markov–secular master equation; it does not merely assert a numerical crossing.

Let \(J_{\mathrm F}(T)\) be the positive hot-to-cold stationary current when the bath attached to the higher-frequency qubit is hot at \(kT\), and let \(J_{\mathrm R}(T)\) be the positive hot-to-cold stationary current after the baths are interchanged. For every fixed admissible model and every \(k>1\), there exists a **unique** \(T_*\in(0,\infty)\) such that
\[
J_{\mathrm F}(T)>J_{\mathrm R}(T)\quad(0<T<T_*),\qquad
J_{\mathrm F}(T_*)=J_{\mathrm R}(T_*),\qquad
J_{\mathrm F}(T)<J_{\mathrm R}(T)\quad(T>T_*).
\]
The crossing can be located by solving a single strictly monotone scalar equation given below. The result is independent of the common positive bath coupling scale.

## Assumptions and scope
Set \(\hbar=k_{\mathrm B}=1\). The system Hamiltonian is
\[
H=\tfrac{\omega_1}{2}Z\otimes I+\tfrac{\omega_2}{2}I\otimes Z+\lambda(\sigma_+\otimes\sigma_-+\sigma_-\otimes\sigma_+),
\]
where \(\omega_1>\omega_2>0\) and \(0<\lambda<\sqrt{\omega_1\omega_2}\). The two local bosonic reservoirs are independent and have the same strictly positive frequency-independent dissipative rate \(g\). Evolution follows the energy-eigenbasis Born–Markov–secular (global Lindblad) equation, with each bath coupling through the corresponding \(X\) operator. There are no other dissipative channels or nonsecular coherences. For all \(T>0\), \(T_{\mathrm h}=kT\) and \(T_{\mathrm c}=T\), with the ratio \(k>1\) fixed. The conclusions concern the stationary hot-to-cold **magnitudes** under swapping these baths, not a signed current at one fixed contact.

Define
\[
\begin{gathered}
\delta=(\omega_1-\omega_2)/2,\quad \Omega=\sqrt{\delta^2+\lambda^2},\quad
p=(1+\delta/\Omega)/2,\quad q=1-p,\\
\omega_\pm=(\omega_1+\omega_2)/2\pm\Omega.
\end{gathered}
\]
Our hypotheses imply \(0<q<p<1\) and \(0<\omega_-<\omega_+\). For positive \(\omega\), let \(n_{\mathrm h}(\omega)=(e^{\omega/(kT)}-1)^{-1}\), \(n_{\mathrm c}(\omega)=(e^{\omega/T}-1)^{-1}\), and \(C_j(\omega)=2n_j(\omega)+1\).

## Proof
**Step 1: stationary current reconstruction.** Each transition frequency has two pairs of energy levels, with squared local spin-flip matrix elements \((p,q)\) at \(\omega_+\) and \((q,p)\) at \(\omega_-\) for contacts \((1,2)\). The population generator is a direct sum of two commuting two-state flip generators on the corresponding energy coordinates. Its unique stationary population vector is their product. The resulting hot-to-cold currents are
\[
\begin{split}
J_{\mathrm F}=gpq\bigg[&\frac{\omega_+(n_{\mathrm h,+}-n_{\mathrm c,+})}{pC_{\mathrm h,+}+qC_{\mathrm c,+}}+\frac{\omega_-(n_{\mathrm h,-}-n_{\mathrm c,-})}{qC_{\mathrm h,-}+pC_{\mathrm c,-}}\bigg],\\
J_{\mathrm R}=gpq\bigg[&\frac{\omega_+(n_{\mathrm h,+}-n_{\mathrm c,+})}{pC_{\mathrm c,+}+qC_{\mathrm h,+}}+\frac{\omega_-(n_{\mathrm h,-}-n_{\mathrm c,-})}{qC_{\mathrm c,-}+pC_{\mathrm h,-}}\bigg].
\end{split}
\]
This expression is the known global-master-equation current formula, rewritten for the specific bath-swap comparison. Positive frequency, positive bath temperatures and \(pq>0\) ensure both currents are positive.

**Step 2: cancellation and scalar factorization.** For \(x>0\), put \(a=1/k\in(0,1)\) and
\[
U(x)=\frac{4\sinh^2((1-a)x)}{\sinh(2ax)\sinh(2x)},\qquad
G(x)=\frac{U(x)}{1+pq\,U(x)}.
\]
Since \(U(\omega/(2T))=(C_{\mathrm h}-C_{\mathrm c})^2/(C_{\mathrm h}C_{\mathrm c})\), subtraction of the two explicit current formulas gives the **exact**, not asymptotic, identity
\[
J_{\mathrm F}-J_{\mathrm R}=\frac{gpq(p-q)}2\left[\omega_-G\left(\frac{\omega_-}{2T}\right)-\omega_+G\left(\frac{\omega_+}{2T}\right)\right].\tag{1}
\]
Let \(R(T)=\omega_-G(\omega_-/(2T))/[\omega_+G(\omega_+/(2T))]\). Equation (1) has the same sign as \(R(T)-1\).

**Step 3: strict logarithmic monotonicity.** Define \(\phi(z)=z\coth z\) on \((0,\infty)\). Direct differentiation yields
\[
\phi'(z)=\coth z-z\operatorname{csch}^{2}z>0,\qquad
\phi''(z)=2\operatorname{csch}^{2}z\,(z\coth z-1)>0.
\]
Thus \(\phi'\) is positive and strictly increasing. Set
\[
H_0(x)=-\frac{xU'(x)}{U(x)}=\phi(2ax)+\phi(2x)-2\phi((1-a)x).
\]
Here \(H_0(0+)=0\) and
\[
H'_0(x)=2a\phi'(2ax)+2\phi'(2x)-2(1-a)\phi'((1-a)x)>0.
\]
Indeed \(2x>(1-a)x\), \(\phi'\) increases strictly, and \(1-a<1\). Consequently \(H_0>0\), \(U'<0\), and
\[
H(x):=-\frac{xG'(x)}{G(x)}=\frac{H_0(x)}{1+pq\,U(x)}
\]
is strictly increasing: its numerator strictly increases from zero and its positive denominator strictly decreases. With \(\beta=1/T\), logarithmic differentiation now gives
\[
\beta\,\frac{d}{d\beta}\log R(1/\beta)
=H\left(\frac{\omega_+\beta}{2}\right)-H\left(\frac{\omega_-\beta}{2}\right)>0.\tag{2}
\]
This establishes strict monotonicity of the ratio as temperature falls. In particular multiple inversions are impossible.

**Step 4: opposite end signs and existence.** At \(x\downarrow0\), \(U(x)\to(1-a)^2/a\), a positive constant, hence
\[
\lim_{T\to\infty}R(T)=\frac{\omega_-}{\omega_+}<1.
\]
As \(x\to\infty\), \(U(x)\sim4e^{-4ax}\), so
\[
R(T)\sim\frac{\omega_-}{\omega_+}
\exp\!\left(\frac{2(\omega_+-\omega_-)}{kT}\right)\to\infty
\quad (T\downarrow0).
\]
Continuity, (2), and these strict endpoint limits prove existence and uniqueness of \(T_*\) and the stated signs. Explicitly it is the unique solution of
\[
\omega_-\frac{U(\omega_-/(2T_*))}{1+pq\,U(\omega_-/(2T_*))}
=\omega_+\frac{U(\omega_+/(2T_*))}{1+pq\,U(\omega_+/(2T_*))}.
\]

## Verification
The standalone `verify.py` independently constructs the four-state transition-rate generator and solves stationary population equations by Gaussian elimination, without substituting the analytic stationary distribution. It compares bath-resolved currents against the closed formulas and their factorization across a reproducible deterministic parameter grid, checks the sign change and unique scalar root numerically for a worked example, and checks the monotonic ratio on a finite grid. These finite checks test the derivation but do **not** replace the infinite all-parameter analytic proof above.

For \(\omega_1=2\), \(\omega_2=1\), \(\lambda=0.4\), \(g=0.01\), and \(k=2\), the unique inversion is at \(T_*\approx0.7918074837116923\). At \(T=0.2\), the two forward/reverse currents are approximately \(0.000103915299811\) and \(0.0000899605193212\), respectively; at \(T=1\) they are approximately \(0.000762820562216\) and \(0.000811734580630\). These numbers can be reproduced by `python3 verify.py` with Python's standard library.

## Relationship to prior work
Upadhyay, Naseem, Marathe, and Müstecaplıoğlu (2021, arXiv:2106.02891) study the same two-channel structure with a Dzyaloshinskii–Moriya interaction whose single-excitation complex hopping is equivalent to real exchange after a local phase change. Their Eqs. (18), (24), and (26) supply a global heat-current formula and exhibit **opposing** frequency-channel contributions. Their Sec. IV.2 also interprets the sign as fixed by the frequency detuning. Neither the exact all-temperature uniqueness theorem nor the above monotonic scalar ratio appears there. The present result makes precise when the competing contributions overcome each other as both temperatures are scaled with fixed ratio; it does not claim discovery of the known formula.

Fogedby (2023, arXiv:2301.13544) independently derives the same-type global secular stationary currents for a coupled-qubit system, but focuses on thermodynamic consistency and heat-current positivity rather than a unique bath-swap rectification crossing. Khandelwal et al. (2022, arXiv:2208.10809) analyze heat-current/rectification trade-offs in several one- and two-qubit devices, including weakly coupled detuned local and strongly coupled resonant global models; their different optimization objective does not imply (2). Earlier temperature-controlled sign reversals in anisotropic spin-chain systems are not claimed absent (for example Zhang et al., *Phys. Rev. B* 80, 172301 (2009)); the scope here is an exact **single-inversion theorem** for a specified detuned two-qubit global model and every temperature ratio.

## Limitations
The conclusions assume exact equality and spectral flatness of the two bath rates, global secular dynamics, strictly positive exchange and detuning, and two distinct positive dressed transition frequencies. At resonance \(\omega_1=\omega_2\) the current difference vanishes identically; at zero coupling both currents vanish; those cases do not have a unique crossing. For frequency-dependent bath spectra, unequal contact strengths, nonsecular coherences, time-dependent drive, or other bath statistics, the result is not asserted. The low-temperature limit assumes a fixed positive exchange splitting and exact rates, not a statement about finite experimental resolution. The temperature crossing does not imply any reversal of heat flow against the temperature gradient: in each orientation heat still flows from hot to cold.

## References
1. V. Upadhyay, M. T. Naseem, R. Marathe, and O. E. Müstecaplıoğlu, *Heat rectification by two qubits coupled with Dzyaloshinskii–Moriya interaction*, arXiv:2106.02891 (first publicly posted 2021-06-05), https://arxiv.org/html/2106.02891v3.
2. H. C. Fogedby, *Heat currents in qubit systems*, arXiv:2301.13544 (first publicly posted 2023-01-31), https://arxiv.org/abs/2301.13544.
3. S. Khandelwal et al., *Characterizing the performance of heat rectifiers*, arXiv:2208.10809 (first publicly posted 2022-08-23), https://arxiv.org/abs/2208.10809.
4. L. Zhang et al., *Reversal of thermal rectification in quantum systems*, *Phys. Rev. B* 80, 172301 (2009), https://doi.org/10.1103/PhysRevB.80.172301.
