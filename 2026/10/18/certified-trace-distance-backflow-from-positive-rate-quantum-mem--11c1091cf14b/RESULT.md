# Certified trace-distance backflow from positive-rate quantum memory resets

## Finding

Consider the continuous-time uniform-historical-memory quantum resetting protocol described below, acting on a qubit. Although its resetting events occur at a **constant positive Poisson rate** and every fixed-time channel is completely positive and trace preserving, its reduced dynamics need not be divisible even by positive trace-preserving propagators. Specifically, for every \(r>0\), take the Hamiltonian \(H=(5r/4)\sigma_z\), whose energy gap is \(\omega=5r/2\), and the antipodal equatorial states \(\rho_\pm(0)=|\pm_x\rangle\langle\pm_x|\). Their evolved trace distance \(D(t)=\frac12\|\Phi_t(\rho_+(0))-\Phi_t(\rho_-(0))\|_1\) obeys the rigorously certified bounds

\[
D(3/r)<\frac1{20},\qquad D(4/r)>\frac1{10}.
\]

Thus \(D(4/r)-D(3/r)>1/20\), giving an explicit lower bound on information backflow and on the Breuer--Laine--Piilo distinguishability-based non-Markovianity measure. More quantitatively, for every gap ratio \(h=\omega/r\) with \( |h-5/2|\le 1/200\), the trace-distance increase is strictly greater than \(3/200\). The same conclusion holds for any finite-dimensional Hamiltonian possessing **any pair of energy levels** with a gap in this certified band, by preparing antipodal superpositions of those eigenstates. The conclusion concerns **resetting to a uniformly selected state from each trajectory's own past**, not resetting to one fixed reference state.

## Assumptions and scope

The Hilbert space is \(\mathbb C^2\), \(\hbar=1\), and the time-independent Hamiltonian is \(H=(\omega/2)\sigma_z\), with \(r>0\) and \(\omega=5r/2\). Between independent rate-\(r\) Poisson events the system evolves as \(\rho\mapsto e^{-iHt}\rho e^{iHt}\). At a reset event at chronological time \(t\), a time \(s\) is sampled uniformly from \([0,t]\), and the instantaneous state is replaced by that same trajectory's state at time \(s\). This rule is applied recursively and averaged over the independent random choices.

Here \(|\pm_x\rangle=(|0\rangle\pm|1\rangle)/\sqrt2\), and \(D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1\). A family \((\Phi_t)_{t\ge0}\) is *positive divisible* if, for every \(t\ge s\ge0\), some positive trace-preserving linear map \(V_{t,s}\) satisfies \(\Phi_t=V_{t,s}\circ\Phi_s\). The backflow result rules out this property and therefore also CP-divisibility. It does not mean that any fixed-time \(\Phi_t\) fails complete positivity. The interval extension permits any finite-dimensional Hamiltonian, provided one Bohr frequency falls within the specified band.

## Proof

**1. Fixed-time complete positivity and coherence equation.** Define the random effective evolution time \(A_0=0\). Between resets \(A_t\) increases with unit slope, and at a reset time \(t\), set \(A_t=A_s\) for the uniformly sampled earlier time \(s\). Every single trajectory then acts as the unitary channel \(U_{A_t}(X)=e^{-iHA_t}Xe^{iHA_t}\), with a random \(A_t\) whose law does not depend on the input density matrix. Thus

\[
\Phi_t(X)=\mathbb E\big[e^{-iHA_t}Xe^{iHA_t}\big]
\]

is a random-unitary, hence completely positive and trace-preserving, channel. Writing \(f_\omega(t)=\mathbb E[e^{-i\omega A_t}]\), conditioning on the increment and reset event gives the Volterra equation

\[
f_\omega'(t)=-(r+i\omega)f_\omega(t)+\frac{r}{t}\int_0^t f_\omega(s)\,ds,
\qquad f_\omega(0)=1.
\]

