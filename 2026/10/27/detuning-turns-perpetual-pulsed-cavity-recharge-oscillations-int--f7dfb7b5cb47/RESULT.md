# Detuning turns perpetual pulsed-cavity recharge oscillations into a finite sequence

## Finding
Consider an initially empty two-mode bosonic charger–battery system with a coherent displacement pulse applied to the lossy charger at time zero. With nonzero loss and coupling in the resonantly underdamped regime, exact resonance produces infinitely many strict local maxima of battery energy, whereas **every nonzero relative detuning produces only finitely many**. The number of charging maxima diverges with an explicit inverse-detuning coefficient as resonance is approached.

More precisely, let \(g>\gamma/4>0\), let the pulsed charger amplitude be \(F>0\), let the battery frequency be \(\omega_b>0\), and write the charger–battery detuning as \(\Delta=\omega_a-\omega_b\). Let \(N(\Delta)\) be the number of strict local maxima of the post-pulse stored battery energy on \((0,\infty)\). Set
\[
G=\sqrt{g^2-\gamma^2/16}>0.
\]
Then
\[
N(0)=\infty,
\qquad
N(\Delta)<\infty\quad(\Delta\ne0),
\]
and the sharp counting law is
\[
\boxed{\displaystyle
N(\Delta)=\frac{4G^2}{\pi\gamma|\Delta|}
\operatorname{arcosh}\!\left(\frac{4g}{\gamma}\right)+O(1)
\quad\text{as }\Delta\to0,\quad\Delta\ne0.}
\]
The bounded remainder refers to fixed \(g,\gamma\). Moreover, at every nonzero detuning the stored energy is strictly positive for all \(t>0\), so the exact zero-energy revival nodes occurring at resonance disappear.

An explicit final possible turning time at \(\Delta\ne0\) is available. Define
\[
\mathcal Z=\sqrt{g^2+(\Delta/2-i\gamma/4)^2},\qquad
\alpha=\gamma/2,\quad \beta=2|\operatorname{Im}\mathcal Z|,\quad
\varpi=2\operatorname{Re}\mathcal Z>0,\quad R=\sqrt{\alpha^2+\varpi^2},
\]
with the square-root branch chosen so \(\operatorname{Re}\mathcal Z>0\). The cutoff is
\[
\boxed{\displaystyle
T_{\mathrm{env}}=
\frac{\operatorname{artanh}(\beta/\alpha)
+\operatorname{arcosh}\!\left(R/\sqrt{\alpha^2-\beta^2}\right)}{\beta}.}
\]
Every time \(t>T_{\mathrm{env}}\) has strictly decreasing stored energy. The cutoff is an envelope bound, not necessarily the time of the last maximum.

## Assumptions and scope
The Hamiltonian after the pulse is
\[
H=\omega_a a^\dagger a+\omega_b b^\dagger b
+g(a^\dagger b+b^\dagger a),
\]
and the zero-temperature amplitude-damping master equation is
\[
\dot\rho=-i[H,\rho]+\gamma\left(a\rho a^\dagger-\frac12\{a^\dagger a,\rho\}\right).
\]
The state immediately after a charger-only displacement pulse is
\(\lvert-iF\rangle_a\otimes\lvert0\rangle_b\).
All parameters are time-independent after the pulse; there is no direct battery loss, no thermal excitation, no nonlinearity, and no later drive. Stored battery energy means \(E_\Delta(t)=\omega_b\operatorname{tr}(\rho(t)b^\dagger b)\), not an accumulated input-work functional. The coupling and damping are strictly positive with \(g>\gamma/4\). The detuning can be any real number for the finite-maxima assertion; the counting asymptotic concerns \(\Delta\to0\) through nonzero values. The number of local maxima counts distinct strict maxima, not tiny oscillations above a fixed detection threshold.

