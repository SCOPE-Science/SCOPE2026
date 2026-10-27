# An exact entanglement-breaking asymptotic channel for a dephased two-qubit battery

## Finding

In the resonant two-level charger–battery dynamics of Shastri et al. [1], the complete long-time map is a **binary measure-and-prepare channel**, for every initial joint density matrix—not merely for the two-ground-state preparation examined in [1]. The closed formula simultaneously classifies all stationary operators, determines what initial information survives, and establishes eventual separability across charger–battery and reference–system partitions.

Take arbitrary \(F,g,\gamma>0\). Define the Hermitian involution

\[
Q=\frac{2F I_{\mathrm C}\otimes X_{\mathrm B}-gZ_{\mathrm C}\otimes Z_{\mathrm B}}{\sqrt{g^2+4F^2}},\qquad P_\pm=\frac{I\pm Q}{2}.
\]

Each \(P_\pm\) is a rank-two orthogonal projection. For **every** initial density matrix \(\rho_0\) on the two-qubit system, put \(c=\operatorname{Tr}(Q\rho_0)\in[-1,1]\). The rotating-frame evolution has the exact norm limit

\[
\boxed{\displaystyle
\lim_{t\to\infty}\rho(t)=\Phi_\infty(\rho_0)
=\frac{I+cQ}{4}
=\operatorname{Tr}(P_+\rho_0)\frac{P_+}{2}
 +\operatorname{Tr}(P_-\rho_0)\frac{P_-}{2}.}
\]

In particular, its stationary operator space is **exactly** \(\operatorname{span}_{\mathbb C}\{I,Q\}\) and its stationary density matrices are **exactly** \((I+cQ)/4\) for \(-1\le c\le1\). The limiting quantum channel \(\Phi_\infty\) is entanglement-breaking: it retains the classical probabilities of a binary measurement and destroys all correlations with an arbitrary external quantum reference that require entanglement.

Every limiting joint state is separable between charger and battery and has zero quantum discord when the measurement is on the charger. Its discord when measured on the battery is strictly positive **if and only if** \(c\ne0\).

With bare battery Hamiltonian \(H_{\mathrm B}=\omega_{\mathrm B}(I+Z_{\mathrm B})/2\), \(\omega_{\mathrm B}>0\), the limiting energy and local ergotropy are

\[
\boxed{E_{\mathrm B}(\infty)=\frac{\omega_{\mathrm B}}2,\qquad
\mathcal E_{\mathrm B}(\infty)=
\frac{\omega_{\mathrm B}F}{\sqrt{g^2+4F^2}}|c|.}
\]

Thus initial states with identical limiting battery energy can retain different extractable work. Over **all** initial two-qubit states, the exact upper bound \(\omega_{\mathrm B}F/\sqrt{g^2+4F^2}\) is attained by any initial state supported in either eigenspace of \(Q\). For the particular two-ground-state preparation in [1], \(c=-g/\sqrt{g^2+4F^2}\), recovering its already-published ergotropy \(\omega_{\mathrm B}Fg/(g^2+4F^2)\). Neither that ground-preparation formula nor the general possibility of nonunique steady states [2] is claimed as new.

## Assumptions and scope

The charger \(\mathrm C\) and battery \(\mathrm B\) are two-level systems. Operators are ordered \(\mathcal H_{\mathrm C}\otimes\mathcal H_{\mathrm B}\). Let \(X,Y,Z\) denote the standard Pauli matrices with \(Z=\operatorname{diag}(1,-1)\), and let \(I\) denote the identity on the relevant tensor product. At exact resonance, the time-independent interaction-picture Hamiltonian and charger-dephasing Lindbladian are

\[
H=F X_{\mathrm C}\otimes I_{\mathrm B}
 +\frac g2\left(X_{\mathrm C}\otimes X_{\mathrm B}
 +Y_{\mathrm C}\otimes Y_{\mathrm B}\right),
\]

\[
\mathcal L(A)=-i[H,A]
+\frac\gamma4\left((Z_{\mathrm C}\otimes I_{\mathrm B})A(Z_{\mathrm C}\otimes I_{\mathrm B})-A\right),
\qquad \rho(t)=e^{t\mathcal L}\rho_0.
\]

The normalization of \(\gamma\) agrees with dephasing by the jump operator \(\sigma^+_{\mathrm C}\sigma^-_{\mathrm C}\) at the rate used in [1]. The theorem assumes \(F,g,\gamma>0\) and makes no assumption of product, pure, thermal, or ground initial state. The limit of the **joint state** is in this rotating frame; the joint laboratory-frame density can retain free-frequency rotations. The bare battery energy and its ergotropy are invariant under those local rotations, which commute with \(H_{\mathrm B}\).

## Proof

