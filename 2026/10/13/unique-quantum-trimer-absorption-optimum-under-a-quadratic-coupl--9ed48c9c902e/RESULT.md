# Unique quantum-trimer absorption optimum under a quadratic coupling budget

## Finding
For a resonant three-site chain with coherent nearest-neighbor couplings \(J_1,J_2>0\), a single irreversible Markovian sink on site 1 of rate \(\kappa>0\), and one excitation initially on site 3, define the hopping budget \(E=J_1^2+J_2^2>0\). The exact mean first-absorption time is

\[
\tau_3(J_1,J_2,\kappa)=\frac{\kappa}{2J_1^2}+\frac{1}{\kappa}\left(\frac{2J_2^2}{J_1^2}+\frac{J_1^2}{J_2^2}\right).
\]

Among **all** positive couplings and sink rates satisfying this fixed budget, the unique minimizer is

\[
J_1^2=\frac{2E}{3},\qquad J_2^2=\frac{E}{3},\qquad\kappa=2\sqrt E,\qquad \min\tau_3=\frac3{\sqrt E}.
\]

The optimal couplings are unequal: the link adjoining the absorber receives twice the squared hopping strength of the entry link. Requiring equal couplings instead yields the strictly larger loss-optimized value \(2\sqrt3/\sqrt E\), so the relative reduction is \(1-\sqrt3/2\approx13.3975\%\).

## Assumptions and scope
There are exactly three orthonormal single-excitation states \(|1\rangle,|2\rangle,|3\rangle\) and an absorbing vacuum \(|\mathrm{vac}\rangle\). With \(\hbar=1\), the Hamiltonian and sole Lindblad jump operator are

\[
H=J_1(|1\rangle\langle2|+|2\rangle\langle1|)
  +J_2(|2\rangle\langle3|+|3\rangle\langle2|),\qquad
L=\sqrt\kappa|\mathrm{vac}\rangle\langle1|.
\]

