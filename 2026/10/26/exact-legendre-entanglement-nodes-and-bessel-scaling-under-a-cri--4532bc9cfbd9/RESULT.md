# Exact Legendre entanglement nodes and Bessel scaling under a critical discrete reset clock

## Finding

A memory-dependent reset process can destroy the entanglement of an ensemble of two-qubit trajectories at **exactly** computable gate phases, even though every trajectory remains maximally entangled. Consider a Bell-state reset and a local phase gate with a probability of reset after \(n\) consecutive gate applications equal to \(r_n=1/[2(n+1)]\). At integer horizon \(t\geq0\), the concurrence of the unconditioned state is exactly

\[
\mathcal C_t(\theta)=\left|P_t\!\left(\cos\frac{\theta}{2}\right)\right|,
\qquad \theta\in[0,2\pi],
\]

where \(P_t\) denotes the degree-\(t\) Legendre polynomial. For every integer \(t\geq1\), the set of strictly interior phases for which the unconditioned state is separable consists of **exactly \(t\) distinct points**. They are precisely

\[
\theta_{t,j}=2\arccos(x_{t,j}),\qquad
P_t(x_{t,j})=0,\quad -1<x_{t,j}<1,
\]

with the \(t\) simple Legendre roots \(x_{t,j}\); their order is reversed when the phases are listed increasingly. Every node is simple for the signed coherence and is a linear cusp for concurrence. There is no positive-width interval of exactly zero concurrence.

For each fixed \(s\in\mathbb R\), the vanishing-phase limit obeys

\[
\lim_{t\to\infty}\mathcal C_t(s/t)=\left|J_0(s/2)\right|,
\]

with \(J_0\) the order-zero Bessel function of the first kind. Writing \(\theta_{t,(k)}\) for the \(k\)-th smallest positive concurrence-zero phase, for every fixed integer \(k\geq1\),

\[
\lim_{t\to\infty}t\,\theta_{t,(k)}=2j_{0,k},
\]

where \(j_{0,k}\) is the \(k\)-th positive zero of \(J_0\). In contrast, at any fixed \(0<\theta<2\pi\), concurrence approaches zero only algebraically. Specifically, with \(\varphi=\theta/2\),

\[
\mathcal C_t(\theta)=\left|\sqrt{\frac{2}{\pi(t+1/2)\sin\varphi}}\,
\cos\left((t+1/2)\varphi-\pi/4\right)+O_\theta(t^{-3/2})\right|.
\]

The last expression is an oscillatory asymptotic, **not** a positive lower bound for every time.

## Assumptions and scope

All Hilbert spaces are over \(\mathbb C\). Begin at integer time \(t=0\) in the normalized Bell state \(\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2\). At every next time step, let the age \(n\) be the count of consecutive gate applications since the last reset. Independently sample an age-dependent Bernoulli action: with probability \(r_n=1/[2(n+1)]\), reset both qubits to \(\lvert\Phi^+\rangle\) and set age to zero; otherwise apply the two-qubit unitary \(U_\theta=I\otimes\operatorname{diag}(1,e^{i\theta})\) and increase the age by one. Each reset action counts as one discrete step; no gate is applied on that step. The phase \(\theta\) is real and is identified modulo \(2\pi\). The state \(\rho_t(\theta)\) is averaged over unobserved reset trajectories. The result concerns this **full-state** Bell-reset protocol, not local single-qubit resets, monitored/postselected concurrence, arbitrary initial states, or a Markovian constant reset probability.

## Proof

**1. Exact renewal-age distribution.** It is instructive first to allow \(r_n=\gamma/(n+1)\), where \(0<\gamma<1\). Write \((a)_n=a(a+1)\cdots(a+n-1)\) for the rising factorial, and \((a)_0=1\). The probability of avoiding a reset for \(n\) steps after a reset equals

\[
S_n=\prod_{j=0}^{n-1}(1-r_j)=\frac{(1-\gamma)_n}{n!}.
\]

If \(f_k=S_{k-1}-S_k\) is the law of the first reset time \(k\geq1\), its ordinary generating function is

\[
F(z)=\sum_{k\geq1}f_kz^k=1-(1-z)^\gamma,
\qquad |z|<1.
\]

