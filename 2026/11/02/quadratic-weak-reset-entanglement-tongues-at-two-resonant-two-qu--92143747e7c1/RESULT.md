# Quadratic weak-reset entanglement tongues at two resonant two-qubit gates

## Finding

Consider a pair of qubits subjected at every discrete step either to a complete reset with probability \(p\in(0,1)\), or to the entangling unitary gate \(U(\theta)=\exp(\mathrm i\theta H)\) with probability \(1-p\). The reset state is \(\lvert\uparrow\uparrow\rangle\), and \(H\) is the four-dimensional Hermitian gate generator specified below. Let \(\rho_p(\theta)\) be the unique stationary density matrix, and let \(\mathcal N_p(\theta)=(\|\rho_p(\theta)^{T_2}\|_1-1)/2\) denote the two-qubit negativity.

For either \(\theta_0=\pi/4\) or \(\theta_0=3\pi/4\), and every fixed real \(c\),

\[
\lim_{p\downarrow0}\frac{\mathcal N_p(\theta_0+c p^2)}{p^2}
=\max\!\left\{0,\frac14-4c^2\right\}.
\]

The convergence is uniform for \(c\) in every compact real interval. Consequently, for fixed \(\lvert c\rvert<1/4\) the stationary state is entangled for all sufficiently small positive \(p\); for fixed \(\lvert c\rvert>1/4\) it is separable for all sufficiently small positive \(p\). The leading asymptotic alone does not decide either fixed boundary value \(c=\pm1/4\).

More strongly, for each \(\theta_0\) and each fixed \(C>1/4\), when \(p>0\) is sufficiently small the window \(\lvert\theta-\theta_0\rvert\le Cp^2\) has exactly one connected interval of entangled states, with boundary angles

\[
\theta_{\pm}(p)=\theta_0\pm\frac{p^2}{4}+O(p^3).
\]

At either exactly resonant angle, entanglement is present for every \(0<p<1\):

\[
\det\rho_p(\theta_0)^{T_2}=
-\frac{p^2(1-p)^3}{16(2-p)\bigl(1+(1-p)^2\bigr)^2}<0.
\]

The asymptotic entanglement tolerance is therefore *quadratic* in the small reset probability, not linear. These statements concern positivity of the partial transpose (equivalently, two-qubit separability), and do not claim an exact concurrence formula.

## Assumptions and scope

Use the ordered computational basis \((\lvert\uparrow\uparrow\rangle,\lvert\uparrow\downarrow\rangle,\lvert\downarrow\uparrow\rangle,\lvert\downarrow\downarrow\rangle)\), and define

\[
H=\begin{pmatrix}
2-\sqrt2&2-\sqrt2&-\mathrm i-\sqrt2&\mathrm i-\sqrt2\\
2-\sqrt2&2-\sqrt2&\mathrm i-\sqrt2&-\mathrm i-\sqrt2\\
\mathrm i-\sqrt2&-\mathrm i-\sqrt2&2+\sqrt2&2+\sqrt2\\
-\mathrm i-\sqrt2&\mathrm i-\sqrt2&2+\sqrt2&2+\sqrt2
\end{pmatrix}.
\]

Its four distinct eigenvalues are \((-2,0,2,8)\). The stochastic quantum channel is

\[
\rho\longmapsto p\lvert\uparrow\uparrow\rangle\langle\uparrow\uparrow\rvert+(1-p)U(\theta)\rho U(\theta)^\dagger.
\]

The superscript \(T_2\) transposes only the second qubit. The reset is global, instantaneous and independent from step to step; no weak-measurement, thermal noise, or local reset channel is included. The small parameter \(p\) is a Bernoulli probability, not a continuous-time Poisson intensity.

## Proof

**Stationary state and resonant projectors.** The channel is a strict trace-norm contraction on differences of density matrices for \(p>0\), and its stationary state is

\[
\rho_p(\theta)=p\sum_{n=0}^{\infty}(1-p)^n U(\theta)^n\lvert\uparrow\uparrow\rangle\langle\uparrow\uparrow\rvert U(\theta)^{-n}.
\]

