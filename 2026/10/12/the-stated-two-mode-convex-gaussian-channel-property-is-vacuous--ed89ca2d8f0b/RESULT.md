# The stated two-mode convex-Gaussian channel property is vacuous
## Finding
Allison and Coffman define a fermionic convex-Gaussian channel as one that maps convex combinations of pure fermionic Gaussian input states to convex combinations of pure fermionic Gaussian output states. For a channel acting on two fermionic modes, that input-output condition is vacuous on the physical state space: every physical two-mode fermionic density operator is already convex-Gaussian.

Consequently every two-mode channel that maps physical fermionic states to physical fermionic states satisfies the stated local convex-Gaussian channel definition. In particular, for the parity-preserving noisy-gate family
\[
\mathcal E_{U,p}=\mathscr D_p^{\otimes 2}\circ\mathscr U,
\]
the stated property holds for every permitted \(U\) and every \(0\le p\le 1\).

This contradicts the paper's Eq. (35), which asserts
\[
\mathcal E_{U,p}\text{ is convex Gaussian}
\quad\Longleftrightarrow\quad
C_+(U,p)=C_-(U,p)=0.
\]
An explicit counterexample is noiseless SWAP. The paper gives \(\eta(\mathrm{SWAP})=1\), \(C_-(U,p)=0\), and
\[
C_+(U,p)=\max\left(0,
\frac12\eta(1-p)(2-p)+\frac{p^2}{8}-\frac p2
\right).
\]
Therefore
\[
C_+(\mathrm{SWAP},0)=1,
\qquad
C_-(\mathrm{SWAP},0)=0,
\]
even though SWAP satisfies the stated local convex-Gaussian input-output property.

It follows that
\[
p_* = \frac{8-2\sqrt6}{5}
\]
cannot be the onset of the local channel property as defined in the paper. The four-mode Choi calculation may instead test a stronger, ancilla-sensitive resource-preservation condition, but that is a different channel notion and requires a separate definition and argument.

## Assumptions and scope
A physical two-mode fermionic state obeys parity superselection. With
\[
P=Z_1Z_2,
\]
this means \([\rho,P]=0\), so \(\rho\) is block diagonal on the even-parity subspace \(\operatorname{span}\{|00\rangle,|11\rangle\}\) and the odd-parity subspace \(\operatorname{span}\{|01\rangle,|10\rangle\}\).

The claim uses the paper's own local definition of a convex-Gaussian channel: preservation of the convex hull of pure fermionic Gaussian states on the two-mode system. It does not assume that this local definition is equivalent to preservation after adjoining arbitrary reference modes.

The channel family considered by Allison and Coffman consists of a parity-preserving two-qubit unitary followed by local depolarizing noise. Such channels preserve the physical parity-superselected state space. The unitary does so by assumption. The local depolarizing channel is covariant under conjugation by \(Z\), hence \(\mathscr D_p^{\otimes2}\) is covariant under conjugation by \(P=Z_1Z_2\); therefore an input commuting with \(P\) is sent to an output commuting with \(P\).

## Proof
First prove that every physical two-mode state is convex-Gaussian. A physical density operator has a parity decomposition
\[
\rho=\rho_+\oplus\rho_-.
\]
Spectrally decompose each positive block. Every pure state appearing in the even block has the form
\[
|\psi_+\rangle=a|00\rangle+b|11\rangle,
\qquad |a|^2+|b|^2=1.
\]
Choose the special-unitary block
\[
A=\begin{pmatrix}a&-b^*\\ b&a^*\end{pmatrix}.
\]
Its determinant is \(1\). Taking the odd block to be the identity gives a matchgate \(G(A,I)\), hence a fermionic Gaussian unitary, and
\[
G(A,I)|00\rangle=|\psi_+\rangle.
\]
Because \(|00\rangle\) is a Fock state, it is Gaussian, so every even-parity pure two-mode state is Gaussian.

Likewise, every odd-parity pure state has the form
\[
|\psi_-\rangle=c|01\rangle+d|10\rangle,
\qquad |c|^2+|d|^2=1.
\]
The block
\[
B=\begin{pmatrix}c&-d^*\\ d&c^*\end{pmatrix}
\]
has determinant \(1\), and the matchgate \(G(I,B)\) maps the Gaussian Fock state \(|01\rangle\) to \(|\psi_-\rangle\). Hence every definite-parity pure state on two modes is fermionic Gaussian.

The spectral decompositions of \(\rho_+\) and \(\rho_-\) therefore express every physical \(\rho\) as a convex combination of pure Gaussian states. Thus the convex-Gaussian state set equals the entire physical two-mode state space.

