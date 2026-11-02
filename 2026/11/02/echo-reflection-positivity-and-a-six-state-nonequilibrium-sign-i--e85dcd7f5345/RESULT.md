# Echo reflection positivity and a six-state nonequilibrium sign inversion

## Finding

A stationary finite-state classical Markov environment that obeys detailed balance has **strictly positive, real** pure-dephasing coherence after any time-antisymmetric spin-echo modulation. Detailed balance is essential for this universal conclusion: an explicitly specified stationary, irreducible, six-state *directed* clock has a strictly **negative real** Hahn echo, even with zero mean coupling and no initial-state bias. The negative value is established by an exact rational polynomial certificate with a rigorous matrix-exponential remainder bound, not by numerical sign sampling.

## Assumptions and scope

Let \(X_t\) be a stationary continuous-time Markov chain with finite state space \(S\), irreducible row-generator \(Q\), and strictly positive invariant distribution \(\pi\). Let \(v:S\to\mathbb R\) be a bounded real frequency shift. For \(\tau>0\), and bounded measurable real \(f:[0,2\tau]\to\mathbb R\) such that \(f(2\tau-t)=-f(t)\) almost everywhere, define the phase-sensitive echo
\[
E_f=\mathbb E_\pi\exp\left(i\int_0^{2\tau}f(t)v(X_t)\,dt\right).
\]
The conventional Hahn echo uses \(f(t)=1\) in the first half and \(f(t)=-1\) in the second half. The measured complex coherence is \(E_f\), *not* its nonnegative modulus. A constant addition to \(v\) has no effect because the modulation has zero integral.

For the counterexample take \(S=\{0,1,2,3,4,5\}\), with transitions \(j\to j+1\pmod 6\) at rate \(6\), no other jumps, and \(\pi_j=1/6\). Put
\[
(v_0,v_1,v_2,v_3,v_4,v_5)=(0,8,8,0,-8,-8),\qquad\tau=3/8.
\]
This irreducible clock has positive stationary circulation and fails detailed balance; its stationary mean frequency is zero.

## Proof

**1. Reversible positivity.** Suppose \(Q\) satisfies detailed balance: \(\pi_jQ_{jk}=\pi_kQ_{kj}\) for all \(j,k\). Condition on the midpoint \(X_\tau=j\). By the Markov property the two path halves are independent under this condition. Detailed balance identifies the conditional law of the *backward* half, viewed outward from the midpoint, with the law of the forward half started at \(j\). The antisymmetry of \(f\) makes the two conditional complex phase expectations conjugate. Consequently
\[
E_f=\sum_{j\in S}\pi_j|h_j|^2,
\]
where \(h_j\) is the conditional expectation of the forward-half phase factor starting at \(j\) with the reflected waveform. Thus \(E_f\ge0\) and is real. To rule out zero, note that \(h\) is the image of the nonzero constant vector \(\boldsymbol1\) under the finite-dimensional Feynman--Kac propagator of the time-dependent matrices \(Q+i\,\mathrm{diag}(f(t)v)\). This propagator is invertible: its determinant solves a scalar nonzero exponential ODE (or follows by solving the linear ODE backward). Hence \(h\ne0\), and positivity is strict because every \(\pi_j>0\).

**2. The nonequilibrium clock.** Let \(P\) be the cyclic shift \((Px)_j=x_{j+1\pmod 6}\) and \(V=\mathrm{diag}(0,8,8,0,-8,-8)\). Its generator is \(Q=6(P-I)\). Feynman--Kac conditioning for the two Hahn halves gives the exact expression
\[
E_{\mathrm H}=\frac16\boldsymbol1^{\mathsf T}
 e^{\tau(Q+iV)}e^{\tau(Q-iV)}\boldsymbol1.
\]
The three-step shift \(P^3\) commutes with \(Q\) and conjugates \(V\) to \(-V\). Since it preserves the uniform initial law and \(\boldsymbol1\), the echo is unchanged by \(V\mapsto-V\). Complex conjugation has exactly that effect, so \(E_{\mathrm H}\) is real.

