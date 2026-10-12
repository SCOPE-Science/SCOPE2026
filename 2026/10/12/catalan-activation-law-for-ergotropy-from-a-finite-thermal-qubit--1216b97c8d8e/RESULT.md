# Catalan activation law for ergotropy from a finite thermal qubit bath

## Finding
Consider a qubit of energy gap \(\varepsilon>0\), initially in its ground state, and \(n\ge1\) independent bath qubits of the same gap, initially in the product Gibbs state with Boltzmann factor \(q=e^{-\beta\varepsilon}\in[0,1]\). Let \(F_n(q)\) be the greatest target excitation probability achievable by **one arbitrary global energy-conserving unitary**, with no work storage system, followed by discarding the bath. Then
\[
F_n(q)=\frac{1}{(1+q)^n}\sum_{k=1}^n\min\!\left\{\binom nk,\binom n{k-1}\right\}q^k.
\]
Writing \(C_j=\binom{2j}{j}/(j+1)\) for the Catalan numbers, the exact all-size solution is
\[
\boxed{F_{2m}(q)=F_{2m-1}(q)=\frac{q}{1+q}\sum_{j=0}^{m-1}C_j\left(\frac{q}{(1+q)^2}\right)^j}\qquad(m\ge1),
\]
and the improvement upon adding the next **pair** of bath qubits is
\[
\boxed{F_{2m+1}(q)-F_{2m-1}(q)=C_m\frac{q^{m+1}}{(1+q)^{2m+1}}}\qquad(m\ge1).
\]
The maximal output ergotropy is \(\mathcal W_n(q)=\varepsilon[2F_n(q)-1]_+\). Thus no finite bath can activate ergotropy if \(q\le\tfrac12\). For every \(q>\tfrac12\) a finite odd bath size suffices; even bath sizes are exactly redundant. If \(n_{\min}(q)\) denotes the least successful bath size, then as \(\delta=q-\tfrac12\downarrow0\),
\[
\boxed{n_{\min}(q)=\frac{2}{\log(9/8)}\left[\log\frac1\delta-\frac32\log\log\frac1\delta\right]+O(1).}
\]
This counts bath qubits, not Hilbert-space dimensions. All maxima are attained by blockwise permutations of computational-basis states conserving total excitation number.

## Assumptions and scope
Use the target Hamiltonian \(H_S=\varepsilon|1\rangle\langle1|\) and bath Hamiltonian \(H_B=\varepsilon\sum_{j=1}^n|1\rangle_j\langle1|\). The input is \(|0\rangle\langle0|\otimes\tau_q^{\otimes n}\), where \(\tau_q=(|0\rangle\langle0|+q|1\rangle\langle1|)/(1+q)\). Optimize over all global unitaries \(U\) satisfying \([U,H_S+H_B]=0\). No locality, depth, catalyst, repeated collision, or upper bound on control complexity is imposed. Absolute zero \(q=0\) and infinite temperature \(q=1\) are included as limits. Ergotropy means the maximum work extractable from the **reduced target state** by a subsequently unrestricted target-only unitary.

## Proof
**1. Exact constrained optimum.** At total excitation number \(k\), the target-ground subspace has dimension \(a_k=\binom nk\), and the target-excited subspace has dimension \(b_k=\binom n{k-1}\), with out-of-range binomial coefficients defined as zero. The input block has precisely \(a_k\) equal positive eigenvalues \(q^k/(1+q)^n\) and \(b_k\) zero eigenvalues. For any projector of rank \(b_k\), the Ky Fan variational principle bounds its output expectation by \(\min(a_k,b_k)q^k/(1+q)^n\). This is attained by exchanging \(\min(a_k,b_k)\) mutually orthogonal target-ground basis states with target-excited basis states in the same excitation sector. The direct sum of these sector permutations commutes with total energy and simultaneously saturates the bounds. Summing over \(k\) yields the asserted formula for \(F_n\). Every output target state is diagonal: the initial joint state commutes with total energy, so the evolved joint state also commutes with total energy, and its target partial trace commutes with \(H_S\) by time-translation covariance. A diagonal qubit with excited population \(p\) has ergotropy \(\varepsilon\max(0,2p-1)\). Thus maximizing \(p\) also maximizes ergotropy.

