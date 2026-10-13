# Independent bit-flip noise breaks the claimed perfect bidirectional teleportation fidelity
## Finding
Consider the bidirectional teleportation protocol of De, R, Ahmed and Sharan, arXiv:2607.23820v1. Its twelve-qubit resource is prepared by Hadamards on qubits \(1,\ldots,6\) followed by CNOTs \((1,7),\ldots,(6,12)\). Therefore the resource is exactly
\[
|G_{12}\rangle=\bigotimes_{j=1}^{6}|\Phi^+\rangle_{j,j+6},
\qquad
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]
The paper's Appendix C defines a one-qubit bit-flip channel by
\[
K_0=\sqrt{1-p}\,I,\qquad K_1=\sqrt p\,X.
\]
If this noise acts independently on the twelve resource qubits, as the usual tensor-product channel associated with these Kraus operators, then each Bell pair becomes
\[
(1-q)|\Phi^+\rangle\langle\Phi^+|+q|\Psi^+\rangle\langle\Psi^+|,
\qquad q=2p(1-p).
\]
Standard Bell-measurement teleportation through this Bell-diagonal resource is therefore the bit-flip channel
\[
\mathcal T_q(\rho)=(1-q)\rho+qX\rho X
\]
on each teleported qubit.

For the paper's Eq. (36) family, put \(s=\sqrt{1-a^2}\). Alice's three-qubit input factors as
\[
|\psi_a\rangle
=|+\rangle_2\otimes\frac{a|00\rangle+s|01\rangle+s|10\rangle+a|11\rangle}{\sqrt2}_{1,3}.
\]
In the bit-flip plot the other bidirectional input is fixed at \(b=1/\sqrt2\), for which that party's state is \(|+\rangle^{\otimes3}\) and is unchanged by bit flips. The exact six-qubit bidirectional input-output fidelity is thus
\[
F_{\mathrm{Bi}}(a,p)
=1-2q(1-q)(2a^2-1)^2,
\qquad q=2p(1-p).
\]
Equivalently,
\[
F_{\mathrm{Bi}}(a,p)
=1-4p(1-p)\bigl(1-2p(1-p)\bigr)(2a^2-1)^2.
\]
Hence the source's claim that the bidirectional protocol has unit fidelity under bit-flip noise for every input and every noise strength is false under the independent local-noise model. A concrete counterexample is
\[
p=\frac12,\qquad a=0,
\qquad F_{\mathrm{Bi}}=\frac12.
\]

If instead the single summation symbol in the paper's Eq. (33) is read literally as forcing one common Kraus label on all twelve qubits, the resulting two operators are proportional to \(I^{\otimes12}\) and \(X^{\otimes12}\) with squared norms \((1-p)^{12}\) and \(p^{12}\). Their completeness sum is
\[
\bigl((1-p)^{12}+p^{12}\bigr)I,
\]
which is not the identity for \(0<p<1\). That literal reading therefore does not define a trace-preserving quantum channel. A genuinely correlated global-flip channel can preserve \(|G_{12}\rangle\), but it is a different noise model from independent per-qubit bit flips.

## Assumptions and scope
The correction concerns the source's bit-flip analysis for its bidirectional protocol. The noise assumption is the standard independent product channel obtained by applying the stated one-qubit bit-flip CPTP map separately to each of the twelve resource qubits before the Bell measurements. The ideal Bell measurements and Pauli feed-forward corrections are those used by the source.

The exact formula above applies to the source's Eq. (36) one-parameter input family with the opposite-direction state fixed at \(b=1/\sqrt2\), as in the bit-flip comparison. It does not analyze the source's other four noise models, and it does not claim that a deliberately correlated global bit-flip model lacks perfect fidelity.

