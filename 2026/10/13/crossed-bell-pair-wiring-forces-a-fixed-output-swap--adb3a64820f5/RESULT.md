# Crossed Bell-pair wiring forces a fixed output SWAP

## Finding
Adhya and Yang propose mentor-initiated asymmetric bidirectional teleportation in which Bob sends an arbitrary two-qubit state
\[
\lvert\psi_2\rangle=\alpha\lvert00\rangle+\beta\lvert01\rangle+\gamma\lvert10\rangle+\delta\lvert11\rangle.
\]
to Alice. For the source's own physical output order \(A_2,A_3\), the exact conditional map contains a fixed SWAP that is not removed by the printed wire assignment.

Use the Bell-state convention
\[
\lvert\beta_{x,z}\rangle=(I\otimes X^xZ^z)\lvert\Phi^+\rangle,
\qquad x,z\in\{0,1\}.
\]
Let \((x_1,z_1)\) and \((x_2,z_2)\) label the mentor outcomes on \((m_1,m_4)\) and \((m_2,m_5)\), and let \((u_1,v_1)\) and \((u_2,v_2)\) label Bob's Bell outcomes on \((b_1,B_1)\) and \((b_2,B_2)\). Define
\[
P_j=X^{x_j\oplus u_j}Z^{z_j\oplus v_j}.
\]
Then, up to a nonzero normalization and global phase, the state on the ordered output register \(A_2A_3\) is
\[
(P_2\otimes P_1)S\lvert\psi_2\rangle,
\]
where \(S\lvert r,s\rangle=\lvert s,r\rangle\). Hence a correct recovery on the named physical order is
\[
S(P_2^\dagger\otimes P_1^\dagger),
\]
or equivalently \((P_1^\dagger\otimes P_2^\dagger)S\). If instead the logical output is explicitly declared to have order \(A_3,A_2\), then the fixed SWAP is merely a wire relabelling and only local Paulis are required.

The source's first all-plus family in Table 3 already exposes the issue: its displayed reduced state is
\[
\alpha\lvert00\rangle+\beta\lvert10\rangle+\gamma\lvert01\rangle+\delta\lvert11\rangle
=S\lvert\psi_2\rangle.
\]
Thus the valid input \(\lvert01\rangle\) appears as \(\lvert10\rangle\) on \(A_2A_3\). A correction that is diagonal in the computational basis cannot exchange those two basis states.

## Assumptions and scope
The statement concerns the ideal noiseless protocol and the gate/wire ordering printed in arXiv:2610.01684v1. Bell-measurement outcomes are represented by the convention above; changing Bell labels can change irrelevant Pauli phases or bit names but cannot remove the fixed crossing of the two teleported wires. The result concerns the Bob-to-Alice arbitrary two-qubit direction. It does not assess the Alice-to-Bob single-qubit direction, noise, experimental imperfections, or implementation-specific endianness conventions beyond the source's named physical register \(A_2,A_3\).

## Proof
The source's first six-qubit resource, in order \(m_1m_2m_3A_1A_2A_3\), has exactly the eight basis strings
\[
000000,\ 001100,\ 010010,\ 011110,\ 100001,\ 101101,\ 110011,\ 111111.
\]
Therefore
\[
\lvert\Omega_1\rangle
=\lvert\Phi^+\rangle_{m_1A_3}
 \otimes\lvert\Phi^+\rangle_{m_2A_2}
 \otimes\lvert\Phi^+\rangle_{m_3A_1}.
\]
Likewise the source's second resource, in order \(m_4m_5m_6B_1B_2B_3\), has basis strings
\[
000000,\ 001001,\ 010010,\ 011011,\ 100100,\ 101101,\ 110110,\ 111111,
\]
so
\[
\lvert\Omega_2\rangle
=\lvert\Phi^+\rangle_{m_4B_1}
 \otimes\lvert\Phi^+\rangle_{m_5B_2}
 \otimes\lvert\Phi^+\rangle_{m_6B_3}.
\]
The source's preparation circuits give the same pairing directly.

