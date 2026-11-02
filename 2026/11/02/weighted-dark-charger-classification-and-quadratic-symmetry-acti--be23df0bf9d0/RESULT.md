# Weighted-dark charger classification and quadratic symmetry activation in two-qubit collisional batteries

## Finding

A fresh two-qubit charger with unequal exchange couplings to a qubit battery has an exactly characterized family of pure states that preserve a completely charged battery while charging any initially incompletely charged battery. This family has a sharp affine concurrence–charging-rate relation and a quadratic symmetry-breaking effect: a weighted dark state inactive at equal couplings becomes a charger under arbitrarily small coupling imbalance. With adaptive *local product* readout of the charger, all nonzero-probability branches have exactly the same battery energy expectation at every collision.

Write \(G=\sqrt{g_1^2+g_2^2}\), \(\Delta=\omega_b-\omega_0\), and
\[
q=\frac{4G^2}{\Delta^2+4G^2}\sin^2\!\left(\frac{\tau\sqrt{\Delta^2+4G^2}}2\right),\qquad
\mathcal C_D=\frac{2g_1g_2}{G^2}.
\]
For \(0<q<1\), define
\[
|D\rangle=\frac{g_1|10\rangle-g_2|01\rangle}{G},\quad
|\chi_{c,\varphi}\rangle=\sqrt{1-c}|11\rangle+e^{i\varphi}\sqrt c|D\rangle,
\quad 0\le c\le1.
\]
**Classification:** a pure fixed charger leaves the battery excited state invariant in population if and only if it lies in \(\operatorname{span}\{|11\rangle,|D\rangle\}\), up to global phase. **Exact law:** each such charger gives, for every battery input with excited probability \(e\),
\[
e'=e+r(1-e),\qquad r=q(1-c\mathcal C_D^2).
\]
Its concurrence is \(\mathcal C=c\mathcal C_D\), hence \(r=q(1-\mathcal C_D\mathcal C)\). There exist adaptive, local, two-qubit projective measurements of every outgoing charger such that every occurring branch has excited probability \(e'\). Repeating identical fresh chargers yields
\[
e_n=1-(1-e_0)(1-r)^n.
\]
In particular, for a pure weighted dark charger \(c=1\), \(g_1=g_2\) yields \(r=0\); for \(g_1=g(1+\epsilon)\) and \(g_2=g(1-\epsilon)\), with \(g>0\) and \(0<|\epsilon|<1\),
\[
r=\frac{4q\epsilon^2}{(1+\epsilon^2)^2}>0.
\]
Thus the previously inactive charger converges to full charge for every nonzero asymmetry, with quadratic small-imbalance rate.

## Assumptions and scope

The charger consists of two two-level systems of the same transition frequency \(\omega_0\), and the battery is one two-level system of frequency \(\omega_b\). Couplings \(g_1,g_2>0\) are real, independent and fixed. With \(\hbar=1\), the Hamiltonian is
\[
H=\omega_0(n_1+n_2)+\omega_b n_B+
\sum_{j=1}^2g_j(\sigma_j^+\sigma_B^-+\sigma_j^-\sigma_B^+).
\]
Every interaction lasts \(\tau>0\); the outgoing charger is measured and discarded; each subsequent charger is freshly prepared in the same pure state. The battery may have any initial pure phase, with excited-state probability \(e_0\in[0,1]\); the unconditional one-step population law also holds for mixed inputs. We require \(0<q<1\) to avoid stroboscopic freezing and the perfect-swap endpoint. A phase-independent result means independent of every coherence phase in the battery input. “Zero fluctuations” refers solely to the variance, across conditional trajectories, of the *expectation* of the battery energy, not the generally nonzero variance of a single projective battery-energy measurement. No energy, preparation, or measurement implementation cost is included.

## Proof

**1. Two distinct bright directions.** Excitation number is conserved. In the one-total-excitation sector \(|00,1\rangle\) couples with amplitude \(G\) to the charger bright state
\[
|B_{\uparrow}\rangle=\frac{g_1|10\rangle+g_2|01\rangle}{G}
\]
with the battery ground. In the two-total-excitation sector the state \(|11,0\rangle\) couples to
\[
|B_{\downarrow}\rangle=\frac{g_2|10\rangle+g_1|01\rangle}{G}
\]
with the battery excited. The normalized \(|D\rangle\) is orthogonal to \(|B_{\downarrow}\rangle\), so \(|D,1\rangle\) is invariant up to a phase, whereas
\[
\langle B_{\uparrow}|D\rangle=\frac{g_1^2-g_2^2}{G^2}=:\delta_g.
\]
Both active sectors reduce to the two-level detuned Rabi Hamiltonian with coupling magnitude \(G\), and therefore share the population transition probability \(q\) displayed above. The orthogonal dark mode of each sector accumulates phase but has zero transition probability.

**2. Full-charge fixed-point classification.** Write an arbitrary normalized pure charger
\[
|\chi\rangle=a_{00}|00\rangle+|\zeta\rangle+a_{11}|11\rangle,
\quad |\zeta\rangle\in\operatorname{span}\{|01\rangle,|10\rangle\}.
\]
With battery input \(|1\rangle\), the output battery-ground component receives orthogonal contributions from the total-excitation-one and -two sectors. Its probability is exactly
\[
p_{1\to0}=q\big(|a_{00}|^2+|\langle B_{\downarrow}|\zeta\rangle|^2\big).
\]
For \(q>0\), this vanishes exactly when \(a_{00}=0\) and \(|\zeta\rangle\) is proportional to \(|D\rangle\). This proves necessity and sufficiency, without assuming the battery's phase or imposing a family of charger amplitudes in advance.

**3. The phase-independent pumping channel.** For \(|\chi_{c,\varphi}\rangle\), a battery-ground input can be excited only by \(|11\rangle\) transferring one quantum with probability \(q\), or by \(|D\rangle\) transferring one with probability \(q|\langle B_{\uparrow}|D\rangle|^2=q\delta_g^2\). Those outgoing excited components have mutually orthogonal charger sectors (one versus zero charger excitations). The probability of upward excitation is therefore
\[
r=q[(1-c)+c\delta_g^2]=q(1-c\mathcal C_D^2).
\]
The battery-excited input never discharges, by Step 2. Moreover, its outgoing excited charger component lies in \(\operatorname{span}\{|11\rangle,|D\rangle\}\), orthogonal to the excited component obtained from a battery-ground input, which lies in \(\operatorname{span}\{|B_{\downarrow}\rangle,|00\rangle\}\). Hence input coherence makes no interference contribution to the output excited probability. Thus \(e'=e+r(1-e)\) for every pure or mixed battery input. The normalized two-qubit pure-state concurrence is \(2|a_{00}a_{11}-a_{01}a_{10}|=c\mathcal C_D\); substituting gives the exact affine rigidity relation \(r=q(1-\mathcal C_D\mathcal C)\).

**4. Existence of local product energy-equalizing measurements.** The following elementary lemma applies to any pure outgoing joint state, independently of the Hamiltonian: write \(|\Psi\rangle=|A\rangle|0\rangle+|B\rangle|1\rangle\) with \(p=\|B\|^2\in(0,1)\), and set \(a=A/\|A\|\), \(b=B/\|B\|\), \(Q=|a\rangle\langle a|-|b\rangle\langle b|\). Expand this traceless two-qubit Hermitian operator in local Pauli observables; let its one-body Bloch vectors be \(u,v\in\mathbb R^3\) and correlation matrix \(T\in\mathbb R^{3\times3}\). Choose a unit Bloch axis \(n\perp u\) (even in the \(xz\)-plane) and then a unit axis \(m\perp\{v,T^{\mathsf T}n\}\); these axes always exist in \(\mathbb R^3\). For product outcome projectors \(P_{s,t}=\frac14(I+s\,n\cdot\sigma)\otimes(I+t\,m\cdot\sigma)\), the Pauli expansion gives
\[
\operatorname{tr}(QP_{s,t})=\frac14[s\,u\cdot n+t\,v\cdot m+st\,n^{\mathsf T}Tm]=0
\]
for all four signs. Therefore \(\langle a|P_{s,t}|a\rangle=\langle b|P_{s,t}|b\rangle\), so the conditional excited probability for any outcome of nonzero probability is exactly \(p\). If \(p=0\) or \(1\), equalization is automatic. Reapply the construction after each fresh collision. Since the conditional population recurrence is phase independent, induction gives the same deterministic \(e_n\) on all trajectories and the closed form stated above.

**5. Quadratic symmetry activation.** Direct substitution yields
\[
\delta_g=\frac{g_1^2-g_2^2}{g_1^2+g_2^2}
=\frac{2\epsilon}{1+\epsilon^2},
\]
so the dark-only charging rate is \(r=q\delta_g^2=4q\epsilon^2/(1+\epsilon^2)^2\). This is zero only at exact coupling symmetry; \(0<q<1\) and \(g_j>0\) imply all the remaining charger family except that single symmetric-dark endpoint charges to unity. The equality \(\delta_g^2+\mathcal C_D^2=1\) proves the rate–concurrence identity on the entire classified family.

## Verification

Run `python verify_weighted_dark.py` with Python, NumPy and SciPy. The standalone script constructs the full \(8\times8\) Hermitian Hamiltonian independently, computes its matrix exponential, tests the Rabi-derived population map and the full-charge leakage criterion for random arbitrary complex chargers, and constructs local product axes directly from Bloch tensors. It verifies equality of the conditional excited probabilities for each nonzero-probability measurement outcome. The tested parameter set includes symmetric and asymmetric couplings, variable detuning, collision duration, input phase and charger entanglement. A successful run prints its actual assertion count. Finite tests corroborate formulas and do not constitute the proof for all continuous parameters; the derivation above supplies that proof.

## Relationship to prior work

Gong, Zhang and Li (2026, arXiv:2610.31242v1, first posted October 22) develop identical conditional energies under adaptive readout for two qubit chargers, explicitly specializing their Hamiltonian to the same exchange coupling \(g\) for each charger. Their printed Bell-like families and general identical-coupling population recurrence do not determine the complete full-charge fixed-point family for unequal \(g_1,g_2\), the two distinct weighted bright directions, or the quadratic activation law. The local readout equalization method is a known motivation; the elementary constructive lemma above gives an independent justification without claiming it as an exclusive novelty. Seah et al. (2021) study repeated *single-qubit* charger units, a different interaction architecture. Quach and Munro (2020) study reservoir-mediated *open* battery stabilization by dark states; the shared language does not imply this finite, closed-collision, local-readout classification. Related spin-charger and collision works may contain implicit reductions; no exhaustive priority certification is claimed.

## Limitations

The theorem is for two noninteracting charger qubits with equal local energy gaps, strictly positive real exchange couplings, ideal identical-duration unitary collisions and freshly reset pure chargers. The energy-expectation fluctuation claim presumes ideal adaptive outcome-conditioned local measurement and feed-forward basis selection; battery-energy shot noise remains. Neither battery ergotropy nor net thermodynamic cost, finite readout accuracy, thermal noise, intercharger coupling, coupling disorder between steps or higher-dimensional charger classification is covered. The nontrivial \(0<q<1\) assumption avoids the degenerate collision zeros and perfect-transfer limit. published-finding corpus and targeted literature comparisons are best-knowledge priority checks, not independent audits.

## References

1. L. Gong, J. Zhang, Y. Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States*, arXiv:2610.31242v1 (first public October 22, 2026), https://arxiv.org/html/2610.31242v1.
2. L. Gong, J. Zhang, Y. Li, *Achieving Identical Stored Energy in Cascaded Collisional Quantum Battery Charging: Analytical Results*, arXiv:2610.01332 (2026), https://arxiv.org/abs/2610.01332.
3. S. Seah et al., *Quantum Speed-Up in Collisional Battery Charging*, Phys. Rev. Lett. 127, 100601 (2021), https://doi.org/10.1103/PhysRevLett.127.100601.
4. J. Q. Quach and W. J. Munro, *Using Dark States to Charge and Stabilize Open Quantum Batteries*, Phys. Rev. Applied 14, 024092 (2020), https://doi.org/10.1103/PhysRevApplied.14.024092.
5. Y. Huangfu and J. Jing, *High-capacity and high-power collective charging with spin chargers*, Phys. Rev. E 104, 024129 (2021), https://arxiv.org/abs/2109.00687.