## Proof
The preparation circuit gives six independent Bell pairs because each gate pair acts on disjoint qubits:
\[
H_j|0\rangle_j\otimes|0\rangle_{j+6}
\xrightarrow{\mathrm{CNOT}_{j\to j+6}}
|\Phi^+\rangle_{j,j+6}.
\]
On one Bell pair, independent bit flips on its two halves have even parity with probability
\[
(1-p)^2+p^2=1-q
\]
and odd parity with probability \(q=2p(1-p)\). Since \((X\otimes X)|\Phi^+\rangle=|\Phi^+\rangle\) while \((X\otimes I)|\Phi^+\rangle=(I\otimes X)|\Phi^+\rangle=|\Psi^+\rangle\), the noisy pair is the Bell-diagonal mixture stated above. Bowen and Bose's standard-teleportation channel formula then gives \(\mathcal T_q\).

For Alice's input, errors on qubit \(2\) act trivially because that factor is \(|+\rangle\). On qubits \(1\) and \(3\), define
\[
|\varphi_a\rangle
=\frac{a|00\rangle+s|01\rangle+s|10\rangle+a|11\rangle}{\sqrt2}.
\]
The relevant overlaps are
\[
\langle\varphi_a|X\otimes X|\varphi_a\rangle=1,
\qquad
\langle\varphi_a|X\otimes I|\varphi_a\rangle
=\langle\varphi_a|I\otimes X|\varphi_a\rangle=2as.
\]
Thus even flip parity on those two qubits contributes fidelity \(1\), while odd parity contributes \(4a^2(1-a^2)\). Averaging gives
\[
\begin{aligned}
F_{\mathrm{Bi}}
&=((1-q)^2+q^2)
+2q(1-q)\,4a^2(1-a^2)\\
&=1-2q(1-q)(2a^2-1)^2.
\end{aligned}
\]
The other party's fixed \(|+\rangle^{\otimes3}\) state has fidelity one under every tensor-product bit-flip error, so the joint bidirectional fidelity equals this expression. At \(p=1/2\), one has \(q=1/2\); at \(a=0\) this gives \(F_{\mathrm{Bi}}=1/2\).

## Verification
The derivation is exact and valid for all \(a\in[0,1]\) and \(p\in[0,1]\) under the stated independent-noise model. The bundled `artifacts/verify.py` uses exact rational arithmetic to check the parity decomposition, the closed form on a grid of rational values of \(a^2\) and \(p\), the counterexample \((a,p)=(0,1/2)\), and the failure of trace preservation under the alternative common-index reading of Eq. (33). These finite checks corroborate the algebra; they are not a substitute for the symbolic proof above.

## Relationship to prior work
The source itself constructs the six disjoint Bell pairs, applies Bell-state measurements and Pauli corrections, and states both the independent one-qubit bit-flip Kraus operators and the claimed all-parameter unit fidelity. Bowen and Bose proved the broader theorem that standard teleportation through a Bell-diagonal mixed resource produces the corresponding Pauli channel. That theorem supplies the standard channel reduction used here, but it predates and does not contain the source-specific contradiction, the factorization of this twelve-qubit resource, or the closed fidelity formula for the source's Eq. (36) family.

Searches for the source identifier, exact title, the phrases “perfectly faithful” and “bit-flip”, Bell-pair factorization aliases, and the equivalent Pauli-channel statement found no prior correction of this source-specific claim.

## Limitations
This finding does not assess the cyclic protocol, the amplitude-damping, phase-damping, phase-flip, or depolarizing plots, or the paper's ideal noiseless teleportation identities. It also does not rule out perfect robustness against a specially engineered correlated global \(X\) error. The conclusion is specifically that the paper's perfect-fidelity statement is incompatible with the standard independent product channel generated by the one-qubit Kraus operators it writes down.

## References
1. S. De, Vedhanayagi R, B. M. Ahmed A, and A. Sharan, *Unified Framework for Bidirectional and Cyclic Teleportation under Noise*, arXiv:2607.23820v1 (2026).
2. G. Bowen and S. Bose, *Teleportation as a Depolarizing Quantum Channel, Relative Entropy and Classical Capacity*, arXiv:quant-ph/0107132v2; Phys. Rev. Lett. 87, 267901 (2001), DOI:10.1103/PhysRevLett.87.267901.