The renewal mass at step \(m\), counting the initial instant as a renewal, has generating function \(1/[1-F(z)]=(1-z)^{-\gamma}\), so the exact renewal mass is \(u_m=(\gamma)_m/m!\). Since age \(A_t=n\) occurs exactly when the last renewal was at \(t-n\) and no reset followed, for every integer \(t\geq0\) and \(0\leq n\leq t\),

\[
\Pr(A_t=n)=S_nu_{t-n}=
\frac{(1-\gamma)_n}{n!}\frac{(\gamma)_{t-n}}{(t-n)!}.
\]

This is precisely the beta-binomial law \(\operatorname{BetaBinomial}(t,1-\gamma,\gamma)\), a consequence of the established renewal formalism. For the **symmetric marginal clock** \(\gamma=1/2\), it reduces to

\[
w_{t,n}:=\Pr(A_t=n)=
\frac{\binom{2n}{n}\binom{2(t-n)}{t-n}}{4^t}.
\]

The generalized binomial theorem gives \(\sum_{n=0}^t w_{t,n}=1\). The special choice \(\gamma=1/2\) balances the two beta-binomial shape parameters and makes the law invariant under \(n\mapsto t-n\); it is not an arbitrary numerical fit.

**2. A two-level density matrix.** After \(n\) consecutive phase gates, the system is in

\[
\lvert\psi_n\rangle=
\bigl(\lvert00\rangle+e^{in\theta}\lvert11\rangle\bigr)/\sqrt2.
\]

With \(\Phi_t(\theta)=\sum_{n=0}^tw_{t,n}e^{in\theta}\), averaging the rank-one matrices gives, in the computational order \((00,01,10,11)\),

\[
\rho_t(\theta)=\frac12
\begin{pmatrix}
1&0&0&\overline{\Phi_t(\theta)}\\
0&0&0&0\\
0&0&0&0\\
\Phi_t(\theta)&0&0&1
\end{pmatrix}.
\]

Its nonzero eigenvalues are \((1\pm|\Phi_t|)/2\). Direct insertion in the two-qubit spin-flip concurrence formula, or the elementary concurrence identity for this even-parity X-state, proves \(\mathcal C_t=|\Phi_t|\). At \(\Phi_t=0\), the matrix is the explicitly separable mixture \((\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)/2\). Every trajectory \(\lvert\psi_n\rangle\) nevertheless has concurrence exactly one.

**3. Legendre reduction.** Since \((1/2)_n/n!=\binom{2n}{n}/4^n\), the two-factor generating function is exactly

\[
\sum_{t=0}^\infty\Phi_t(\theta)z^t
=\frac1{\sqrt{(1-z)(1-ze^{i\theta})}},\qquad |z|<1.
\]

Set \(w=ze^{i\theta/2}\) and \(x=\cos(\theta/2)\). The denominator becomes \(\sqrt{1-2xw+w^2}\). By the standard Legendre generating identity, coefficient comparison yields

\[
\Phi_t(\theta)=e^{it\theta/2}
P_t\!\left(\cos\frac{\theta}{2}\right).
\]

The standard Legendre orthogonality theorem implies that \(P_t\) has precisely \(t\) distinct simple real zeros in \((-1,1)\). The map \(\theta\mapsto\cos(\theta/2)\) strictly decreases from \(1\) to \(-1\) for \(\theta\in(0,2\pi)\), so the classification is exact and exhaustive. Since the derivative of this map does not vanish in the interior, if \(x_{t,j}=\cos(\theta_{t,j}/2)\) is a root then

\[
\mathcal C_t(\theta)=\frac12
|P_t'(x_{t,j})\sin(\theta_{t,j}/2)|\,
|\theta-\theta_{t,j}|+O((\theta-\theta_{t,j})^2).
\]

In particular no finite time has an open interval of separability.

**4. Bessel edge and root scaling.** The beta-binomial mixture gives a random variable \(X\) having density \(1/[\pi\sqrt{x(1-x)}]\) on \((0,1)\) such that conditionally on \(X=x\), \(A_t\) is binomial with \(t\) trials and success probability \(x\). Consequently

\[
\Phi_t(s/t)=\mathbb E\bigl[1-X+Xe^{is/t}\bigr]^t
\longrightarrow \mathbb E[e^{isX}]
=e^{is/2}J_0(s/2).
\]