Let \(\lambda_a\in\{-2,0,2,8\}\) and let \(P_a\) be the associated spectral projectors. Write \(R=\lvert\uparrow\uparrow\rangle\langle\uparrow\uparrow\rvert\), \(\Delta_{ab}=\lambda_a-\lambda_b\), and

\[
F_{ab}(p,\theta)=\frac{p}{1-(1-p)e^{\mathrm i\theta\Delta_{ab}}}.
\]

Then \(\rho_p(\theta)=\sum_{a,b}F_{ab}(p,\theta)P_a R P_b\). In particular, the spectral projectors are explicitly reconstructible without arbitrary eigenvector phases from

\[
P_a=\prod_{b\ne a}\frac{H-\lambda_b I}{\lambda_a-\lambda_b}.
\]

At each \(\theta_0\in\{\pi/4,3\pi/4\}\), precisely the pair of levels \(0,8\) has a nontrivial coincident gate phase (besides the diagonal pairs). Direct substitution gives the common limiting partial transpose

\[
A_0=\lim_{p\downarrow0}\rho_p(\theta_0)^{T_2}
=\frac18\begin{pmatrix}
3&1&0&0\\1&3&0&0\\0&0&1&-1\\0&0&-1&1
\end{pmatrix}.
\]

Its spectrum is \((1/2,1/4,1/4,0)\), and a normalized vector spanning its kernel is \(z=(0,0,1,1)^T/\sqrt2\).

**Second-order singular perturbation.** Set \(\theta=\theta_0+c p^2\). For a resonant ordered pair with \(e^{\mathrm i\theta_0\Delta_{ab}}=1\), expansion of the geometric-series factor gives, uniformly for bounded \(c\),

\[
F_{ab}=1+\mathrm i\Delta_{ab}c\,p
-\bigl(\Delta_{ab}^{2}c^{2}+\mathrm i\Delta_{ab}c\bigr)p^2+O(p^3).
\]

For a nonresonant pair, putting \(q_{ab}=e^{\mathrm i\theta_0\Delta_{ab}}\ne1\),

\[
F_{ab}=\frac{p}{1-q_{ab}}-\frac{p^2q_{ab}}{(1-q_{ab})^2}+O(p^3).
\]

After partial transpose, these expansions give an analytic Hermitian family \(A=A_0+pA_1(c)+p^2A_2(c)+O(p^3)\). Finite exact matrix multiplication using the displayed polynomial projectors yields

\[
\langle z,A_1z\rangle=0,\qquad
A_1z=\begin{pmatrix}
\mathrm i c\mp\sqrt2/8\\
\mathrm i c\pm\sqrt2/8\\0\\0
\end{pmatrix},\qquad
\langle z,A_2z\rangle=8c^2.
\]

The upper signs correspond to \(\theta_0=\pi/4\); the lower to \(3\pi/4\). On the orthogonal complement of \(z\), \(A_0\) is positive. Let \(A_0^+\) denote its Moore--Penrose inverse. The two first coordinates of \(A_1z\) have components \(\sqrt2\mathrm ic\) and \(\mp1/4\) along eigenvectors with eigenvalues \(1/2\) and \(1/4\), respectively. Consequently

\[
\langle z,A_1A_0^+A_1z\rangle
=\frac{2c^2}{1/2}+\frac{1/16}{1/4}
=4c^2+\frac14.
\]

Second-order perturbation theory for the simple zero eigenvalue, or equivalently its Schur complement against the positive three-dimensional block, now gives

\[
\lambda_{\min}\bigl(\rho_p(\theta_0+cp^2)^{T_2}\bigr)
=p^2\!\left(4c^2-\frac14\right)+O_C(p^3).
\]

All three other eigenvalues remain strictly positive for sufficiently small \(p\), uniformly for bounded \(c\). By the Peres--Horodecki criterion, nonpositive partial transpose is equivalent to entanglement for two qubits. Therefore negativity equals the magnitude of the negative small eigenvalue, when there is one, which proves the limit and its uniformity.

