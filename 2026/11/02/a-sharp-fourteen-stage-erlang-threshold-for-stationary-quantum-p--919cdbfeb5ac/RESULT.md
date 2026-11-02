# A sharp fourteen-stage Erlang threshold for stationary quantum purity–fidelity reversal

## Finding

For finite-dimensional, closed quantum systems repeatedly reset to the same pure state at independently sampled Erlang waiting times, the integer Erlang shape has a sharp threshold governing the order between stationary purity and fidelity to the reset state.

**Theorem.** Fix a finite-dimensional Hermitian Hamiltonian \(H\), a normalized vector \(|\psi\rangle\), a rate \(\lambda>0\), and an integer Erlang shape \(k\geq1\). Let the waiting times between complete resets to \(|\psi\rangle\) be independent \(\operatorname{Gamma}(k,\lambda)\) variables, where \(\lambda\) is the *rate*, not the mean reset frequency. Write \(\rho_k\) for the equilibrium-renewal stationary averaged state and

\[
P_k=\operatorname{Tr}(\rho_k^2),\qquad F_k=\langle\psi|\rho_k|\psi\rangle.
\]

Then:

1. For \(k=1\), \(P_1=F_1\) for every \(H\), \(|\psi\rangle\), and \(\lambda\).
2. For every integer \(2\leq k\leq13\), \(P_k\geq F_k\) for every such system, and equality occurs precisely when \(|\psi\rangle\) lies in one eigenspace of \(H\). In every other case \(P_k>F_k\).
3. For **every integer \(k\geq14\)** there exists a balanced qubit superposition and a positive energy gap with \(F_k>P_k\). For the same shape, sufficiently small or sufficiently large nonzero gaps give \(P_k>F_k\); hence as the qubit energy gap varies there are at least two distinct order reversals.
4. At the threshold shape \(k=14\), the ordering reverses **exactly twice** as the dimensionless qubit gap \(x>0\) increases. The open interval where \(F_{14}>P_{14}\) has squared-gap endpoints \(y_-\approx0.291690295932021\) and \(y_+\approx0.356312958818599\). An exact witness is \(x=1/\sqrt3\).

The theorem compares the stationary *unconditioned state* to its pure reset state. It does not assert such orderings for arbitrary mixed resetting states, arbitrary renewal laws, or finite observation times.

## Assumptions and scope

Fix units with \(\hbar=1\). Let \(H=\sum_j E_j|j\rangle\langle j|\) on a finite-dimensional Hilbert space; repeated eigenvalues are permitted. Expand \(|\psi\rangle=\sum_j a_j|j\rangle\) and set \(w_j=|a_j|^2\), so \(\sum_j w_j=1\). Between resets the state evolves unitarily under \(U(t)=e^{-iHt}\), while each renewal event instantaneously and completely restores \(|\psi\rangle\langle\psi|\), independently of the past. The process is sampled in its equilibrium-renewal regime (not immediately after a renewal). Erlang interarrival density is \(\lambda^k t^{k-1}e^{-\lambda t}/(k-1)!\), with mean \(k/\lambda\).

The stationary *age* \(T\) since the last reset has density

\[
f_k(t)=\frac{\lambda}{k}e^{-\lambda t}\sum_{j=0}^{k-1}\frac{(\lambda t)^j}{j!},\qquad t\geq0.
\]

Consequently \(\rho_k=\mathbb E[U(T)|\psi\rangle\langle\psi|U(T)^\dagger]\). For the energy-gap ratio \(x=|E_j-E_\ell|/\lambda\), let

\[
\phi_k(x)=\mathbb E e^{ix\lambda T}
=\frac1k\sum_{j=1}^{k}(1-ix)^{-j}
=\frac{i}{kx}\left[1-(1-ix)^{-k}\right]
\]

for \(x\ne0\), continuously extended by \(\phi_k(0)=1\). Define the scalar difference

\[
D_k(x)=\operatorname{Re}\phi_k(x)-|\phi_k(x)|^2.
\]

By spectral expansion (and the reality and evenness of \(D_k\)),

\[
F_k-P_k=\sum_{j,\ell}w_jw_\ell D_k\!\left(\frac{|E_j-E_\ell|}{\lambda}\right).
\]

For a balanced qubit supported equally on two distinct energy eigenstates,

\[
F_k=\frac{1+\operatorname{Re}\phi_k(x)}2,\qquad
P_k=\frac{1+|\phi_k(x)|^2}2,\qquad F_k-P_k=\frac{D_k(x)}2.
\]

## Proof