Assume \(J_1>0,J_2>0,\kappa>0\), no on-site detuning, no other losses, no dephasing and no reinjection. Start from \(|3\rangle\). The survival probability \(S(t)\) is the probability that no absorption has occurred by time \(t\); the first-absorption density is \(f(t)=-S'(t)\). The performance objective is its unconditional mean \(\tau_3=\int_0^\infty t f(t)\,dt\). Fix the physically specified quadratic coupling resource \(E=J_1^2+J_2^2\), proportional to the squared Frobenius norm of the hopping Hamiltonian, and optimize both individual couplings and the separately tunable sink rate. The statement is **not** a universal optimization over different cost models.

## Proof
Put \(P=|1\rangle\langle1|\) and \(Q=-iH-\kappa P/2\), acting on the three single-excitation states. Then \(S(t)=\|e^{Qt}|3\rangle\|^2\). Every eigenvalue of \(Q\) has strictly negative real part: if \(Qv=\lambda v\), then \(2\operatorname{Re}\lambda\|v\|^2=-\kappa|v_1|^2\). Equality would require \(v_1=0\); the first and second component equations successively imply \(v_2=v_3=0\) because both couplings are nonzero. Thus \(S(t)\to0\) exponentially, total absorption is one, the mean is finite, and integration by parts gives

\[
\tau_3=\int_0^\infty S(t)\,dt=\langle3|X|3\rangle,
\quad X=\int_0^\infty e^{Q^\dagger t}e^{Qt}dt,
\quad Q^\dagger X+XQ=-I_3.
\]

The Hermitian matrix solving this Lyapunov equation is explicitly

\[
X=\begin{pmatrix}
\frac3\kappa & \frac{i}{J_1} & \frac{2J_2^2-J_1^2}{\kappa J_1J_2}\\
-\frac{i}{J_1}&\frac{\kappa^2+4J_1^2+4J_2^2}{2\kappa J_1^2}&\frac{i}{2J_2}\\
\frac{2J_2^2-J_1^2}{\kappa J_1J_2}&-\frac{i}{2J_2}&\frac{\kappa^2J_2^2+4J_2^4+2J_1^4}{2\kappa J_1^2J_2^2}
\end{pmatrix}.
\]

Direct multiplication establishes the Lyapunov identity for arbitrary positive parameters; stability guarantees uniqueness, so the lower-right entry is the claimed mean. This is an algebraic identity, not an inference from finite sampling.

Now impose \(E=J_1^2+J_2^2\) and set \(x=J_1^2/J_2^2>0\). Substitution yields

\[
\tau_3=\frac\kappa{2E}\left(1+\frac1x\right)+\frac1\kappa\left(x+\frac2x\right).
\]

For each \(x>0\), arithmetic–geometric mean gives the sharp bound

\[
\tau_3\ge\sqrt{\frac2E}\sqrt{x+1+\frac2x+\frac2{x^2}},
\]

with equality only when \(\kappa=\sqrt{2E(x^2+2)/(x+1)}\). The remaining one-variable inequality is **globally sharp** because

\[
x+1+\frac2x+\frac2{x^2}-\frac92
=\frac{(x-2)^2(2x+1)}{2x^2}\ge0.
\]

Equality forces \(x=2\) and then \(\kappa=2\sqrt E\), giving the unique claimed minimizer. At equal couplings \(x=1\), the sink-optimized time is \(2\sqrt3/\sqrt E\). Both limiting coupling allocations \(x\downarrow0\) and \(x\to\infty\) have divergent optimized time, so no boundary minimizer is omitted.

## Verification
The standalone `verify.py` symbolically reconstructs the three-site non-Hermitian generator and the entire Hermitian Lyapunov Gramian, checks **all nine** entries of \(Q^\dagger X+XQ+I_3=0\) identically in independent positive symbolic parameters, checks the exact optimizing factorization, and independently solves the nine-complex-entry linear Lyapunov system at three unequal rational parameter triples. Invoke `python verify.py` after installing `requirements.txt`. The analytic stability, Gramian identity, and factorization prove the full continuum claim; tests alone would not.

## Relationship to prior work
Riberi's May 8, 2026 work [1] analyzes a Lindblad boundary absorber and exact quantum-walk first-passage observables on a **semi-infinite** line, rather than jointly optimizing two tunable hopping strengths on a finite trimer. Zhang and collaborators [2,3] establish related finite-chain trapping-time methods, including the **previously known uniform-coupling opposite-end formula**, so homogeneous-path trapping and sink-rate optimization are **not** claimed here as new. Contreras-Pulido and collaborators [4] study linear triple-dot steady transport with source injection, dephasing and predominantly **equal** tunneling links; their measured quantity and resource optimization differ. Peter and collaborators [5] study coherent transport/trapping and optimize extraction settings in a richer emitter model, but do not present the present pure single-excitation, three-site, quadratic-budget global classification in the inspected material. The contribution assessed here is the **unique exact joint optimum for two freely allocated link strengths and a terminal sink under fixed squared-coupling budget**, including a sharp quantitative comparison with the equal-link design.

## Limitations
This theorem does not cover longer chains, interactions, non-Markovian sinks, competing decay, dephasing, coherent detuning, weighted pump–drain steady current, or alternative resource penalties. It optimizes mean first absorption, not the full hitting-time law or time-constrained success probability. A standard Liouvillian inversion can represent the objective without giving this explicit resource-optimal classification. Earlier unindexed or implicit equivalent optimizations cannot be ruled out by search alone. No independent scientific audit has been conducted.

## References
[1] F. Riberi, *An Exactly Solvable Absorbing Quantum Walk* (first public May 8, 2026), arXiv:2605.08056; subsequent version titled *Boundary-localized non-Hermitian modes in an absorbing quantum walk*. https://arxiv.org/abs/2605.08056

[2] Y. Zhang, G. L. Celardo, F. Borgonovi, L. Kaplan, *Optimal dephasing for ballistic energy transfer in disordered linear chains*, Phys. Rev. E 96, 052103 (2017), arXiv:1706.09524, especially Eq. (17) and the discussion of initial conditions. https://arxiv.org/abs/1706.09524

[3] Y. Zhang, G. L. Celardo, F. Borgonovi, L. Kaplan, *Opening-Assisted Coherent Transport in the Deep Classical Regime*, Phys. Rev. E 95, 022122 (2017), arXiv:1608.08910. https://arxiv.org/abs/1608.08910

[4] L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga, M. B. Plenio, *Dephasing-assisted transport in linear triple quantum dots*, New J. Phys. 16, 113061 (2014), arXiv:1407.0924. https://arxiv.org/abs/1407.0924

[5] J. S. Peter, R. Holzinger, S. Ostermann, S. F. Yelin, *Examining the quantum signatures of optimal excitation energy transfer*, Phys. Rev. Res. 6, 033252 (2024), arXiv:2403.00058. https://doi.org/10.1103/PhysRevResearch.6.033252