**2. Binomial parity and Catalan increments.** Define the numerator polynomial \(A_n(q)=(1+q)^nF_n(q)\). A binomial row is increasing up to its center and decreasing thereafter. Using \(\binom nk=\binom{n-1}k+\binom{n-1}{k-1}\), the coefficients of \(A_{2m}\) coincide, term by term, with those of \((1+q)A_{2m-1}\); this includes the central two coefficients by binomial symmetry. Hence \(F_{2m}=F_{2m-1}\). Comparing \(A_{2m+1}\) with \((1+q)^2A_{2m-1}\), the same Pascal comparison cancels every coefficient except the coefficient at degree \(m+1\). That discrepancy is
\[
\binom{2m-1}{m}-\binom{2m-1}{m+1}=\frac1{m+1}\binom{2m}m=C_m.
\]
Consequently \(A_{2m+1}=(1+q)^2A_{2m-1}+C_mq^{m+1}\). As \(F_1=q/(1+q)\), induction gives the two claimed Catalan formulas, with every boundary coefficient accounted for.

**3. Sharp activation.** Put \(z=q/(1+q)^2\). The Catalan generating function satisfies \(\sum_{j\ge0}C_jz^j=(1-\sqrt{1-4z})/(2z)\) for \(0<z\le1/4\). Since \(0<q\le1\) implies \(\sqrt{1-4z}=(1-q)/(1+q)\), one gets \(F_{2m-1}(q)\uparrow q\) as \(m\to\infty\), and the inequality is strict at every finite \(m\) when \(q>0\). Therefore \(q\le1/2\) precludes inversion at every finite size, while \(q>1/2\) eventually allows it. For each fixed \(m\), \(F_{2m-1}(q)\) increases strictly with \(q\in[0,1]\): the derivative of the \(j\)-th summand \(q^{j+1}/(1+q)^{2j+1}\) has the strictly positive sign of \((j+1)-jq\). For \(m\ge2\), \(F_{2m-1}(1/2)<1/2\) while \(F_{2m-1}(1)\ge F_3(1)=5/8\). There is consequently one crossing \(q_m\in(1/2,1)\), given exactly as the unique root of \(F_{2m-1}(q_m)=1/2\). The Catalan increment is positive for \(q>0\), so \(q_{m+1}<q_m\) and \(q_m\downarrow1/2\). The first successful bath size is always odd.

**4. Sharp size divergence.** Let \(\delta=q-1/2>0\), \(r(q)=4q/(1+q)^2\) and \(T_m(q)=q-F_{2m-1}(q)\). The exact nonnegative series tail is
\[
T_m(q)=\frac{q}{1+q}\sum_{j=m}^{\infty}C_j\left(\frac{q}{(1+q)^2}\right)^j.
\]
By Stirling's formula, \(C_j=4^j/(\sqrt\pi\,j^{3/2})(1+O(j^{-1}))\). Uniformly for \(q\) in a fixed sufficiently small neighborhood of \(1/2\), one has \(0<r(q)<1\) and summing the exponentially dominated tail gives
\[
T_m(q)=\frac{q}{(1+q)\sqrt\pi(1-r(q))}\frac{r(q)^m}{m^{3/2}}(1+O(m^{-1})).
\]
Here \(r(1/2)=8/9\) and the prefactor tends to \(3/\sqrt\pi\). Let \(m_*(q)\) be the least integer with \(T_m(q)<\delta\); the least successful bath has size \(2m_*-1\). Since \(T_{m_*-1}\ge\delta>T_{m_*}\), the displayed two-sided tail estimates first imply \(m_*=\Theta(\log(1/\delta))\). Thus \(m_*\delta\to0\), permitting \(\log r(q)=\log(8/9)+O(\delta)\) to be replaced by its endpoint value with bounded total error. Taking logarithms across the crossing yields
\[
m_*\log(9/8)+\tfrac32\log m_*=\log(1/\delta)+O(1).
\]
Solving by one substitution gives \(m_*=[\log(1/\delta)-\tfrac32\log\log(1/\delta)]/\log(9/8)+O(1)\); the announced formula follows from \(n_{\min}=2m_*-1\). This is a true two-sided \(O(1)\) error, not an unquantified leading-order equivalence.