**1. Equilibrium age and spectral reduction.** An Erlang renewal has finite positive mean and a nonlattice interarrival distribution. The renewal-age theorem gives stationary age density \(f_k(t)=\mathbb P(W>t)/\mathbb E W\). Here the survival function of \(W\sim\operatorname{Gamma}(k,\lambda)\) is \(e^{-\lambda t}\sum_{j=0}^{k-1}(\lambda t)^j/j!\), yielding the displayed density. Integrating its finite Erlang mixture yields the displayed characteristic function. In the energy basis the stationary density has entries \((\rho_k)_{j\ell}=a_j\overline{a_\ell}\phi_k((E_\ell-E_j)/\lambda)\). Thus

\[
P_k=\sum_{j,\ell}w_jw_\ell|\phi_k(x_{j\ell})|^2,\qquad
F_k=\sum_{j,\ell}w_jw_\ell\operatorname{Re}\phi_k(x_{j\ell}),
\]

where \(x_{j\ell}=|E_j-E_\ell|/\lambda\), proving the reduction. For \(k=1\), \(\phi_1(x)=(1-ix)^{-1}\), so \(\operatorname{Re}\phi_1=|\phi_1|^2\) identically.

**2. Exact polynomial sign reduction.** For integers \(k\geq2\) set \(y=x^2>0\), and let \(B_k(x)=(1+ix)^k\). Substituting the closed expression for \(\phi_k\) gives

\[
D_k(x)=\frac{N_k(y)}{k^2y(1+y)^k},\quad
N_k(y)=kx\operatorname{Im}B_k(x)-(1+y)^k+2\operatorname{Re}B_k(x)-1.
\]

The constant and linear terms of \(N_k\) cancel, so \(N_k(y)=y^2Q_k(y)\), where

\[
Q_k(y)=\sum_{j=2}^{k}c_{k,j}y^{j-2},\qquad
c_{k,j}=-\binom kj+2(-1)^j\binom k{2j}+k(-1)^{j-1}\binom k{2j-1}.
\]

Binomial coefficients with lower index outside \([0,k]\) are zero. In particular

\[
c_{k,2}=-\frac{k^2(k^2-1)}{12}<0,\qquad c_{k,k}=-1.
\]

For each of the twelve integers \(k=2,3,\ldots,13\), the exact rational Sturm calculation in `verify.py` establishes that \(Q_k\) has **zero positive real roots**. Since its constant coefficient is strictly negative, continuity makes \(Q_k(y)<0\) for every \(y>0\). Therefore \(D_k(x)<0\) for all \(x>0\). The spectral sum implies \(F_k\leq P_k\), with strict inequality whenever the reset vector has positive amplitudes in eigenspaces with two different eigenvalues. This proves part 2 including the equality case.

For \(k=14\) the exact signed Sturm sequence for \(Q_{14}\) has \(5\) sign variations at \(0^+\) and \(3\) at \(+\infty\), giving exactly **two distinct positive real zeros**. Exact rational substitution shows

\[
Q_{14}(291/1000)<0<Q_{14}(292/1000),\qquad
Q_{14}(356/1000)>0>Q_{14}(357/1000).
\]

Both roots therefore lie in these disjoint rational brackets; since \(Q_{14}(0)<0\) and there are only two positive zeros, its sign is positive precisely between them. This proves the exact two-crossing statement, with the reported decimal approximations given only for orientation.

**3. Uniform analytic witness for every integer \(k\geq14\).** Put \(\theta=7\pi/3\), \(x_k=\tan(\theta/k)>0\), and \(q_k=\cos^k(\theta/k)\). Note \(0<\theta/k\leq\pi/6\). Then \((1-ix_k)^{-k}=q_ke^{i\theta}\), and direct substitution gives

\[
k^2x_k^2D_k(x_k)=\frac{\sqrt3}{2}k\tan(\theta/k)q_k+q_k-1-q_k^2=:M_k.
\]

At \(k=14\), \(x_{14}=1/\sqrt3\), \(q_{14}=(3/4)^7\), and

\[
M_{14}=8q_{14}-1-q_{14}^2=\frac{13436039}{268435456}>0.
\]

For real \(k\geq15\), the function \(q(k)=\cos^k(\theta/k)\) is strictly increasing: with \(u=\theta/k\), its logarithmic derivative is \(\log\cos u+u\tan u>0\), because the latter expression is zero at \(u=0\) and has derivative \(u\sec^2u>0\). Also \(u_{15}=7\pi/45<22/45<1/2\). On \([0,1/2]\), the alternating Taylor expansion implies \(\cos u\geq1-u^2/2+u^4/25\); the polynomial on the right is decreasing there. Exact integer/rational arithmetic in `verify.py` verifies