## Proof
**1. Exact detuned energy.** A passive quadratic Hamiltonian and zero-temperature loss preserve coherent product states. With \(\bar\omega=(\omega_a+\omega_b)/2\), the coherent amplitudes solve
\[
i\frac{d}{dt}\binom{A}{B}=
\begin{pmatrix}\omega_a-i\gamma/2&g\\g&\omega_b\end{pmatrix}
\binom{A}{B},\qquad (A(0),B(0))=(-iF,0).
\]
Subtracting the scalar \(\bar\omega-i\gamma/4\) leaves a traceless matrix whose square equals \(\mathcal Z^2I\). Therefore
\[
B(t)=-\frac{Fg}{\mathcal Z}\sin(\mathcal Zt)
 e^{-\gamma t/4-i\bar\omega t},
\]
and the energy is exactly
\[
\boxed{\displaystyle E_\Delta(t)=
\frac{\omega_bF^2g^2}{2|\mathcal Z|^2}
 e^{-\alpha t}\bigl(\cosh(\beta t)-\cos(\varpi t)\bigr).}
\tag{1}
\]
Because \(g>\gamma/4\), \(\operatorname{Re}\mathcal Z>0\). If \(\Delta\ne0\), the imaginary part is nonzero: taking imaginary parts of \(\mathcal Z^2=g^2+(\Delta/2-i\gamma/4)^2\) gives \(2\operatorname{Re}\mathcal Z\operatorname{Im}\mathcal Z=-\gamma\Delta/4\). Hence \(\beta>0\). The dissipative two-by-two generator is strictly stable for \(g>0\): a hypothetical undamped eigenvector would have vanishing charger component, incompatible with the nonzero coupling. Its two eigenvalue real parts are \(-\gamma/4\pm\beta/2\), so \(0<\beta<\alpha\). Equation (1) is strictly positive at \(t>0\) for \(\Delta\ne0\), since \(\cosh(\beta t)>1\ge\cos(\varpi t)\).

**2. Finite-time envelope.** Apart from a positive factor, the derivative of (1) has the sign of
\[
\begin{aligned}
\Phi(t)&=\alpha\cos(\varpi t)+\varpi\sin(\varpi t)-L(t),\\
L(t)&=\alpha\cosh(\beta t)-\beta\sinh(\beta t).
\end{aligned}
\tag{2}
\]
Here \(L(t)>0\), \(L(0)=\alpha<R\), and
\[
L(t)=\sqrt{\alpha^2-\beta^2}
\cosh\!\left(\beta t-\operatorname{artanh}(\beta/\alpha)\right).
\]
It first decreases, reaches one positive minimum, then increases unboundedly. There is exactly one positive solution of \(L(t)=R\), and it is \(T_{\mathrm{env}}\) above. For \(t>T_{\mathrm{env}}\), the oscillatory part in (2) is bounded above by \(R<L(t)\). Thus \(E_\Delta'(t)<0\) throughout that half-line. Analyticity on the compact interval from zero to \(T_{\mathrm{env}}\), together with the nonidentically-zero derivative, rules out infinitely many interior isolated maxima. The derivative is positive immediately after zero because \(\Phi(0)=0\) and \(\Phi'(0)=\varpi^2+\beta^2>0\).

