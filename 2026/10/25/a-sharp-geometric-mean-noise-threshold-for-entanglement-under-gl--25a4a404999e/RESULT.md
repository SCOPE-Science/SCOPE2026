# A sharp geometric-mean noise threshold for entanglement under global quantum resetting

## Finding

For two coupled qubits undergoing independent local bit-flip noise and Poissonian global resets to a fixed product state, the steady-state entanglement phase diagram has an exact threshold controlled by the **geometric mean of the two noise rates**, rather than their sum. There is **no steady-state entanglement at any positive reset rate** when the interaction strength is at most that geometric mean. Above it, there is **exactly one positive reset-rate transition** from separable to entangled stationary states.

Precisely, fix \(J>0\), \(a>0\), \(b>0\), and reset rate \(r>0\). Let \(s=a+b\) and define

\[
\begin{aligned}
P(r)={}&(ab-J^2)r^4+4s(ab-J^2)r^3\\
&+2s^2(3ab-J^2)r^2+4s^3(ab+J^2)r\\
&+4s^2(a^2+J^2)(b^2+J^2).
\end{aligned}
\]

The unique stationary two-qubit state is entangled if and only if \(P(r)<0\). If \(J^2\le ab\), this never occurs. If \(J^2>ab\), \(P\) has exactly one positive zero \(r_c\), and entanglement occurs **exactly when** \(r>r_c\). On that branch,

\[
C(r)=\frac{2(J-\sqrt{ab})}{r}+O(r^{-2})\quad(r\to\infty),
\]

where \(C\) is the two-qubit Wootters concurrence. In particular, strong global resetting does not produce a second *finite-rate* disentanglement transition, although the concurrence tends to zero asymptotically.

## Assumptions and scope

Use units with \(\hbar=1\). The system has Hilbert space \(\mathbb C^2\otimes\mathbb C^2\), computational basis \(|00\rangle,|01\rangle,|10\rangle,|11\rangle\), Hamiltonian \(H=JX_1X_2\), and bit-flip Lindblad dynamics

\[
\mathcal L(\rho)=-i[H,\rho]+a(X_1\rho X_1-\rho)+b(X_2\rho X_2-\rho),
\]

where \(X_1=\sigma_x\otimes I\), \(X_2=I\otimes\sigma_x\). Independent Poisson reset events replace the complete two-qubit density operator by \(\rho_0=|00\rangle\langle00|\), independently of previous states, at total rate \(r\). The full master equation is

\[
\dot\rho=\mathcal L(\rho)+r(\rho_0-\rho).
\]

All inequalities in the theorem concern the unique *unconditional stationary density matrix*; they do not assert entanglement along each quantum trajectory. The two local noise rates may differ arbitrarily. The assumptions exclude correlated flips, other Hamiltonian terms, partial resets, and zero noise rates.

## Proof

**1. Exact stationary density matrix.** The no-reset superoperators commute because \(X_1\), \(X_2\), and \(H=JX_1X_2\) are mutually commuting Hermitian operators. The renewal-resolvent formula is

\[
\rho_*(r)=r\int_0^\infty e^{-rt}e^{t\mathcal L}(\rho_0)\,dt.
\]

It is the unique stationary solution because \(r-\mathcal L\) is invertible on the finite-dimensional matrix space for \(r>0\). Introduce

\[
\begin{gathered}
A=\frac r{r+2a+2b},\qquad d_a=(r+2a)^2+4J^2,\qquad d_b=(r+2b)^2+4J^2,\\
B_a=\frac{r(r+2a)}{d_a},\qquad B_b=\frac{r(r+2b)}{d_b},\qquad
S_a=\frac{2Jr}{d_a},\qquad S_b=\frac{2Jr}{d_b}.
\end{gathered}
\]

Direct evaluation of the exponentially weighted no-reset orbit gives the following \(X\)-state, with all unspecified entries zero and Hermitian conjugates understood:

\[
\begin{array}{ll}
(\rho_*)_{00,00}=(1+A+B_a+B_b)/4,&
(\rho_*)_{11,11}=(1+A-B_a-B_b)/4,\\
(\rho_*)_{01,01}=(1-A+B_a-B_b)/4,&
(\rho_*)_{10,10}=(1-A-B_a+B_b)/4,\\
(\rho_*)_{00,11}=i(S_a+S_b)/4,&
(\rho_*)_{01,10}=i(S_a-S_b)/4.
\end{array}
\]

Normalization is manifest from the four diagonal elements. Positivity follows directly from the convex resolvent integral.

**2. The potentially competing partial-transpose branch is impossible.** For a two-qubit \(X\)-state, entanglement is equivalent to one of the inequalities

\[
|\rho_{00,11}|^2>\rho_{01,01}\rho_{10,10},\qquad
|\rho_{01,10}|^2>\rho_{00,00}\rho_{11,11}.
\]

Before resetting, write \(u=e^{-2at}\), \(v=e^{-2bt}\). Directly from the commuting evolution,

\[
16\bigl(\rho_{00,00}(t)\rho_{11,11}(t)-|\rho_{01,10}(t)|^2\bigr)
=(1-u^2)(1-v^2)+4uv\sin^2(2Jt)\ge0.
\]

Hence \(|\rho_{01,10}(t)|\le\sqrt{\rho_{00,00}(t)\rho_{11,11}(t)}\) at every time. Averaging with the positive exponential reset-age density and applying Cauchy–Schwarz preserves the inequality, so only the first partial-transpose branch can contribute.

**3. Exact polynomial sign.** Substitution yields the algebraic identity

\[
|\rho_{00,11}|^2-\rho_{01,01}\rho_{10,10}
=-\frac{P(r)}{(r+2a+2b)^2d_a d_b}.
\]

The denominator is strictly positive. When \(J^2\le ab\), all coefficients of \(P\) are nonnegative and the constant term is positive; therefore \(P(r)>0\) for all \(r>0\). When \(J^2>ab\), the leading and cubic coefficients are negative, the linear and constant coefficients positive, and the quadratic coefficient may have either sign. In descending order the nonzero coefficient sequence therefore has exactly one sign variation. Descartes' rule of signs gives at most one positive root. Since \(P(0)>0\) and \(P(r)\to-\infty\) as \(r\to\infty\), the intermediate-value theorem supplies a positive root; uniqueness and the asserted sign arrangement follow. At equality \(P(r)=0\), the state has zero concurrence and is separable.

**4. Strong resetting and the noise-product condition.** As \(r\to\infty\), the off-diagonal relevant to entanglement obeys \(\rho_{00,11}=iJ/r+O(r^{-2})\), while \(\rho_{01,01}=b/r+O(r^{-2})\) and \(\rho_{10,10}=a/r+O(r^{-2})\). The standard two-qubit \(X\)-state concurrence formula therefore gives

\[
C(r)=2\max\{0,|\rho_{00,11}|-\sqrt{\rho_{01,01}\rho_{10,10}}\}
=\frac{2(J-\sqrt{ab})}{r}+O(r^{-2})
\]

in the regime \(J^2>ab\).

**5. Symmetric-rate check.** When \(a=b=\gamma\in(0,J)\), solving the reduced quadratic yields the explicit critical reset rate

\[
r_c=2\left(\sqrt{\frac{\gamma J(\gamma+J)}{J-\gamma}}-\gamma\right).
\]

This is a specialization of the unique general positive root, not a separate phase.

## Verification

The standalone `checker.py` uses independent exact symbolic algebra and finite-dimensional Liouvillian calculations. It checks the quartic identity by symbolic cancellation, solves the full complex \(16\times16\) stationary linear system independently for 350 randomly sampled parameter sets, verifies positive-semidefiniteness and trace normalization, compares the analytic \(X\)-state concurrence against direct Wootters eigenvalue concurrence, tests the single-positive-root criterion in another 250 parameter sets, and checks the symmetric and strongly asymmetric regimes. Running `python checker.py` with NumPy and SymPy produced `PASS 3646 algebraic and finite-dimensional checks`. The theorem for *all* positive parameters relies on the exact identities and sign proof above, not finite sampling.