Now let \(\mathcal E\) be any channel that preserves parity superselection. If \(\rho\) is convex-Gaussian, it is a physical two-mode state; \(\mathcal E(\rho)\) is again physical and therefore, by the preceding paragraph, convex-Gaussian. Thus \(\mathcal E\) satisfies the local input-output definition.

For the paper's family \(\mathcal E_{U,p}\), parity preservation follows from the parity-preserving \(U\) and covariance of local depolarization. In particular, at \(p=0\), SWAP is a valid parity-preserving channel and therefore satisfies the stated local definition.

The paper independently derives, for a parity-preserving gate \(U=A\oplus B\),
\[
\eta(U)=\frac12|\det A-\det B|,
\]
with \(\eta(\mathrm{SWAP})=1\), and gives
\[
C_+(U,p)=\max\left(0,
\frac12\eta(1-p)(2-p)+\frac{p^2}{8}-\frac p2
\right),
\qquad
C_-(U,p)=0.
\]
Substituting \(p=0\) and \(\eta=1\) yields \(C_+=1\) and \(C_-=0\). Hence the right-hand side of Eq. (35) is false while its left-hand side, interpreted by the paper's own local definition, is true. This is a direct counterexample to the claimed equivalence.

The older Oszmaniec--Gutt--Kuś paper supplies an independent structural cross-check: it calls four modes the first non-trivial convex-Gaussian state case and states that for two and three modes all even pure states are Gaussian. Its four-mode concurrence theorem is a theorem about states; it does not state the channel-Choi equivalence asserted in Eq. (35).

## Verification
The proof is analytic and all-dimensional statements used here concern only the fixed two-mode output system. The key classification follows from explicit matchgate constructions for arbitrary normalized coefficients in each parity sector, not from finite enumeration.

The accompanying checker verifies the following algebraic consequences: the SWAP matrix commutes with parity; its even and odd blocks have determinant separation \(\eta=1\); the paper's concurrence formula gives \(C_+(\mathrm{SWAP},0)=1\) and vanishes at the stated threshold; representative special-unitary parity blocks have determinant \(1\); and every two-qubit Pauli conjugation either commutes or anticommutes with total parity, so the corresponding depolarizing branches preserve parity superselection. These calculations corroborate, but do not replace, the general proof above.

## Relationship to prior work
Oszmaniec, Gutt, and Kuś proved the four-mode state criterion
\[
\rho\text{ is convex-Gaussian}
\quad\Longleftrightarrow\quad
C_+(\rho)=C_-(\rho)=0
\]
for four-mode fermionic states. Their paper explicitly identifies four modes as the first non-trivial convex-Gaussian state case. That result supports the two-mode state-space collapse used above, but it does not establish that a two-mode channel preserves convex-Gaussian states if and only if its four-mode Choi state is convex-Gaussian.

Allison and Coffman use the four-mode state criterion on a Choi state and promote it to the channel equivalence in Eq. (35). A public technical review of their preprint had already identified that channel-to-Choi step as unproved. The result here is stronger than a missing-proof observation: the written local definition admits the explicit noiseless-SWAP counterexample, so Eq. (35) is false under that definition.

Targeted literature and semantic-index searches did not locate a prior source giving this exact two-mode vacuity argument or the explicit \(p=0\) SWAP contradiction. The classical four-mode state theorem and the existing public review are therefore the closest prior coverage.

## Limitations
The result is a definition-level correction. It does not show that the paper's four-mode Choi state or concurrence algebra is wrong. It also does not show that \((8-2\sqrt6)/5\) fails to characterize some stronger channel resource notion that is stable under extension by reference modes. Indeed, a Choi test naturally probes an enlarged system-reference state, so such a stronger interpretation is plausible; it is simply not the local input-output definition written in the paper.

Accordingly, no claim is made here about the optimal fault-tolerance upper bound after replacing the channel definition by a suitable ancilla-sensitive one. Establishing that repaired statement would require a separate theorem connecting the chosen stronger channel notion to the four-mode Choi criterion and to efficient simulation of larger circuits.

## References
1. O. Allison and L. Coffman, “Noise Limits on Fault-Tolerant Fermionic Quantum Computing,” arXiv:2609.09467v1, first public 2026-09-08.
2. M. Oszmaniec, J. Gutt, and M. Kuś, “Classical simulation of fermionic linear optics augmented with noisy ancillas,” arXiv:1406.1577v1; Phys. Rev. A 90, 020302(R) (2014).