**1. Conservation and projector normalization.** The two Pauli products in the numerator of \(Q\) anticommute and each squares to the identity. Hence \(Q^\dagger=Q\), \(Q^2=I\), and \(\operatorname{Tr}Q=0\). Its eigenvalues are \(\pm1\), each with multiplicity two. Direct Pauli commutation gives

\[
[H,I_{\mathrm C}\otimes X_{\mathrm B}]=-igY_{\mathrm C}\otimes Z_{\mathrm B},\qquad
[H,Z_{\mathrm C}\otimes Z_{\mathrm B}]=-2iF Y_{\mathrm C}\otimes Z_{\mathrm B}.
\]

Thus \([H,Q]=0\), while \([Z_{\mathrm C}\otimes I_{\mathrm B},Q]=0\). It follows that \(\mathcal L(Q)=0\), \(\mathcal L(I)=0\), and \(c=\operatorname{Tr}(Q\rho(t))\) is conserved (the generator is Hilbert–Schmidt self-dual on these two operators).

**2. Exact fixed algebra.** For any complex \(4\times4\) operator \(A\), the Hermitian dissipator has the real Hilbert–Schmidt dissipation identity

\[
\operatorname{Re}\operatorname{Tr}(A^\dagger\mathcal L(A))
=-\frac\gamma8\|[Z_{\mathrm C}\otimes I_{\mathrm B},A]\|_2^2.
\]

If \(\mathcal L(A)=0\), this forces \(A\) to commute with \(Z_{\mathrm C}\otimes I_{\mathrm B}\), so in the charger \(Z\)-basis \(A=\operatorname{diag}(A_0,A_1)\) with two battery blocks. The Hamiltonian is off-diagonal in this basis, with upper-right block \(T=F I_{\mathrm B}+g\sigma^-_{\mathrm B}\); \(\det T=F^2>0\). The equation \([H,A]=0\) is equivalent to

\[
A_0T=TA_1,\qquad A_1T^\dagger=T^\dagger A_0.
\]

Eliminating \(A_1\) shows \([A_0,TT^\dagger]=0\). The two eigenvalues of \(TT^\dagger\) are

\[
F^2+\frac{g^2}{2}\pm\frac g2\sqrt{g^2+4F^2},
\]

which are distinct for \(g>0\). The commutant of this nondegenerate Hermitian \(2\times2\) operator has complex dimension two; \(A_1\) is uniquely determined by \(A_0\). Hence \(\dim_{\mathbb C}\ker\mathcal L=2\). The two already-known independent fixed operators \(I,Q\) span the entire kernel.

**3. Convergence for every initial operator.** If \(\mathcal L(A)=i\nu A\) for real \(\nu\), the dissipation identity again makes \(A\) block-diagonal in charger \(Z\). Then \(\mathcal L(A)=-i[H,A]\) has only off-diagonal charger blocks, whereas \(i\nu A\) has only diagonal blocks; for \(\nu\ne0\) these can coincide only for \(A=0\). Therefore zero is the only imaginary-axis eigenvalue. The finite-dimensional unital completely positive semigroup is bounded, so its peripheral eigenvalues have no nontrivial Jordan blocks. All other eigenvalues have strictly negative real part. Its limit is the Hilbert–Schmidt orthogonal projection onto \(\ker\mathcal L\): the kernel coincides with that of the adjoint because the same dissipation and commutant argument applies. Orthogonality \(\operatorname{Tr}(IQ)=0\) and \(\operatorname{Tr}(Q^2)=\operatorname{Tr}(I^2)=4\) give

\[
\lim_{t\to\infty}e^{t\mathcal L}(A)
=\frac{\operatorname{Tr}(A)}4 I+
\frac{\operatorname{Tr}(QA)}4Q.
\]

For a density matrix this is the claimed limit. Its eigenvalues are \((1\pm c)/4\), each twice, so positivity holds exactly when \(|c|\le1\). Equivalently, since \(P_\pm\) are orthogonal rank-two projections, the limit is the stated positive trace-preserving measure-and-prepare channel. That formula alone establishes entanglement-breaking even for inputs entangled with an arbitrarily large reference.

**4. Separability, asymmetric discord, and work.** Since \(Q\) contains only \(I_{\mathrm C}\) and \(Z_{\mathrm C}\) on the charger, each fixed state is block-diagonal in the charger's \(Z\)-basis and is a convex combination of two product density matrices, hence separable and classical on the charger. Conditioned on the two equiprobable charger outcomes, the battery states are

\[
\rho_{\mathrm B}^{\pm}=\frac12\left(I_{\mathrm B}
+\frac{2Fc}{\sqrt{g^2+4F^2}}X_{\mathrm B}
\mp\frac{gc}{\sqrt{g^2+4F^2}}Z_{\mathrm B}\right).
\]

