# Renewal-event monotonicity exactly governs universal Heisenberg divisibility under quantum resetting

## Finding

Consider a discrete-time quantum system updated between resets by one fixed unitary gate. Resets occur according to an independent renewal law and replace the system by a fixed density matrix. Although every physical averaged-time map is completely positive, positivity of *the inter-time maps in the Heisenberg picture* is a separate question. The answer, uniformly over all finite-dimensional gates and reset states, is controlled by the renewal **event probabilities**, rather than by the individual waiting-time hazards.

**Theorem (universal dual-divisibility criterion).** Let \(h_j\in(0,1)\) be the probability of a reset at waiting age \(j\), for every integer \(j\ge1\). Define
\[
S_0=1,\qquad S_j=\prod_{a=1}^{j}(1-h_a),\qquad p_j=S_{j-1}h_j,
\]
and the renewal mass sequence \(\nu_0=0\) and, for \(t\ge1\),
\[
\nu_t=\sum_{j=1}^{t}p_j\,\nu_{t-j}+p_t.
\]
The equivalent renewal convention uses the dummy initial event at time zero and replaces the displayed recursion by \(\nu_t=\sum_{j=1}^t p_j u_{t-j}\), with \(u_0=1\) and \(u_t=\nu_t\) for \(t\ge1\); both expressions count events at strictly positive times. Assume \(S_t\to0\) so that the waiting-time law is proper.

For every finite dimension \(d\ge2\), unitary \(U\in\mathbb C^{d\times d}\), and density matrix \(\sigma\), let \(\Phi_t\) denote the averaged Schrödinger channel and \(\Phi_t^*\) its Hilbert--Schmidt dual. Define the *Heisenberg intertwiner* by
\[
\Psi_{t,s}=\Phi_t^*\circ(\Phi_s^*)^{-1},\qquad t>s\ge0.
\]
The following assertions are equivalent:

1. \(\nu_{t+1}\ge\nu_t\) for every integer \(t\ge1\).
2. For every \(d,U,\sigma\) as above, every Heisenberg intertwiner \(\Psi_{t,s}\) is positive and unital.
3. For every \(d,U,\sigma\) as above, every Heisenberg intertwiner \(\Psi_{t,s}\) is completely positive and unital.

More sharply, for **each fixed** dimension, gate, and reset state, the Heisenberg maps are positive-divisible exactly when they are completely-positive-divisible; both properties hold exactly when the matrices \(B_t-B_{t-1}\) defined below are positive semidefinite for every \(t\ge1\). In any finite horizon \(1\le t\le T\), the universal equivalent condition is just \(\nu_1\le\cdots\le\nu_T\); any first violation at \(t=m\) has a witness in dimension \(d=m\).

**Strict separation from hazard monotonicity.** In particular, choose \(h_1=1/10\), \(h_2=9/10\), and \(h_j=91/100\) for \(j\ge3\). These are nondecreasing positive hazards, but
\[
\nu_1=\frac1{10},\qquad \nu_2=\frac{41}{50},\qquad \nu_3=\frac{2449}{10000}<\nu_2.
\]
With a three-dimensional cyclic-shift gate and a pure basis reset, \(\Psi_{3,2}\) is not even positive. In contrast, the **Schrödinger-picture** one-step maps are CPTP for *every* gate and reset state under the same nondecreasing hazards. Thus a physically valid increasing-hazard protocol can have universal Schrödinger CP-divisibility while failing Heisenberg P-divisibility.

## Assumptions and scope

The space is \(\mathbb C^d\), \(d\ge2\). The reset clock starts at age zero at absolute time zero. At each integer time, conditional on no preceding reset since its most recent reset, the system is reset to the *same* density matrix \(\sigma\) with probability \(h_j\), where \(j\) is the elapsed waiting age; otherwise the unitary channel \(\mathcal U(X)=UXU^\dagger\) acts. The reset clock is classical and independent of the quantum state. The reset sequence is independent of the initial system state, and all probabilities lie strictly between zero and one. The assumption \(S_t\to0\) ensures a proper renewal law; the finite-horizon algebra does not require this limit.

The symbol \(\nu_t\) denotes the probability that a reset occurs at *absolute* time \(t\), regardless of earlier resets, and **not** the one-cycle waiting-time probability \(p_t\) or the hazard \(h_t\). Set \(\nu_0=0\); the initial time is not counted as a reset event. The convolution recursion in the theorem is a finite sum and is unambiguous under this convention.