**3. Counting the near-resonant maxima.** Put \(\phi=\arctan(\varpi/\alpha)\). For \(0<t<T_{\mathrm{env}}\), let
\[
\vartheta(t)=\arccos\!\left(L(t)/R\right),\qquad 0<\vartheta(t)<\pi/2.
\]
The turning-point equation \(\Phi(t)=0\) is equivalent to one of the two phase equations
\[
\varpi t-\phi=2\pi k\pm\vartheta(t),\qquad k\in\mathbb Z.
\tag{3}
\]
Differentiating yields
\[
\vartheta''(t)=
-\frac{\beta^2L(t)}{\sqrt{R^2-L(t)^2}}
-\frac{L(t)L'(t)^2}{\bigl(R^2-L(t)^2\bigr)^{3/2}}<0.
\tag{4}
\]
For sufficiently small nonzero detuning, \(\vartheta'(0)=\beta^2/\varpi<\varpi\). It follows that \(t\mapsto\varpi t-\phi-\vartheta(t)\) increases strictly from its initial value to \(\varpi T_{\mathrm{env}}-\phi\). The opposite-sign phase function \(t\mapsto\varpi t-\phi+\vartheta(t)\) is strictly concave, initially increasing, and has only one turning point: its derivative tends to \(-\infty\) as \(t\uparrow T_{\mathrm{env}}\). Its final descending excursion changes its value by less than \(\pi/2\), since \(\vartheta<\pi/2\). Thus, each phase branch gives \(\varpi T_{\mathrm{env}}/(2\pi)+O(1)\) solutions, and at most a bounded number of zeros are tangential or shared. Consequently the alternating simple roots of \(E_\Delta'\) give
\[
N(\Delta)=\frac{\varpi T_{\mathrm{env}}}{2\pi}+O(1).
\tag{5}
\]
All bounds implicit here are uniform for sufficiently small nonzero \(\Delta\) with fixed \(g,\gamma\).

Now the square root has the expansions
\[
\varpi=2G+O(\Delta^2),\qquad
\beta=\frac{\gamma|\Delta|}{4G}+O(|\Delta|^3).
\]
Since \(R/\alpha\to4g/\gamma\), the exact envelope time obeys
\[
T_{\mathrm{env}}=
\frac{4G}{\gamma|\Delta|}\operatorname{arcosh}\!\left(\frac{4g}{\gamma}\right)+O(1).
\]
Substitution into (5) proves the stated asymptotic coefficient.

**4. Exact resonance.** When \(\Delta=0\), \(\mathcal Z=G>0\) and (1) reduces to a positive constant times \(e^{-\gamma t/2}\sin^2(Gt)\). It has strict maxima at
\[
t_k=\frac{\arctan(4G/\gamma)+k\pi}{G},\qquad k=0,1,2,\ldots,
\]
and exact positive-time zero nodes at \(t=k\pi/G\) for every integer \(k\ge1\). Thus infinitely many strict local maxima exist at exact resonance and none of those positive-time nodes persists when \(\Delta\ne0\).

## Verification
The standalone `verify.py` needs Python with NumPy and SciPy. It independently compares the exact energy against direct exponentiation of the dissipative two-mode matrix for 300 parameter/time combinations; tests the strict post-cutoff decay inequality in 80 cases; checks strictly positive off-resonant energy; and counts stationary maxima by root bracketing for four nonzero detunings. For \(g=\gamma=1\), the predicted leading coefficient is \(2.4630465695533523\ldots\); the observed values \(|\Delta|N(\Delta)\) are \(2.60,2.50,2.48,2.47\) at respective detunings \(0.1,0.05,0.02,0.01\). Finite tests support but do not replace the analytic proof, especially its infinite-count and asymptotic parts.

## Relationship to prior work
Downing and Ukhtary, *Energetics of a pulsed quantum battery* (2024), provide the resonant two-mode pulsed model, its exceptional point and energy/power formulae. Their equal-frequency assumption is explicit; the detuning-dependent finite-extrema theorem and its asymptotic coefficient are not given there. The diagonalization of two coupled dissipative modes is standard and is not claimed to be novel. The mathematical contribution is the singular classification and quantitative count of physically distinct post-pulse energy recharge maxima under detuning. Farina et al. (2019) analyze charger-mediated energy transfer under open dynamics but do not supply this specific pulse-and-detuning peak-count law in material inspected. Shastri et al. (2025) study a different dephasing-driven charger and emphasize detuning robustness of steady charging; their behavior does not imply the transient amplitude-damping peak count here.

## Limitations
The result is for a linear, zero-temperature, single-pulse Gaussian bosonic model, with photon loss confined to the charger, no subsequent forcing and \(g>\gamma/4\). The inverse-detuning coefficient does not claim an operational number of **detectable** cycles above a fixed noise floor, or a corresponding count under coherent pumping, non-Markovian loss, direct battery loss, dephasing, or nonlinear modes. The mathematically exact extrema become exponentially small as their time increases. Literature searching cannot establish absolute novelty, and closely related damped-mode theory may contain an equivalent formulation not identified here.

## References
1. C. A. Downing and M. S. Ukhtary, *Energetics of a pulsed quantum battery*, Europhysics Letters **146** (2024), 10001, DOI: 10.1209/0295-5075/ad2e79; public article date 2024-03-27; arXiv:2403.20155 (submitted 2024-03-29). https://arxiv.org/abs/2403.20155
2. D. Farina, G. M. Andolina, A. Mari, M. Polini, and V. Giovannetti, *Charger-mediated energy transfer for quantum batteries: An open-system approach*, Physical Review B **99** (2019), 035421, arXiv:1810.10890. https://arxiv.org/abs/1810.10890
3. R. Shastri et al., *Dephasing enabled fast charging of quantum batteries*, npj Quantum Information **11** (2025), article 9, DOI: 10.1038/s41534-025-00959-5. https://doi.org/10.1038/s41534-025-00959-5
4. C. A. Downing and M. S. Ukhtary, *Hyperbolic enhancement of a quantum battery*, Physical Review A **109** (2024), 052206, DOI: 10.1103/PhysRevA.109.052206. https://doi.org/10.1103/PhysRevA.109.052206