**3. Exact negative certificate.** Define \(B=\tau(Q+iV)\) and \(\overline B=\tau(Q-iV)\), and \(p_{40}(Z)=\sum_{k=0}^{40}Z^k/k!\). All entries of \(B\), and both components of the complex entries of \(p_{40}(B)\), are rational. The standalone `proof_checker.py` evaluates, using exact `fractions.Fraction` arithmetic,
\[
E_{40}=\frac16\boldsymbol1^{\mathsf T}p_{40}(B)p_{40}(\overline B)\boldsymbol1,
\]
and establishes **exactly** \(\operatorname{Im}E_{40}=0\) and \(\operatorname{Re}E_{40}<-1/10\). As each row of \(B\) has total absolute entry sum at most \(15/2<8\), the matrix infinity-norm satisfies \(\|B\|_\infty<8\). The Taylor remainder of either exponential is at most
\[
R=3^8\frac{8^{41}}{41!},
\]
because \(e^8<3^8\). Moreover \(\|p_{40}(B)\|_\infty\le3^8\), so
\[
|E_{\mathrm H}-E_{40}|\le 2\,3^8R+R^2<10^{-4}.
\]
Thus \(E_{\mathrm H}<-1/10+10^{-4}<0\) rigorously. Direct matrix exponentiation, used only as a supplementary check, gives \(E_{\mathrm H}\approx-0.11467096450199\). The strict sign persists for all sufficiently small changes in model parameters (for the real part), by continuity.

## Verification

Run `python3 proof_checker.py` using Python's standard library. The script constructs the six-state Taylor products without floating-point arithmetic, verifies the exact rational imaginary cancellation, and proves the strict rational sign and remainder inequalities. A separate floating-point matrix-exponential comparison is optional and not part of the proof. The algebraic argument establishes the result for *every* stationary irreducible reversible finite-state generator and all bounded real antisymmetric modulations, not merely the tested example.

## Relationship to prior work

Hahn's original echo provides the refocusing protocol. Galperin--Altshuler--Shantsev (arXiv:cond-mat/0312490) develops the echo phase-memory functional and explicitly treats two-state telegraph fluctuators; the later Galperin--Altshuler--Bergli--Shantsev study (arXiv:cond-mat/0511238) gives single-fluctuator echo formulas and plateau effects. Lo Franco and coauthors (arXiv:1408.6885) study echo coherence and entanglement under bistable fluctuators. Their full-text formulations concern equilibrium two-state fluctuators or their independent combinations, rather than a single nonreversible cyclic Markov environment. The norm-square argument uses standard detailed-balance and Markov/Feynman--Kac principles; originality is **not** claimed for those separate tools. The assessed contribution is the sign distinction with a finite, exactly certified, real-valued negative echo under stationary irreversible noise.

## Limitations

A negative *phase-sensitive* echo is not a negative echo **magnitude**, probability, fidelity, or concurrence. The statement does not assert that every irreversible bath yields a negative echo, that six states are minimal, or that a negative signal alone uniquely diagnoses irreversibility outside the stated classical stationary pure-dephasing model. The construction uses a unidirectional six-state clock, ideal instantaneous inversion, and no qubit energy relaxation or back-action. The result concerns a static generator and exact ensemble coherence; experimentally resolving its sign requires a phase reference. Historical priority of the full sign distinction is not independently certified.

## References

- E. L. Hahn, *Spin Echoes*, Physical Review **80**, 580 (1950), https://doi.org/10.1103/PhysRev.80.580 .
- Y. M. Galperin, B. L. Altshuler, and D. V. Shantsev, *Low-frequency noise as a source of dephasing of a qubit*, publicly posted 18 December 2003, https://arxiv.org/abs/cond-mat/0312490 .
- Y. M. Galperin, B. L. Altshuler, J. Bergli, and D. V. Shantsev, *Non-Gaussian low-frequency noise as a source of qubit decoherence*, posted 9 November 2005, https://arxiv.org/abs/cond-mat/0511238 .
- R. Lo Franco et al., *Spin-echo entanglement protection from random telegraph noise*, posted 28 August 2014, https://arxiv.org/abs/1408.6885 .