The divisibility notion is the left composition \(\Phi_t^*\circ(\Phi_s^*)^{-1}\) on observables, not \((\Phi_t\circ\Phi_s^{-1})^*\). This distinction is essential. The theorem is about averaged reduced dynamical maps; it does not claim that the underlying renewal history is quantum Markovian in a process-tensor sense.

## Proof

**1. Renewal decomposition and invertibility.** Writing \(\sigma_j=U^j\sigma U^{-j}\) for nonnegative integers \(j\), the last-reset renewal equation yields
\[
\Phi_t(X)=S_tU^t XU^{-t}+\operatorname{tr}(X)B_t,
\qquad
B_t=\sum_{j=0}^{t-1}\nu_{t-j}S_j\sigma_j,\quad B_0=0.
\]
Here \(\operatorname{tr}B_t=1-S_t\). In consequence,
\[
\Phi_t^*(Y)=S_tU^{-t}YU^t+\operatorname{tr}(B_tY)I.
\]
Since \(S_t>0\), its inverse is given explicitly by
\[
(\Phi_t^*)^{-1}(Y)
=\frac1{S_t}U^t\left[Y-\operatorname{tr}(U^{-t}B_tU^tY)I\right]U^{-t}.
\]
Indeed, substituting this expression into the preceding display returns \(Y\), using \(\operatorname{tr}B_t=1-S_t\). Thus no singular-time inverse is required under the hypotheses.

**2. Exact Heisenberg intertwiner.** For each \(t\ge1\), direct substitution into \(\Psi_{t,t-1}=\Phi_t^*\circ(\Phi_{t-1}^*)^{-1}\) gives
\[
\Psi_{t,t-1}(Y)=k_tU^{-1}YU+\operatorname{tr}(F_tY)I,
\quad
k_t=\frac{S_t}{S_{t-1}}=1-h_t,
\]
where
\[
F_t=\frac1{S_{t-1}}U^{-(t-1)}(B_t-B_{t-1})U^{t-1},
\qquad\operatorname{tr}F_t=1-k_t=h_t.
\]
The map is unital by the trace identity. For \(d\ge2\), any map of the displayed form with \(k_t\ge0\) is positive **if and only if** \(F_t\succeq0\). Sufficiency implies complete positivity: when \(F_t\succeq0\), the first term is a nonnegative unitary-conjugation map and the second is a nonnegative measure-and-replace map on observables. Conversely, if a unit vector \(v\) satisfies \(\langle v,F_tv\rangle<0\), applying the map to \(Y=|v\rangle\langle v|\) gives a negative expectation on any unit vector orthogonal to \(U^{-1}v\), which exists for \(d\ge2\). Hence even positivity fails. Therefore positivity and complete positivity coincide for each such Heisenberg intertwiner.

Since a product of positive (respectively CP) unital maps is positive (respectively CP) and unital, testing adjacent steps is equivalent to testing all \(s<t\), proving the fixed-system matrix criterion.

**3. Renewal-increment decomposition.** Subtracting the two last-reset sums and using \(\nu_0=0\), one obtains the *exact* identity
\[
B_t-B_{t-1}
=\sum_{j=0}^{t-1}(\nu_{t-j}-\nu_{t-1-j})S_j\sigma_j.
\]
If \(\nu_t\) is nondecreasing, each summand is a nonnegative scalar multiple of a positive semidefinite matrix, so \(B_t-B_{t-1}\succeq0\) for all choices of \(U,\sigma,d\). By step 2 every Heisenberg intertwiner is CP and unital.

Conversely, suppose \(\nu_m<\nu_{m-1}\) for some \(m\ge2\). Take \(d=m\), \(\sigma=|0\rangle\langle0|\), and let \(U|j\rangle=|j+1\pmod m\rangle\). For \(0\le j\le m-1\), the matrices \(\sigma_j\) are distinct orthogonal basis projections. In the displayed expansion at \(t=m\), the diagonal entry of \(B_m-B_{m-1}\) in state \(|0\rangle\) is precisely \(\nu_m-\nu_{m-1}<0\). Hence \(F_m\) is not positive semidefinite and \(\Psi_{m,m-1}\) is not positive. This proves the necessity under universal quantification. The same witness proves the finite-horizon statement.