They commute if and only if \(Fgc^2=0\). With \(F,g>0\), this occurs precisely when \(c=0\). A classical-on-charger state has zero battery-measured discord exactly when the two conditional battery density matrices are simultaneously diagonalizable; therefore it has strictly positive battery-measured discord exactly for \(c\ne0\).

Taking the partial trace gives \(\rho_{\mathrm B}(\infty)=\tfrac12(I_{\mathrm B}+(2Fc/\sqrt{g^2+4F^2})X_{\mathrm B})\), whose \(Z\)-component is zero and whose Bloch length is \(2F|c|/\sqrt{g^2+4F^2}\). The qubit energy and ergotropy formulas then yield the boxed values above. As \(Q\) has eigenvalues \(\pm1\), \(|c|\le1\) is sharp; its extremizers are states supported in a single eigenspace. The ground-state value follows by taking the expectation of \(Q\) in \(|g_{\mathrm C}g_{\mathrm B}\rangle\), for which both local \(Z\) eigenvalues are negative.

## Verification

The standalone script `verify_dephased_battery.py` constructs the entire \(16\times16\) Lindblad superoperator directly and checks the analytical map and its conserved observable against 80 deterministic-seeded random positive parameter triples and random full-rank two-qubit density matrices. It verifies exactly two numerical zero eigenvalues, strict numerical decay of the remaining 14 modes, normalization and stationarity of the two rank-two projectors, long-time matrix exponentiation, and reduced ergotropy. The source's ground-state ergotropy at \(F/g=1/2\) is reproduced. The recorded numerical residuals and command appear in `VERIFICATION.md`. The infinite-time conclusion and quantum-channel properties follow from the proof, **not** from finitely many sampled tests.

## Relationship to prior work

Shastri et al. [1] derived the resonant two-TLS model and its charging dynamics for a specified ground-state preparation. In particular they already give the limiting half-excitation energy and the ground-preparation ergotropy \(\omega_{\mathrm B}Fg/(g^2+4F^2)\). These formulas, the model, and its moment equations are not new here. Purkait, Venkatesh, and Watanabe [2] subsequently noted explicitly that resonant dephased charger–battery stationary states are nonunique, while studying collective \(N\)-qubit batteries by numerical steady-state analysis. **Nonuniqueness itself is not claimed as original.** The present result instead gives an exact two-qubit fixed-point algebra, all-input limiting superoperator, complete entanglement-breaking classification, directional quantum-correlation characterization, and sharp preparation-dependent ergotropy range. General fixed-point and entanglement-breaking channel principles are standard tools, not new principles attributed to this result.

Farina et al. [3] study related coherently driven charger–battery models with thermal dissipators, not the charger's local Hermitian pure-dephasing channel. Wang and Jin [4] examine early-time non-Markovian effects in a dephased charger system rather than the all-input Markovian long-time map. The relevant open literature was searched for logically covering specializations; an unidentified equivalent derivation remains a residual possibility.

## Limitations

The claim applies only to the stated exactly resonant, driven, two-qubit, Markovian pure-dephasing model with \(F,g,\gamma>0\) and no charger energy relaxation, battery dephasing, additional drive phases, or detuning. At \(F=0\), \(g=0\), or \(\gamma=0\), the rank and convergence proof must not be extrapolated. The long-time **joint density matrix** is stationary in the rotating frame only. The statement that the asymptotic map is entanglement-breaking does **not** assert that \(e^{t\mathcal L}\) is entanglement-breaking at any finite time. Ground-preparation optimum and arbitrary-preparation optimum differ because additional initial coherence or correlations constitute a preparation resource; the latter is not a free charging advantage. No assertion of uniqueness in general many-battery models is made.

## References

[1] R. Shastri, C. Jiang, G.-H. Xu, B. P. Venkatesh and G. Watanabe, *Dephasing Enabled Fast Charging of Quantum Batteries*, arXiv:2402.16999v1 (first public posting 2024-02-26), https://arxiv.org/abs/2402.16999 ; npj Quantum Information **11**, 9 (2025), https://doi.org/10.1038/s41534-025-00959-5 .

[2] C. Purkait, B. P. Venkatesh and G. Watanabe, *Asymptotic freedom of dephased charging*, arXiv:2508.13497v1 (2025), https://arxiv.org/abs/2508.13497 . See the paragraph explicitly acknowledging nonunique resonant steady states.

[3] D. Farina, G. M. Andolina, A. Mari, M. Polini and V. Giovannetti, *Charger-mediated energy transfer for quantum batteries: an open system approach*, arXiv:1810.10890 (2018), https://arxiv.org/abs/1810.10890 .

[4] Y. Wang and J. Jin, *Early-stage memory effect on the dephasing charger-mediated quantum battery*, arXiv:2602.14146 (2026), https://arxiv.org/abs/2602.14146 .
