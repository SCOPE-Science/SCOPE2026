# Zero collective dipole exactly characterizes phase-blind two-qubit quantum-battery chargers

## Finding
For a pair of identically exchange-coupled qubit chargers, the vanishing of their **collective transverse dipole** is a necessary and sufficient condition for the collision's battery excitation to be independent of *every* incoming battery relative phase, at any generic interaction duration. This supplies a complete complex-amplitude classification, an exact affine energy recurrence under locally measured collisions, and an explicit coherent **separable** example outside the usual Bell-like families.

Write \(|B\rangle=(|01\rangle+|10\rangle)/\sqrt2\) and \(|D\rangle=(|01\rangle-|10\rangle)/\sqrt2\). For the arbitrary pure charger
\[
|\chi\rangle=a|00\rangle+b|B\rangle+c|D\rangle+d|11\rangle,
\qquad |a|^2+|b|^2+|c|^2+|d|^2=1,
\]
put \(Q=\bar a b+\bar b d\). Whenever the collision's transfer amplitude and survival amplitude are both nonzero, the exact characterization is
\[
\boxed{\text{Phase independence for all battery phases}\quad\Longleftrightarrow\quad Q=0\quad\Longleftrightarrow\quad\langle\chi|J_-|\chi\rangle=0,}\qquad J_-=\sigma_1^-+\sigma_2^-.
\]
The condition accommodates arbitrary dark-singlet admixture \(c\), and for \(b\neq0\) it is the concrete constraint \(d=-\bar a b/\bar b\), up to normalization. It is not equivalent to separability, absence of coherence, or the battery already being fully excited.

## Assumptions and scope
The charger consists of spins \(1,2\), the battery of spin \(b\). The eigenvalue of \(n_j=\sigma_j^+\sigma_j^-\) is \(0\) on \(|0\rangle\) and \(1\) on \(|1\rangle\). We use \(\hbar=1\), a fixed time \(\tau>0\), equal real couplings \(g>0\), bare charger frequency \(\omega_0\), and battery frequency \(\omega_b>0\). The Hamiltonian during a collision is
\[
H=\omega_0(n_1+n_2)+\omega_b n_b+g\sum_{j=1}^{2}(\sigma_j^+\sigma_b^-+\sigma_j^-\sigma_b^+),
\qquad \Delta=\omega_b-\omega_0,
\qquad \Omega=\sqrt{\Delta^2+8g^2}.
\]
There are no extraneous drives, dissipation, unequal couplings or interactions between successive fresh chargers. Before the collision the battery is any pure state \(\sqrt{1-e}|0\rangle+\sqrt e\,e^{i\gamma}|1\rangle\), with \(0\le e\le1\) and arbitrary phase \(\gamma\) when \(0<e<1\). The observable is its mean excitation \(e=\langle n_b\rangle\), not its single-shot energy outcome.

Define the amplitudes and excitation-transfer probability
\[
 u=\cos(\Omega\tau/2)-i\frac{\Delta}{\Omega}\sin(\Omega\tau/2),\qquad
 v=-i\frac{2\sqrt2 g}{\Omega}\sin(\Omega\tau/2),\qquad
 p=|v|^2=\frac{8g^2}{\Omega^2}\sin^2(\Omega\tau/2).
\]
They obey \(|u|^2+|v|^2=1\). The classification's *generic-pulse* hypothesis is \(uv\neq0\); in particular \(0<p<1\). The exceptional cases \(p=0\) and \(u=0\) are addressed below.

## Proof
**1. Exact phase-dependent energy map.** Total excitation is conserved. In the one-excitation sector the only interacting pair is \(|B,0\rangle\) and \(|00,1\rangle\), and in the two-excitation sector it is \(|11,0\rangle\) and \(|B,1\rangle\). In both, the off-diagonal matrix element is \(\sqrt2g\) and the diagonal energy difference is \(\Delta\); the states \(|D,0\rangle\) and \(|D,1\rangle\) are dark. Exponentiating these two \(2\times2\) blocks and tracing the final battery number operator gives the identity
\[
\begin{aligned}
 e'={}&e+p\bigl[(|b|^2+|d|^2)-e(|a|^2+2|b|^2+|d|^2)\bigr]\\
 &+2\sqrt{e(1-e)}\operatorname{Re}\left[e^{-i\gamma}\bar u v(\bar a b+\bar b d)\right].
\end{aligned}
\]
This identity includes detuning and complex charger amplitudes without approximations; the dark amplitude \(c\) enters through normalization but contributes no transition or interference term.