The limit follows by dominated convergence for real \(s\), with the final identity obtained by substituting \(x=(1+\cos u)/2\) in the arcsine integral. On each compact set of complex \(s\), the binomial characteristic functions converge uniformly (all \(X\) remain in \([0,1]\)); the limiting entire function has simple real positive zeros in its dephased factor. Hurwitz's theorem, together with the exact Legendre real-root count, gives \(t\theta_{t,(k)}\to2j_{0,k}\) for each fixed \(k\geq1\). Equivalently, this is the classical Mehler–Heine formula for Legendre polynomials; it is used here for the entanglement node locations.

**5. Fixed-phase time decay.** At any fixed \(0<\varphi<\pi\), the standard Hilb asymptotic for Legendre polynomials is

\[
P_t(\cos\varphi)=\sqrt{\frac{2}{\pi(t+1/2)\sin\varphi}}
\cos\bigl((t+1/2)\varphi-\pi/4\bigr)
+O_\varphi(t^{-3/2}).
\]

Substituting \(\varphi=\theta/2\) into the exact concurrence identity proves the asserted fixed-phase decay. No stronger uniform claim near the endpoints is made.

## Verification

The independent process recursion, the beta-binomial coefficients, the Legendre generating-function expression, and the four-by-four spin-flip concurrence were checked using `verify_legendre.py`. Exact rational arithmetic established agreement of the reset-age law for every horizon from zero through 23. Numerical checks compared the complex coherence for eight phases at every such horizon, independently reconstructed the density and concurrence at 40 parameter settings, examined the full root counts for degrees 5, 10, 20, 40, 80, and 160, and compared scaled amplitudes with \(J_0\) at horizon 500. The code reports `PASS` with the stated library dependencies. These finite checks are consistency tests, not an infinite proof; the proof is the renewal/generating-function and classical root/asymptotic argument above.

## Relationship to prior work

Wald, Yao, Platini, Hooley, and Carollo (arXiv:2410.11497, publicly submitted 2024-10-15) provide the general discrete-time stochastic quantum resetting model, its renewal equations (1)–(5), two-qubit concurrence measurements, and a power-law hazard family \(r_n=\gamma/(n+1)^\alpha\) in their non-Poissonian section. Those model identities, the definition of concurrence, the beta-binomial distribution, the Legendre generating function, the Legendre root theorem, and the Mehler–Heine/Hilb asymptotics are established mathematical tools, not claimed inventions. The particular **joint result** here is the complete horizon-by-horizon concurrence-node classification under a symmetric critical renewal clock and the associated Bessel edge location of entanglement loss. Their inspected full paper discusses numerical non-Poissonian relaxation rather than this closed form. Sevilla and Valdés-Hernández (arXiv:2209.05643) address continuous-time closed quantum resetting, not this specific discrete reset clock and finite-time node theorem. Carollo, Lesanovsky, and Garrahan (Phys. Rev. E 109, 044129, 2024) study quantum-jump trajectory ordering in generalized continuous-time reset dynamics; no equivalent finite-time phase diagram was found in the material inspected. Published mathematical formula databases already contain the special-function identities; their reuse alone would not be novel.

## Limitations

The full theorem requires global Bell-state replacement, a specific inverse-linear age-dependent reset clock with \(\gamma=1/2\), identical phase increment per gate, and no additional quantum noise. It is not a theorem for arbitrary hazard exponents, local reset channels, or arbitrary two-qubit unitaries. Finite-horizon nodes concern the **unconditioned** density matrix, not typical individual trajectories. The Bessel limit is on the shrinking phase scale \(\theta=s/t\), and the fixed-phase Hilb estimate is not uniform as \(\theta\to0\) or \(\theta\to2\pi\). Unindexed or inaccessible work could contain an equivalent physical interpretation; the claim is not independently audited.

## References

1. S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first submission 2024-10-15, https://arxiv.org/abs/2410.11497 . Full open HTML inspected at https://arxiv.org/html/2410.11497v3 .
2. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643, https://arxiv.org/abs/2209.05643 .
3. F. Carollo, I. Lesanovsky, and J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, Physical Review E **109**, 044129 (2024), https://doi.org/10.1103/PhysRevE.109.044129 .
4. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Physical Review Letters **80**, 2245–2248 (1998), https://doi.org/10.1103/PhysRevLett.80.2245 .
5. NIST Digital Library of Mathematical Functions, Chapter 18, *Orthogonal Polynomials*, especially the generating functions, zeros, and asymptotic limits for Legendre polynomials, https://dlmf.nist.gov/18 .