**5. Representative exact instance.** At \(q=2/3\), the optimal excited populations for bath sizes \(n=1,2\) are \(2/5\), for \(n=3,4\) are \(62/125<1/2\), and for \(n=5,6\) are \(1694/3125>1/2\). Thus five thermal qubits are necessary and sufficient, and the maximal target ergotropy is exactly \(263\varepsilon/3125\).

## Verification
The included standard-library script `verify.py` uses exact rational arithmetic. It computes excitation-sector ranks independently by enumerating bath bit strings for \(n\le9\), checks the binomial and Catalan closed formulas through \(n=13\), checks the odd-even and pair-gain identities through \(m=20\), verifies the numerator polynomial coefficient identity through \(m=24\), and checks the infinite-temperature central-binomial identity \(F_{2m-1}(1)=1-4^{-m}\binom{2m}m\). Its recorded execution returned `VERIFY_OK 509 exact arithmetic checks`. These are finite checks of explicit identities; the arguments above, not enumeration, establish the universal conclusions and asymptotic.

## Relationship to prior work
Singh, Saha, and Sen (2026) study ergotropy injection by thermal environments, including an impossibility for a **single thermal qubit** and possible injection with a thermal qutrit. The present result agrees with the single-qubit impossibility but instead solves the distinct all-size problem of one energy-conserving interaction with \(n\) *independent, identical-gap thermal qubits*. Standard thermal-operations and finite-bath majorization results, including Scharlau and Mueller (2018), motivate the energy-shell rank optimization; this basic variational principle is not claimed as new. The contribution is the closed finite-size Catalan/parity law, exact inversion classification, and sharp logarithmic-plus-logarithmic-correction resource threshold. Yáñez-Soria et al. (2026) analyze repeated interactions with thermal-ancilla clusters that charge through steady-state coherence rather than the single-shot diagonal population inversion considered here. Łobejko (2021) treats finite heat baths in general work-extraction inequalities rather than the identical-gap bath-size optimum derived here. Source-access limitations and possible alternative specializations are recorded in the accompanying review.

## Limitations
Only the specified pure-ground-state target, identical-gap independent bath qubits, Gibbs input, and arbitrary *global* energy-preserving unitaries are covered. The theorem does not provide low-depth protocols, bounds on interaction strength or time, robustness to imperfect energies or bath correlations, work cost of implementing the unitary, or an optimum for arbitrary finite reservoirs. The bound \(n_{\min}\) describes existence of a mathematically permitted unitary, not experimentally efficient implementation. Only the published abstracts, not the full text, of the closest 2026 ergotropy-injection and thermal-cluster preprints could be inspected; coverage in inaccessible body text cannot be excluded.

## References
1. D. Singh, D. Saha, U. Sen, *Towards minimal conditions for ergotropy injection in open quantum systems*, arXiv:2609.04457v1, first posted 2026-09-03, https://arxiv.org/abs/2609.04457.
2. J. Scharlau, M. P. Mueller, *Quantum Horn's lemma, finite heat baths, and the third law of thermodynamics*, Quantum **2**, 54 (2018), https://doi.org/10.22331/q-2018-02-22-54.
3. O. S. Yáñez-Soria, G. Guarnieri, B. Çakmak, R. Román-Ancheyta, *Ergotropy from energetic coherence and the third law of thermodynamics*, arXiv:2609.38724v1 (2026), https://arxiv.org/abs/2609.38724.
4. M. Łobejko, *The tight Second Law inequality for coherent quantum systems and finite-size heat baths*, Nature Communications **12**, 918 (2021), https://doi.org/10.1038/s41467-021-21140-4.
5. L. Bassman Oftelie, A. De Pasquale, M. Campisi, *Dynamic Cooling on Contemporary Quantum Computers*, PRX Quantum **5**, 030309 (2024), https://doi.org/10.1103/PRXQuantum.5.030309.