**2. Necessary and sufficient cancellation.** Fix any \(e\in(0,1)\) and \(uv\neq0\). The last term is constant as \(\gamma\) varies through all of \([0,2\pi)\) precisely if its complex coefficient \(Q=\bar a b+\bar b d\) vanishes. Since \(J_-|B\rangle=\sqrt2|00\rangle\), \(J_-|11\rangle=\sqrt2|B\rangle\), and \(J_-|D\rangle=0\), one has \(\langle J_-\rangle=\sqrt2Q\). This proves the equivalence, and in particular shows that cancellation for one non-pole population entails cancellation for all pure input battery states.

**3. Local product measurements can equalize every branch.** After a collision let the normalized joint pure state be \(|\Psi\rangle=|\psi_0\rangle|0\rangle+|\psi_1\rangle|1\rangle\), where the unnormalized \(|\psi_j\rangle\) are two-qubit charger vectors and \(P_j=\langle\psi_j|\psi_j\rangle\). If \(P_0P_1=0\), all nonempty branches already have identical battery populations. Otherwise set
\[
D=\frac{|\psi_1\rangle\langle\psi_1|}{P_1}-\frac{|\psi_0\rangle\langle\psi_0|}{P_0},\qquad \operatorname{Tr}D=0.
\]
Define real Pauli coefficients \(r_i=\operatorname{Tr}[D(\sigma_i\otimes I)]\), \(s_j=\operatorname{Tr}[D(I\otimes\sigma_j)]\), \(T_{ij}=\operatorname{Tr}[D(\sigma_i\otimes\sigma_j)]\). Choose a unit Bloch vector \(n\perp r\); then choose a unit \(m\perp s\) and \(m\perp T^\top n\). Such vectors always exist in \(\mathbb R^3\), including degenerate cases. For the four local product-basis projectors \(\Pi_{\alpha\beta}=\frac14(I+\alpha n\cdot\sigma)\otimes(I+\beta m\cdot\sigma)\), with \(\alpha,\beta\in\{+1,-1\}\), the Pauli expansion yields
\[
\operatorname{Tr}(D\Pi_{\alpha\beta})=\tfrac14[\alpha(r\cdot n)+\beta(s\cdot m)+\alpha\beta\, n^\top Tm]=0.
\]
Hence the unnormalized outcome probabilities satisfy \(q_{1,\alpha\beta}/P_1=q_{0,\alpha\beta}/P_0\). Every outcome of nonzero total probability therefore has battery excited fraction exactly \(P_1\), the unconditional postcollision value. This is an explicit existence construction using **only separate single-qubit projective measurements**, with axes allowed to depend on the known premeasurement state.

**4. Closed collision recurrence.** Under \(Q=0\), define \(A=|b|^2+|d|^2\) and \(B=|a|^2+2|b|^2+|d|^2\), both nonnegative. If each collision uses an identically prepared fresh charger and its outgoing local product-basis measurement is selected as above, all nonzero-probability branches have the deterministic excited population
\[
e_{n+1}=(1-pB)e_n+pA.
\]
For \(B>0\) this solves to
\[
\boxed{e_n=\frac AB+\left(e_0-\frac AB\right)(1-pB)^n.}
\]
Because \(0\le pB\le2\), the fixed-point value is reached when \(0<pB<2\); the edge \(pB=2\) permits a period-two population sequence. If \(B=0\), the charger is the pure dark singlet and no energy moves. Thus ideal branchwise *mean* stored energy \(\omega_b e_n\) has zero trajectory variance, although each individual battery energy measurement can remain random.

