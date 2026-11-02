# Exact purity turnarounds and a Bose–Fermi entropy crossover in a coherent qubit battery

## Finding

The stationary qubit battery of a resonant thermal collision model has a sharp and unexpected finite-cluster behavior: the work extractable by a cyclic unitary increases strictly with thermal ancilla-cluster size, while the battery's purity is generally **not** monotone in that size. Each choice of thermal ancilla statistics has one unique real cluster-size purity minimum. The ordering of the purities of oscillator and qubit reservoirs reverses at one exact finite-size threshold, even though oscillator reservoirs always give strictly more ergotropy at the same finite size and temperature.

The following statement is valid for every \(f_1,f_2,\omega,\beta>0\) with finite \(\beta\), and every integer \(N\ge1\). Work in units \(\hbar=k_{\mathrm B}=1\) and put
\[
p=\tanh(\beta\omega/2)\in(0,1),\quad
u=f_1^2>0,\quad v=f_2^2>0,\quad
A=2u+v/2,\quad B=u+v/2,\quad K=AB,\quad L=A(A+v).
\]
Write \(\mathcal P_F(N)\) and \(\mathcal P_B(N)\) for the stationary purity under an \(N\)-qubit ancilla cluster and an \(N\)-oscillator ancilla cluster, respectively. The corresponding ergotropies are \(\mathcal W_F(N)\) and \(\mathcal W_B(N)\).

**Purity turnarounds.** As the real-valued cluster parameter \(N>0\) varies, \(\mathcal P_F(N)\) has its unique strict minimum at
\[
N_F^*=\frac{2\omega}{\sqrt{Av}},
\]
and \(\mathcal P_B(N)\) has its unique strict minimum at
\[
N_B^*=\frac{2p\omega}{\sqrt{Av}}.
\]
Each purity decreases strictly for \(N<N_X^*\) and increases strictly for \(N>N_X^*\), where \(X\) is \(F\) or \(B\). These are smooth algebraic extensions of the physically allowed integer sequence; they do not assert a physically accessible decrease whenever a minimum lies below one.

**Unique entropy-order reversal.** Define
\[
q_c=\frac{2Bv}{1+p^2+\sqrt{(1+p^2)^2+16p^2Bv/A^2}},\qquad
N_c=\frac{\omega}{\sqrt{q_c}}.
\]
Then
\[
N_B^*<N_c<N_F^*,
\]
and, at every integer \(N\ge1\),
\[
\begin{array}{lll}
N<N_c:& \mathcal P_B(N)<\mathcal P_F(N),& S_B(N)>S_F(N),\\
N=N_c:& \mathcal P_B(N)=\mathcal P_F(N),& S_B(N)=S_F(N),\\
N>N_c:& \mathcal P_B(N)>\mathcal P_F(N),& S_B(N)<S_F(N).
\end{array}
\]
Here \(S_X(N)=-\operatorname{tr}(\rho_X\log\rho_X)\) is the von Neumann entropy. The equality case only occurs in an integer cluster when \(N_c\) is itself an integer. If \(N_c\le1\), the smaller-cluster branch is not observed among physical integers.

**Work does not turn around.** For every \(N\ge1\) and all the stated parameters,
\[
0<\mathcal W_F(N)<\mathcal W_B(N),
\]
and \(\mathcal W_F\) and \(\mathcal W_B\) are strictly increasing functions of the continuously extended cluster parameter \(N>0\).

**Exact integer-step classification and finite-size tail.** For either ancilla type \(X\), set \(c_F=1\), \(c_B=p^2\), and \(q_{X,N}=c_X\omega^2/N^2\). The sign of the purity change from \(N\) to \(N+1\) is exactly the sign of
\[
\frac{L}{K+q_{X,N}}+\frac{L}{K+q_{X,N+1}}-4.
\]
This expression increases strictly with \(N\); thus the integer sequence either increases throughout, or decreases and then increases, with one minimum or a tie between exactly two adjacent minimizing integers. With
\[
\mathcal P_\infty=\frac{1+p^2R(0)}2,
\qquad R(0)=1-\frac{4u^2}{K}+\frac{u^2L}{K^2},
\]
the precise common limiting purity is approached **from below**:
\[
\mathcal P_F(N)=\mathcal P_\infty-\frac{p^2u^2Av\omega^2}{2K^3N^2}+O(N^{-4}),
\]
\[
\mathcal P_B(N)=\mathcal P_\infty-\frac{p^4u^2Av\omega^2}{2K^3N^2}+O(N^{-4}).
\]
All asymptotics fix the couplings, positive inverse temperature and level splitting as \(N\to\infty\).

## Assumptions and scope