**4. An increasing-hazard obstruction.** For \(h_1=1/10\), \(h_2=9/10\), and \(h_j=91/100\) for \(j\ge3\), the interarrival probabilities are \(p_1=1/10\), \(p_2=81/100\), and \(p_3=819/10000\). Renewal convolution gives \(\nu_1=p_1\), \(\nu_2=p_2+p_1^2\), and \(\nu_3=p_3+2p_1p_2+p_1^3\), which yields the theorem's fractions. For the three-cycle witness, \(S_2=9/100\), and the smallest eigenvalue of \(F_3\) is \((\nu_3-\nu_2)/S_2=-639/100\).

For completeness, nondecreasing \(h_j\) produces valid Schrödinger one-step CPTP intermediates. Repeating step 2 in the Schrödinger picture gives
\[
\Lambda_{t,t-1}(X)
=(1-h_t)UXU^{-1}+\operatorname{tr}(X)C_t,
\]
with
\[
C_t=\nu_t\sigma+
\sum_{s=1}^{t-1}\nu_sS_{t-1-s}(h_t-h_{t-s})\sigma_{t-s}.
\]
All coefficients are nonnegative under increasing hazards, and \(\operatorname{tr}C_t=h_t\), so these are CPTP. This proves the advertised strict separation independently of any earlier derived statement.

## Verification

The standalone `verify_heisenberg.py` numerically constructs each full Heisenberg superoperator on matrix-unit bases and independently compares its exact matrix inverse intertwiner against the derived \(F_t\)-representation, for dimensions \(2,3,4\) and four different hazard sequences per dimension. A second family uses cyclic-shift unitaries in dimensions \(3,4,5,6\). The program also checks renewal normalization, exact benchmark renewal masses and the negative witness eigenvalue. The packaged program reports 89 successful deterministic comparisons; finite numerical tests supplement but do not replace the preceding all-dimensional proof.

## Relationship to prior work

Carollo and Wald (arXiv:2601.13367v1, main text and supplementary material) introduce the same age-dependent quantum reset renewal dynamics, the Schrödinger and Heisenberg intertwining definitions, and numerical/special-case examples of unequal divisibility. Their examples and formulas are prior work. The present theorem instead provides a *necessary and sufficient universal criterion*, expressed entirely in the monotonicity of the classical renewal **event** sequence, and a cyclic-unitary witness for every violation; the existing special nondivisibility example does not establish this iff classification.

Wald, Yao, Platini, Hooley and Carollo (arXiv:2410.11497v3) derive the reset-age probabilities and stationary-state criteria, but do not classify Heisenberg P/CP-divisibility. Settimo et al. (arXiv:2506.08103v2) develop the general distinction between the two pictures and provide examples and witnesses, but not the above renewal-sequence equivalence.

The standard facts that a positive matrix defines a completely positive rank-one measure-and-replace map and that cyclic shifts provide orthogonal orbits are elementary tools, not claimed as new. The classical renewal convolution is also prior theory. The new content assessed here is the exact dual-intertwiner reduction and the two-way all-gate classification built from it.

## Limitations

The theorem requires a fixed unitary between resets, a fixed reset state, classical state-independent renewal hazards satisfying \(0<h_j<1\), and finite Hilbert spaces of dimension at least two. Its **universal** necessity uses gates of dimension growing with the earliest violation time; it does not assert the same necessity for one fixed qubit gate. It does not classify arbitrary nonunitary between-reset channels, singular survival probabilities, quantum-coherent reset protocols, or the process-tensor Markov property. A particular unitary-reset pair can remain Heisenberg divisible even when \(\nu_t\) decreases.

## References

1. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367v1 (first posted 2026-01-19), especially main-text equations (2)--(6) and the supplemental discussion of intertwining maps. https://arxiv.org/html/2601.13367v1
2. F. Settimo, A. Smirne, K. Luoma, B. Vacchini, J. Piilo and D. Chruściński, *Divisibility of dynamical maps: Schrödinger vs. Heisenberg picture*, arXiv:2506.08103v2 (2026 revision). https://arxiv.org/html/2506.08103v2
3. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v3. https://arxiv.org/html/2410.11497v3