**Local phase boundaries.** Since the family has an analytic extension after the substitution \(\theta=\theta_0+cp^2\), the isolated small eigenvalue divided by \(p^2\) has an analytic extension near \(p=0\), with limiting value \(4c^2-1/4\). Its \(c\)-derivative at the two simple limiting roots \(c=\pm1/4\) is \(\pm2\). The analytic implicit-function theorem gives unique boundary functions \(c_\pm(p)=\pm1/4+O(p)\) in neighborhoods of those roots. Uniform convergence and strict signs away from the roots rule out further boundaries in any fixed bounded \(c\)-window containing both roots. This proves the asserted unique entanglement interval and endpoint asymptotics.

**Exact-on-resonance assertion.** At either \(\theta_0\), the phases \(e^{\mathrm i\theta_0\Delta_{ab}}\) belong to \(\{1,-1,\mathrm i,-\mathrm i\}\), so \(F_{ab}\) is rational in \(p\). Substituting the four polynomial projectors into \(\rho_p^{T_2}\) and calculating its determinant gives the displayed negative expression for every \(0<p<1\). A Hermitian matrix with negative determinant has a negative eigenvalue; hence these states are entangled for every nontrivial resetting probability.

## Verification

The standalone file `checks/resonant_negativity_check.py` reconstructs the spectral projectors from \(H\), verifies their completeness, computes both exact-on-resonance partial-transpose determinants, and checks the second-order perturbation coefficient symbolically for both angles. It also compares finite-parameter spectral evaluations against the asymptotic law and independently iterates the quantum reset channel to its stationary state. Execute with Python 3, SymPy, NumPy and SciPy: `python checks/resonant_negativity_check.py`. The tests finish with explicit PASS messages. The exact algebra displayed in the proof, not finite-precision samples, establishes the asymptotic assertions.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo (arXiv:2410.11497, first submitted 2024-10-15) establish the reset channel, its exact spectral stationary-state formula and resonances, and numerically show concurrence peaks near \(\pi/4\) and \(3\pi/4\). The present theorem takes their *same* two-qubit generator and isolates the previously unstated quadratic detuning scale, its exact \(1/4\) coefficient, the limiting negativity profile, local entanglement endpoints, and the all-positive-reset exact-resonance determinant. It does not claim novelty of the model or of the stationary-state resolvent.

The Peres--Horodecki criterion supplies the established separability characterization used here. Lee, Chan and Wang's 2014 entanglement tongue concerns dissipatively coupled nonlinear quantum oscillators and physical frequency-detuning/coupling thresholds, not Bernoulli resetting of this two-qubit gate. General analytic perturbation and spectral-projector methods are standard; the specific singular balance and evaluated coefficient concern this concrete gate. A prior specialized or more general result implying exactly this boundary-layer law has not been ruled out by an exhaustive publication search.

## Limitations

The statement treats only the specified entangling generator, global pure-state resetting, a stationary channel, and the weak-reset limit near two angles. Its local uniqueness assertion is confined to detunings of order \(p^2\), not all phase angles or all reset strengths. It does not give a global concurrence diagram or noise robustness for alternative gates. The leading law leaves the fixed scaled equality cases \(c=\pm1/4\) undecided without higher-order analysis; it instead determines nearby exact moving boundaries. Finite numerical checks are not proofs of the uniform limit. The reviewed literature does not establish exhaustive publication priority.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (first submitted 2024-10-15), especially Eqs. (7), (10)--(12), (25)--(33), Fig. 4, Appendix A. https://arxiv.org/abs/2410.11497
2. M. Horodecki, P. Horodecki, R. Horodecki, *Separability of Mixed States: Necessary and Sufficient Conditions*, arXiv:quant-ph/9605038 (1996). https://arxiv.org/abs/quant-ph/9605038
3. T. E. Lee, C.-K. Chan, S. Wang, *Entanglement tongue and quantum synchronization of disordered oscillators*, arXiv:1312.3630 (2014). https://arxiv.org/abs/1312.3630