The battery has Hilbert space \(\mathbb C^2\), Hamiltonian \(H=\omega\sigma_z/2\), and density operator \(\rho\). Let
\[
s=f_1\sigma_z+f_2\sigma_-,\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
\]
Each thermal cluster is independent, resonant with the battery, and prepared at inverse temperature \(\beta>0\). In the standard weak, short repeated-collision limit, the reduced generator is
\[
\dot\rho=-i[H,\rho]
+\frac{k(1+p)}2\mathcal D[s](\rho)
+\frac{k(1-p)}2\mathcal D[s^\dagger](\rho),
\]
where \(k=N\) for a cluster of \(N\) thermal qubits and \(k=N/p\) for a cluster of \(N\) thermal harmonic oscillators. The positive rates are the corresponding collective thermal emission and absorption second moments; no oscillator Hilbert-space truncation is assumed in the reduced generator. The displayed result is about the stationary state of this generator, with \(f_1f_2\ne0\), and about standard single-qubit unitary ergotropy, not the net energy efficiency after collision-switching costs. The parameters remain fixed when comparing \(N\), except for the prescribed statistical rate scale \(k\).

## Proof

**1. Stationary Bloch vector and its uniqueness.** Put \(\rho=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\). Direct substitution in the stated Lindblad generator gives
\[
\dot x=-kAx-\omega y+k f_1f_2z+2kp f_1f_2,
\qquad
\dot y=\omega x-kAy,
\qquad
\dot z=k f_1f_2x-kv(z+p).
\]
Here \(A=2f_1^2+f_2^2/2>0\). In a stationary solution the last two equations give \(y=\omega x/(kA)\) and \(z=(f_1/f_2)x-p\). Substitution in the first equation gives a strictly positive denominator \(B+\omega^2/(k^2A)\). Hence the stationary solution is unique. With \(q=(\omega/k)^2>0\), it is
\[
(x(q),y(q),z(q))
=\frac{p}{K+q}\left(f_1f_2 A,\ f_1f_2\sqrt q,\ -Av/2-q\right).
\]
For qubit and oscillator clusters the corresponding arguments are respectively
\[
q_F=(\omega/N)^2,\qquad q_B=p^2(\omega/N)^2.
\]
The formula holds for the stated positive parameters; the generator itself ensures this Bloch vector gives a positive density operator.

**2. Purity and its minimum.** Squaring the components and simplifying yields the exact identity
\[
\mathcal P(q)=\frac{1+p^2R(q)}2,\qquad
R(q)=1-\frac{4u^2}{K+q}+\frac{u^2L}{(K+q)^2},
\]
where \(u=f_1^2\), \(v=f_2^2\), \(K=AB\), and \(L=A(A+v)\). Differentiating and using \(L-2K=Av/2\) gives
\[
R'(q)=\frac{4u^2(q-Av/4)}{(K+q)^3}.
\]
Thus \(q_0=Av/4\) is the unique strict minimum of \(R\) on \((0,\infty)\). Since each \(q_X\) decreases strictly with \(N\), the unique real cluster-size minima are \(N_F^*=\omega/\sqrt{q_0}\) and \(N_B^*=p\omega/\sqrt{q_0}\), proving the two turnaround assertions.

**3. Unique statistical crossover.** Write \(q=(\omega/N)^2\) and \(t=p^2\in(0,1)\). The difference of the two squared-Bloch-length factors is
\[
R(tq)-R(q)=u^2\left(\frac1{K+tq}-\frac1{K+q}\right)
\left[L\left(\frac1{K+tq}+\frac1{K+q}\right)-4\right].
\]
The first parenthesis is strictly positive. Multiplying the second by its positive denominator shows its sign is precisely the sign of
\[
Bv-(1+t)q-\frac{4t}{A^2}q^2.
\]
This polynomial is positive at \(q=0\) and strictly decreases to minus infinity. Its sole positive root is the stated \(q_c\). Therefore \(\mathcal P_B>\mathcal P_F\) exactly for \(q<q_c\), and the inequality reverses for \(q>q_c\). At \(q=q_0\), strict minimality of \(R\) gives \(R(tq_0)>R(q_0)\); at \(q=q_0/t\), it gives \(R(tq_0/t)<R(q_0/t)\). The unique root consequently satisfies \(q_0<q_c<q_0/t\), which is equivalent to \(N_B^*<N_c<N_F^*\).

The eigenvalues of a qubit state with Bloch length \(r\) are \((1\pm r)/2\). Its von Neumann entropy is strictly decreasing in \(r\) for \(0<r<1\), whereas the purity \((1+r^2)/2\) is strictly increasing. Since finite positive temperature gives \(0<r<1\), the entropy comparisons follow with the opposite signs.

**4. Ergotropy inequalities.** The two-level passive rearrangement gives \(\mathcal W=\omega(z+\sqrt{x^2+y^2+z^2})/2\). In terms of \(q\), put \(d=Av/2+q\), \(h=K+q\), and \(g=\sqrt{d^2+uv(A^2+q)}>d\). Then
\[
\mathcal W(q)=\frac{\omega p}{2}\frac{g-d}{h}>0.
\]
An exact differentiation gives
\[
2gh^2\frac{d}{dq}\left(\frac{g-d}{h}\right)
=2uA(d-g)+uv\bigl(h-2(A^2+q)\bigr)<0.
\]
Indeed \(g>d\), and \(h-2(A^2+q)=A(B-2A)-q<0\). Hence ergotropy strictly decreases with \(q\). Both \(q_F\) and \(q_B\) decrease as \(N\) grows, and \(0<q_B<q_F\) for every finite \(N\), proving all work-ordering statements.