The mentor measures \((m_1,m_4)\), \((m_2,m_5)\), and \((m_3,m_6)\) in the Bell basis. Thus entanglement swapping connects \(A_3\) to \(B_1\), \(A_2\) to \(B_2\), and \(A_1\) to \(B_3\), up to outcome-dependent local Paulis.

For a single crossed chain, direct contraction of two Bell resources and the two Bell bras gives the standard identity
\[
(\langle\beta_{u,v}\rvert_{bB}\langle\beta_{x,z}\rvert_{mn})
\bigl(\lvert\chi\rangle_b\lvert\Phi^+\rangle_{mA}\lvert\Phi^+\rangle_{nB}\bigr)
\propto X^{x\oplus u}Z^{z\oplus v}\lvert\chi\rangle_A,
\]
with only a convention-dependent global sign. Applying this independently to the two Bob input systems is valid even when they are entangled, by linearity. The first input qubit \(b_1\) is therefore teleported to \(A_3\) with Pauli \(P_1\), while the second input qubit \(b_2\) is teleported to \(A_2\) with Pauli \(P_2\). In logical order \(A_3,A_2\), the output is \((P_1\otimes P_2)\lvert\psi_2\rangle\). Rewriting the same vector in the source's stated physical order \(A_2,A_3\) gives
\[
(P_2\otimes P_1)S\lvert\psi_2\rangle.
\]
Inverting this map yields the recovery stated above. Since the exact conditional map is a product of one-qubit Paulis followed by a fixed SWAP, no branch-dependent entangling correction is needed.

## Verification
The bundled checker `artifacts/verify.py` uses exact integer arithmetic. It verifies all sixteen single-chain combinations of mentor and sender Bell labels, verifies the two source resource-state factorizations from their printed basis strings, and checks the all-plus basis witness \(S\lvert01\rangle=\lvert10\rangle\neq\lvert01\rangle\). The checker prints `VERIFY_OK`. The general proof is algebraic; the checker is corroborative rather than an extrapolation from finite samples.

## Relationship to prior work
Bennett et al. established exact one-qubit teleportation by a Bell measurement plus an outcome-dependent local correction. Żukowski et al. established entanglement swapping. Cao, Zhu, and Fang showed that teleporting an arbitrary multi-particle state through independent EPR pairs reduces to a series of single-qubit teleportations. Those results supply the standard identities used here, but they do not state the source-specific crossed pairing \(b_1\to A_3\), \(b_2\to A_2\), nor do they correct arXiv:2610.01684v1's named output ordering.

Exact-title, source-identifier, SWAP/wire-order, Bell-pair-factorization, and implication-equivalent literature searches found no prior source-specific correction. The closest inspected literature concerns the general teleportation identities rather than this protocol's physical wire assignment.

## Limitations
This result does not show that the architecture is incapable of teleporting an arbitrary two-qubit state. It shows that, with the physical output named \(A_2,A_3\), the printed recovery rule misses a fixed permutation; the architecture is repaired by one fixed SWAP, or equivalently by declaring the logical output order to be \(A_3,A_2\), together with the appropriate local Paulis. If the authors intended the reversed logical ordering implicitly, the scientific issue is an unstated output-register convention rather than loss of teleportation capability. No claim is made about noisy operation or hardware performance.

## References
1. S. Adhya and B. Yang, *Mentor-Initiated Asymmetric Bidirectional Quantum Teleportation Protocol for Arbitrary Qubit States*, arXiv:2610.01684v1 (first public 2026-10-01).
2. C. H. Bennett et al., *Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels*, Phys. Rev. Lett. 70, 1895 (1993), DOI 10.1103/PhysRevLett.70.1895.
3. M. Żukowski, A. Zeilinger, M. A. Horne, and A. K. Ekert, *Event-ready-detectors Bell experiment via entanglement swapping*, Phys. Rev. Lett. 71, 4287 (1993), DOI 10.1103/PhysRevLett.71.4287.
4. M. Cao, S. Q. Zhu, and J. X. Fang, *Teleportation of n-particle state via n pairs of EPR channels*, Commun. Theor. Phys. 41, 689 (2004), DOI 10.1088/0253-6102/41/5/689.