**5. Coherent separable witness.** The product charger
\[
|\chi_\times\rangle=|+\rangle\otimes|-\rangle
=\frac{|00\rangle-|01\rangle+|10\rangle-|11\rangle}{2}
\]
has \(a=1/2\), \(b=0\), \(c=-1/\sqrt2\), \(d=-1/2\). It has nonzero coherences and nonzero support in the zero-, one- and two-excitation charger sectors, yet \(Q=0\). Moreover \(A=1/4\), \(B=1/2\), and from a battery ground state
\[
\boxed{e_n=\frac12\left[1-(1-p/2)^n\right].}
\]
It is a *separable state outside the computational basis and outside either two-basis-state Bell-like subspace*. Its two single-qubit transverse polarizations cancel as a collective dipole.

At exceptional collision times \(v=0\), no population exchange occurs; at \(u=0\) (only at resonance and a complete transfer pulse), the phase-dependent interference vanishes for every charger. These exceptional pulses do not satisfy the stated generic-pulse necessity and are not counterexamples.

## Verification
The accompanying standalone `verify.py`, executable with Python 3, NumPy and SciPy, independently builds the full three-qubit \(8\times8\) Hamiltonian and exponentiates it. It compares exact collision energies with the closed formula over randomized complex charger states and arbitrary detuning; checks local product projective measurement branches; explores independent phase choices; and checks both bright-cancellation families and the separable witness. It reports 4,600 passing finite-dimensional assertions with a deterministic random seed. The infinite-parameter statement follows from the above algebra, **not** from these finite checks.

## Relationship to prior work
Gong, Zhang and Li (October 2026, arXiv:2610.31242) introduced the motivating two-charger/one-battery collision and adaptive measurement setting, and reported Bell-like charger families with phase-independent stored energy. Their earlier work (arXiv:2610.01332) establishes energy equalization for a single charger qubit. These achievements are assumed background, not presented as new. The new result is the *necessary-and-sufficient collective-dipole cancellation condition for all pure two-qubit charger states* in the explicitly written Hamiltonian, along with its coherent separable non-Bell witness and resulting exact map.

Li, Chen, Yu and Hao (Physical Review A 113, 052437, 2026) study phase-controlled pairs of coherent ancillas and an antiphase charging regime in a multilevel, master-equation setting; their published abstract does not establish the present local post-collision measurement criterion. Quach and Munro (2020) use dark states to stabilize open-system batteries with collective reservoir coupling; that is not the present closed three-qubit repeated-collision map. Earlier quantum collisional battery studies by Seah and coauthors address coherent charging and energy fluctuations without this all-pure-state phase-blind characterization.

## Limitations
The theorem concerns a precisely specified ideal equal-coupling exchange Hamiltonian and an adaptive, known-state projective measurement protocol. It does not cover unequal or complex couplings, noisy or inefficient readout, thermal or mixed incoming battery states without a separate proof, memory across chargers, the thermodynamic cost of charger preparation or measurement, or the variance of projective battery energy outcomes. The phase-blind class includes physically distinct chargers with different energy fixed points and rates; it does not imply maximum useful work. The highest-priority originality uncertainty is the full text of the related phase-controlled coherent-ancilla study, which was not available for comparison; only its abstract could be assessed. The principal motivating preprint's displayed equations in web rendering were partly inaccessible; the independent proof is tied to the explicit Hamiltonian above rather than to any unverified reading of omitted equations.

## References
1. L. Gong, J. Zhang and Y. Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States* (2026), arXiv:2610.31242, first publicly submitted October 22, 2026. https://arxiv.org/abs/2610.31242
2. L. Gong, J. Zhang and Y. Li, *Achieving Identical Stored Energy in Cascaded Collisional Quantum Battery Charging: Analytical Result* (2026), arXiv:2610.01332. https://arxiv.org/abs/2610.01332
3. H. Li, X. Chen, W. Yu and Y. Hao, *Charging optimization of quantum battery via phase-controlled coherent ancillae*, Physical Review A **113**, 052437 (2026). https://doi.org/10.1103/39yj-zgwf
4. J. Q. Quach and W. J. Munro, *Using dark states to charge and stabilise open quantum batteries* (2020), arXiv:2002.10044. https://arxiv.org/abs/2002.10044
5. S. Seah et al., *Quantum Speed-Up in Collisional Battery Charging*, Physical Review Letters **127**, 100601 (2021). https://doi.org/10.1103/PhysRevLett.127.100601