**5. Exact integer-step rule and asymptotics.** Applying the difference factorization of step 3 with two successive arguments \(q_{X,N+1}<q_{X,N}\) gives the integer-step sign criterion, with a strictly positive prefactor. Both reciprocal denominators increase strictly as \(N\) increases. Thus there can be at most one sign transition from negative to positive in the integer sequence, with an equality step producing exactly two adjacent minimizing integers. Finally,
\[
R'(0)=-\frac{u^2Av}{K^3},
\]
and Taylor expansion of the exact rational expression at \(q=0\), separately with \(q_F=\omega^2/N^2\) and \(q_B=p^2\omega^2/N^2\), proves the two positive-coefficient \(N^{-2}\) approaches from below and the claimed \(O(N^{-4})\) remainders.

## Verification

The supplied standalone `verify.py` reconstructs the stationary density matrix by explicitly constructing the full complex two-by-two Lindblad superoperator and solving its trace-one stationary linear system. It tests the exact Bloch solution, positivity, ergotropy ordering, purity difference, exact crossover, symbolic rational identities, derivative factorization, finite-cluster integer-step signs and large-cluster coefficients. It passed 1,832 deterministic checks across positive-coupling, frequency, occupation and cluster-size samples. The exact symbolic identities and the proof above, not any finite test set, support the universal assertions.

A physical integer witness makes the sign reversal explicit. At \(f_1=f_2=1\), \(\omega=3\), and \(p=1/2\), the exact threshold is \(q_c\simeq1.05699380446\), or \(N_c\simeq2.918\). For \(N=1\), \(\mathcal P_B-\mathcal P_F\simeq-0.0204638841\); for \(N=10\), \(\mathcal P_B-\mathcal P_F\simeq+0.0003483373\). Meanwhile \(\mathcal W_B-\mathcal W_F>0\) in both cases. The corresponding finite inverse temperature is \(\beta=2\operatorname{artanh}(1/2)/3\). The standalone program can be run with `python verify.py`; it requires NumPy and SymPy.

## Relationship to prior work

Yáñez-Soria, Guarnieri, Çakmak and Román-Ancheyta (2026), arXiv:2609.38724, derive this composite-interaction collision generator, the stationary Bloch components for arbitrary thermal cluster size (Appendix B, equations 36–47), and the qubit ergotropy formula (equation 7). Their finite-cluster figures and their large-cluster thermodynamic analysis are prior work; the present statement is a new sign and threshold classification of purity, entropy, and work along those explicit stationary solutions. It does not present the stationary solution or general qubit ergotropy formula as new.

Román-Ancheyta and collaborators (2020/2021), arXiv:2008.05200, provide the original collision-coherence mechanism and study purity versus cluster size in particular parameter plots (Section II.1 and Section III.1). The present theorem does not dispute those plotted results. It identifies the full positive-parameter finite-size U-shape, its exact integer-step boundary, and the unique Bose-versus-qubit entropy-order reversal, none of which is explicitly classified by the cited plots or their stated large-cluster approximation. The quantum-state ergotropy relation itself is standard; Choquehuanca and collaborators (2024), arXiv:2403.04698, is an additional contextual source. All derived results are mathematically consequences of the earlier exact stationary generator, so their priority as a separate classification remains subject to further literature comparison.

## Limitations

The physical cluster size is an integer; the real-valued minimizers and crossover are useful exact boundaries, but a particular parameter choice may have no observable initial decrease or no finite-integer sign reversal. Positive finite temperature and strictly positive composite couplings are essential to the strict inequalities: zero-temperature, infinite-temperature and decoupled limits require separate limiting statements. The theorem concerns resonant, independent Gibbs ancillas, the Markovian collision limit and stationary single-qubit states; it does not treat finite collision durations, non-Markovian baths, transient purity, optimized couplings varying with cluster size, laboratory implementation constraints or total efficiency after switching work. The prior papers already supply the exact stationary state, and more general unlocated analyses may imply the classification. The analytical proof has not received an independent mathematical or publication-priority audit.

## References

1. O. S. Yáñez-Soria, G. Guarnieri, B. Çakmak and R. Román-Ancheyta, *Ergotropy from energetic coherence and the third law of thermodynamics*, arXiv:2609.38724, first public 2026-09-30. https://arxiv.org/abs/2609.38724
2. R. Román-Ancheyta and collaborators, *Enhanced steady-state coherence via repeated system-bath interactions*, arXiv:2008.05200, first public 2020-08-12. https://arxiv.org/abs/2008.05200
3. J. Choquehuanca and collaborators, *Qubit dynamics of ergotropy and environment-induced work*, arXiv:2403.04698, 2024. https://arxiv.org/abs/2403.04698
