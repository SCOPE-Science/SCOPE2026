# Unitary-pulse no-go for compressing an isotropic depolarizing channel
## Finding
For the qubit depolarizing channel used in arXiv:2605.16463v1,
\[
\mathcal N_p(\rho)=(1-p)\rho+\frac p3\!\left(X\rho X+Y\rho Y+Z\rho Z\right),
\qquad 0<p<\frac34,
\]
instantaneous unitary pulse control cannot transform the stated memoryless channel into a strictly less noisy depolarizing channel with \(p'<p\).

More precisely, if \(\mathcal D_t\) is an isotropic depolarizing semigroup and unitary pulses \(U_1,\ldots,U_m\) are inserted between time intervals \(t_1,\ldots,t_m\), then
\[
\mathcal D_{t_m}\circ\operatorname{Ad}_{U_m}\circ\cdots\circ
\mathcal D_{t_1}\circ\operatorname{Ad}_{U_1}
=
\operatorname{Ad}_{U_m\cdots U_1}\circ\mathcal D_T,
\qquad T=\sum_{j=1}^m t_j.
\]
After returning to the pulse frame, the effective channel is exactly \(\mathcal D_T\). Thus Pauli dynamical decoupling does not compress the depolarizing parameter in the channel model actually written in the source.

The source's Appendix C average has an additional exact consequence:
\[
\frac1M\sum_{k=1}^M\mathcal N_p(P_k\rho P_k^\dagger)
=
\mathcal N_p\!\left(\frac1M\sum_{k=1}^M P_k\rho P_k^\dagger\right).
\]
For a balanced average over \(I,X,Y,Z\), the inner average is \(I/2\), so this literal expression produces \(I/2\), not a less noisy copy of \(\rho\). With the natural output-frame correction, each term instead equals \(\mathcal N_p(\rho)\), again leaving the noise unchanged.

Finally, the formula printed in the source,
\[
p'=p\exp(-\gamma/f_{\mathrm{DD}}),
\]
has
\[
\lim_{f_{\mathrm{DD}}\to\infty}p'=p,
\]
not \(0\). This arithmetic inconsistency is supplementary: the covariance no-go remains even if that exponential were replaced by a different decreasing function.

## Assumptions and scope
The statement applies to the channel-level qubit depolarizing map explicitly defined in arXiv:2605.16463v1 and, for the interleaved-pulse theorem, to its standard continuous-time isotropic semigroup realization. Pulses are arbitrary instantaneous qubit unitaries and may be Pauli pulses as in the source.

The theorem does not say that dynamical decoupling is useless for a microscopic system-bath Hamiltonian with memory, colored noise, or anisotropic couplings. Such models contain temporal information that a single fixed CPTP depolarizing map does not. It also does not rule out quantum error correction, encoding into a larger system, adaptive controls with additional resources, or the source's separate amplitude-damping discussion.

## Proof
For any qubit density matrix \(\rho\),
\[
X\rho X+Y\rho Y+Z\rho Z=2I-\rho.
\]
Therefore
\[
\mathcal N_p(\rho)
=
\left(1-\frac{4p}3\right)\rho+\frac{2p}3I
=
\alpha\rho+(1-\alpha)\frac I2,
\qquad
\alpha=1-\frac{4p}3.
\]
For every unitary \(U\),
\[
\mathcal N_p(U\rho U^\dagger)
=
\alpha U\rho U^\dagger+(1-\alpha)\frac I2
=
U\mathcal N_p(\rho)U^\dagger.
\]
Hence \(\mathcal N_p\) commutes with every unitary conjugation.

For a depolarizing semigroup write
\[
\mathcal D_t(\rho)=e^{-\kappa t}\rho+\left(1-e^{-\kappa t}\right)\frac I2.
\]
It obeys both
\[
\mathcal D_s\circ\mathcal D_t=\mathcal D_{s+t}
\]
and
\[
\mathcal D_t\circ\operatorname{Ad}_U
=
\operatorname{Ad}_U\circ\mathcal D_t.
\]
Moving every pulse through the neighboring depolarizing segment and composing the noise intervals gives
\[
\mathcal D_{t_m}\circ\operatorname{Ad}_{U_m}\circ\cdots\circ
\mathcal D_{t_1}\circ\operatorname{Ad}_{U_1}
=
\operatorname{Ad}_{U_m\cdots U_1}\circ\mathcal D_T.
\]
Conjugating by the inverse net pulse removes the first factor and leaves exactly \(\mathcal D_T\). Thus the contraction and the associated depolarizing parameter are unchanged by the pulse schedule.

For the average written in Appendix C, linearity gives
\[
\frac1M\sum_k\mathcal N_p(P_k\rho P_k^\dagger)
=
\mathcal N_p\!\left(\frac1M\sum_kP_k\rho P_k^\dagger\right).
\]
The four-Pauli twirl satisfies
\[
\frac14\left(\rho+X\rho X+Y\rho Y+Z\rho Z\right)=\frac I2,
\]
so a balanced version of that displayed average returns \(I/2\). If each pulse is instead undone in the output frame, covariance gives
\[
P_k^\dagger\mathcal N_p(P_k\rho P_k^\dagger)P_k
=
\mathcal N_p(\rho)
\]
term by term.

For the source's frequency law, elementary continuity gives
\[
\lim_{f\to\infty}p\exp(-\gamma/f)=p.
\]
Therefore neither the channel covariance nor the printed frequency law supports the asserted limit \(p'\to0\).

## Verification
The bundled `artifacts/verify.py` checks the depolarizing covariance identity on deterministic random pure states, the balanced Pauli-twirl identity, the corrected-pulse-frame identity, semigroup composition, and numerical convergence of \(p\exp(-\gamma/f)\) to \(p\). These are finite consistency checks only; the universal result is established by the analytic identities above.

The full arXiv text of arXiv:2605.16463v1 was inspected at its explicit depolarizing construction and Appendix C. The source defines the same \(\mathcal N_p\), asserts \(p'<p\), writes the pulse average above, and states that \(p'=p\exp(-\gamma/f_{\mathrm{DD}})\) tends to zero at high pulse frequency.

The source's cited Uhrig paper was also inspected. It analyzes a qubit coupled through \(\sigma_z\) to a bosonic bath with a spectral cutoff and finite bath correlation time; it explicitly describes \(T_2\)-type phase decoherence with no spin flips. That microscopic pure-dephasing model is materially different from a fixed memoryless isotropic depolarizing CPTP map.

## Relationship to prior work
Unitary covariance of the depolarizing channel and the general use of dynamical decoupling for structured system-bath models are standard facts. The contribution here is the source-specific implication: the concrete Pauli-DD compression step used in arXiv:2605.16463v1 is incompatible with the depolarizing channel that the same paper writes down.

The closest cited DD source, G. S. Uhrig's optimized \(\pi\)-pulse work, assumes an explicit system-bath Hamiltonian and a finite bath correlation time. Its pulses reverse a \(\sigma_z\) coupling and suppress phase decoherence. It does not state that arbitrary unitary pulses can reduce an already-specified isotropic depolarizing CPTP map.

A prior analysis of arXiv:2605.16463v1 established a different issue concerning the paper's post-channel LOCC optimization and global relative entropy of entanglement. That result does not imply the present covariance theorem or the pulse-level no-go; the two corrections concern independent sides of the claimed comparison.

Targeted searches of the published published-finding corpus corpus for the source identifier, depolarizing-channel dynamical decoupling, unitary covariance, Pauli twirling, and the printed \(p'\) law did not locate an implication-equivalent source-specific correction.

## Limitations
The theorem is a no-go for changing the fixed isotropic depolarizing channel by unitary pulses alone. It does not exclude a model in which the channel itself is derived from a non-Markovian or frequency-resolved system-bath Hamiltonian and the pulses alter that derivation. It does not assess the source's amplitude-damping construction or every conceivable pre-channel encoding protocol.

No claim is made that the covariance identity is new. The originality claim is limited to its exact consequence for the recent depolarizing/DD construction and to the separation of that channel-level model from the microscopic DD assumptions of the cited literature.

## References
1. G. Lyu, W. Sun, Y. Jin, H. Nan, “Pre-Channel Entanglement Shaping Achieves Fundamental Superiority over Post-Distillation: A Geometric Entropy Perspective,” arXiv:2605.16463v1, 15 May 2026.
2. G. S. Uhrig, “Keeping a Quantum Bit Alive by Optimized \(\pi\)-Pulse Sequences,” arXiv:quant-ph/0609203v2; Phys. Rev. Lett. 98, 100504 (2007).