\[
q_k\geq q_{15}\geq
\left(1-\frac{(22/45)^2}{2}+\frac{(22/45)^4}{25}\right)^{15}>\frac3{20}.
\]

Using \(\tan u>u\), \(\sqrt3>5/3\), and \(\pi>3\), we obtain for all \(k\geq15\)

\[
M_k>\frac{41}{6}q_k-1-q_k^2
\geq\frac{41}{6}\frac3{20}-1-\left(\frac3{20}\right)^2
=\frac1{400}>0.
\]

The second inequality uses that the quadratic \(41q/6-1-q^2\) is increasing for \(3/20\leq q\leq1\). Thus \(D_k(x_k)>0\) for **every** integer \(k\geq14\), which yields a balanced-qubit witness with \(F_k>P_k\).

**4. Strict opposite signs at both gap extremes.** The first two moments of the dimensionless equilibrium age are \(\mathbb E(\lambda T)=(k+1)/2\) and \(\mathbb E[(\lambda T)^2]=(k+1)(k+2)/3\). Expanding the characteristic function gives

\[
D_k(x)=-\frac{k^2-1}{12}x^2+O_k(x^4)\qquad(x\downarrow0).
\]

For fixed \(k\geq2\), the closed characteristic function gives \(D_k(x)=-1/(k^2x^2)+o_k(x^{-2})\) as \(x\to\infty\). Both are strictly negative near their respective limits. Because \(D_k\) is continuous and positive at \(x_k\), each \(k\geq14\) has at least two crossing points. All four statements follow.

## Verification

The attached `verify.py` is a standalone Python-3 standard-library checker using exact `fractions.Fraction` arithmetic. It constructs every \(Q_k\), computes signed rational polynomial remainders for Sturm variations at \(0^+\) and \(+\infty\), verifies the twelve root exclusions and shape-14 two-root count, checks the shape-14 rational brackets and witness, verifies the universal rational Taylor bound, and separately checks the rational characteristic-transform and polynomial formulas for 24 parameter combinations. **92 exact assertions passed.** The finite Sturm computations are exhaustive for the specifically bounded shapes \(2\leq k\leq14\); the all-\(k\geq14\) claim relies on the analytic witness above, not extrapolation from those computations. Direct numerical stationary-age quadrature for representative qubits independently corroborated both signs, but is not used as proof.

Reproduce with `python3 verify.py`. Every required input is either in the present proof or generated inside that single script; no downloaded databases, external binaries, or additional file paths are needed.

## Relationship to prior work

Sevilla and Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting* (first arXiv appearance September 12, 2022), already derive the **general renewal-state formula**, treat gamma waiting laws, and provide stationary purity and fidelity expressions (their Sections 2.1, 3.1–3.3, equations (13), (34), (42), (47), and qubit equation (49)). Those results supply an implicit route to calculating the present scalar functions; the new claim is **not** the stationary density formula or the purity/fidelity expansion. The increment is the sharp, all-finite-dimensional ordering for exactly shapes \(1\) through \(13\), its first failure at \(14\), a rigorous all-higher-shape witness, and the exact two-crossing classification at the boundary shape. The checked source does not explicitly state those sharp sign and threshold conclusions.

Kulkarni and Majumdar, *Generating Entanglement by Quantum Resetting* (first arXiv appearance July 14, 2023), explicitly note equality of stationary purity and reset-state fidelity in their Poisson-reset two-spin example (Section III.2). The \(k=1\) portion here explains that equality for arbitrary finite-dimensional Hamiltonians and pure reset states; the novel threshold is for non-Poisson renewal clocks. Wald et al., *Stochastic resetting in discrete-time quantum dynamics* (first arXiv appearance October 15, 2024), study a different **discrete-time** reset protocol and do not directly imply this continuous-time Erlang integer threshold.

## Limitations

The classification assumes complete resetting to the *same pure state*, a finite-dimensional unitary between-renewal dynamics, equilibrium-renewal sampling, and Erlang waiting times with integer shape. For shapes at least \(15\), existence of a reversal interval is proved but neither the number nor uniqueness of all positive intervals is classified. The theorem does not address finite-time ensembles, mixed initial reset states, general waiting-time distributions, or operational quantum metrology. Earlier generic renewal formulas already imply the ingredients of the reduction, so novelty is specifically attributed to the evaluated sharp threshold and its global proof; independently exhaustive publication-priority certification has not been performed.

## References

1. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643, initial version September 12, 2022. https://arxiv.org/abs/2209.05643
2. M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, initial version July 14, 2023. https://arxiv.org/abs/2307.07485
3. S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, initial version October 15, 2024. https://arxiv.org/abs/2410.11497