It implies \(f_\omega'(0)=-i\omega\). Eliminating the integral and differentiating gives

\[
t f_\omega''(t)+[1+(r+i\omega)t]f_\omega'(t)+i\omega f_\omega(t)=0.
\]

With \(a=i\omega/(r+i\omega)\), \(z=-(r+i\omega)t\), the unique solution regular at \(t=0\) is Kummer's confluent hypergeometric function

\[
f_\omega(t)={}_1F_1\left(a;1;z\right)
=\sum_{n=0}^{\infty}\frac{(a)_n z^n}{(n!)^2}.
\]

This is the source paper's established exact coherence formula; its derivation is included here to fix signs, normalization and the physical dynamical map.

**2. Trace distance.** The two antipodal equatorial input states have the difference \(\rho_+(0)-\rho_-(0)=\sigma_x\). Under \(\Phi_t\) their difference has zero diagonal and off-diagonal entries \(f_\omega(t)\) and its complex conjugate. Its eigenvalues are \(\pm|f_\omega(t)|\); therefore

\[
D(t)=|f_\omega(t)|.
\]

**3. Exact finite inequality with a rigorously bounded infinite tail.** Put \(u=rt\), \(\omega/r=5/2\). Then

\[
a=\frac{25+10i}{29},\qquad z_u=-u\left(1+\frac52i\right),\qquad u\in\{3,4\}.
\]

For both \(u\), \(|z_u|<11\); also \(|a|^2=725/841<1\). Hence \(|(a)_n|\le n!\), and the remainder after summing terms \(n=0,\ldots,79\) has modulus bounded by

\[
B=\sum_{n=80}^\infty\frac{11^n}{n!}
\le\frac{81}{70}\frac{11^{80}}{80!}<10^{-10}.
\]

Writing \(S_u=\sum_{n=0}^{79}(a)_n z_u^n/(n!)^2\), all \(S_u\) components are rational numbers. Exact rational arithmetic (not floating-point approximation) gives

\[
\frac{17}{10000}<|S_3|^2<\frac{18}{10000},
\qquad
\frac{119}{10000}<|S_4|^2<\frac{120}{10000}.
\]

In particular, the verified stronger comparisons \(|S_3|^2<(1/20-1/10000)^2\) and \(|S_4|^2>(1/10+1/10000)^2\), together with \(B<1/10000\), imply

\[
|f_\omega(3/r)|<\frac1{20},\qquad
|f_\omega(4/r)|>\frac1{10}.
\]

Every rational comparison and the tail inequality is reproduced by the standalone standard-library checker `check_backflow_exact.py`.

**4. Divisibility and a certified spectral window.** Any positive trace-preserving map is contractive for the trace distance of quantum states. If a positive trace-preserving propagator \(V_{4/r,3/r}\) existed, contractivity would force \(D(4/r)\le D(3/r)\), contradicting step 3. Thus positive divisibility and CP-divisibility fail, and the total positive variation of \(D(t)\) is strictly greater than \(1/20\).

For quantitative robustness, write the dimensionless accumulated time \(Y_u=r A_{u/r}\). The very construction of the historical reset clock gives \(0\le Y_u\le u\) pathwise. For \(h=\omega/r\), the coherence is \(f_h(u)=\mathbb E[e^{-ihY_u}]\). The elementary inequality \(|e^{-ihy}-e^{-ih_0y}|\le |h-h_0|y\) therefore gives

\[
\big|\,|f_h(u)|-|f_{h_0}(u)|\,\big|\le u|h-h_0|.
\]

At \(h_0=5/2\), step 3 gives \(|f_{h_0}(4)|-|f_{h_0}(3)|>1/20\). Hence whenever \(|h-5/2|\le1/200\),

\[
|f_h(4)|-|f_h(3)|>\frac1{20}-(4+3)\frac1{200}=\frac3{200}.
\]

For an arbitrary finite-dimensional Hamiltonian, any two eigenstates with gap \(\omega>0\) span an invariant subspace. Restrict the two antipodal input pure states to that subspace. Their trace distance under the full history-reset channel is still \(|f_{\omega/r}(rt)|\). Thus the spectral-window conclusion holds without assuming the rest of the spectrum is gapped or nondegenerate. This finishes the proof.

## Verification

Run `python3 check_backflow_exact.py` with a standard Python 3 interpreter. The program constructs the two 80-term hypergeometric partial sums as pairs of exact `fractions.Fraction`, checks the deterministic tail estimate, and compares squared complex moduli using integer arithmetic only. The reported decimal values are illustrative and never enter acceptance. The whole infinite series is controlled by the explicit geometric bound on its tail; finite truncation alone is not the proof.

## Relationship to prior work

De Mauro, Kulkarni and Majumdar (2026) introduce the uniform-history quantum protocol and solve its coherence dynamics for arbitrary Hamiltonians, obtaining the Kummer formula used in step 1. Their result includes algebraic coherence decay but does not state the explicit increasing trace-distance interval, its certified lower bound, or consequent failure of positive divisibility. The present claim is about an operational implication that requires establishing a strict inequality for the nontrivial Kummer modulus, not a new coherence solution.

Carollo and Wald (2026) study a distinct **discrete-time**, fixed-reference-state reset mechanism with elapsed-time-dependent reset probabilities; their trace-distance revival example concerns effective negative probabilities. Here the physical Poisson hazard is positive and constant, while the chosen reset state depends on the trajectory's history. Breuer, Laine and Piilo (2009) establish trace-distance revival as an information-backflow and divisibility criterion. Their criterion is applied here but is not itself new.

## Limitations

The theorem supplies a certified spectral band forcing failure of divisibility, not an exact classification of all ratios or the total optimized non-Markovianity measure. It assumes a two-level, time-independent Hamiltonian and uniform sampling of each trajectory's past. The result does not apply merely because a generic quantum process has a memory kernel: the particular history-resetting channel and its exact coherence function are essential. It makes no claim about entanglement revival, intermediate-map complete positivity at every other time pair, or experimental implementation.

## References

1. G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1, first posted 2026-08-03, https://arxiv.org/abs/2608.02297 .
2. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367v1, first posted 2026-01-19, https://arxiv.org/abs/2601.13367 .
3. H.-P. Breuer, E.-M. Laine and J. Piilo, *Measure for the Degree of Non-Markovian Behavior of Quantum Processes in Open Systems*, Phys. Rev. Lett. 103, 210401 (2009), arXiv:0908.0238, https://arxiv.org/abs/0908.0238 .