## Relationship to prior work

Kulkarni and Majumdar, *Generating Entanglement by Quantum Resetting* (2023), establish reset-generated concurrence for an **isolated**, coherently evolving pair of interacting spins; their published two-spin application does not include the independent local bit-flip dissipators used here. Hartmann, Dür, and Briegel (2005–2007) earlier established noise-resistant steady-state entanglement using **single-qubit local resets**, and already described a qualitative onset threshold and nonzero entanglement at arbitrarily large finite local reset rates for pure reset states. Their reset generator acts independently on each particle, not by replacing the entire correlated pair with a fixed \(|00\rangle\) state at one Poisson clock; their statements therefore do not supply the present geometric-mean independent-bit-flip threshold or quartic global-reset criterion. The qualitative existence of reset-stabilized entanglement and the no-finite-upper-transition mechanism are antecedents, not claimed in isolation as new. The stationary-reset resolvent is also established method, not a novelty claim. Magoni, Carollo, Perfetto, and Lesanovsky (2022) study reset-generated correlations in **noninteracting** coherently driven spin systems, a different mechanism. Sevilla and Valdés-Hernández (2022) develop renewal treatments of closed quantum resetting. Shea and Romito (2024) investigate local noise with **continuous local monitoring** rather than global Poisson reset, so their studied entanglement dynamics do not directly provide the present exact noise-product phase criterion. Riera-Campeny, Ollé, and Masó-Puigdellosas (2020) derive renewal return and switching times for measurement-outcome resets of open systems. Perfetto, Carollo, and Lesanovsky (2021) supply open-system resetting and quantum-jump renewal methodology for two- and three-level atoms; the open resetting framework itself is not claimed as new. The quantitative \(J^2=ab\) boundary and single finite critical resetting rate are the claimed additions.

## Limitations

The threshold is a statement about a two-qubit unconditional stationary state for a specified generator and full-product-state global resetting. It does not establish robustness under additional local fields, correlated jump operators, finite-time observation, imperfect resets, or many-body extensions. The derivation does not determine the reset rate maximizing concurrence. A general existing quantum-channel entanglement criterion might offer an equivalent formulation; independent priority assessment has not been performed.

## References

1. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, first posted 2023-07-14, https://arxiv.org/abs/2307.07485.
2. L. Hartmann, W. Dür, and H.-J. Briegel, *Steady state entanglement in open and noisy quantum systems at high temperature*, arXiv:quant-ph/0512219 (2005), https://arxiv.org/abs/quant-ph/0512219.
3. L. Hartmann, W. Dür, and H.-J. Briegel, *Entanglement and its dynamics in open, dissipative systems*, arXiv:quant-ph/0703138 (2007), https://arxiv.org/abs/quant-ph/0703138.
4. M. Magoni, F. Carollo, G. Perfetto, and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655, https://arxiv.org/abs/2202.12655.
5. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643, https://arxiv.org/abs/2209.05643.
6. D. Shea and A. Romito, *Stochastic action for the entanglement of a noisy monitored two-qubit system*, arXiv:2403.08422, https://arxiv.org/abs/2403.08422.
8. A. Riera-Campeny, J. Ollé, and A. Masó-Puigdellosas, *Measurement-induced resetting in open quantum systems*, arXiv:2011.04403 (2020), https://arxiv.org/abs/2011.04403.
9. G. Perfetto, F. Carollo, and I. Lesanovsky, *Thermodynamics of quantum-jump trajectories of open quantum systems subject to stochastic resetting*, arXiv:2112.05078 (2021), https://arxiv.org/abs/2112.05078.
10. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, https://arxiv.org/abs/2410.11497.
